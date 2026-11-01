---
name: isaacflath-ocr-guides
title: Isaac Flath — Documents in AI Products (OCR Pipeline Guides)
category: reference
summary: "14-post blog series covering OCR model selection, VLM OCR, speculative decoding, PDF retrieval, chunking, quantization, and document QA — practical guidelines for designing OCR pipelines"
tags: [ocr, vlm, retrieval, chunking, quantization, colbert, rag, document-processing, pdf]
reviewed: 2026-09-03
acquired: 2026-09-03
license: n/a
security_flags: []
overlaps: [ovisocr2, opendataloader-pdf]
source: unknown
---

## What it does

Three blog series by Isaac Flath (isaacflath.com) covering the full document-AI pipeline: reading documents (OCR model selection, VLM architectures, speculative decoding, failure modes), searching documents (BM25, dense/multivector retrieval, ColBERT quantization, late chunking, reranking), and using documents (citation-grounded QA, RLM agent architecture). Includes benchmark comparisons of OCR models, retrieval methods, and cost/latency tradeoffs.

## Assessment

Directly applicable to OCR pipeline design. Covers the decision matrix for self-host vs API, open pipeline vs VLM, and cost tradeoffs at scale. The retrieval posts inform chunking and search strategy downstream of OCR. Written by a practitioner (talks feature Joe Barrow from Adobe Document Intelligence Lab). Content is opinionated and grounded in production experience at Pattern Data (~7M pages of local laws, hundreds of millions of document pages).

## Mechanical details

Source: isaacflath.com, API at `/api/posts`. Full verbatim content archived locally:

- reading-documents — Speculative Decoding, OCR Examples Gallery, How to Choose an OCR Model, VLM OCR for Hard Documents
- searching-documents-1 — What Actually Improves PDF Retrieval, Query Disambiguation, Quantization for ColBERT, RAG Context Problem
- searching-documents-2 — mgrep, Keyword Search, Late Chunking, Retrieval 101
- using-documents — Document Answers You Can Check, How My RLM Tool Works

Key models/tools discussed: Chandra 2, Surya, LightOnOCR-2, PaddleOCR, MonkeyOCR, GLM-OCR, AWS Textract, Gemini 3.5 Flash, Mixedbread Wholembed, ColBERT, Jina, Voyage, vLLM, Modal.

## Security

Blog content, no code execution. Source files are local archival copies for personal reference.

## Usage notes

- Signature OCR (Isaac Flath, Sep 2026): on a page with two clear and two faint signatures, Gemini marked all four signed; AWS Textract found 3 of 4 regions at 32–41% confidence. Faint/erased marks force a policy decision (route to human? re-sign? where's the signed/unsigned line?) — include non-perfect and faded signatures in the eval set and decide handling up front.
- Table layout (same source): basic OCR lost number↔column-heading relationships in a financial table; Docling and Chandra restored the complete table including the total row, while Qwen and Gemini returned JSON records instead — use Docling/Chandra when output must mirror the source layout, Qwen/Gemini when re-rendering or cross-checking.
- LandingAI DPT-3 structured extraction on a loan estimate + closing disclosure loaded into SQLite: all six dollar amounts matched; fields absent from the source correctly stayed empty.
- EVIE (document page-image search incl. charts/diagrams): intended page ranked first in three realistic queries — small sample, failure modes not yet mapped.

- OCR model auto-router (Isaac Flath via Instagram reel, Oct 2026, referencing a Reducto blog post): train two regression models per candidate OCR-model pair — one predicting the accuracy delta, one predicting the latency delta between a light and a heavy model on a page. Build the training set by running every page through both models and scoring/timing each; feed the regressors summary statistics of the light model's output (e.g., word count, confidence scores), not its raw output. At inference only the light model runs; its stats predict both deltas, and a separate decision rule (e.g., is a 5% accuracy gain worth 3 extra seconds) decides whether to escalate that page to the heavy model. A regression model is preferred over a binary classifier because the escalation threshold can be tuned later without retraining. The presenter's own worked pairing (Tesseract light / Chandra heavy) is explicitly not the model pair Reducto said it used; the approach generalizes to any two-model pair (e.g., a light parser escalating to Docling, or Docling escalating to a VLM like Qwen). (source: https://www.instagram.com/reel/DeRx_ZXFT42/)

- OCR router error analysis + worked 3-step demo (Isaac Flath via Instagram reel, Oct 2026): walks a LiteParse → Docling → Qwen router through a real 2-page PDF with annotated traces. A simple text page stops after LiteParse (near-perfect, missed only a page number and a dash); a dense-table page escalates through all three steps as LiteParse mangles the table, Docling fixes structure but merges two values into one cell, and a cropped-region Qwen pass fixes that but shifts two values to the wrong row — even a 3-step router still needs error analysis, since no step is perfect. Deterministic routing rules check for sparse text, complex layout, table presence, merged cells, and embedded images to decide escalation. Common router failure modes shown: failing to escalate when a model's output looks structurally plausible but actually scrambles label-to-value associations (a utility bill processed by Docling), and escalating when unnecessary because the cheaper step was already correct (added cost/latency with no accuracy gain). For the regression-model approach, concrete candidate features are listed: page width/height/aspect ratio, OCR confidence scores, word/line counts and words-per-line, plus structural guesses (row/column counts, merged-cell presence, empty-cell fraction) — all computed from the small model's own output so the routing step stays cheap. See reducto-model-routing for the underlying framework, and liteparse/tesseract for the light-model tools named. (source: https://www.instagram.com/reel/DfAVR6MtdFR/)
