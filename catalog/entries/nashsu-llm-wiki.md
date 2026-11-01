---
name: nashsu-llm-wiki
title: LLM Wiki (nashsu)
url: https://github.com/nashsu/llm_wiki
source_url: https://github.com/nashsu/llm_wiki
category: framework
summary: Cross-platform Tauri desktop app implementing Karpathy's LLM Wiki pattern — ingests documents (PDF/DOCX/PPTX/XLSX/EPUB/images/web clips) and incrementally compiles them into a persistent, interlinked wiki instead of re-deriving answers via RAG each query; ships a knowledge-graph visualizer (sigma.js/graphology, 4-signal relevance, Louvain community detection), optional LanceDB vector search, a tool-using chat agent, a local token-protected HTTP API plus MCP server for Claude Code/Codex, and an Obsidian-compatible vault output; ~21k GitHub stars; GPLv3
tags:
  - llm-wiki
  - knowledge-base
  - knowledge-graph
  - tauri
  - desktop-app
  - obsidian
  - mcp-server
  - vector-search
  - rag-alternative
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - karpathy-llm-wiki
  - nvk-llm-wiki
license: GPL-3.0
security_flags:
  - network-service
  - api-keys-required
  - copyleft-license
source: web
---

## What it does

Desktop application (Rust/Tauri backend, React/TypeScript frontend) implementing Andrej Karpathy's LLM Wiki pattern: instead of RAG re-deriving answers from raw sources on every query, the app ingests documents once via a two-step chain-of-thought process (analysis then generation) and incrementally compiles them into a persistent, cross-linked markdown wiki. Supports PDF, DOCX, PPTX, XLSX, EPUB/MOBI, images, and web clips (via a bundled Chrome extension); the output wiki directory is Obsidian-vault-compatible. Includes a knowledge-graph view (sigma.js + graphology + ForceAtlas2 layout) built on a 4-signal relevance model (direct links, source overlap, Adamic-Adar, type affinity) with Louvain community detection for cluster discovery, plus a "Graph Insights" feature that surfaces gaps and unexpected connections via one-click deep research. Search combines tokenized keyword search, graph relevance, and optional LanceDB vector embeddings. Ships a Rust backend chat agent that can search the wiki/sources/graph, do web search (Tavily/SerpApi/SearXNG), read/write workspace files, and run shell commands with approval. Exposes a local, token-protected HTTP API (127.0.0.1:19828) and a bundled MCP server plus an installable agent skill so external clients (Claude Code, Codex) can query the wiki, traverse the graph, and trigger source rescans.

## Mechanical details

- Stack: Tauri v2 (Rust) backend, React 19 + TypeScript + Vite frontend, shadcn/ui + Tailwind CSS v4, Milkdown (ProseMirror) editor, react-i18next (English, Chinese).
- Document processing: pdf-extract, optional MinerU, docx-rs, calamine, EPUB/MOBI parsers.
- Install: pre-built binaries for macOS (Apple Silicon), Windows (.msi), Linux (.deb/.AppImage) via GitHub Releases; building from source requires Node.js 20+, Rust 1.88+, protoc.
- LLM providers: OpenAI, Anthropic, Google, Ollama, and custom OpenAI-compatible endpoints — all require the user's own API keys.
- ~21.2k GitHub stars, ~2.4k forks, 907 commits at time of review.

## Security

GPL-3.0 (copyleft; derivative works and modified distributions must also be GPL-3.0). Runs a local HTTP API bound to 127.0.0.1 and token-protected; exposure is local-only by default. LLM calls, optional web-search integrations (Tavily/SerpApi/SearXNG), and optional MinerU PDF processing can send data to third-party cloud endpoints and require API keys configured by the user. No telemetry described in the README.

## Usage notes

- Cited in an Instagram reel (uncredited blind benchmark methodology) as "the most starred" of three LLM-wiki implementations tested, but performing no better than plain Claude Code on blind-graded answer accuracy even with vector search enabled, while costing more per answer; the reel's conclusion was that GitHub star count did not predict benchmark performance (source: https://www.instagram.com/reel/DfFSZDvN6oV/)
