"""Shared multimodal-read stage (WK-0094 Phase B; generalized from
`instagram_read.py`): one `claude --print` call, prompt text plus N ordered
images (each with its own media type), stream-json in and out, usage parsed
from the final result event. Claude command flags, stream-json shape and
parsing stay exactly as the WK-0080 Instagram slice captured them (I3) —
verified against the real `claude --print` invocations captured in
`toolkit-workbench/reel/fixtures/or1/*.cmd.txt` (this module is a fresh
implementation against that evidence, not an import from the gitignored
workbench, R9).

WK-0094 Phase B: the reel adapter passes one image; the carousel adapter
(WK-0087) will pass up to 20 — this stage accepts a list from the start, so
no shared-code edit is needed when that adapter lands. Response-JSON *domain*
parsing (the reel's `tools`/`on_screen_text` shape) stays adapter-owned —
this stage only knows about the generic stream-json/result-event contract.
"""

from __future__ import annotations

import base64
import json
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

CLAUDE_FLAGS = [
    "--print", "--setting-sources", "project", "--tools", "", "--strict-mcp-config",
    "--no-session-persistence", "--input-format", "stream-json", "--output-format",
    "stream-json", "--verbose", "--model", "sonnet",
]
CLAUDE_BUDGET_FLAGS = ["--max-budget-usd", "0.50"]


def build_claude_command() -> list[str]:
    return ["claude"] + CLAUDE_FLAGS + CLAUDE_BUDGET_FLAGS


@dataclass
class ReadImage:
    """One ordered image attachment for the read call."""

    path: Path
    media_type: str = "image/jpeg"


def build_stream_message(text_blocks: list[str], images: list[ReadImage] | None = None) -> str:
    """One stream-json stdin line: a single `type: "user"` message whose
    `content` is the given text block(s) followed by zero or more ordered
    base64 image blocks, each carrying its own media type — exact shape
    verified against `fixtures/or1/*.cmd.txt` for the single-image case."""
    content: list[dict] = [{"type": "text", "text": t} for t in text_blocks]
    for image in images or []:
        data = base64.b64encode(image.path.read_bytes()).decode("ascii")
        content.append({"type": "image", "source": {"type": "base64", "media_type": image.media_type, "data": data}})
    msg = {"type": "user", "message": {"role": "user", "content": content}, "parent_tool_use_id": None}
    return json.dumps(msg) + "\n"


def parse_claude_stream_result(stdout_text: str) -> dict | None:
    """Scan stdout as JSON-lines for the final `type: "result"` event and pull
    the OR-1 usage fields — written against `tests/fixtures/instagram/
    read_response.jsonl` and `fixtures/or1/*.json` (real captures), not memory."""
    result_event = None
    for line in stdout_text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and obj.get("type") == "result":
            result_event = obj
    if result_event is None:
        return None
    usage = result_event.get("usage", {}) or {}
    model_usage = result_event.get("modelUsage", {}) or {}
    model_id = next(iter(model_usage.keys()), None)
    # WK-0087 pricing fix: the CLI reports cache-creation tokens split by TTL
    # under `usage.cache_creation` (`ephemeral_1h_input_tokens` /
    # `ephemeral_5m_input_tokens`) and bills the 1-hour bucket at a higher
    # rate than the generic (5-minute) rate `pricing.price_usage` used to
    # apply to all of it. Real evidence (WK-0087 steps 1-2, De9SalRGOhy): the
    # 20-slide golden's `cache_creation` is entirely `ephemeral_1h_input_tokens`
    # (73816 of 73816), and only pricing that split at its own rate reproduces
    # the CLI's own `modelUsage.*.costUSD` exactly.
    cache_creation = usage.get("cache_creation", {}) or {}
    return {
        "is_error": result_event.get("is_error"),
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "cache_read_tokens": usage.get("cache_read_input_tokens"),
        "cache_creation_tokens": usage.get("cache_creation_input_tokens"),
        "cache_creation_1h_tokens": cache_creation.get("ephemeral_1h_input_tokens"),
        "cache_creation_5m_tokens": cache_creation.get("ephemeral_5m_input_tokens"),
        "model": model_id,
        "result_text": result_event.get("result", ""),
        "raw": result_event,
    }


class ReadCallFailedError(RuntimeError):
    """The claude subprocess failed, timed out, returned no result event, or
    the result event itself reported `is_error: true`."""


@dataclass
class RawReadResult:
    """Generic read-call outcome: the result event's raw text plus usage —
    no domain-specific parsing. Adapters parse `result_text` into their own
    shape (e.g. the reel's `tools`/`on_screen_text` JSON)."""

    result_text: str
    raw_stdout: str
    usage: dict = field(default_factory=dict)


def run_claude_read(prompt: str, images: list[ReadImage] | None = None, *, timeout: int = 300) -> RawReadResult:
    """One read call (I3): fresh empty temp cwd, prompt + N ordered images on
    stdin as stream-json, usage read from the final result event."""
    msg = build_stream_message([prompt], images)
    with tempfile.TemporaryDirectory() as tmp:
        proc = subprocess.run(
            build_claude_command(), input=msg, capture_output=True, text=True, timeout=timeout, cwd=tmp,
        )
    parsed = parse_claude_stream_result(proc.stdout) if proc.stdout else None
    if parsed is None or proc.returncode != 0:
        raise ReadCallFailedError(proc.stderr.strip()[-800:] or "no result event in claude stdout")
    if parsed["is_error"]:
        raise ReadCallFailedError(f"claude returned is_error=true: {parsed['result_text'][:400]}")

    return RawReadResult(
        result_text=parsed["result_text"],
        raw_stdout=proc.stdout,
        usage={
            "input_tokens": parsed["input_tokens"],
            "output_tokens": parsed["output_tokens"],
            "cache_read_tokens": parsed["cache_read_tokens"],
            "cache_creation_tokens": parsed["cache_creation_tokens"],
            "cache_creation_1h_tokens": parsed["cache_creation_1h_tokens"],
            "cache_creation_5m_tokens": parsed["cache_creation_5m_tokens"],
            "model": parsed["model"],
        },
    )
