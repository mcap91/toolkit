---
name: rag-anything
title: RAG-Anything
url: https://github.com/HKUDS/RAG-Anything
category: framework
summary: All-in-one multimodal RAG framework from HKU's Data Intelligence Lab, built on LightRAG — parses PDFs/Office/images/audio/video via MinerU, Docling, or PaddleOCR, then builds a multimodal knowledge graph linking text, tables, equations, and images; three query modes (text, VLM-enhanced, direct multimodal); 23,500+ GitHub stars; MIT
tags:
  - rag
  - multimodal
  - knowledge-graph
  - document-parsing
  - lightrag
  - python
  - mineru
  - docling
  - paddleocr
  - vlm
reviewed: 2026-10-28
acquired: 2026-10-28
overlaps: []
license: MIT
security_flags: []
source: web
source_url: https://github.com/hkuds/rag-anything
---

## What it does

RAG-Anything extends LightRAG (the same research group's graph-based RAG engine) to handle documents that mix text with images, tables, equations, charts, audio, and video, rather than treating them as text-only. It is built around a four-stage pipeline: document parsing, multimodal content analysis, multimodal knowledge-graph construction, and modality-aware hybrid retrieval.

Document parsing is delegated to a pluggable backend — MinerU (default, strongest OCR/table extraction, GPU-accelerated), Docling (better for Office/HTML, the only built-in parser that accepts HTML), or PaddleOCR (OCR-focused). The parser produces a `content_list` of typed blocks (text, image, table, equation, audio, video, generic), which specialized processors route through dedicated analyzers: a vision-model-backed image analyzer, a structured-data interpreter for tables, a LaTeX-aware equation parser, and an extensible plugin interface for custom content types. Audio is transcribed locally with faster-whisper; video uses scene detection plus keyframe VLM captioning merged with the audio transcript.

Each multimodal element becomes an entity in a knowledge graph with "belongs_to" relationships that preserve document hierarchy, plus weighted cross-modal relationship edges (e.g., a table linked to the paragraph describing it). Retrieval fuses vector similarity search with graph traversal over this structure.

Three query modes: plain text queries routed through LightRAG (`hybrid`/`local`/`global`/`naive` modes), VLM-enhanced queries that automatically load and send retrieved images to a vision model alongside text context, and explicit multimodal queries where the caller supplies specific image/table/equation content to reason about alongside the knowledge base.

Can also skip parsing entirely via `insert_content_list()` to ingest a pre-parsed content list from an external source, and can wrap an existing LightRAG instance rather than creating a new one.

## Installation

```
pip install raganything
pip install 'raganything[all]'     # all optional format support (excludes Docling)
pip install 'raganything[image]'   # BMP/TIFF/GIF/WebP via Pillow
pip install 'raganything[text]'    # TXT/MD via ReportLab
pip install 'raganything[audio]'   # faster-whisper transcription
pip install 'raganything[video]'   # needs ffmpeg on PATH
pip install docling                # for HTML and better Office handling
```

Requires Python 3.10–3.13 for the default MinerU parser path (MinerU 3.x does not support 3.14; on 3.14, use the Docling parser instead). MinerU 4.x is not supported — RAG-Anything pins `mineru[core]>=3.4.1,<4`. Office document formats (.doc/.docx/.ppt/.pptx/.xls/.xlsx) require a separate LibreOffice install.

## Mechanical details

Core API: `RAGAnything(config, llm_model_func, vision_model_func, embedding_func)`, then `process_document_complete(file_path, ...)` for end-to-end ingestion, `process_folder_complete(folder_path, ...)` for batch ingestion, and `aquery()` / `aquery_with_multimodal()` for retrieval. Parser is fixed per-instance via `RAGAnythingConfig(parser=...)`, not switchable per call.

Multimodal (image/table/equation) processing is skipped by default for documents already marked fully processed, to avoid redundant LLM calls; `force_multimodal_reprocess=True` re-runs it, needed when migrating to a new graph/vector storage backend (e.g., switching from file-based storage to Neo4j).

Natively reads MinerU 3.x's `content_list_v2.json` page-grouped output format ahead of the legacy flat format, preserving bounding boxes, anchors, and heading levels. Page headers/footers/page-numbers are excluded from retrieval by default (`include_layout_blocks=True` to keep them).

Academic paper: "RAG-Anything: All-in-One RAG Framework" (arXiv:2510.12323), authored by the HKU Data Intelligence Lab team (Zirui Guo, Xubin Ren, Lingrui Xu, Jiahao Zhang, Chao Huang) — the same group behind LightRAG.

## Security

MIT license. 23,500+ GitHub stars as of October 2026, grown from 1k stars in July 2025. Markdown ingestion resolves local image references on disk and sends them to the configured vision model — the README itself warns to "only ingest Markdown whose image references you trust." LibreOffice-based Office-to-PDF conversion can fetch remote URLs and embed local files referenced in the document, which is why HTML files are rejected by the MinerU/PaddleOCR parsers rather than silently converted. No CVEs or published security audits found.

## How to use it

pip install raganything
