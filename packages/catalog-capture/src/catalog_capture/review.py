"""Shared review module (WK-0094 Phase B), replacing the reel-only
`toolkit-workbench/reel/scripts/make_review.py` for every registered
adapter: a pre-filled review sheet per captured item, a `REVIEW.md` index
with a suggested sample, and a verdict tally. Ported layout (header, link,
`**Verdict:**`/`**Notes:**` lines, then markdown sections) from
`make_review.py`'s `render_sheet`/`write_review_md`/`tally` — re-implemented
here against this package's own adapters, not imported from the gitignored
workbench (R9).

This module never writes a verdict — `groundtruth` sheets are operator-owned
(WK-0079 S9 / OR-2: finder != verifier, kb SRC-0024 RD-16/RD-31). Adapters
supply the "what we captured" sections (and, optionally, which of their own
items belong in the suggested sample); this module owns the one sheet/index/
tally format.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

VERDICT_LINE_RE = re.compile(r'^\*\*Verdict:\*\*\s*(.*)$')
COMMENT_RE = re.compile(r'<!--.*?-->')

# Matches a markdown *image* link whose target is an absolute filesystem
# path, e.g. `![slide 3](/abs/path/to/slide_03.jpg)` — never a plain link
# (`[text](url)`) and never an image link that's already a relative path or
# an http(s) URL (WK-0087 fix-up: adapters hand this module the slide/sheet
# image's absolute path; this module is the one place that knows the sheet's
# own on-disk location, so it's the one place that can make the link
# resolve from there).
IMAGE_LINK_RE = re.compile(r'(!\[[^\]]*\]\()(/[^)\s]+)(\))')

# WK-0094 OR-5: the operator spot-checks at most 5 sheets total, not per
# adapter — "I am not doing that for 12 ... I will do that for at most 5."
SAMPLE_CAP = 5


@dataclass
class ReviewItem:
    """One row the review module can render a sheet for — adapter-agnostic.
    `sections` are (heading, body-markdown) pairs, supplied by the adapter
    (e.g. "What we captured", "Caption", "Transcript", "Contact sheet")."""

    adapter: str
    item_id: str
    url: str
    sections: list[tuple[str, str]] = field(default_factory=list)


def _relativize_image_links(markdown: str, out_dir: Path) -> str:
    """Rewrites every absolute-path image link in `markdown` to a path
    relative to `out_dir` — the directory the sheet containing this markdown
    is about to be written into (WK-0087 fix-up). An adapter hands
    `review_items()` the slide/sheet image's absolute on-disk path baked
    into the markdown precisely so this one spot, which is the only place
    that knows the sheet's own write location, can make the link resolve
    from there instead of from wherever the adapter happened to read the
    image from (the sources dir, not necessarily `out_dir`)."""
    def repl(m: re.Match[str]) -> str:
        rel = os.path.relpath(m.group(2), out_dir)
        return f"{m.group(1)}{rel}{m.group(3)}"
    return IMAGE_LINK_RE.sub(repl, markdown)


def render_sheet(item: ReviewItem, out_dir: Path) -> str:
    sections_md = "\n\n".join(f"## {heading}\n\n{body}" for heading, body in item.sections)
    sections_md = _relativize_image_links(sections_md, out_dir)
    return f"""# {item.adapter} {item.item_id}

[{item.url}]({item.url})

**Verdict:** <!-- yes / good enough / wrong / no / missed <x> -->

**Notes:** <!-- free text -->

{sections_md}
"""


def sheet_filename(item: ReviewItem) -> str:
    return f"{item.adapter}-{item.item_id}.md"


def _sample_reason(adapter_obj: object | None, item: ReviewItem) -> str | None:
    """Adapter-supplied sample rule (`BaseAdapter.sample_reason`'s default
    returns None), if the adapter has one; otherwise None (the caller falls
    back to a default rule). `adapter_obj` is None when the caller's
    `adapters` dict has no entry for this item's adapter name."""
    if adapter_obj is None:
        return None
    return adapter_obj.sample_reason(item)


def suggest_sample(
    items: list[ReviewItem], *, adapters: dict[str, object] | None = None, cap: int = SAMPLE_CAP
) -> list[tuple[ReviewItem, str]]:
    """Returns up to `cap` (ReviewItem, reason) pairs.

    An adapter gets first say over its own items via `sample_picks(items)`
    (WK-0087 fix-up) — a whole-batch rule (e.g. "most slides", "lowest
    cross-tool agreement") that a one-item-at-a-time hook can't express.
    When an adapter's `sample_picks` returns non-`None`, those picks are
    used verbatim (cap-limited) for every item of that adapter, and the
    per-item fallback below never runs for it.

    Absent that, each registered adapter may supply its own
    `sample_reason(item) -> str | None` to flag items worth a spot-check;
    absent that too, the default rule flags the first item of each adapter
    ("first captured") so the sample is never empty while still respecting
    the hard cap (WK-0094 OR-5). This fallback path is unchanged from
    before `sample_picks` existed."""
    adapters = adapters or {}

    # Resolve each present adapter's whole-batch picks once, up front, from
    # its own item sublist only (first-seen order) — before the per-item
    # sweep below, so a `sample_picks` adapter's items are never re-touched
    # by the per-item fallback.
    forced: dict[str, list[tuple[ReviewItem, str]]] = {}
    for name in dict.fromkeys(item.adapter for item in items):  # first-seen order, deduped
        adapter_obj = adapters.get(name)
        if adapter_obj is None:
            continue
        sub_items = [i for i in items if i.adapter == name]
        picks = adapter_obj.sample_picks(sub_items)
        if picks is not None:
            forced[name] = picks

    picked: list[tuple[ReviewItem, str]] = []
    seen_adapters: set[str] = set()
    handled_forced: set[str] = set()
    for item in items:
        if len(picked) >= cap:
            break
        if item.adapter in forced:
            if item.adapter in handled_forced:
                continue
            handled_forced.add(item.adapter)
            seen_adapters.add(item.adapter)
            for pick_item, reason in forced[item.adapter]:
                if len(picked) >= cap:
                    break
                picked.append((pick_item, reason))
            continue
        reason = _sample_reason(adapters.get(item.adapter), item)
        if reason is None and item.adapter not in seen_adapters:
            reason = "first captured"
        if reason is not None:
            picked.append((item, reason))
            seen_adapters.add(item.adapter)
    return picked[:cap]


def write_sheets(items: list[ReviewItem], out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for item in items:
        path = out_dir / sheet_filename(item)
        path.write_text(render_sheet(item, out_dir), encoding="utf-8")
        written.append(path)
    return written


def render_index(items: list[ReviewItem], sample: list[tuple[ReviewItem, str]]) -> str:
    def row(item: ReviewItem, reason: str | None) -> str:
        link = f"[{item.item_id}]({item.url})"
        sheet = f"[sheet]({sheet_filename(item)})"
        cells = [item.adapter, link, sheet]
        if reason is not None:
            cells.append(reason)
        return "| " + " | ".join(cells) + " |"

    sample_lines = "\n".join(row(item, reason) for item, reason in sample)
    all_lines = "\n".join(row(item, None) for item in items)

    return f"""# Catalog capture review

Operator spot-check, not ground truth (WK-0079 OR-2, WK-0094 Phase B). Each sheet below is
pre-filled with what the adapter captured; the operator compares it with the source and writes
one verdict per sheet.

## How to spot-check a sheet

1. Open the sheet and read "What we captured".
2. Open the source URL (or the linked artifacts) and compare.
3. Fill in the `**Verdict:**` line with exactly one of: `yes` / `good enough` / `wrong` /
   `no` / `missed <x>` (name what was missed). Add any free-text notes on the `**Notes:**` line.

Sheets are never pre-filled with a verdict — review is operator-owned (WK-0079 OR-2: finder !=
verifier).

## Suggested spot-check sample ({len(sample)} of {len(items)}, capped at {SAMPLE_CAP} per WK-0094 OR-5)

| adapter | item | sheet | why sampled |
|---|---|---|---|
{sample_lines}

## All {len(items)} items

| adapter | item | sheet |
|---|---|---|
{all_lines}

## Tally

Run after filling in verdicts:

```
uv run python -m catalog_capture review tally --out <this directory>
```

This counts the `**Verdict:**` value in every sheet (blank = unchecked) and prints counts with
n. Not filled in by this module — verdicts are operator-owned.
"""


def build_review(
    items: list[ReviewItem], out_dir: Path, *, adapters: dict[str, object] | None = None, cap: int = SAMPLE_CAP
) -> Path:
    """Writes one sheet per item plus `REVIEW.md` into `out_dir`. Never
    writes a verdict. Returns the REVIEW.md path."""
    write_sheets(items, out_dir)
    sample = suggest_sample(items, adapters=adapters, cap=cap)
    index_path = out_dir / "REVIEW.md"
    index_path.write_text(render_index(items, sample), encoding="utf-8")
    return index_path


def extract_verdict(text: str) -> str:
    """Returns the verdict value with any placeholder HTML comment stripped,
    or "" if blank."""
    for line in text.splitlines():
        m = VERDICT_LINE_RE.match(line.strip())
        if m:
            return COMMENT_RE.sub('', m.group(1)).strip()
    return ""


def classify_verdict(value: str) -> str:
    if value == "":
        return "unchecked"
    v = value.lower()
    if v in ("yes", "good enough", "wrong", "no"):
        return v
    if v.startswith("missed"):
        return "missed"
    return "unrecognized"


def tally(sheets_dir: Path) -> dict:
    """Counts the `**Verdict:**` value in every `*.md` sheet in `sheets_dir`
    (excluding `REVIEW.md` itself). Returns {"n": int, "counts": dict,
    "unrecognized": [(filename, value), ...]}."""
    sheets = sorted(p for p in Path(sheets_dir).glob("*.md") if p.name != "REVIEW.md")
    counts: dict[str, int] = {}
    unrecognized = []
    for f in sheets:
        value = extract_verdict(f.read_text(encoding="utf-8"))
        cls = classify_verdict(value)
        counts[cls] = counts.get(cls, 0) + 1
        if cls == "unrecognized":
            unrecognized.append((f.name, value))
    return {"n": len(sheets), "counts": counts, "unrecognized": unrecognized}
