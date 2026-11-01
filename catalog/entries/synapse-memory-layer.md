---
name: synapse-memory-layer
title: Synapse (memory-layer)
url: "https://github.com/rickymm3/memory-layer/"
category: framework
summary: "Early-stage, self-hosted persistent memory backend for LLMs (Claude Desktop, Claude Code/VS Code via MCP) that stores structured 'memory atoms' plus immutable evidence 'signals' in Postgres+pgvector behind a write-quality/critic/risk-gate commit pipeline; roadmap includes routing low-confidence questions to specific human experts and folding their answers back into memory."
tags: [memory, mcp-server, postgres, pgvector, rag-alternative, knowledge-graph, self-hosted, prototype, human-in-the-loop]
reviewed: 2026-08-09
acquired: 2026-08-09
license: LicenseRef-unknown
security_flags: [no-license-stated, early-prototype, single-author, requires-anthropic-api-key, no-tests-evident]
overlaps: [claude-mem, gbrain, memstack, mempalace, ai-memory-comparison]
source: unknown
---

## What it does

Synapse (repo name `memory-layer`) is a persistent, LLM-agnostic memory layer that plugs into Claude Desktop (MCP stdio), Claude Code/VS Code (MCP), and a hosted Flask site. Every conversation across these surfaces writes structured "memory atoms" — canonical beliefs with `content`, `memory_type` (fact/decision/instruction/observation/preference/correction), `scope` (project/model/user), `confidence`, `importance`, `visibility`, `lifecycle_status`, and a 4096-dim embedding (local `qwen3-embedding` via Ollama) — into a shared Postgres+pgvector store. Every write also creates an immutable "memory signal" (the evidence event that produced or modified the atom); signals aggregate into support/opposition weights that drive automatic confidence recomputation and a disagreement score. No atom is silently overwritten — history is preserved, and contested beliefs queue for signal-based resolution.

All writes, from any surface, pass through the same pipeline: write-quality scoring → reconciliation against existing atoms → an LLM critic review → a risk gate → the Postgres write (dual-write of a `memory_atom` and a `memory_signal`). A chat pipeline retrieves top-K atoms by cosine similarity and routes each turn as direct (no memory), context (inject and answer), or recursive (contested atom → draft → evaluate → web search → revise), followed by background post-turn reflection that extracts new memory candidates.

## Differentiators

An MCP server exposes 8 tools (`memory_health`, `memory_search`, `memory_store_auto`, `memory_get`, `memory_task_context`, `memory_audit`, `memory_link_atoms`, `memory_related`) over stdio or SSE/HTTP. The hosted site adds a per-user "Brain," auto-clustered "Discussions" from public atoms with novelty scoring, a D3 force-directed knowledge-graph view, an admin atom browser, and a REST ingest endpoint (`POST /api/ingest`) for non-MCP clients (ChatGPT/Gemini/Grok via custom actions). The stated core product direction — not yet built — is "demand-driven question routing": when the AI's confidence on a question falls below a threshold, it generates a targeted forum-style post routed to specific users whose profiles suggest they can answer (locals, experts, hobbyists), collects and weights their responses by agreement/disagreement, and folds the result back into the shared memory layer. The author (source Reddit comment, in a "RAG isn't the default answer for enterprise anymore" discussion) frames this as going one step beyond RAG because users/team members can correct data that comes back out of it, with corrections fanning out to other team members — described as an early, working prototype.

## Mechanical details

- Self-host: `git clone`, `.env` with `DATABASE_URL`/`ANTHROPIC_API_KEY`/`CHAT_MODEL`, `docker compose up -d` (Postgres+pgvector), `make doctor`, then `make site` / `make mcp` / `make mcp-sse` / `make dashboard`.
- Requires `ANTHROPIC_API_KEY` for the critic, reflect, and chat pipelines; default `CHAT_MODEL` is `claude-haiku-4-5-20251001`.
- Embeddings: `qwen3-embedding` (4096-dim, local Ollama) currently; a migration to Voyage AI `voyage-3` (1024-dim, HNSW-compatible) is planned pre-launch. No direct HNSW index exists yet on the 4096-dim vectors — exact cosine search only until that migration.
- Claude Desktop integration on Windows runs the MCP server via WSL with a thin stdio wrapper (`scripts/mcp_stdio.py`) that filters blank lines before they reach FastMCP's strict JSON-RPC parser.
- A zero-dependency Node.js bridge (`npm/lib/bridge.js`) lets hosted-mode users connect without running Python locally.
- Design invariants stated in the README: Postgres rows are the source of truth (embeddings are pointers); signals are immutable, atoms are revised not deleted; all writes are dual (one atom + one signal); `FLASK_SECRET_KEY` must be set or the app raises at startup; parameterized SQL only; the critic forces `visibility: private` for passwords/API keys/tokens/credentials/health/address/financial content.

## Security

No SPDX license identifier found in the fetched README — treat as unverified. Single-author, early-stage project explicitly described by its own author as "just an early prototype... but working," with 254 memory atoms noted in the README as the current dataset. No test suite or CI configuration is referenced in the fetched content. Requires an `ANTHROPIC_API_KEY` for its critic/reflect/chat pipelines, meaning conversation content is sent to Anthropic's API as part of normal operation. `FLASK_SECRET_KEY` is required with no dev fallback (a reasonable default-deny choice), and the critic auto-forces private visibility for a documented list of sensitive-content categories. The MCP SSE/HTTP transport uses bearer-token auth; the design intent (parameterized SQL only, no raw f-string interpolation of user input) is stated but not independently verified against the actual code in this review.
