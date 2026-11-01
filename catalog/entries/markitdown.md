---
name: markitdown
title: MarkItDown
url: "https://github.com/microsoft/markitdown"
category: cli-tool
summary: "directly useful for converting PDFs, Excel, PPTX, and other docs to markdown for LLM pipelines; MIT, Microsoft-maintained"
license: MIT
tags: [markdown, conversion, pdf, documents, excel, llm-preprocessing]
reviewed: 2026-05-27
acquired: 2026-05-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

A lightweight Python utility from Microsoft that converts diverse file formats to Markdown for use with LLMs and text analysis pipelines. Supports PDF, PowerPoint, Word, Excel, images (with EXIF metadata and OCR), audio (with metadata and transcription), HTML, CSV, JSON, XML, ZIP files, YouTube URLs, and EPub. Preserves document structure — headings, lists, tables, and links. Offers both a CLI (`markitdown path-to-file.pdf > doc.md`) and a Python API. Optional integrations with Azure Document Intelligence for enhanced extraction and OpenAI-compatible clients for LLM-based image descriptions. Has a third-party plugin system for extended functionality.

## Assessment

No existing catalog entry covers file-to-markdown conversion. Directly useful for two common scenarios: (1) converting computational biology papers and supplementary PDFs into markdown for skill ingestion via Book to Skill or LLM context, and (2) converting Excel/CSV data files into structured markdown for pipeline documentation. MIT licensed, actively maintained by Microsoft, lightweight install. Pilot to verify quality of PDF table extraction on typical bioinformatics supplementary material before adopting broadly.

## Mechanical details

Install: `pip install 'markitdown[all]'` (the `[all]` extra pulls OCR and audio dependencies). CLI usage: `markitdown input.pdf -o output.md` or piped `cat input.pdf | markitdown`. Python API: `from markitdown import MarkItDown; md = MarkItDown(); result = md.convert("input.pdf")`. Docker image also available. Pilot test: convert a methods-heavy PDF with tables and check structural fidelity.

## Security

MarkItDown runs with the full I/O privileges of the calling process — it behaves like `open()` or `requests.get()` and will access any resource the process can reach. The upstream documentation explicitly flags this: untrusted input must be validated before passing to `convert()`, including restricting file paths, limiting URI schemes, and blocking access to private or metadata-service addresses. In server-side or agent pipeline use, prefer the narrower `convert_local()`, `convert_response()`, or `convert_stream()` APIs over the catch-all `convert()` to minimize attack surface.

Third-party plugins (disabled by default, opt-in via `--use-plugins`) execute arbitrary Python code; only enable plugins from trusted sources and pin plugin package versions. The optional Azure Document Intelligence and Azure Content Understanding backends make billable outbound API calls — ensure credentials are scoped and not over-privileged. No CVEs are on record as of the review date; the project is MIT-licensed and maintained by Microsoft under their open-source security policy.

## How to use it

pip install 'markitdown[all]'
