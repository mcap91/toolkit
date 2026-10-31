# Semantic Search

Survey-first search over catalog entries: a complete lexical sweep, backstopped by
flagged semantic suggestions for concepts phrased differently. The lexical set is never
capped or truncated — if a term matches, the entry is in the response.

## What it does

Search runs two independent passes over the filtered universe of entries:

- **Lexical sweep** (the backbone): each term — explicit, or the whole query folded into
  one term when no terms are supplied — is matched as a word-prefix (`(?<!\w)token`,
  case-insensitive) against the raw entry text. A multi-word term matches only when every
  one of its tokens matches (AND). This set is complete: every matching entry is
  returned, ordered by BM25 internally, tie-broken by title then name. No score is
  exposed.
- **Semantic rescue**: the top `semantic_n` non-lexical entries by cosine similarity
  (cosine > 0.0), appended after the lexical block with a `rank` (1..N) — no cosine value
  is exposed. There may be fewer than `semantic_n`, including zero.

Passing explicit `terms` runs a real survey — an OR of independent AND-of-tokens terms,
each reported with its own hit count in `swept_terms`. Omitting `terms` treats the whole
query as a single AND lookup term (a narrow, exact-ish lookup, not a broad sweep) — the
single-term fallback exists for backward compatibility with query-only callers.

An empty query with no terms is **listing mode**: every entry in the filtered universe is
returned with `match: {"type": "listing"}`, and `swept_terms` is empty — this is how
listing is distinguished from a miss.

A **miss** is `lexical_total: 0` with a non-empty `swept_terms` (every term's hit count
was zero). Semantic selection still runs on a miss — it may return entries phrased
differently than the query, or it may return nothing if no candidate has positive
cosine. An empty result set is only legal on a true miss or an empty universe.

## Prerequisites

- Python 3.10+
- [uv](https://astral.sh/uv) — Python package/environment manager
- `fastembed` (installed via the setup command below)

## Setup

```bash
cd {YOUR_PROJECT}/packages/catalog-embedder
uv venv
uv pip install -r requirements.txt
```

The embedding model (~34MB) downloads once to `/tmp/fastembed_cache` on first use, then runs
offline.

## CLI usage

Build the vector index for all entries:

```bash
python -m catalog_embedder build --dir {YOUR_PROJECT}
```

Run a survey:

```bash
python -m catalog_embedder search --query "ocr" \
  --dir {YOUR_PROJECT} \
  [--term ocr --term "text extraction"] \
  [--semantic-n 10] \
  [--decision-status adopted] \
  [--category "document-processing"]
```

Both commands take `--dir`, the path to the project root containing the catalog data.
`--term` is repeatable (max 50, 200 chars each) and expands the sweep beyond the query
text — e.g. `--term ocr --term "text extraction"` runs both as independent AND terms.
`--semantic-n` (1–50, default 10) bounds the semantic suggestion count. Omitting
`--term` entirely falls back to the query tokenized into one AND term.

## Auto-rebuild

Vectors are a derived artifact — not committed to source control — and rebuild automatically
in three cases:

1. **On index** — whenever the catalog's `index` tool regenerates derived files.
2. **On `git pull`** — a git post-merge hook detects changes to catalog entries and rebuilds.
3. **On first search** — if no vector file exists yet, a search triggers a build before
   returning results.

There is no manual build step for normal use.

### Enabling the post-merge hook

Git hooks aren't enabled by default on clone. Point git at the repo's hooks directory once:

```bash
git config core.hooksPath .githooks
```

After that, pulling changes that touch catalog entries automatically rebuilds the vector
index in the background.

## Using this from another repo

Consuming repos don't need to run the CLI directly. Register the project's MCP server in
`.mcp.json` as usual, then call its `search` tool — the tool invokes the embedding CLI as a
subprocess and returns the survey response (lexical sweep + semantic suggestions)
transparently. No extra configuration is required beyond the one-time `uv`/`fastembed`
setup on the host running the server.

If the Python environment isn't set up, `search` returns an error describing the missing
setup step rather than silently returning empty results.

## Performance

- **Cold start**: ~1-2 seconds per query (Python interpreter startup, model load, embedding,
  scoring).
- **Build**: tens of seconds for a few hundred entries; scales with catalog size.
- **Model**: downloaded once (~34MB), then fully offline.

## Evaluation

`../toolkit-workbench/semantic-bench/eval/` holds a search eval that scores three engines — **substring**
(the baseline: the repo's original `search.ts` substring lookup, run verbatim via
`eval/substring_search.ts`), **lexical** (`run_search`, keeping only
`match.type == "lexical"` results), and **lexical+semantic** (the full `run_search`
response) — against 40 engineered queries (`eval/queries.json`) spanning 5 topics
(`eval/topics.json`) and 4 query types: **name** (answer is one entry, scored on whether
it is the first result), **keyword**, **description**, and **keyword_list**.

Each run builds a **sealed corpus**: every entry's content at a fixed `corpus_commit` is
written into a fresh temp directory and vectors are rebuilt unconditionally for exactly
that corpus, so results never depend on working-tree state or stale `.vectors.json`.

The **answer key** (`eval/answer_key.json`) is built once by `eval/label.py`: a no-tools
model call labels every entry against every topic from an empty temp directory (so no
repo config can leak in), reading entry text from `corpus_commit` via `git show`. The
prompt is sent to `claude` on stdin, never as an argument, because batch prompts reach
~200 KB, above Linux's single-argument limit. Ten
fixed calibration entries are included in every batch to measure cross-batch consistency
(`calibration.unanimous_rate`). The model only classifies — batching, response parsing,
consistency checks, and the majority vote are deterministic.

Before scoring, `eval/run_eval.py` enforces five gates (exact corpus match, answer-key
topic/name validity, a production-parser check, `queries.json` schema, and a sanity check
that the answer key's own topic examples are labeled correctly) — any failure exits 1 with
a named reason. It never asserts which engine wins.

**Wording rules** for any report of these numbers: call the metrics "topic recall" /
"topic precision" (non-name queries are scored against their topic's full answer list,
not judged one by one); report each query type separately, never one overall winner;
state the lexical candidate counts for description and keyword_list queries; state the
calibration `unanimous_rate`. Every number must come from `results.json`. The figure and
README report **relevant entries surfaced**: found / should have found, summed over the
queries of each style (`relevant_found_sum` / `relevant_total_sum`), so every percent comes
with its count.

Commands (run with the project venv, from the repo root):

```bash
# Build the answer key (labels the current HEAD commit — commit catalog changes first)
packages/catalog-embedder/.venv/bin/python ../toolkit-workbench/semantic-bench/eval/label.py --dir .

# Run the eval and render the figure
packages/catalog-embedder/.venv/bin/python ../toolkit-workbench/semantic-bench/eval/run_eval.py --dir .
packages/catalog-embedder/.venv/bin/python ../toolkit-workbench/semantic-bench/eval/plot.py

# Validate
(cd packages/catalog-embedder && .venv/bin/python -m pytest && .venv/bin/python -m pytest eval/test_label.py)
npm test && npm run typecheck
```
