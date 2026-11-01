---
name: parsebench
title: ParseBench
url: "https://github.com/run-llama/ParseBench"
category: framework
summary: "LlamaIndex document parser benchmark — tests parsers across text, formatting, tables, charts, and page-location attribution; v1.0 with visual checks and scoring fixes (breaking change from v0.2)"
tags: [benchmark, document-parsing, evaluation, llamaindex]
reviewed: 2026-09-16
acquired: 2026-09-16
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

ParseBench evaluates how well document parsers convert PDFs and other documents into structured output that AI agents can reliably act on. It scores parsers across five capability dimensions: text/content faithfulness, semantic formatting, tables, charts, and visual grounding (page-location attribution).

The visual grounding dimension tests whether a parser can point back to the source location (page/region) of a given result, so extracted content can be verified against the original document rather than trusted blindly.

Evaluation is rule-based and deterministic by default — ParseBench does not require LLM-as-a-judge for scoring; API keys are used only to call the parsing tool under test, not to grade its output.

The evaluation set spans human-verified pages drawn from publicly available documents across domains (insurance, finance, government, and others), with dense per-dimension test-rule coverage for diagnosing where a given parser breaks down.

Distributed as an installable Python package (`parse-bench` on PyPI) with a pluggable provider system supporting 30+ parsing backends (OpenAI, Anthropic, Gemini, local models, and specialized document-parsing services, including LlamaParse).

## Differentiators

- **Page-location attribution** — scores whether a parser can cite the source location of a result, not just whether the extracted text matches
- **Chart evaluation** — scores extraction of actual chart values with correct series names and axis labels, rather than raw OCR dumps or skipped charts
- **Rule-based scoring** — deterministic, rule-driven evaluation rather than LLM-as-a-judge by default
- **Broad provider coverage** — 30+ pluggable parsing providers/backends evaluated under one harness
- **v1.0 rework** — corrected scoring/provider bugs from earlier versions, added new rule types and visual-grounding checks, and packaged for PyPI to simplify installation

## Mechanical details

- Source: https://github.com/run-llama/ParseBench
- Package: `parse-bench` (PyPI)
- Paper: arXiv:2604.08538
- Dataset: HuggingFace `llamaindex/ParseBench` (also mirrored on Kaggle)
- Leaderboard: parsebench.ai
- **Breaking change in v1.0**: scores produced by v0.2 and earlier are not compatible with v1.0 due to scoring-core fixes (blank-page handling, table canonicalization, visual grounding/extract scoring, TEDS/GriTS scoring implementations) — benchmarks run on older versions must be rerun under v1.0 for comparable results
- Post-1.0.0 patch releases added further scoring adjustments, a new layout-detection provider, a dependency removal (scikit-learn), and additional model/provider integrations

## Security

License: Apache-2.0. Evaluation harness calls out to third-party parsing providers/APIs configured by the user (API keys used only to invoke the parser under test, not for LLM-based grading).
