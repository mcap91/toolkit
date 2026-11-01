---
name: cartographer
title: Cartographer
url: "https://github.com/kingbootoshi/cartographer"
category: plugin
summary: "Claude Code plugin plus companion Bun CLI for codebase mapping/documentation: the plugin's legacy skill orchestrates parallel Sonnet subagents into docs/CODEBASE_MAP.md and a CLAUDE.md summary, while the v2 CLI indexes a repo into a local SQLite graph for bounded agent briefs, removal/completeness audits, and evidence-backed notes"
tags: [claude-code-plugin, codebase-mapping, documentation, subagents, code-graph, sqlite, cli, mcp]
reviewed: 2026-09-16
acquired: 2026-09-16
license: MIT
security_flags: [no-license-file, single-contributor, stale-4-months]
overlaps: [repowise, understand-anything, openwiki]
source: unknown
---

## What it does

Cartographer ships two related deliverables in one repo:

1. **Legacy Claude Code plugin** (`/cartographer` command or natural-language "map this codebase"): runs a scanner script that builds a file tree with per-file token counts (respecting `.gitignore`), plans how to split the codebase across subagents by token budget, spawns Sonnet subagents in parallel — each reads and analyzes an assigned portion of the codebase and returns a structured summary — then synthesizes all subagent reports into `docs/CODEBASE_MAP.md` (architecture map with file purposes, dependencies, data flows, navigation guides) and updates `CLAUDE.md` with a pointer summary. Re-running `/cartographer` checks git history since the last mapping and only re-analyzes changed modules, merging updates into the existing map.
2. **v2 graph CLI** (standalone, Bun-based): indexes a repository into a local SQLite graph (`graph.sqlite`) plus a JSON manifest and `CODEBASE_MAP.md`, then serves that graph to coding agents through bounded "briefs" (context scoped to a path, package, symbol, env var, DB/IaC object, audit ledger, or changed-file set), removal/completeness audit ledgers, an evidence-backed notes system, graph diffing, and an "adoption" command that scores whether an agent used graph context before editing. A thin newline-delimited MCP stdio wrapper (`cartographer:mcp`) exposes the same operations as MCP tools.

The README frames the plugin workflow as legacy, superseded for new agent/orchestrator workflows by the v2 brief/audit/notes commands, though both remain in the repo and are documented.

## Differentiators

Relative to other codebase-mapping/documentation tools already in this catalog (`openwiki` — CI-driven LLM wiki generation; `repowise` — multi-language dependency-graph + git-analytics codebase-intelligence engine with ~11 MCP tools; `understand-anything` — multi-agent knowledge graph with an interactive web dashboard), Cartographer's distinguishing points are:

- Dual delivery: a Claude-Code-marketplace-installed plugin/skill *and* a separate standalone Bun CLI/MCP server, rather than one or the other
- An explicit cost-control design rule baked into the plugin skill — "Opus orchestrates, Sonnet reads": the orchestrating agent is instructed never to read codebase files directly, always delegating reads to Sonnet (or cheaper Haiku) subagents
- Bounded, purpose-scoped "briefs" (by path/package/symbol/env-var/DB-IaC-object/audit-ledger/changed-files) rather than a full-graph or full-wiki dump
- Task-specific removal and completeness audit ledgers (`audit removal`, `audit verify`) for verifying a deletion or feature is fully accounted for in the graph
- An "adoption" command that scores agent runtime traces for whether graph context was actually consulted before edits — a compliance/behavior signal not present in the other cataloged tools
- Incremental re-indexing via a SQLite file-hash cache (unchanged repos reuse prior artifacts unless `--force`/`--no-incremental`)

## Mechanical details

- Plugin install: `/plugin marketplace add kingbootoshi/cartographer` then `/plugin install cartographer`; restart Claude Code (required for skill load); trigger with `/cartographer` or "map this codebase"
- Plugin requires `tiktoken` for token counting (`pip install tiktoken` or `uv pip install tiktoken`)
- v2 CLI install: `bun install`; run via `bun run cartographer -- --help`
- Core v2 commands: `mcp`, `index`, `verify` (`--fresh` fails on drift from live repo), `view`, `brief` (`--path --mode implementation --json`), `audit removal`/`audit verify`, `notes ingest`/`notes audit`/`notes accept`/`notes retire`, `export graph` (`debug-json`/JSONL), `diff`, `slice`/`impact`/`context`/`preflight` (broad selectors gated behind `--allow-broad`/`--debug-graph`), `adoption`, legacy `annotate`/`annotations` (OpenRouter-based, superseded by `notes`)
- `index` writes `.cartographer/manifest.json`, `.cartographer/graph.sqlite`, JSON schemas, and `CODEBASE_MAP.md`
- MCP wrapper (`bun run cartographer:mcp`) exposes `cartographer_index`, `cartographer_view`, `cartographer_brief`, `cartographer_context`, `cartographer_preflight`, `cartographer_verify`, `cartographer_audit_removal`, `cartographer_audit_verify`, `cartographer_notes_audit`, `cartographer_diff`; wraps the same library functions as the CLI, described in-repo as not becoming "a long-lived graph brain or agent manager"
- Deterministic eval profiles: `eval:cartographer:smoke`, `eval:cartographer:codex`, `eval:cartographer:codex:live` (the latter two use an external read-only target repo path and write append-only JSON reports under `docs/reports`)
- Language: TypeScript; package manager: Bun (`bun.lock`)
- Full plugin documentation: `plugins/cartographer/README.md` in-repo

## Security

- README states "License MIT" but no `LICENSE` file exists at the repo root (GitHub API returns 404 for `/LICENSE`; GitHub's repository metadata reports `license: null`) — the MIT claim is unformalized in the repo itself
- Single contributor: GitHub Contributors API lists only `kingbootoshi` (35 commits); no co-maintainers
- No `.github/workflows` (CI) directory or dedicated test directory visible in the repo root listing
- Last code push per GitHub API: 2026-05-13 — roughly 4 months before this review (2026-09-16), despite the README describing an actively-evolving v2 feature set
- Repo stats at review time: 699 stargazers, 49 forks, 5 open issues (GitHub API)
- The legacy plugin's subagent workflow reads the full target codebase and sends file contents to the Anthropic API (via Sonnet/Haiku subagents) for analysis — standard LLM-codebase-analysis data exposure, no additional exfiltration path observed in the README
- The v2 CLI's graph artifacts (SQLite DB, JSON) are written locally under `.cartographer/`; the MCP wrapper is a stdio process, not a network listener
- Plugin install path is the standard Claude Code plugin-marketplace mechanism; no curl-pipe-bash installer observed in the README
