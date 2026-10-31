# Agent Operating Guide

<!-- BEGIN kb-managed -->
Managed by kb — edits inside this block are overwritten by `kb bootstrap` / `kb sync-contract`; edit outside the markers.

## kb integration

This repository uses the `kb` toolkit (repo-local wiki, reviewed dispatch, deterministic graph). The kb
MCP servers (`kb-wiki`, `kb-dispatch`) are registered in this repo's `.mcp.json` and run from the kb
checkout; every kb tool call targets this repository via `dir`.

### Retrieval — do this before substantive work

Repository-context retrieval is a wiki/docs retrieval problem first, not a filesystem-search problem first.

1. Search the wiki with the kb wiki MCP `search` tool. This is the first retrieval step.
2. If you need a structured overview, regenerate views with the MCP `generate` tool and read them
   (`catalog`, `now`, `inbox`, `backlog`, `archive`).
3. Then read the relevant durable `docs/` pages.
4. Then check related `wiki/decisions/`, `wiki/issues/`, `wiki/initiatives/`, `wiki/areas/`, `wiki/sources/`.
5. Only then inspect implementation files.

If the kb wiki MCP server is not available this session, run the same steps via the kb CLI from the kb
checkout (`npm run wiki -- search --dir <this repo>`, `npm run wiki -- generate --dir <this repo>`). Do
not use raw `rg`, file globbing, or direct file reads as the first retrieval step — use the wiki MCP tools
(`search`, `generate`, `lint`), or the CLI fallback, first. Do not parallelize implementation search with
the initial retrieval pass.

### Operating rules

- Wiki: prefer the `kb-wiki` MCP tools (`search`, `generate`, `lint`, `create`, `allocate-id`,
  `build-search-index`, `sync-contract`, `bootstrap`); CLI fallback `npm run wiki -- … --dir <this repo>`.
- `allocate-id` is an idempotent **peek/reserve**, not a counter: repeat calls return the same id until
  `create` writes the record that claims it. Do not loop it expecting increments — call `create` to claim
  an id (it allocates and writes the record atomically). Repeated identical ids are correct, not a bug.
- Dispatch: multi-agent handoff protocol — author HOs (`create-handoff`), dispatch workers
  (Pi/codex/claude in bwrap jail), capture results, review, merge. The dispatch MCP server
  instructions carry the full orchestration recipe (dispatch loop, polling, kind routing,
  fix-up budget, merge/cleanup, wiki-update-after-completion). Prefer `kb-dispatch` MCP
  tools; CLI fallback `npm run dispatch -- …`.
- For pipeline work, delegate via kb-dispatch; do not spawn Claude Code subagents or
  workflows unless the operator explicitly approves.
- Graph: kb CLI (`npm run graph -- --dir <this repo>`).
- Dashboard: `npm run dashboard -- <ID> --dir <this repo>` generates a self-contained HTML tracker
  for PLN, IN, or WK-set records. Output: `wiki/dashboard/<ID>.html`. See `docs/dashboard.md` in the
  kb checkout.
- Always pass `dir` pointing at this repository; run kb from its own checkout, not this repo root.
- Do not create `HO-*` via `wiki create` — handoffs are dispatch-owned under `wiki/handoffs/`.
- If wiki records and code/tests disagree, report the mismatch rather than trusting a grep-first conclusion.

<!-- END kb-managed -->

## What this repo is

Three layers, from DEC-0005.

**Catalog.** Public data: `catalog/entries/`, one template per entry, hand-curated by the operator. This
is the product — a personal library of tools, techniques, and references, each entry written deep enough
that an agent never has to re-fetch the source to answer a question about it.

**Reader.** Public code: an MCP server (a small background program that exposes callable tools to an
agent over the Model Context Protocol) running `search` and `index`, a lint CLI for contributors, and
`index.md` as a table of contents an agent can read straight off the raw GitHub URL.

**Workbench.** A private sibling repo, `../toolkit-workbench`: the pipeline that writes the catalog,
every project that uses the catalog to build or test something, raw runs, and third-party captures. It
has no wiki of its own — every record for both repos lives in this repo's `wiki/`.

No code in this repo writes a catalog entry. Intake — pulling links, curating the inbox, draining to the
queue, running the headless processing loop — runs from the workbench now.

## Working here

Work-tracking records (`WK`, `IN`, `DEC`, and the rest) live in `wiki/`, a private, gitignored repo nested
in this checkout. Start from `wiki/dashboard/chain.md`, the cross-initiative status surface the overseer
maintains.

Two settings carry the only paths that cross the repo boundary: `CATALOG_DIR` (default
`../toolkit/catalog`) and `WORKBENCH_DIR` (default `../toolkit-workbench`). No repo name, operator name,
or machine path goes into code or settings beyond these two.

Media and third-party captures never enter this repo. The `.gitignore` backstops that rule.

## Catalog entries

Every entry follows the same section order: What it is, How it works, How to use it, Evaluation and
limits, Context from the source, Related, Security.

Entries are factual. No verdicts, no adoption recommendations, no notes on whether the operator should
use the thing — those decisions happen outside the entry.

Three frontmatter fields carry provenance: `url` (the subject itself — a repo, a tool's site),
`source_url` (the link the item came in on, when different from `url`), and `source` (what that link
derives to: `instagram`, `reddit`, `x`, `web`, or `text`).

`catalog/recipe.md` is today's working description of the template. `catalog/template.md` (WK-0099) will
replace it as the formal contract.

## Reader MCP

The catalog MCP server lives in `packages/catalog-mcp`. Run it directly with:

```
npx tsx packages/catalog-mcp/src/server.ts
```

As of WK-0100 it registers 12 tools: `index`, `lint`, `search`, `config`, `queue`, `drain`, `ingest`,
`fetch-url`, `build-prompt`, `validate-entry`, `write-entry`, `annotate-entry`. The write tools move to
the workbench pipeline package under WK-0101, after which the public server exposes `search` and `index`
only.

## Workbench projects

- **ocr-bench** (IN-0002) — benchmark OCR and parser tools against a Sonnet agent on scientific PDFs; owes a
  results page.
- **semantic bench** (IN-0012) — embedding and reranking models for catalog search, measured on the sealed
  operator-brief eval; owes a benchmark page and, if it passes, a pinned model in the reader.
- **pipeline** (IN-0011) — intake (Gmail to inbox to queue), capture, one fresh session per queue item,
  `upsert-entry`, lint, index, and the commit back into this repo.
- **kb lab** (IN-0013) — wiki operations at scale and agent-rule experiments; results publish in the kb repo.

Graduation rule: a workbench project owes one public artifact under `docs/benchmarks/` — a results page,
a package, a recipe or template change, or a pinned-model change. The artifact moves into this repo; raw
runs and captures stay in the workbench.
