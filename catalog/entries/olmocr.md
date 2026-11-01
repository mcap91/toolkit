---
name: olmocr
title: olmOCR
url: "https://github.com/allenai/olmocr"
category: cli-tool
summary: "AI2's VLM-based PDF/image-to-Markdown toolkit — 7B parameter model converts PDFs with equations, tables, handwriting, multi-column layouts into clean Markdown; <$200/M pages; multi-node S3-coordinated batch pipeline; ships comprehensive benchmark (7K+ test cases); Apache 2.0"
tags: [ocr, pdf, markdown, vlm, document-processing, allen-ai, vllm, batch-pipeline, benchmark, bioinformatics]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: []
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

olmOCR is a toolkit from the Allen Institute for AI (AI2) that converts PDFs, PNGs, and JPEGs into clean Markdown using a 7B-parameter vision language model (based on Qwen2.5-VL, fine-tuned with SFT and GRPO RL training). It handles equations, tables, handwriting, complex formatting, multi-column layouts, figures, and insets while preserving natural reading order and automatically removing headers/footers.

Key capabilities:

- **Single-file conversion**: `olmocr ./workspace --markdown --pdfs document.pdf`
- **Batch pipeline**: Process millions of PDFs with multi-node coordination via AWS S3 work queues. Workers grab items from a shared queue automatically.
- **Remote inference**: Use any OpenAI-compatible endpoint (vLLM, DeepInfra, Parasail, Cirrascale) with `--server` flag. Lightweight install (`pip install olmocr`) when using remote inference — no GPU dependencies.
- **Docker support**: Pre-built images (~30GB with model included) for containerized deployment.
- **Benchmark suite (olmOCR-Bench)**: 7,000+ test cases across 1,400 documents covering ArXiv, old scans, math, tables, headers/footers, multi-column, long tiny text. v0.4.0 scores 82.4, competitive with Chandra OCR (83.1) and Infinity-Parser (82.5).

Outputs in Dolma format (AI2's data format) and optionally Markdown. Cost is under $200 USD per million pages converted.

## Mechanical details

Requires NVIDIA GPU with 12+ GB VRAM for local inference (tested on RTX 4090, L40S, A100, H100). Uses vLLM for inference. Python 3.11 recommended via conda. System dependencies: poppler-utils and Microsoft core fonts. Supports tensor parallelism and data parallelism for multi-GPU setups. Beaker cluster integration for AI2 internal use.

Reusable code components: GPT-4o prompting strategy for silver data generation (`buildsilver.py`), language/SEO-spam filtering (`filter.py`), SFT training code (`train.py`), GRPO RL trainer (`grpo_train.py`), synthetic data generation (`mine_html_templates.py`).

## Security

Apache 2.0 licensed. Developed by AI2 (non-profit). No security flags. The pipeline processes documents locally or via user-specified inference endpoints. Model weights hosted on Hugging Face. Docker images available on Docker Hub. No telemetry or external data collection.

## How to use it

pip install olmocr[gpu] --extra-index-url https://download.pytorch.org/whl/cu128
