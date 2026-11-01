---
name: seb-ocr
title: seb-ocr
url: "https://github.com/ALucek/seb-ocr"
category: cli-tool
summary: "Vision-language pipeline for turning scanned historical pages into structured datasets — Gemini-based OCR with adaptive rate limiting, sliding-window entity extraction via Pydantic-constrained JSON, incremental caching, and semantic deduplication via embedding cosine similarity; single-script Python, MIT"
tags: [ocr, gemini, entity-extraction, historical-documents, vlm, pydantic, deduplication, embeddings, political-science]
reviewed: 2026-09-03
acquired: 2026-09-03
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

seb-ocr is a single-script Python pipeline that converts scanned historical document pages into structured entity datasets. Built for political science research, it uses Google's Gemini models for both vision-OCR and text entity extraction.

The pipeline has four stages:

1. **OCR pass**: each input image is sent to a multimodal Gemini model with a handcrafted transcription prompt. Calls run in parallel threads (configurable `MAX_WORKERS`) with an adaptive rate limiter to stay within API quotas.
2. **Sliding-window parsing**: transcriptions are processed in overlapping windows (`WINDOW_SIZE` pages, `WINDOW_STEP` stride) so the LLM captures cross-page context. The model returns JSON conforming to a strict Pydantic schema.
3. **Incremental caching**: window results are cached on disk so subsequent runs resume instantly without reprocessing.
4. **Semantic deduplication**: candidate entities are embedded (Gemini `text-embedding-004`) and clustered by cosine similarity to merge duplicates appearing across multiple pages.

Output: deduplicated `entities.json` and `entities.csv`.

## Differentiators

- End-to-end in a single `main.py` — no external services or databases required
- Sliding-window approach captures cross-page entity context that per-page extraction misses
- Semantic deduplication via embeddings rather than string matching
- Adaptive rate limiting for Gemini API quotas
- Incremental caching enables resume on interrupted runs
- Three run modes: full pipeline (`all`), OCR-only (`transcribe`), extraction-only (`extract`)

## Mechanical details

- Language: Python, managed with uv
- Models: Gemini 2.5 Flash (generation), text-embedding-004 (embeddings) — configurable via `.env`
- Input: page-scanned images in `input_images/` with page numbers in filenames
- Output: `output/transcriptions/` (raw OCR), `output/window_outputs/` (cached windows), `output/final_outputs/` (deduplicated entities)
- Configuration: `.env` file for API key, model selection, rate limits, parallelism, and window parameters

## Security

- MIT license
- Requires Gemini API key stored in `.env` file (not committed)
- No web-facing components; runs locally as a CLI script
- No eval() or shell injection patterns observed
- Small single-author research project