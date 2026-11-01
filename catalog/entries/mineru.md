---
name: mineru
title: MinerU
url: "https://github.com/opendatalab/MinerU"
category: framework
summary: "Open-source document parsing engine by OpenDataLab — converts PDFs, images, Office docs (Word/PPT/Excel), EPUB, OFD, HTML/MHTML, CSV into LLM-ready Markdown/JSON with four quality tiers (flash/basic/standard/advanced); VLM+OCR dual engine supporting 109 languages; local-first with optional remote API; CLI with agent-oriented continuation/locator system; local document library with search/watch/scan; MCP server; integrations with LangChain, RAGFlow, Dify, FastGPT; Python >=3.10; Apache-2.0 with commercial threshold (100M MAU or $20M revenue); ~80k stars"
tags: [document-parsing, pdf, ocr, markdown, json, vlm, rag, agent, mcp, python, office, epub]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: [unstructured]
license: Apache-2.0
security_flags: [commercial-threshold-license]
source: unknown
---

## What it does

MinerU is a document parsing engine that extracts content from unstructured documents and converts it to machine-readable Markdown and JSON. It targets three use cases: LLM pre-training data pipelines, RAG document ingestion, and agent-driven document reading workflows.

Version 4.0 combines document parsing, a local document library, and service tools into one CLI:

- **Parsing**: Processes PDFs (including scanned), images (PNG/JPG/WebP/GIF/BMP/TIFF/JP2), Word (.doc/.docx), PowerPoint (.ppt/.pptx), Excel (.xls/.xlsx), RTF, OpenDocument (.odt/.ods/.odp), EPUB, OFD, HTML/MHTML, and CSV/TSV. Four quality tiers — flash (fastest, lowest quality), basic (OCR/model-based), standard (high quality, default), and advanced (maximum quality, slowest). PDF and images support all tiers; Office/HTML/EPUB/OFD use local flash parsing.
- **Agent reading**: Continuation-based reading with stable locators (`doc:{id}/tier:{tier}/page:{page}/block:{block}`) for citation, follow-up reads, and progressive document traversal. Default reads first 10 pages with continuation markers. `--json` mode for structured agent control flow.
- **Local document library**: Background service with file discovery (`scan`), persistent folder watching (`watch`), content search across indexed documents, and cache management. `DoclibClient` Python SDK for programmatic access.
- **Privacy-first**: All parsing runs locally by default. Remote parsing requires explicit `--remote` flag and user consent. Local failure does not silently fall back to remote.

Uses PDF-Extract-Kit models internally. Model engines include ONNX (CPU), PyTorch (GPU/MPS), llama.cpp (Vulkan), and vLLM/lmdeploy/mlx for VLM inference. Base install (~0.8–2 GB models) works on CPU; `mineru[full]` extra adds GPU-accelerated inference for NVIDIA GPUs with 8+ GB VRAM.

## Installation

Install via `uv tool install "mineru>=4.0,<5"` (preferred), `pipx install "mineru>=4.0,<5"`, or `pip install "mineru>=4.0,<5"`. Requires Python >=3.10,<3.15. Base package uses ONNX CPU + llama.cpp Vulkan; `mineru[full]` adds PyTorch + vLLM/lmdeploy for NVIDIA GPU acceleration. After install: `mineru server start` to launch the background parsing service. Models download on first use or via `mineru-kit models download --tier <tier>`.

Also installable as a Claude Code skill (`mineru skill`) that provides the agent with a structured decision tree for document reading, continuation, and error recovery.

## Mechanical details

CLI commands: `parse` (first read from file), `read` (by locator), `find` (filename search), `search` (content search), `show`/`list` (status inspection), `watch`/`scan` (library management), `config` (settings), `server` (background service), `forget`/`invalidate`/`cleanup` (cache control). All commands support `--json` for structured output. Error codes are machine-readable with `retryable` flags and `user_action` suggestions.

Managed parse server has two startup tiers: basic (ONNX, ~0.8 GB models, 2 GB RAM) and standard (ONNX + llama.cpp or PyTorch + VLM, ~2–3 GB models, 8–16 GB RAM). Advanced tier uses standard infrastructure with more compute per request.

MinerU ecosystem includes MinerU-Diffusion (ECCV 2026, diffusion-based OCR), MinerU-Popo (MIT, post-processing OCR output into document trees), and MinerU-Document-Explorer (agent-native knowledge engine with MCP tools).

## Security

Apache-2.0 with additional commercial terms: free for commercial use unless the entity exceeds 100M monthly active users or $20M monthly revenue, at which point a separate commercial license is required. Optional anonymous usage telemetry (no document content, filenames, or paths collected) — can be disabled via `mineru telemetry disable`. Remote parsing sends documents to OpenDataLab servers only when explicitly authorized with `--remote`. ~80k GitHub stars, 6.7k forks, backed by OpenDataLab (Shanghai AI Laboratory).

## How to use it

uv tool install "mineru>=4.0,<5"
