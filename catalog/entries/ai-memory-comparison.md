---
name: ai-memory-comparison
title: AI Memory Comparison
url: "https://github.com/carsteneu/ai-memory-comparison"
category: reference
summary: Definitive source-backed survey of 73 open-source AI agent memory systems across 79 features — every claim cites public code or docs.
tags: [memory, agents, comparison, survey, mcp, rag, vector-db]
reviewed: 2026-06-10
acquired: 2026-06-10
license: CC0-1.0
security_flags: []
overlaps: []
source: unknown
---
## What it does

A sortable, filterable comparison table of 73 open-source memory systems built specifically for AI coding agents (Claude Code, Codex, OpenCode, etc.). Systems are evaluated across 79 features on seven axes: Data Model, Search & Retrieval, Knowledge Lifecycle, Extraction Pipeline, Platform Support, Architecture, and Benchmarks. Every checkmark links to the exact README line, docs page, or source file that proves the feature exists. The live table is hosted at carsteneu.github.io/ai-memory-comparison. An `evidence/` directory in the repo stores per-system citation files so claims are re-auditable at any time.

## Assessment

`adopt` as the go-to shortlist tool when evaluating memory backends for an agent project. The source-citation discipline and coding-agent focus make it far more trustworthy than vendor marketing comparisons. Scope is deliberately narrow (no general vector DBs, no pure RAG frameworks), so signal-to-noise is high. CC0 license means it can be embedded, forked, or redistributed without restriction.

Note: the maintainer is also the author of YesMem (one of the 73 listed systems), which is disclosed in the README; YesMem follows the same evidence rules as all other entries.

## What to adopt

- Use the live table (carsteneu.github.io/ai-memory-comparison) when selecting a memory backend — filter by the axes relevant to your use case (e.g. MCP integration, persistence model, extraction pipeline).
- Check a system's `evidence/` file before committing — it shows exactly which source lines back each feature claim.
- Contribute corrections or new systems via PR with a complete evidence file (see CONTRIBUTING.md).

## Security

No code is executed; this is a static comparison resource. No installation or runtime surface area. CC0 — freely usable. Maintainer conflict of interest (YesMem authorship) is disclosed; the same evidence standard applies to all entries.
