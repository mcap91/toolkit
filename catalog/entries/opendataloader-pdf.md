---
name: opendataloader-pdf
title: OpenDataLoader PDF
url: "https://github.com/opendataloader-project/opendataloader-pdf"
category: cli-tool
summary: "Top-benchmarked open-source PDF parser with bounding boxes, formula extraction, and RAG-ready output — worth piloting for bioinformatics literature ingestion before committing."
tags: [pdf, rag, ocr, markdown, json, bioinformatics, langchain, accessibility]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [java-runtime-required, self-reported-benchmarks, pii-sanitization-opt-in, local-server-process]
overlaps: [markitdown]
source: unknown
---

## What it does

OpenDataLoader PDF converts PDFs to structured Markdown, JSON (with per-element bounding boxes), HTML, or Tagged PDF. It runs in two modes: a fast deterministic local mode (Java-based, ~60 pages/sec on CPU) and a hybrid mode that routes complex pages to a local AI backend for higher accuracy. Hybrid mode adds OCR (80+ languages), borderless table extraction, LaTeX formula extraction, and AI-generated chart/image descriptions. A built-in prompt injection filter strips hidden text, off-page content, and invisible layers before content reaches an LLM. LangChain integration is available via `langchain-opendataloader-pdf`. There is also an accessibility pipeline that auto-tags untagged PDFs into Tagged PDFs (free, Apache 2.0); full PDF/UA export is an enterprise add-on.

## Assessment

Pilot: the feature set is directly relevant to bioinformatics literature pipelines — multi-column layout handling, LaTeX formula extraction, scanned-paper OCR, and JSON bounding boxes for source citations in RAG answers. The self-reported benchmark places it #1 overall (0.907) across 200 real-world PDFs, ahead of docling (0.882), marker (0.861), and pymupdf4llm (0.732). Apache 2.0 with no copyleft obligations is clean for commercial or research use. The main reservations are: (1) Java 11+ is a heavyweight runtime dependency not always present in Python/bio environments; (2) benchmarks are self-reported and need independent confirmation; (3) each `convert()` call spawns a JVM process, so naive loop usage is slow — batching is required. These are manageable but warrant a pilot before adoption.

## Mechanical details

- Install: `pip install -U opendataloader-pdf` (local mode) or `pip install "opendataloader-pdf[hybrid]"` (hybrid + OCR + formulas)
- Requires: Java 11+ on PATH; Python 3.10+; Node.js and Java SDK bindings also available
- API: `opendataloader_pdf.convert(input_path=[...], output_dir="...", format="markdown,json")`
- Hybrid mode: start a local backend server (`opendataloader-pdf-hybrid --port 5002`), then pass `--hybrid docling-fast` to the client CLI or `hybrid="docling-fast"` in Python
- Outputs: `json` (element list with bounding boxes and semantic types), `markdown`, `html`, `text`, `tagged-pdf`, `annotated-pdf` (visual debug)
- JSON element fields: `type`, `id`, `page number`, `bounding box` ([left, bottom, right, top] in PDF points), `content`
- Batch all files in a single `convert()` call — repeated single-file calls are slow due to per-call JVM startup
- LangChain: `pip install langchain-opendataloader-pdf` then use `OpenDataLoaderPDFLoader`
- PII sanitization (emails, URLs, phone numbers → placeholders): opt-in via `--sanitize` flag
- Formula extraction requires `--enrich-formula` on the hybrid server and `--hybrid-mode full` on the client
- License changed from MPL 2.0 (pre-2.0 versions) to Apache 2.0 (2.0+)

## Security

- **License**: Apache-2.0 for core (all extraction, OCR, auto-tagging). Enterprise add-ons (PDF/UA export, accessibility studio) are proprietary.
- **Java runtime**: requires a JVM on the host; JVM dependency broadens the attack surface and adds a non-Python supply chain component.
- **Hybrid mode server**: spawns a local HTTP server process on a configurable port; ensure it is not exposed on a network interface.
- **Prompt injection filtering**: built-in and on by default — strips hidden/invisible text before content is passed to LLMs. PII sanitization is separate and must be explicitly enabled with `--sanitize`.
- **Benchmarks**: all benchmarks are self-reported on the project README; independent third-party verification has not been confirmed.
- **Supply chain**: project is under the `opendataloader-project` GitHub org; contributor count and release signing status are not visible from the README alone — verify before production adoption.
- **No dangerous code patterns** observed in the documented API (no `eval()`, no shell injection vectors visible in the public interface).
