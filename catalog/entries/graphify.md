---
name: graphify
title: Graphify
url: "https://github.com/safishamsi/graphify"
category: framework
summary: direct inspiration for kb graph; concepts like confidence-tagged edges and clustering worth learning from
tags: [knowledge-graph, ast, visualization, kb]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it does

Transforms codebases, documentation, and multimedia into interactive knowledge graphs using a three-stage pipeline. Stage 1 extracts via tree-sitter AST (31 languages, local, no API calls) plus LLM semantic extraction for docs/PDFs/images and faster-whisper for audio/video. Stage 2 semantically enriches: comments tagged `# NOTE:`, `# WHY:`, `# HACK:` become separate nodes; docstrings and design rationale are extracted; edges get confidence tags (EXTRACTED, INFERRED, AMBIGUOUS). Stage 3 runs community detection via Leiden clustering, identifying "god nodes" (highest-degree hubs) and surprising cross-module connections. Output is `graphify-out/graph.html` (interactive visualization), `GRAPH_REPORT.md` (human-readable summary), and `graph.json` (queryable JSON). Registers as a `/graphify` skill so agents can issue `graphify query "<question>"` for scoped queries instead of reading full files.

## Assessment

Graphify is the direct inspiration for kb graph — the concept of making implicit project understanding explicit and agent-accessible, and the graph-as-queryable-knowledge-base pattern rather than just a visualization, both originated here. The comparison below shows where kb graph has caught up and where it hasn't.

| Feature | Graphify | kb graph |
|---|---|---|
| Input sources | Code (31 langs), docs, PDFs, images, video | Wiki records, code files, docs |
| Parsing | tree-sitter AST (local) + LLM (for docs) | Static analysis of imports/references |
| Edge types | Calls, imports, data flow, semantic relationships | Structural relationships (depends_on, blocks, references) |
| Confidence | Three-level: EXTRACTED, INFERRED, AMBIGUOUS | Binary (present or not) |
| Enrichment | Design rationale as nodes, comment extraction | No rationale extraction |
| Clustering | Leiden community detection, god nodes | No clustering |
| Output | Interactive HTML + JSON + markdown report | .graph.json + graph-summary.md |
| Query interface | `/graphify query` skill | kb graph CLI + search index |

**What kb graph could still learn from Graphify**:

1. **Confidence-tagged edges** — EXTRACTED vs INFERRED vs AMBIGUOUS; kb graph currently has binary edges with no certainty signal
2. **Design rationale as nodes** — `# WHY:` comments becoming queryable entities, making intent searchable not just structure
3. **Community detection / clustering** — Leiden algorithm to identify god nodes and unexpected cross-module dependencies
4. **Interactive HTML visualization output** — kb graph produces JSON and markdown but no interactive visual

## Mechanical details

Install from GitHub. Requires tree-sitter for code parsing (local, no API calls for code extraction) and an LLM API for doc/multimedia extraction. The `/graphify query` interface is the primary agent integration point. Not recommended for installation — kb graph covers the core use case and this would be a parallel graph system. Study the source for the confidence tagging and clustering concepts rather than running it alongside kb.

## Security

No license is stated in the repository; the PyPI package is `graphifyy` (double-y) and the README explicitly notes it is the only official package — other `graphify*` packages are unaffiliated, which is a mild supply-chain surface to be aware of at install time. Code files are processed entirely locally via tree-sitter with no API calls, so source code never leaves the machine. Docs, PDFs, and images are sent to a third-party LLM API (whichever backend key is configured), making data residency dependent on the chosen provider; for sensitive corpora the README recommends `--backend ollama` for fully local inference. Query logging writes to `~/.cache/graphify-queries.log` by default and can be disabled via `GRAPHIFY_QUERY_LOG_DISABLE=1`. The MCP HTTP server defaults to loopback-only (`127.0.0.1`) and requires explicit `--host 0.0.0.0 --api-key` to expose beyond localhost, which is a reasonable default. No telemetry or usage tracking is claimed by the project.
