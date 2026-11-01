---
name: extractbench
title: ExtractBench
url: "https://github.com/run-llama/ExtractBench"
category: reference
summary: "ExtractBench evaluates document extraction systems on 370 enterprise-grade documents across 67 document types and 8 business domains, scoring schema-valid JSON output with a deterministic unified value F1 metric and no LLM-as-judge"
tags: [benchmark, document-extraction, ocr, enterprise, llamaindex, kaggle, evaluation, structured-output]
reviewed: 2026-09-02
acquired: 2026-09-02
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

ExtractBench evaluates document extraction systems on enterprise-grade inputs. Given a document and a user-defined JSON Schema, a system must return schema-valid JSON with correct values and complete record lists. The benchmark covers 370 enterprise documents spanning insurance filings, financial reports, regulatory submissions, contracts, invoices, and more across 67 document types in 8 business domains.

Evaluation uses five axes: task challenge (form-filling, record-list extraction, needle-in-haystack), perception quality (scans, handwriting, rotated inputs), table structure (merged cells, page breaks), document length (short/medium/long), and domain coverage. The headline metric is unified value F1, computed as an unweighted mean over documents. Scoring is deterministic and rule-based with no LLM-as-judge.

Systems evaluated include frontier VLMs (GPT-5.5, Claude Opus 4.8, Gemini 3.5 Flash), coding agents (Codex, Claude Code), open-source models (Qwen3.6 35B, Lift Datalab 9B), and specialized extraction APIs (Reducto, LlamaIndex Extract). Commercial VLMs perform well on short documents but truncate record lists on long ones (Gemini 3.5 Flash drops from 87.9% to 27.9%). Coding agents retain accuracy but cost 3–8x more per page than specialized APIs.

## Mechanical details

- **Dataset:** 370 documents, 4,869 pages, 67 document types, 8 business domains
- **Metric:** Unified value F1 (unweighted mean over documents)
- **Leaderboard:** Kaggle (ExtractBench Leaderboard)
- **Dataset:** HuggingFace (llamaindex/ExtractBench)
- **Code:** GitHub (run-llama/ExtractBench)
- **Paper:** arXiv, presented at KDD 2026
- **Companion:** ParseBench (document OCR/parsing evaluation)
- **Top result (Jul 2026):** LlamaExtract Agentic Plus — 95.6% F1 at 8.1¢/page

## Security

Benchmark code and dataset only — no runtime security concerns. Systems under test handle enterprise documents that may contain sensitive data; the benchmark dataset uses curated test documents.