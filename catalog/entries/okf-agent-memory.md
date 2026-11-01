---
name: okf-agent-memory
title: OKF Agent Memory
url: "https://github.com/okf-memory/okf-agent-memory"
category: framework
summary: "Git-native persistent memory framework for AI coding agents — a compact push-layer behavioral codex (AGENTS.md, ~100-150 tokens) enforced through Agent Action Grammar (AAG), plus a pull-layer knowledge bundle (OKF v0.2 Markdown+YAML) searched via a pure-Go embedded MCP server with sub-300us in-memory BM25; ships a linter enforcing AAG's token budget, ASCII-only syntax, and tool-signature parity rules"
tags: [context-engineering, memory, mcp, prompt-optimization, agent-architecture]
reviewed: 2026-09-16
acquired: 2026-09-16
license: MIT
security_flags: [new-project, unverified-vendor-claims]
overlaps: [ai-memory-comparison]
source: unknown
---

## What it does

OKF Agent Memory ("Dual-Memory Agent Architecture", DMAA) splits agent context into two layers. The **push layer** is a compact behavioral codex committed to `AGENTS.md` (documented at roughly 100-150 tokens) that is loaded into every session and written in Agent Action Grammar (AAG) rather than prose. The **pull layer** is a git-versioned `knowledge/` bundle of Markdown+YAML concept files that the project describes as conforming to "OKF v0.2" (the project's own term, "Open Knowledge Format"; the repo's tagline additionally labels it "Google OKF v0.2" without independent corroboration that Google owns or publishes this spec). Pull-layer content is retrieved on demand — the project states it costs "0 tokens at baseline" — via an embedded MCP server that performs in-memory BM25 lexical search (documented at <300 microseconds, <15MB resident, ~4ms to validate a 50+ concept corpus).

Core behavioral rules include "search-before-write" (query existing memory before authoring new concepts, to avoid duplication/divergence) and "code-to-knowledge binding" (architecture-decision entries carry `code_refs` linking them to source files, queryable with `--for-path`). The CLI (`bin/okf`, built with `make build`) provides `bootstrap` (scaffold `knowledge/`, `AGENTS.md`, and agent skills into a target project), `validate --strict --drift`, `search`, `show`, `create`, and `mcp` (start the MCP server over stdio). The project supplies pre-built domain codices (software/Clean Code/TDD/security, editorial/literature analysis, ICF coaching competencies) for v0.3.0.

## Differentiators

Agent Action Grammar (AAG) is a formally specified (ISO/IEC 14977 EBNF) constrained pseudocode for behavioral rules: `ON event:` triggers, `IF cond => action` guard clauses evaluated top-to-bottom, `ASSERT(expr, ELSE=remedy)` completion gates, RFC 2119 modal verbs (MUST / MUST NOT / NEVER / PREFER / ALWAYS / SHOULD / MAY), and tool calls (`okf_search(query=..., limit=3)`) whose signatures are required to mirror the real MCP/runtime API ("tool signature parity"). The spec documents per-pattern token-reduction benchmarks against equivalent prose: 79.4% (tool constraint/guard), 79.3% (subsystem scope check), 78.9% (completion pipeline gate), 84.3% (full repository instruction set), and a worked example going from 38 tokens of prose to 12 tokens of AAG (~68%). The repo-level description separately claims an 80% token-bloat reduction attributable to progressive disclosure of the pull layer as a whole. These are the project's self-reported figures; an independent third-party review (published within days of the repo's public launch) noted the benchmarks measure latency and token counts but not retrieval recall/precision, and that no comparison is offered against hand-curated (non-monolithic) context files.

A companion linter enforces AAG compliance, including rule AAG-005 (push-layer codex must not exceed a 150-token budget), an ASCII-only lexical invariant (identifiers restricted to `[a-z][a-z0-9_-]*`; the spec argues multi-byte Unicode characters such as box-drawing glyphs or emoji cost 3-4 BPE tokens versus 1 for ASCII primitives like `@`, `=>`, `!`), and the tool-signature-parity check described above.

## Mechanical details

- Language/runtime: pure Go, no external database or vector-store dependency; build via `make build` to produce a standalone `bin/okf` binary.
- MCP server: `okf mcp knowledge`, stdio transport, documented as compatible with Claude Code, Cursor, and Codex.
- Retrieval: in-memory BM25 lexical search, documented at <300 microseconds; corpus validation documented at ~4ms for 50+ concepts; memory footprint documented at <15MB.
- Storage format: OKF v0.2 concept files (Markdown body + YAML frontmatter) under a `knowledge/` directory, plain text and git-version-controlled; hierarchical `index.md` files implement "progressive disclosure" so only relevant concepts are loaded.
- Specs live in-repo under `docs/spec/` (Agent Action Grammar RFC, OKF v0.2 compatibility matrix, Dual-Memory Agent Architecture RFC); a single canonical `AGENTS.md` convention is intended to replace divergent per-IDE instruction files.
- Repository published 2026-09-05 per an independent review; by the time of this catalog review the GitHub repo showed several hundred stars and 100+ commits, up from single-digit commit counts reported at initial launch.

## Security

- License: MIT (confirmed independently via GitHub repo metadata and a third-party review).
- No code-execution or credential-handling surface beyond normal local git/file operations and the stdio MCP server; no evidence in reviewed material of network calls, telemetry, or external API key requirements.
- Project is new: publicly launched 2026-09-05 (roughly two weeks before this review), with disproportionately fast star growth relative to its very small initial commit count — a pattern an independent reviewer flagged alongside the absence of recall/precision metrics for its BM25 retrieval and the absence of a baseline comparison against hand-curated (non-monolithic) instruction files. Treat all performance and token-reduction figures as vendor-reported and unverified by this catalog entry.
- The "Google OKF v0.2" attribution in the project's own tagline could not be independently corroborated as an actual Google-published standard; it is reported here as the project's self-description, not a verified fact.
