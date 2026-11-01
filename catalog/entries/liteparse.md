---
name: liteparse
title: LiteParse
url: https://github.com/run-llama/liteparse
source_url: https://www.instagram.com/reel/DfAVR6MtdFR/
source: instagram
category: framework
license: Apache-2.0
summary: Open-source, local-first document parser from the LlamaIndex team (`@llamaindex/liteparse`, PyPI `liteparse`, crates.io `liteparse`) — PDFium-based native text extraction in ~2-5ms/page when a document already has selectable text, bundled Tesseract OCR fallback (or a pluggable HTTP OCR backend) for scanned pages, and a per-page `is-complex`/needs_ocr check for routing decisions; Rust core with Node.js, Python, and WASM bindings plus a `lit` CLI; ~12.9k stars.
tags:
  - document-parsing
  - pdf
  - ocr
  - tesseract
  - rust
  - nodejs
  - python
  - wasm
  - llamaindex
  - cli
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
security_flags: []
---

## What it does

LiteParse is an open-source, local-first document parser built by the LlamaIndex team. It extracts text with spatial positioning (bounding boxes) from PDFs and other document formats using PDFium for native text extraction — typically 2-5ms per page when the document already contains selectable text, with no OCR model needed. For scanned or image-based pages it falls back to OCR: Tesseract is bundled by default, or an HTTP OCR server (EasyOCR, PaddleOCR, or a custom backend) can be plugged in via a documented OCR API spec. A built-in complexity check (`lit is-complex`) flags per-page `needs_ocr` reasons (scanned, no-text, sparse-text, embedded-images, garbled, vector-text, annotation-text) before a full parse, positioning it as a cheap first step in document-routing pipelines that escalate complex pages to heavier tools like Docling or a vision-language model.

## Mechanical details

- Core implemented in Rust; bindings via napi-rs (Node.js), PyO3 (Python), wasm-bindgen (browser/WASM).
- Install: `npm i -g @llamaindex/liteparse` (Node CLI `lit`), `pip install liteparse` (Python), `cargo install liteparse` (Rust), `npm i @llamaindex/liteparse-wasm` (browser).
- CLI: `lit parse document.pdf`, `lit parse --format markdown -o output.md`, `lit screenshot document.pdf -o ./screenshots`, `lit is-complex document.pdf`, `lit batch-parse ./input ./output`.
- Output formats: Markdown (reconstructed headings/tables/lists/images/links), JSON, plain text; also extracts embedded images, vector graphics, AcroForm fields, annotations, and tagged-structure trees.
- Supports PDF plus Office formats (DOCX/XLSX/PPTX) and images; non-PDF formats are auto-converted to PDF before parsing.
- Maintained by run-llama (LlamaIndex); ~12.9k stars / 893 forks at review.

## Usage notes

- In a 3-step LiteParse → Docling → Qwen OCR router demo, LiteParse extracted a simple one-page text document almost perfectly, missing only a page number and one dash; on a page with a complex merged-cell table, LiteParse's native-text extraction misplaced row labels above the table and split the table into two, triggering escalation to Docling. (source: https://www.instagram.com/reel/DfAVR6MtdFR/)

## Security

- Apache-2.0.
- Bundled Tesseract OCR runs locally; the optional HTTP OCR backend sends document content to a configured external server — a standard data-exfiltration consideration for any pluggable-OCR design.
- No disclosed CVEs or incident reports found in review.