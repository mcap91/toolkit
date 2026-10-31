"""Shared inbox-block renderer (WK-0094 Phase B). One `source:` line plus
adapter-supplied body sections, inside a ```text fence, with the inbox's
fence-break defusal applied once to the fully-assembled body. Adapters
supply raw (un-defused) sections, in order — this is the one place
`defuse_fence_breaks` is applied to block content, not a per-adapter copy.

Design input from the Phase B baseline: `render_block` returns the block
with **no trailing newline** — the rewrite engine (`registry.py`) owns line
endings (the baseline's `re.sub` only replaces the matched span, so the
original line's trailing `\\n` survives after the substituted block)."""

from __future__ import annotations

from .fence import defuse_fence_breaks


def render_block(*, source: str, sections: list[str]) -> str:
    """`sections` are joined with a blank line between them (matching both
    the Reddit single-section body and the Instagram multi-section body,
    byte-for-byte against the pre-refactor renderers)."""
    body = "\n\n".join(sections)
    safe_body = defuse_fence_breaks(body)
    return f"```text\nsource: {source}\n{safe_body}\n```"


def render_hints_block(hints: list[dict]) -> str:
    """`- <name>: <url or '(no url)'>` per hint, one per line, or
    `(none mentioned)` if empty — the one shared "Mentioned (unverified
    hints)" line format for every adapter that surfaces unverified
    tool/repo/project hints straight from a read (OR-3): the Instagram reel
    adapter, and the Instagram post adapter (WK-0087). Consolidates what
    used to be two copies of this exact formatting rule (`instagram_rewrite.
    py`'s and `instagram_sources.py`'s `_hint_line`, WK-0094's own finding)
    back into a per-adapter private function each time a new adapter needs
    it — one shared function instead."""
    if not hints:
        return "(none mentioned)"
    return "\n".join(f"- {h.get('name')}: {h.get('url') or '(no url)'}" for h in hints)
