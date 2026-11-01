---
name: mempalace
title: MemPalace
url: "https://github.com/MemPalace/mempalace"
category: framework
summary: "Local-first AI memory with 96.6% R@5 retrieval, 33 MCP tools, verbatim storage, and pluggable backends; strong benchmarks and Claude Code integration make it worth trialing"
tags: [memory, semantic-search, mcp-server, local-first, chromadb, knowledge-graph, claude-code]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: []
overlaps: [claude-mem, memstack, ai-memory-comparison]
source: unknown
---

## What it does

A local-first AI memory system that stores conversation history as verbatim text (no summarization, extraction, or paraphrasing) and retrieves it with semantic search. The index is structured like a memory palace: people and projects become wings, topics become rooms, and original content lives in drawers. Searches can be scoped to specific wings/rooms rather than running against a flat corpus.

Key capabilities: 33 MCP tools for palace reads/writes, knowledge-graph operations, cross-wing navigation, drawer management, and agent diaries. Temporal entity-relationship graph with validity windows backed by local SQLite. Auto-save hooks for Claude Code, Codex CLI, and Cursor IDE. Can mine Claude Code session transcripts and project files into the palace.

Benchmark results: 96.6% R@5 on LongMemEval (500 questions) with zero API calls; 98.4% with hybrid heuristics (keyword boosting, temporal proximity, preference patterns); 99%+ with LLM rerank. All benchmarks reproducible from the repository.

## Assessment

The retrieval quality is best-in-class for local-only memory — 96.6% R@5 with no LLM dependency is remarkable and independently reproducible. The verbatim storage approach avoids the lossy summarization that plagues other memory systems. The structured palace metaphor (wings/rooms/drawers) gives meaningful scoping that flat vector stores lack. The 33 MCP tools provide comprehensive integration with Claude Code and other MCP-capable agents. Auto-save hooks for Claude Code sessions solve the real problem of losing context across conversations. Pluggable backends (ChromaDB, SQLite, Qdrant, pgvector) provide deployment flexibility. The team is transparent about benchmark methodology, explicitly refusing misleading cross-project comparisons. Pilot to evaluate integration with our existing wiki-based retrieval and whether the overhead of maintaining a palace alongside the wiki is justified.

## Mechanical details

- Install: `uv tool install mempalace` or `pipx install mempalace` or Docker
- Initialize: `mempalace init ~/projects/myapp`
- Mine content: `mempalace mine ~/projects/myapp` (files) or `mempalace mine ~/.claude/projects/ --mode convos` (Claude sessions)
- Search: `mempalace search "why did we switch to GraphQL"`
- Session context: `mempalace wake-up` loads context for new sessions
- MCP server: 33 tools, stdio transport, configurable in `.mcp.json`
- Backends: ChromaDB (default), `sqlite_exact`, `qdrant` (REST), `pgvector` (Postgres)
- Embedding models: embeddinggemma-300m (multilingual, ~300MB) or all-MiniLM-L6-v2 (English, ~30MB)
- Knowledge graph: temporal entity-relationship graph with validity windows, local SQLite
- Auto-save hooks: periodic saves and pre-compression snapshots for Claude Code/Codex/Cursor
- Per-message recall: `mempalace sweep <transcript-dir>` for message-level verbatim drawers
- Agent support: each specialist agent gets its own wing and diary, discoverable at runtime

## Security

- **License**: MIT
- **Dependency health**: ChromaDB, numpy, grpcio as core dependencies; optional extras for extract, spellcheck, pgvector. Recommend isolated install via `uv tool` or `pipx` to avoid conflicts
- **Code quality signals**: Comprehensive benchmarks with reproducible methodology; full per-question result files committed; CONTRIBUTING.md present; CHANGELOG.md for releases
- **Supply chain**: Active open-source project; warns about impostor sites distributing malware (documented in docs/HISTORY.md) — indicates the project is popular enough to be targeted
- **Dangerous patterns**: Data stays local by default. External backends (Qdrant, pgvector) send verbatim text to the configured server — this is documented as an explicit opt-in, never the default. Namespace isolation and local marker files guard against silently connecting to the wrong server
- **Maintenance**: Active development; multiple storage backends, Docker support, and multi-platform hooks indicate sustained engineering effort