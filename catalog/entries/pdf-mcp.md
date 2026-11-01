---
name: pdf-mcp
title: pdf-mcp
url: "https://github.com/jztan/pdf-mcp"
category: mcp-server
summary: "MCP server for surgical PDF access by AI agents — 13 tools for hybrid search (BM25 + semantic), selective page reading, table/image/chart extraction, OCR via Tesseract, corpus-wide multi-document search, and multi-column/CJK layout support; SQLite cache persists across restarts. MIT."
license: MIT
tags: [pdf, mcp-server, search, ocr, rag, tables, charts, corpus, hybrid-search, cjk, tesseract]
reviewed: 2026-09-04
acquired: 2026-09-04
overlaps: [opendataloader-pdf]
security_flags: [exposes-local-filesystem-paths]
source: unknown
---

## What it does

pdf-mcp is an MCP server that gives AI agents structured, token-efficient access to PDF documents. Instead of loading entire PDFs into context, the agent calls specialized tools: `pdf_info` for page count and TOC, `pdf_search` for hybrid keyword+semantic search with paragraph-level excerpts, `pdf_read_pages` for selective page reading, and `pdf_extract_chart` for (x, y) data from vector charts. A corpus mode (`pdf_corpus_warm`, `pdf_corpus_overview`, `pdf_corpus_search`) enables triage and search across entire folders of PDFs. OCR for scanned pages uses Tesseract, parallelized across pages. Multi-column and vertical Japanese (tategaki) layouts are handled by geometric reading-order reconstruction from glyph positions. All parsed content is cached in SQLite so repeated access avoids re-parsing.

13 tools total: `pdf_info`, `pdf_search`, `pdf_read_pages`, `pdf_read_all`, `pdf_get_toc`, `pdf_render_pages`, `pdf_extract_chart`, `pdf_corpus_warm`, `pdf_corpus_overview`, `pdf_corpus_search`, `pdf_cache_stats`, `pdf_cache_clear`, `server_info`.

## Assessment

pdf-mcp addresses a real gap: large PDFs overwhelm agent context windows and naive text extraction loses structure. The hybrid search (BM25 + semantic via RRF) with section-aware chunking means the agent often gets an answer from search excerpts alone without needing to read full pages. The corpus tools turn a folder of PDFs into a searchable knowledge base with no ingestion pipeline or vector database. 811 commits in the trailing 12 weeks (as of September 2026) and active maintenance. The 13-tool surface is well-decomposed: `pdf_info` → `pdf_search` → `pdf_read_pages` is the canonical agent workflow. HTTP transport mode (`pdf-mcp-http`) supports remote deployment with auth tokens and path allow-lists. Content-trust detection flags hidden or injected text without stripping it.

## Mechanical details

- **Install:** `pip install pdf-mcp` (hybrid search, corpus tools, multi-column/CJK work out of the box)
- **OCR requires system Tesseract:** `brew install tesseract` (macOS), `apt install tesseract-ocr` (Ubuntu), `winget install Tesseract-OCR` (Windows)
- **Claude Code setup:** `claude mcp add pdf-mcp -- pdf-mcp`
- **MCP name:** `io.github.jztan/pdf-mcp`
- **HTTP transport:** `pdf-mcp-http` for remote/shared deployment; Docker images on GHCR for amd64/arm64
- **Typical agent workflow:** `pdf_info` (plan) → `pdf_search` (locate, often terminal) → `pdf_read_pages` (deep read if needed)
- **Corpus workflow:** `pdf_corpus_warm` (cache folder) → `pdf_corpus_overview` (triage) → `pdf_corpus_search` (cross-document search)
- **Cache:** SQLite, survives restarts, manageable via `pdf_cache_stats` / `pdf_cache_clear`

## Security

MIT licensed. The server accesses local filesystem paths specified by the agent or user; path restrictions can be configured. The HTTP transport (`pdf-mcp-http`) fails closed: without an auth token and path allow-list, the process exits rather than serving an open endpoint. Content-trust detection flags hidden text that a human reader cannot see (e.g., invisible text layers, prompt injection attempts) — flagged per page, not stripped. A published `SECURITY.md` documents the threat model and reporting channel. The primary risk is filesystem exposure: the server reads whatever paths the calling agent provides, bounded only by OS permissions and optional configuration.

## How to use it

pip install pdf-mcp
