"""Instagram reel adapter (WK-0094 Phase B; formerly `instagram_rewrite.py` +
`instagram_capture.py` + `instagram_probe.py` + half of `instagram_read.py`).
Needs-link URL rule, id parse, the full capture pipeline (via the shared
`stages.media` / `stages.transcribe` / `stages.frames` / `stages.read`
stages), block body, and sources-file body/artifacts all live here.

OR-3 (operator ruling, supersedes G1/G2/I1/I2/I9): "reel -> transcript and
capture of images etc -> agent decides what goes into the catalog ... the
agent should be the one making the call." The capture never verifies a
tool's URL or decides what the reel is "about" — it produces exactly **one**
fenced block per reel, `source: <reel url>`, carrying the caption,
transcript, on-screen text, key claims, and whatever tools/URLs the read
spotted, labeled as unverified hints.

Only `/reel/` URLs are matched — Instagram carousels (`/p/`) stay
`⚠ needs-link` until the carousel adapter lands (WK-0087).
"""

from __future__ import annotations

import json
import os
import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from .. import pricing
from .. import versions as ver
from ..registry import BaseAdapter, CaptureFailedError, CaptureOutcome
from ..rendering import render_hints_block
from ..stages import frames, media, transcribe
from ..stages.read import ReadImage, run_claude_read

# Mirrors the host rule this package and drain.ts would need for Instagram —
# but drain.ts already blocks every instagram.com URL unconditionally via
# `hostBlocked()` + `catalog/config.json`'s `blocked_domains` entry (no
# `allow_paths`), regardless of path (I7). So this regex only needs to match
# what this adapter can itself resolve: `/reel/<id>` needs-link lines.
INSTAGRAM_NEEDS_LINK_RE = re.compile(
    r"^⚠ needs-link ("
    r"(?:https?://)?(?:www\.)?instagram\.com/reel/[^/\s?#]+/?(?:[?#]\S*)?"
    r")(?:\s+—\s+[^\n]*)?$",
    re.MULTILINE | re.IGNORECASE,
)

# Same idea as reddit.py's BROAD_REDDIT_NEEDS_LINK_LINE: any needs-link line
# mentioning instagram.com, matched or not — so a carousel (`/p/...`, WK-0087)
# or any other unhandled Instagram shape is surfaced by name instead of
# silently staying `⚠ needs-link` forever with no explanation.
BROAD_INSTAGRAM_NEEDS_LINK_LINE = re.compile(r"^⚠ needs-link [^\n]*instagram\.com[^\n]*$", re.MULTILINE | re.IGNORECASE)

REEL_ID_RE = re.compile(r"/reel/([A-Za-z0-9_-]+)/?")


def reel_id_from_url(url: str) -> str | None:
    m = REEL_ID_RE.search(url)
    return m.group(1) if m else None


# --------------------------------------------------------------------------
# Shared section-split helper (WK-0087 second fix-up): `review_items` on
# both this adapter and `instagram_post.py` used to split a sources-file
# body on a generic `\n##\s+` pattern — any line shaped like a markdown
# heading. Real data broke this: a captured slide's own text legitimately
# contained a Python comment line `## HOUSE_RULES`, which the generic split
# mistook for a new section boundary and cut the real "Slides" section
# short (slides 17-20 fell into a fake "HOUSE_RULES" section). Section
# content (slide text, transcript, on-screen text, etc.) is untrusted,
# verbatim capture text and can contain any line, including one that
# exactly matches a real heading's text — so this helper only ever splits
# on the exact, known heading list a writer emits, in the order it emits
# them, never a generic pattern.
# --------------------------------------------------------------------------


def split_known_sections(body: str, headings: list[str]) -> dict[str, str]:
    """Splits a sources-file `body` into the named sections in
    `build_outcome`'s own `source_body` — the exact `## <heading>` lines a
    writer emits, in the order it emits them (e.g. `["Caption", "Slides",
    "Mentioned (unverified hints)"]` for the post adapter). Returns
    {heading: content} for however many of `headings` are found; a heading
    that never occurs (a differently-shaped or corrupt file) is simply
    absent from the result.

    Boundary rule: the *last* heading in `headings` is located by its
    *last* occurrence in the whole text — nothing legitimate follows the
    final section, so any earlier occurrence of that exact heading line
    can only be inside an earlier section's own untrusted content (the
    real WK-0087 case: a slide's text containing a line that reads exactly
    like a section heading). Every other heading is located by its
    *first* occurrence after the previous boundary already found, since
    that heading's own real content has not started yet at that point."""
    text = "\n" + body
    markers = [f"\n## {h}\n" for h in headings]
    positions: list[int] = []
    search_from = 0
    last = len(markers) - 1
    for i, marker in enumerate(markers):
        idx = text.rfind(marker) if i == last else text.find(marker, search_from)
        positions.append(idx)
        if idx != -1:
            search_from = idx + len(marker)

    sections: dict[str, str] = {}
    for i, heading in enumerate(headings):
        start = positions[i]
        if start == -1:
            continue
        content_start = start + len(markers[i])
        content_end = len(text)
        for j in range(i + 1, len(headings)):
            if positions[j] != -1:
                content_end = positions[j]
                break
        sections[heading] = text[content_start:content_end].strip()
    return sections


# The exact heading order `InstagramReelAdapter.build_outcome` writes
# (`source_body` below) — `review_items` splits on this list, never a
# generic `## ` pattern.
REEL_SECTION_HEADINGS = [
    "Caption",
    "Transcript",
    "On-screen text",
    "Key claims",
    "Info channel",
    "Mentioned (unverified hints)",
]


class InstagramCaptureError(RuntimeError):
    """Any stage of the Instagram pipeline failed. Carries the stage name and
    the original error text, so the inbox marker can say which stage broke."""

    def __init__(self, stage: str, original: BaseException | str):
        self.stage = stage
        self.original_text = str(original)
        super().__init__(f"{stage}: {self.original_text}")


class ReadResponseUnparsableError(RuntimeError):
    """The read's result text did not contain the expected `tools`/
    `on_screen_text`/`key_claims`/`info_channel` JSON object."""


@dataclass
class InstagramCaptureResult:
    reel_id: str
    reel_url: str
    info_json_text: str
    caption: str | None
    transcript_text: str
    sheet_path: Path
    on_screen_text: str
    key_claims: list[str] = field(default_factory=list)
    info_channel: str = ""
    # Raw `{"name": str, "url": str | None}` entries straight from the read
    # (OR-3: "Mentioned (unverified hints)" — never HTTP-checked or
    # GitHub-normalized at capture time; the processing agent decides what,
    # if anything, each one becomes).
    tools: list[dict] = field(default_factory=list)
    read_raw_stdout: str = ""
    read_usd: float | None = None
    read_usd_reason: str | None = None
    versions: dict[str, str] = field(default_factory=dict)
    # True when `sheet_path` is a loose OS tempfile this call created (the
    # `workdir=None` default) that nothing else owns — the caller must delete
    # it once done reading it (after copying it into the sources dir), even on
    # a failure path, or it leaks in /tmp forever. False when `sheet_path`
    # lives inside a caller-supplied `workdir`, whose lifecycle is the
    # caller's to manage.
    sheet_is_temp: bool = False


def build_read_prompt(caption: str | None, transcript_text: str) -> str:
    """This slice's read prompt (I3): a *list* of named tools (G2: one reel
    can name several) plus the on-screen text itself — used to list each
    tool as an unverified hint (OR-3) and to fill the sources file's
    "on-screen text" field."""
    caption_block = caption or "(no caption captured)"
    return f"""You are shown the caption posted with an Instagram reel, a transcript of its spoken audio, and an attached contact sheet image tiling keyframes extracted from the reel's video.

Caption (posted with the reel):
\"\"\"
{caption_block}
\"\"\"

Transcript (spoken audio, timestamps in seconds):
\"\"\"
{transcript_text}
\"\"\"

Based on the attached contact sheet image, the caption, and the transcript, answer:
1. List every distinct tool, repo, or named project this reel is about or demonstrates. For each one, give its name and its URL if the URL is visible on screen in the contact sheet, spoken aloud in the transcript, or given in the caption — otherwise null for that tool's url. If the reel names no tool/repo/project, return an empty list.
2. Transcribe any text visible on screen in the contact sheet image (filenames, shell commands, URLs, step labels, UI labels, etc.) into one string, in reading order. Empty string if no text is visible.
3. List the key claims made in the reel.
4. Which channel carried the key information: "spoken" (the transcript), "on-screen" (visible in the contact sheet image), or "caption" (the posted caption text)?

Respond with ONLY a JSON object matching this exact shape, no other text before or after it:
{{
  "tools": [{{"name": "<string>", "url": "<string or null>"}}],
  "on_screen_text": "<string>",
  "key_claims": ["<string>", "<string>", "..."],
  "info_channel": "spoken" | "on-screen" | "caption"
}}"""


def _parse_read_response(result_text: str) -> dict:
    m = re.search(r"\{.*\}", result_text, re.DOTALL)
    if not m:
        raise ReadResponseUnparsableError(f"no JSON object in result text: {result_text[:400]}")
    try:
        obj = json.loads(m.group(0))
    except json.JSONDecodeError as e:
        raise ReadResponseUnparsableError(f"result text JSON did not parse: {e}") from e

    tools = obj.get("tools")
    if not isinstance(tools, list):
        raise ReadResponseUnparsableError(f'"tools" missing or not a list: {obj.get("tools")!r}')

    return {
        "tools": [{"name": t.get("name"), "url": t.get("url")} for t in tools if isinstance(t, dict) and t.get("name")],
        "on_screen_text": str(obj.get("on_screen_text") or ""),
        "key_claims": [str(c) for c in obj.get("key_claims") or []],
        "info_channel": str(obj.get("info_channel") or ""),
    }


def _tool_versions() -> dict[str, str]:
    return {
        "yt-dlp": ver.yt_dlp_version(),
        "ffmpeg": ver.ffmpeg_version(),
        "faster-whisper": ver.faster_whisper_version(),
        "ctranslate2": ver.ctranslate2_version(),
        "claude": ver.claude_version(),
    }


def _write_temp_sheet(data: bytes) -> Path:
    """The caller's own tempdir is about to be cleaned up — persist the sheet
    bytes to a fresh tempfile that outlives this call, so the result's
    `sheet_path` stays valid."""
    fd, name = tempfile.mkstemp(suffix=".jpg", prefix="ig-sheet-")
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    return Path(name)


def capture_instagram_reel(
    url: str, *, workdir: Path | None = None, prices_path: Path | None = None
) -> InstagramCaptureResult:
    """Run the full pipeline against a live Instagram reel URL: probe caption
    -> audio -> transcribe -> video -> frames/contact sheet -> one read.
    Raises `InstagramCaptureError` naming the stage that failed."""
    reel_id = reel_id_from_url(url)
    if reel_id is None:
        raise InstagramCaptureError("probe", f"could not parse a reel id from {url!r}")

    own_tmp = workdir is None
    tmp_ctx = tempfile.TemporaryDirectory() if own_tmp else None
    outdir = Path(tmp_ctx.name) if own_tmp else Path(workdir)
    outdir.mkdir(parents=True, exist_ok=True)

    try:
        try:
            probe_result = media.probe_caption(url)
        except Exception as e:  # noqa: BLE001 - fail loud, name the stage
            raise InstagramCaptureError("probe", e) from e

        try:
            audio_path = media.download_audio(url, outdir)
        except Exception as e:  # noqa: BLE001
            raise InstagramCaptureError("audio", e) from e

        try:
            pcm_path = transcribe.decode_to_pcm(audio_path, outdir)
            transcribed = transcribe.transcribe_small_cpu_int8(pcm_path)
        except Exception as e:  # noqa: BLE001
            raise InstagramCaptureError("transcribe", e) from e

        try:
            video_path = media.download_video(url, outdir)
            sheet_path = frames.extract_contact_sheet(video_path, outdir)
        except Exception as e:  # noqa: BLE001
            raise InstagramCaptureError("frames", e) from e

        prompt = build_read_prompt(probe_result.caption, transcribed.text)
        try:
            raw_read = run_claude_read(prompt, [ReadImage(sheet_path)])
            parsed = _parse_read_response(raw_read.result_text)
        except Exception as e:  # noqa: BLE001
            raise InstagramCaptureError("read", e) from e

        usd, usd_reason = pricing.price_usage(raw_read.usage, prices_path=prices_path)

        # The contact sheet file must outlive a self-owned tmpdir, since the
        # caller reads it after this function returns (to copy it into the
        # sources dir). Persist it under the caller-visible workdir path when
        # we created our own tempdir, by reading the bytes now.
        sheet_bytes = sheet_path.read_bytes()
        persisted_sheet = outdir / "sheet.jpg" if not own_tmp else None

        return InstagramCaptureResult(
            reel_id=reel_id,
            reel_url=url,
            info_json_text=probe_result.info_json_text,
            caption=probe_result.caption,
            transcript_text="\n".join(transcribed.transcript_lines),
            sheet_path=persisted_sheet or _write_temp_sheet(sheet_bytes),
            on_screen_text=parsed["on_screen_text"],
            key_claims=parsed["key_claims"],
            info_channel=parsed["info_channel"],
            tools=parsed["tools"],
            read_raw_stdout=raw_read.raw_stdout,
            read_usd=usd,
            read_usd_reason=usd_reason,
            versions=_tool_versions(),
            sheet_is_temp=own_tmp,
        )
    finally:
        if tmp_ctx is not None:
            # Keep the tempdir alive only long enough to read the sheet bytes
            # above; _write_temp_sheet() has already persisted a copy.
            tmp_ctx.cleanup()


def cleanup_sheet(cap: InstagramCaptureResult) -> None:
    """Delete the loose OS tempfile `capture_instagram_reel` created for
    `cap.sheet_path` (`sheet_is_temp=True`), once the caller is done reading
    it. A no-op when the sheet lives in a caller-supplied `workdir` instead."""
    if cap.sheet_is_temp:
        Path(cap.sheet_path).unlink(missing_ok=True)


class InstagramReelAdapter(BaseAdapter):
    name = "instagram_reel"
    platform_dir = "instagram"
    # WK-0094 Phase B review fix-up: one shared default (`BaseAdapter.
    # DEFAULT_DELAY_S`), not a `DEFAULT_DELAY_S = 3.0` literal copied into
    # this module.
    delay_s = BaseAdapter.DEFAULT_DELAY_S
    line_re = INSTAGRAM_NEEDS_LINK_RE
    broad_re = BROAD_INSTAGRAM_NEEDS_LINK_LINE
    broad_hint = "/reel/ pattern"

    def __init__(
        self,
        capture_fn: Callable[[str], InstagramCaptureResult] | None = None,
        *,
        prices_path: Path | None = None,
    ):
        self._prices_path = prices_path
        self._capture_fn = capture_fn or (lambda url: capture_instagram_reel(url, prices_path=prices_path))

    def capture(self, url: str) -> InstagramCaptureResult:
        try:
            return self._capture_fn(url)
        except InstagramCaptureError as e:
            raise CaptureFailedError(str(e)) from e
        except Exception as e:  # noqa: BLE001 - fail loud, keep the line blocked
            raise CaptureFailedError(" ".join(str(e).split())) from e

    def build_outcome(self, raw: InstagramCaptureResult, *, captured_at: str) -> CaptureOutcome:
        claims_block = "\n".join(f"- {c}" for c in raw.key_claims) if raw.key_claims else "(none)"
        hints_block = render_hints_block(raw.tools)

        block_sections = [
            f"Caption:\n{raw.caption or '(no caption captured)'}",
            f"Transcript:\n{raw.transcript_text}",
            f"On-screen text:\n{raw.on_screen_text or '(none)'}",
            f"Key claims:\n{claims_block}",
            f"Mentioned (unverified hints):\n{hints_block}",
        ]
        source_body = "\n\n".join([
            f"## Caption\n\n{raw.caption or '(no caption captured)'}",
            f"## Transcript\n\n{raw.transcript_text}",
            f"## On-screen text\n\n{raw.on_screen_text or '(none)'}",
            f"## Key claims\n\n{claims_block}",
            f"## Info channel\n\n{raw.info_channel or '(unknown)'}",
            f"## Mentioned (unverified hints)\n\n{hints_block}",
        ]) + "\n"

        return CaptureOutcome(
            id=raw.reel_id,
            source=raw.reel_url,  # OR-3: source is always the reel URL itself
            block_sections=block_sections,
            source_header_lines=[f"reel: {raw.reel_url}", f"captured: {captured_at}"]
            + [f"{name}: {v}" for name, v in raw.versions.items()],
            source_body=source_body,
            artifacts={
                "info.json": raw.info_json_text,
                "transcript.txt": raw.transcript_text,
                "sheet.jpg": raw.sheet_path,
                "read_response.jsonl": raw.read_raw_stdout,
            },
            mentioned_count=len(raw.tools),
        )

    def cleanup(self, raw: InstagramCaptureResult) -> None:
        cleanup_sheet(raw)

    def describe_ok(self, result) -> str:
        """Per-item needs-link summary detail for a successful capture
        (cli.py) — this adapter's own wording, not a shared-code special
        case for "reel"."""
        return f"captured reel {result.id}: {result.mentioned_count} tool(s) mentioned (unverified)"

    # -- review (WK-0094): rebuild review sections from an already-written
    # sources .md + its sibling artifacts dir. ---------------------------

    def review_items(self, sources_dir: Path):
        from ..review import ReviewItem

        out_dir = Path(sources_dir) / self.platform_dir
        items = []
        if not out_dir.is_dir():
            return items
        for md_path in sorted(out_dir.glob("*.md")):
            text = md_path.read_text(encoding="utf-8")
            if not text.startswith("reel: "):
                # Not one of this adapter's own captures (WK-0087 fix-up):
                # `catalog/sources/instagram/` also holds the post/carousel
                # adapter's files, whose first header line is `post: <url>`,
                # never `reel: `. Skip — the post adapter owns its own items.
                continue
            lines = text.split("\n")
            url = lines[0][len("reel: "):]
            reel_id = md_path.stem
            body = text.split("\n\n", 1)[1] if "\n\n" in text else ""
            parsed = split_known_sections(body, REEL_SECTION_HEADINGS)

            # Port of make_review.py's layout: a "What we captured" section
            # groups the read's own fields (info channel, on-screen text, key
            # claims, unverified tool hints); Caption/Transcript/Contact
            # sheet stay their own sections, same as the reel-only bench.
            what_we_captured = "\n\n".join(
                filter(None, [
                    parsed.get("Info channel") and f"**Info channel:** {parsed['Info channel']}",
                    parsed.get("On-screen text") and f"**On-screen text:**\n\n{parsed['On-screen text']}",
                    parsed.get("Key claims") and f"**Key claims:**\n\n{parsed['Key claims']}",
                    parsed.get("Mentioned (unverified hints)")
                    and f"**Mentioned (unverified hints):**\n\n{parsed['Mentioned (unverified hints)']}",
                ])
            )
            sections = [("What we captured", what_we_captured)]
            if "Caption" in parsed:
                sections.append(("Caption", parsed["Caption"]))
            if "Transcript" in parsed:
                sections.append(("Transcript", parsed["Transcript"]))
            sheet_path = out_dir / reel_id / "sheet.jpg"
            if sheet_path.exists():
                # Absolute path (WK-0087 fix-up): `review.render_sheet`
                # relativizes this against the sheet's own `out_dir` at
                # write time, which may differ from `sources_dir` (the bug
                # this fixes — a link relative to `sources_dir` only
                # resolved when `--out` happened to equal it).
                sections.append(("Contact sheet", f"![contact sheet]({sheet_path.resolve()})"))
            items.append(ReviewItem(adapter=self.name, item_id=reel_id, url=url, sections=sections))
        return items
