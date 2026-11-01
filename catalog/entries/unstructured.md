---
name: unstructured
title: Unstructured
url: "https://github.com/Unstructured-IO/unstructured"
category: framework
summary: "Open-source document ETL library — partitions 60+ file types (PDFs, Word, HTML, images, emails) into structured elements (Title, NarrativeText, Table, etc.) with layout ML enrichment, OCR, chunking, and embedding; connectors for 40+ sources/destinations; MCP server (Unstructured Transform) for agent-driven document processing; Apache-2.0, 15k+ stars"
tags: [document-parsing, etl, ocr, pdf, chunking, embedding, rag, mcp-server, llm-preprocessing, python]
reviewed: 2026-09-03
acquired: 2026-09-03
license: Apache-2.0
security_flags: [telemetry-default-on]
overlaps: [docling-mcp]
source: unknown
---

## What it does

Unstructured converts unstructured documents into structured data for LLM pipelines. The library partitions files into typed elements (Title, NarrativeText, Table, ListItem, Image, PageBreak, etc.) with metadata including coordinates, page numbers, languages, and content hashes. It supports 60+ file types: PDFs (native and scanned), Word, PowerPoint, Excel, HTML, XML, JSON, email (EML/MSG), images, and more.

The processing pipeline: load from 40+ connectors (filesystem, S3, Gmail, Jira, Google Drive, etc.) → partition into elements using file-type-specific parsers → enrich with layout ML (table detection, header hierarchy, image OCR via Tesseract) → chunk for retrieval → embed → output as JSON, Markdown, HTML, or Arrow to destination connectors (vector databases, cloud storage, etc.).

Unstructured Transform is an MCP server that exposes document processing to AI agents — parse, enrich, chunk, and embed files directly within an agent session. Works with Claude Code, Cursor, Codex CLI, and other MCP-compatible hosts.

## Differentiators

- Broadest file-type coverage among open-source document parsers (60+ formats)
- Modular architecture: install only the extras needed (`pip install "unstructured[pdf,docx]"`)
- Both open-source library and hosted API/platform for production workloads
- MCP server mode (Unstructured Transform) for agent-driven document processing
- 40+ source/destination connectors for ETL pipelines
- Active development since 2022; 15k+ GitHub stars, 261 contributors, regular releases (latest 0.24.0, July 2026)

## Mechanical details

- Language: Python
- Install: `pip install "unstructured[all-docs]"` or Docker (`downloads.unstructured.io/unstructured-io/unstructured:latest`)
- System dependencies: libmagic (filetype detection), poppler-utils (PDF/images), tesseract-ocr (OCR), libreoffice (MS Office)
- Core API: `partition(filename=...)` auto-detects file type and routes to type-specific partitioner
- Dev tooling: uv for dependency management, pre-commit hooks, Makefile-based workflow
- Enterprise: Unstructured Pipelines (hosted) with advanced chunking, embedding, and image/table enrichment via low-code UI or API

## Security

- Apache-2.0 license
- Sends lightweight telemetry by default (package version, platform info, partition characteristics — no document content or filenames); opt out via `DO_NOT_TRACK` or `SCARF_NO_ANALYTICS` environment variables
- Standard Python ML/NLP dependency stack; uses poppler, tesseract, libreoffice as system dependencies
- Active security policy with vulnerability reporting process
- No eval() or shell injection patterns observed in core partitioning code