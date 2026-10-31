"""The one `SourceAdapter` registry and the one needs-link rewrite engine
(WK-0094 Phase B). A new source type is one new adapter registered here with
no edit to this module, `rendering.py`, `sources_writer.py`, or `cli.py`.

# DECISION: `adapters/` holds one module per source type (its needs-link URL
# rule, id parse, capture pipeline, and the sections it hands to the shared
# renderer/writer/review modules). `stages/` holds the shared capture-pipeline
# building blocks adapters call into (browser page capture, yt-dlp media
# fetch, audio decode+transcribe, keyframes+contact sheet, the multimodal
# read) — never copied per adapter. Top-level modules (`rendering.py`,
# `sources_writer.py`, `review.py`, `pricing.py`, this module) are the one
# shared format/engine every adapter feeds.

Registration is explicit and mutable (`register()`), not a hardcoded list —
`adapters/__init__.py` registers the two shipped adapters (Reddit, Instagram
reel) on import, and a test can register a throwaway adapter the same way
with no edit to this file (the extensibility claim, tested in
`test_adapter_extensibility.py`).
"""

from __future__ import annotations

import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol, runtime_checkable

from .rendering import render_block
from .sources_writer import render_source_md, write_source_file


class CaptureFailedError(RuntimeError):
    """Adapter-raised: an ordinary, expected capture failure. `str(e)` is
    the already-formatted message shown after '⚠ capture-failed {url} — '."""


class NeedsLinkSoftMarker(RuntimeError):
    """Adapter-raised: a terminal marker other than "capture-failed" (e.g.
    the Reddit adapter's PDF-download event). `reason` is the exact
    '⚠ <reason>' text (the adapter includes the url in it itself); `status`
    is the free-form label used in per-item result summaries."""

    def __init__(self, reason: str, status: str):
        self.reason = reason
        self.status = status
        super().__init__(reason)


@dataclass
class CaptureOutcome:
    """What an adapter hands back after a successful `capture()` + the
    engine's `captured_at` stamp: everything the shared renderer, the shared
    sources writer, and the needs-link summary line need. Adapters supply
    sections, not formats."""

    id: str
    source: str  # the inbox block's `source:` line value
    block_sections: list[str]  # raw (un-defused) sections for the shared block renderer
    source_header_lines: list[str]  # "key: value" lines for the sources .md header
    source_body: str  # body text/markdown for the sources .md (verbatim — never defused)
    artifacts: dict[str, Any] | None = None  # sibling artifact files for the sources writer
    mentioned_count: int = 0  # for the needs-link summary line (0 if not applicable)


@runtime_checkable
class SourceAdapter(Protocol):
    """The full adapter contract. The six members below are *required* —
    every adapter must define them itself. `BaseAdapter` (just below) is
    where the *optional* hooks live — `cleanup`, `describe_ok`, `broad_re`,
    `broad_hint`, `status_buckets`, `review_items`, `sample_reason` — each
    with a documented default so a new adapter author finds the whole
    contract (required here, optional on `BaseAdapter`) in one place. A new
    adapter should subclass `BaseAdapter` and define these six; it only
    needs to override an optional hook if it wants something other than
    that hook's default."""

    name: str  # registry key, used by --only
    platform_dir: str  # catalog/sources/<platform_dir>/
    delay_s: float  # default seconds between captures, used unless --delay overrides
    line_re: re.Pattern[str]  # matches a whole `⚠ needs-link <url>[ — reason]` line; group(1) = url

    def capture(self, url: str) -> Any:
        """Run the full capture pipeline for `url`. Returns an adapter-owned
        raw result on success. Raises `CaptureFailedError` or
        `NeedsLinkSoftMarker` on failure — never a sentinel return value."""

    def build_outcome(self, raw: Any, *, captured_at: str) -> CaptureOutcome:
        """Derive the shared renderer/writer inputs from a raw capture
        result plus the engine's `captured_at` stamp."""


class BaseAdapter:
    """Default implementations of every *optional* `SourceAdapter` hook —
    the declared contract for what used to be seven separate
    `getattr(adapter, name, default)` lookups in `registry.py`, `cli.py`,
    and `review.py` (WK-0094 Phase B review fix-up). A new adapter
    subclasses this plus defines the six required `SourceAdapter` members;
    it overrides only the hooks below it needs something other than the
    default for. Every default here is exactly the `getattr(...)` default
    each call site used before this class existed, so adopting it changes
    no observable output.
    """

    #: One shared default for `SourceAdapter.delay_s` (WK-0094 Phase B
    #: review fix-up) — previously a `DEFAULT_DELAY_S = 3.0` literal copied
    #: into both `adapters/reddit.py` and `adapters/instagram_reel.py`.
    #: Adapters may still override `delay_s` with a different value.
    DEFAULT_DELAY_S: float = 3.0

    #: Looser "this needs-link line is probably mine" pattern. Used by
    #: `unmatched_needs_link_lines` to name a malformed/unexpected line for
    #: this adapter instead of leaving it silently unreported. Default: `None`
    #: (this adapter is never named in a near-miss report).
    broad_re: re.Pattern[str] | None = None

    #: Human-readable label used in the "not matched by the <hint>" line
    #: `cli.py` prints for a `broad_re` near-miss. Default: a generic label.
    broad_hint: str = "its pattern"

    #: Extra terminal status labels (besides "ok"/"failed") this adapter's
    #: `capture()` can produce via `NeedsLinkSoftMarker` (e.g. the Reddit
    #: adapter's `"pdf"`) — shown in the needs-link summary line even at
    #: zero. Default: none.
    status_buckets: tuple[str, ...] = ()

    def cleanup(self, raw: Any) -> None:
        """Release any resources tied to a raw capture result (e.g. a loose
        tempfile) after the engine has rendered and written it, whether that
        write succeeded or not. Default: no-op."""

    def describe_ok(self, result: ItemResult) -> str | None:
        """One extra line of detail to print under a successful capture in
        the needs-link summary (`cli.py`). Default: no extra line (returns
        `None`, printed as nothing)."""
        return None

    def review_items(self, sources_dir: Path) -> list[Any]:
        """Rebuild this adapter's `review.ReviewItem` list from its own
        already-written files under `sources_dir`, for the `review build`
        command. Default: no review items (the adapter opts out of
        review — equivalent to it not participating at all)."""
        return []

    def sample_reason(self, item: Any) -> str | None:
        """Adapter-owned rule flagging which of its own captured items
        deserve an operator spot-check (`review.suggest_sample`, WK-0094
        OR-5). Default: `None` (defers to the caller's own "first captured"
        fallback)."""
        return None

    def sample_picks(self, items: list[Any]) -> list[tuple[Any, str]] | None:
        """Adapter-owned rule that picks its own suggested sample across its
        *whole* batch of captured items at once (WK-0087 fix-up) — for a
        rule that needs to compare items against each other (e.g. "the item
        with the most slides", "the lowest cross-tool agreement"), which
        `sample_reason`'s one-item-at-a-time signature can't express.
        `items` is this adapter's own `review.ReviewItem` list (only), in
        whatever order the caller's `items` list carries them. Returns an
        ordered list of (item, reason) pairs this adapter wants in the
        sample, or `None` (default) to defer entirely to
        `review.suggest_sample`'s per-item `sample_reason` fallback. The
        caller still applies its own overall cap."""
        return None


_REGISTRY: dict[str, SourceAdapter] = {}


def register(adapter: SourceAdapter) -> SourceAdapter:
    _REGISTRY[adapter.name] = adapter
    return adapter


def unregister(name: str) -> None:
    _REGISTRY.pop(name, None)


def registered_adapters() -> list[SourceAdapter]:
    return list(_REGISTRY.values())


def get_adapter(name: str) -> SourceAdapter | None:
    return _REGISTRY.get(name)


# Matches any `⚠ needs-link` line at all, regardless of platform — the one
# scan the engine runs; each adapter's own `line_re` decides whether it owns
# a given line. A line no adapter matches is returned untouched (`repl`'s
# fallback), same as a precise-regex miss did pre-refactor.
ANY_NEEDS_LINK_LINE_RE = re.compile(r"^⚠ needs-link [^\n]*$", re.MULTILINE)


@dataclass
class ItemResult:
    url: str
    status: str  # adapter/engine-defined: 'ok' | 'failed' | or an adapter-specific soft status (e.g. 'pdf')
    adapter: str | None = None
    id: str | None = None
    error: str | None = None
    mentioned_count: int = 0


def _adapter_for_line(line: str, adapters: list[SourceAdapter]) -> tuple[SourceAdapter, str] | None:
    for adapter in adapters:
        m = adapter.line_re.match(line)
        if m:
            return adapter, m.group(1)
    return None


def process_needs_link(
    text: str,
    *,
    sources_dir: Path,
    adapters: list[SourceAdapter],
    limit: int | None = None,
    delay_s: float | None = None,
) -> tuple[str, list[ItemResult]]:
    """Replace every `⚠ needs-link` line any adapter owns (up to `limit`)
    with its outcome: a fenced block, a `⚠ capture-failed`/adapter-specific
    marker, or — for a line no adapter matches — the line untouched.

    Capture happens sequentially, with `delay_s` (or, when not given, the
    matched adapter's own `delay_s`) between loads, not before the first
    item overall — the WK-0054 session-state decision to avoid tripping a
    platform's rate limits by running concurrently, now applied once across
    every registered adapter instead of once per platform."""
    results: list[ItemResult] = []
    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        line = m.group(0)
        found = _adapter_for_line(line, adapters)
        if found is None:
            return line
        adapter, url = found

        if limit is not None and count >= limit:
            return line
        effective_delay = delay_s if delay_s is not None else adapter.delay_s
        if count > 0 and effective_delay:
            time.sleep(effective_delay)
        count += 1

        try:
            raw = adapter.capture(url)
        except NeedsLinkSoftMarker as e:
            results.append(ItemResult(url=url, status=e.status, adapter=adapter.name))
            return f"⚠ {e.reason}"
        except CaptureFailedError as e:
            err = str(e)
            results.append(ItemResult(url=url, status="failed", adapter=adapter.name, error=err))
            return f"⚠ capture-failed {url} — {err}"
        except Exception as e:  # noqa: BLE001 - fail loud, keep the line blocked
            err = " ".join(str(e).split())
            results.append(ItemResult(url=url, status="failed", adapter=adapter.name, error=err))
            return f"⚠ capture-failed {url} — {err}"

        captured_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        stage = "render"
        try:
            outcome = adapter.build_outcome(raw, captured_at=captured_at)
            block_text = render_block(source=outcome.source, sections=outcome.block_sections)
            md = render_source_md(header_lines=outcome.source_header_lines, body=outcome.source_body)
            stage = "write"
            write_source_file(sources_dir, adapter.platform_dir, outcome.id, md, artifacts=outcome.artifacts)
        except OSError as e:
            # One bad write must not cost the rest of the batch: mark this
            # item capture-failed and let `re.sub` move on to the next line.
            err = " ".join(str(e).split())
            results.append(ItemResult(url=url, status="failed", adapter=adapter.name, error=f"{stage}: {err}"))
            return f"⚠ capture-failed {url} — {stage}: {err}"
        finally:
            adapter.cleanup(raw)

        results.append(ItemResult(
            url=url, status="ok", adapter=adapter.name, id=outcome.id, mentioned_count=outcome.mentioned_count,
        ))
        return block_text

    out = ANY_NEEDS_LINK_LINE_RE.sub(repl, text)
    return out, results


def unmatched_needs_link_lines(text: str, adapters: list[SourceAdapter]) -> list[tuple[SourceAdapter, str]]:
    """For every `⚠ needs-link` line in `text`, check each adapter's own
    `broad_re` (a looser "this is probably meant for me" pattern) — the
    generalized form of the two broad regexes `cli.py` used to hardcode one
    per platform. Returns (adapter, line) for every line a `broad_re`
    recognizes but no adapter's precise `line_re` actually matched — so a
    malformed/unexpected shape for a *known* platform is surfaced by name,
    same as before. A line no adapter's `broad_re` recognizes at all (a
    different, not-yet-supported platform) is not reported, same as before."""
    out: list[tuple[SourceAdapter, str]] = []
    for line in ANY_NEEDS_LINK_LINE_RE.findall(text):
        if _adapter_for_line(line, adapters) is not None:
            continue
        for adapter in adapters:
            if adapter.broad_re is not None and adapter.broad_re.match(line):
                out.append((adapter, line))
                break
    return out
