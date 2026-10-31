# catalog-capture

Resolves `⚠ needs-link` lines in `catalog/inbox.md` into catalog-ready text, with no manual
copy-paste: Reddit `/s/` share links and Instagram reels today, through one `SourceAdapter`
registry (WK-0094 Phase B). Adding a source type is one new adapter — no edit to the shared
rewrite engine, block renderer, sources writer, or review module.

uv only — never base Python.

## Setup

```
cd packages/catalog-capture
uv sync --extra dev
```

Chromium must already be available to Playwright (shared download cache, or
`uv run playwright install chromium` if not) for the Reddit path.

## Module layout

- `registry.py` — the `SourceAdapter` protocol, the registry (`register`/`get_adapter`/
  `registered_adapters`), the one needs-link rewrite engine, and the shared `CaptureOutcome`
  shape every adapter returns. `# DECISION:` comment there records the `adapters/`/`stages/`
  split.
- `rendering.py` — the one inbox block renderer (`source:` line + adapter-supplied sections,
  fence-break defused once, no trailing newline).
- `sources_writer.py` — the one `catalog/sources/<platform>/<id>.md` writer (header lines +
  body + optional sibling artifact directory).
- `review.py` — the one review-sheet/index/tally module (replaces the reel-only
  `make_review.py`; never writes a verdict).
- `pricing.py` — LiteLLM price-table lookup, with a configurable path (CLI option and/or env
  var); a missing table always returns `(None, reason)`.
- `canonical.py`, `fence.py`, `versions.py` — small shared helpers (Reddit canonical-URL/post-id
  derivation, inbox fence-break defusal, tool-version strings).
- `cli.py` — `python -m catalog_capture capture|needs-link|review ...`.
- `adapters/` — one module per source type:
  - `reddit.py` — the `RedditAdapter` (needs-link URL rule, capture via `stages.browser`, block/
    sources sections).
  - `instagram_reel.py` — the `InstagramReelAdapter` (needs-link URL rule, the full
    probe→audio→transcribe→frames→read pipeline via `stages.*`, block/sources sections, OR-3's
    one-block-per-reel shape).
  - `instagram_post.py` — the `InstagramPostAdapter` (needs-link URL rule for `/p/<shortcode>`,
    instaloader fetch, carousel yt-dlp slide-count cross-check, the shared read over every slide
    in order, block/sources sections, one-block-per-post).
- `stages/` — shared capture-pipeline building blocks, called by adapters, never copied:
  - `browser.py` — headless-Chromium page capture with a per-site wait table (today: Reddit's
    `shreddit-post` poll).
  - `media.py` — yt-dlp anonymous probe + bestaudio/bestvideo download.
  - `transcribe.py` — ffmpeg decode to 16 kHz PCM + faster-whisper transcription.
  - `frames.py` — ffmpeg keyframe extraction + PIL contact sheet.
  - `read.py` — the multimodal `claude --print` read call: a prompt plus an ordered list of
    images (each with its own media type), stream-json in and out, usage parsing.

## Reddit

Engine: headless Playwright Chromium with a Chrome user agent (clears Reddit's JS challenge),
one capture module with a per-site wait table (`reddit.com` → poll for `shreddit-post`, soft — on
timeout it keeps the page text anyway). This is the WK-0054 ENGINE CHOICE ("own script"), copied
from `toolkit-workbench/web-capture/own/capture.py`. See `wiki/issues/WK-0054.md` and
`wiki/issues/WK-0080.md` ("Spec check — Reddit slice") for the evidence and rulings this package
follows.

## Instagram reels

Pipeline (WK-0079's recommended default stack, I4): yt-dlp `-j` anonymous caption probe →
yt-dlp bestaudio download → ffmpeg (imageio-ffmpeg, never a system ffmpeg) decode to 16 kHz mono
→ faster-whisper `small` CPU int8, VAD off → yt-dlp bestvideo download → ffmpeg keyframes
(`select='eq(n\,0)+gt(scene\,0.3)'`) + a PIL contact sheet → one Claude read (stream-json, no
tools, caption + transcript + sheet image) naming every tool/repo the reel shows plus any
on-screen text. Per OR-3 (operator ruling, 2026-10-26): the capture never verifies a URL or
decides what the reel is "about" — it hands the processing agent everything the read spotted,
labeled as unverified hints, and the agent decides what goes into the catalog. See
`wiki/issues/WK-0080.md` ("OR-3 Operator ruling: capture captures, the processing agent
decides") for the evidence and rulings.

## Instagram posts (`/p/`)

Pipeline (WK-0087, built on WK-0094 OR-6): anonymous instaloader fetch (no login, no cookies) at
the largest `image_versions2.candidates` size, branching on `media_type` — `1` is a single image
(one slide), `8` is a multi-image carousel (`GraphSidecar`). Carousels get an independent yt-dlp
`-J` `playlist_count` cross-check against instaloader's own declared slide count (non-fatal if it
disagrees or fails). Every slide, in swipe order, plus the caption, goes through one shared
`stages.read` call; if that call errors or hits the budget cap, it falls back to chunks of at most
10 slides (each chunk carrying the caption and its own slides' absolute position) and merges the
result, retrying the chunked read once if the merged indices aren't exactly `1..N`. The block holds
the caption, each slide's text under its slide number, then unverified tool/repo hints (same OR-3
shape as reels). A video `/p/` post, or a carousel with any video slide, has no capture yet and
becomes `⚠ capture-failed <url> — unsupported media_type <n>`.

## CLI

Capture one URL and print its inbox block (auto-detects the adapter from the URL, or pass
`--adapter`):

```
uv run python -m catalog_capture capture <url>
uv run python -m catalog_capture capture <url> --sources catalog/sources
```

Resolve every `⚠ needs-link` line any registered adapter owns, in an inbox file, in place:

```
uv run python -m catalog_capture needs-link --inbox catalog/inbox.md --sources catalog/sources
```

Options:
- `--limit N` — process at most N items across every adapter (useful for a dry run).
- `--delay SECONDS` — seconds between captures, sequential, not applied before the first item
  overall. Default: each matched line's own adapter delay (currently 3s for Reddit, Instagram
  reels, and Instagram posts) — pass `--delay` to override every adapter's delay for this run.
- `--only NAME` — restrict the run to one registered adapter (`reddit`, `instagram_reel`, or
  `instagram_post`), leaving every other adapter's lines untouched. This replaces the old separate
  `instagram-needs-link` command: run `--only instagram_reel` or `--only instagram_post` for the
  equivalent scope.
- `--prices-path PATH` — LiteLLM price table path for the Instagram read's USD estimate
  (default: the documented kb-checkout path, or the `CATALOG_CAPTURE_LITELLM_PRICES_PATH` env
  var). A missing table still yields `(None, reason)`, never a substitute rate.

Each matched line is replaced in place with a fenced block (`inbox.ts`'s existing `source:`-
prefixed `\`\`\`text` format), or left untouched if no adapter's rule matches it. A capture
failure becomes `⚠ capture-failed <url> — <error>` (never a silent drop); the Reddit adapter's
PDF-download event becomes `⚠ pdf <url>`. A line no adapter matches, but whose text mentions a
known platform (reddit.com, instagram.com), is reported on stdout as a near-miss worth a manual
check. Everything else in the inbox is left byte-identical. Exits non-zero (after printing a
summary) if any item failed.

**Retrying a `capture-failed` or `pdf` line.** `needs-link` only matches `⚠ needs-link <url>`
lines in a shape some adapter's rule recognizes. To retry, manually edit the line back to
`⚠ needs-link <url>` (drop the `capture-failed`/`pdf` reason and any trailing error text) before
running `needs-link` again — there is no automatic retry.

### Review sheets

Render one pre-filled review sheet per captured item (`catalog/sources/` → a sheet directory),
a `REVIEW.md` index with a suggested spot-check sample (capped at 5, WK-0094 OR-5), and tally
operator verdicts once they're filled in. This never writes a verdict — review is operator-owned
(WK-0079 OR-2: finder != verifier).

```
uv run python -m catalog_capture review build --sources catalog/sources --out <review dir>
uv run python -m catalog_capture review tally --out <review dir>
```

`review build` takes `--only NAME` (same as `needs-link`) to build sheets for one adapter only,
and `--sample-cap N` to override the default cap of 5.

## Concurrent edits

A full run can take several minutes (one capture per item, with a delay between them). The
inbox is read once at the start and written once at the end via a tmp file + atomic rename; if
the file's mtime or size changed on disk in between (someone edited it mid-run), the run
aborts without writing and reports which items it had already captured — their source files are
not lost, but the inbox lines for them are not updated, so run it again after resolving the
conflict.

## Tests

```
uv run pytest -v
```

The Reddit golden fixture (`tests/fixtures/JNjEe87YeN.txt`) is a real, unedited WK-0054
own-engine capture — not hand-written. The fence-break edge case is derived by mutating it.

The Instagram reel golden fixtures (`tests/fixtures/instagram/`) are the real golden reel
(`De5smNojeZm`) artifacts copied byte-for-byte from `toolkit-workbench/reel/outputs/De5smNojeZm/`
(`probe_ytdlp.json`, `transcript_small_cpu_int8.txt`, `sheet_t0.3.jpg`), plus this slice's own
real Claude read response (`read_response.jsonl`) captured against that exact sheet/transcript/
caption. The Instagram carousel golden fixtures
(`tests/fixtures/instagram/carousel/De9SalRGOhy/`, `.../DeCKnW0DAGc/`) are real, unedited
instaloader + yt-dlp probe captures plus this slice's own real read responses (WK-0094 Phase A,
WK-0087 steps 1-2); `InstagramPostAdapter`'s golden tests feed them through the real pipeline,
mocking only the instaloader CLI call and the `claude --print` call. The single-image post fixture
(`tests/fixtures/instagram/post/Deqni2Tic2N/`) is a real, unedited instaloader capture of one of
the five single-image `/p/` links WK-0094 Phase A probed.

`tests/test_output_snapshots.py` pins byte-exact output (rendered blocks, sources files, inbox
rewrites, and the Reddit CLI stdout/stderr) from before the WK-0094 Phase B refactor. Never
hand-edit a file under `tests/fixtures/snapshots/` — regenerate with `UPDATE_SNAPSHOTS=1` only
from code you've already verified is correct, then re-run without the env var to confirm the
snapshot is deterministic.
