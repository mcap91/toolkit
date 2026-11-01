---
name: docling-mcp
title: Docling MCP
url: "https://github.com/docling-project/docling-mcp"
category: mcp-server
summary: "MCP server for document conversion, processing, and generation via the Docling library — converts PDFs and other documents into structured DoclingDocument JSON with OCR, table structure detection, and image handling; supports local, remote (Docling Serve), and hybrid modes; RAG integrations with Milvus, LlamaIndex, and LlamaStack; LF AI & Data project from IBM Research Zurich, MIT, 730+ stars"
tags: [document-parsing, mcp-server, ocr, pdf, table-extraction, docling, ibm, rag, document-generation, python]
reviewed: 2026-09-03
acquired: 2026-09-03
license: MIT
security_flags: []
overlaps: [unstructured]
source: unknown
---

## What it does

Docling MCP is an MCP server that wraps the Docling document processing library, exposing document conversion, processing, and generation as MCP tools callable by AI agents. It converts PDF documents into structured DoclingDocument format (JSON) with layout-aware parsing including OCR, table structure detection, and optional image retention.

The server operates in three modes:

- **Remote**: lightweight client that calls a Docling Serve instance (API-based, ~50MB install)
- **Local**: full Docling pipeline runs locally with all ML models (`pip install docling-mcp[local]`)
- **Hybrid**: remote-first with automatic fallback to local if the service is unreachable

Tools include document conversion (PDF → structured JSON), document generation (programmatic creation of new documents with titles, sections, paragraphs, lists), Markdown/format export, and RAG workflows (Milvus vector upload/retrieval, LlamaIndex RAG, LlamaStack extraction).

## Differentiators

- Official MCP server for the Docling ecosystem (LF AI & Data Foundation project, IBM Research Zurich)
- Three deployment modes (remote/local/hybrid) with ~90% size reduction in v2.0 for remote mode
- Document generation tools — not just conversion but programmatic creation of new structured documents
- Built-in RAG integrations: Milvus vector DB, LlamaIndex with configurable embedding/LLM, LlamaStack for structured extraction
- Supports stdio, SSE, and streamable-http transports for different MCP client requirements
- Local document caching for repeated access performance
- 730+ GitHub stars; active development (v3.0+ for MCP SDK v2 compatibility)

## Mechanical details

- Language: Python
- Install: `pip install docling-mcp` (remote) or `pip install docling-mcp[local]` (local mode with ML models)
- Launch: `uvx --from docling-mcp docling-mcp-server --transport stdio`
- Configuration: environment variables with `DOCLING_MCP_` prefix (conversion mode, service URL, OCR toggle, table structure, image handling, RAG endpoints)
- MCP SDK compatibility: v3.0+ requires `mcp>=2.0.0`; v2.x works with `mcp>=1.9.4,<2.0.0`
- Toolgroups: selectable via `--tools` flag (e.g., `llama-index-rag`, `llama-stack-rag`, `llama-stack-ie`)

## Security

- MIT license
- API key for remote Docling Serve passed via environment variable (not embedded in code)
- No eval() or shell injection patterns observed
- LLM endpoint credentials for RAG integrations configured via environment variables
- Part of LF AI & Data Foundation; IBM Research Zurich origin

## Usage notes

- Docling is the enabling technology for IBM's "Chunkless RAG" architecture — reconstructs logical document hierarchy from PDFs so an AI agent can navigate the tree structure (headings, sections, subsections) instead of retrieving fixed-size chunks. See the chunkless-rag catalog entry.

- On the same IRS depreciation table (3 years, dollar/percentage/deduction columns) where PaddleOCR mislinked years to amounts, Docling produced a complete and correctly structured table — all columns, headers, and numbers present and properly linked. Output still needed post-processing cleanup: inconsistent dollar-sign/percent-sign formatting across rows, and unnecessary leading/trailing dots in two columns (likely table-line/dot-fill artifacts from the source PDF). (source: https://www.instagram.com/reel/DecS5IkjwSA/)

- On the same IRS tax-computation worksheet table where PaddleOCR misread the upper limit of the "over $197,300" row as $50,525, Docling correctly read the upper limit as $250,000. (source: https://www.instagram.com/reel/DeUWz-7FAgX/)

- On a complex merged-cell table in a 3-step OCR router demo (LiteParse → Docling → Qwen), Docling preserved the table structure far better than LiteParse's native-text extraction, but merged two numeric values into a single cell (e.g. "0.1" and "100" separated only by a space in the raw output) — the specific trigger a deterministic routing rule used to escalate that table region from Docling to a cropped-region Qwen pass. (source: https://www.instagram.com/reel/DfAVR6MtdFR/)
