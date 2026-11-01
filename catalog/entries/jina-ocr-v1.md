---
name: jina-ocr-v1
title: Jina-OCR-v1
url: "https://huggingface.co/jinaai/jina-ocr-v1"
category: framework
summary: "End-to-end document-to-Markdown OCR model (3.4B total / 570M active MoE) with FastMTP speculative decoding (K=3, ~2x decode speed on L4) — scores 91.14 OmniDocBench, 83.4 olmOCR-Bench, 2.57 pages/s on A100; handles text, tables, math, handwriting, 100+ languages; runs via Transformers or vLLM; hosted via Jina Reader API; CC BY-NC 4.0 (weights)"
tags: [ocr, document-parsing, speculative-decoding, moe, vision-language, markdown, vllm, transformers, jina]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: CC-BY-NC-4.0
security_flags: [trust-remote-code, noncommercial-license]
source: unknown
---

## What it does

Jina-OCR-v1 is a visual document parser that converts a page image into clean Markdown in one pass — text, formulas (LaTeX), tables (HTML), and reading order together. It builds on DeepSeek-OCR's backbone: a DeepEncoder vision tower (256 visual tokens for a 1024x1024 view + dynamic local tiles) and a 3B-parameter MoE decoder (12 layers, 64 routed + 2 shared experts, top-6 routing, ~570M active parameters per token).

The key addition is **FastMTP** — a speculative decoding head where one dense draft block is applied recursively for K=3 prediction steps (not K separate heads). Greedy verification accepts the longest token-equality prefix, making it lossless (byte-identical to autoregressive decoding). On an L4 at batch 1, FastMTP lifts eager-mode decoding from 42.7 to 83.1 tokens/s (1.95x). Commits ~2.7 tokens per verifier pass on average.

## Mechanical details

Runs locally via Transformers (no FastMTP, MoE decoder only) or vLLM ≥ 0.21 (with FastMTP via `method="eagle"` registration). Requires `trust_remote_code=True`. Ships a sliding-window no-repeat-ngram processor to suppress repetition. Hosted via Jina Reader API (`r.jina.ai`) or OpenAI-compatible chat/completions endpoint at `api.jina.ai`. GGUF-quantized version available but drops FastMTP (llama.cpp lacks DeepSeek MTP support).

Benchmarks: 91.14 OmniDocBench v1.6, 83.4 olmOCR-Bench (+7.4 over DeepSeek-OCR backbone), 2.57 pages/s (highest of 14 systems measured, A100, concurrency 32). Shortest outputs of any system scoring above 83 (1,085 tokens/page).

## Security

CC BY-NC 4.0 — noncommercial use; commercial requires contacting Jina AI. Requires `trust_remote_code=True` for loading, which executes arbitrary Python from the HuggingFace snapshot. GGUF variant available for llama.cpp (no remote code execution). arXiv: 2609.03181.