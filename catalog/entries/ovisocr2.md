---
name: ovisocr2
title: OvisOCR2
url: "https://huggingface.co/ATH-MaaS/OvisOCR2"
category: framework
summary: "Compact 0.8B-parameter vision-language model for end-to-end page-level document parsing — given a document page image, generates a single structured Markdown document (plain text, LaTeX formulas, HTML tables, and visual regions in natural reading order) without a multi-stage OCR pipeline; scores 96.58 overall on OmniDocBench v1.6 and 75.06 Avg3 on PureDocBench per the publisher's technical report"
tags: [ocr, vision-language-model, document-parsing, markdown, huggingface, qwen, vllm, table-extraction, formula-recognition]
reviewed: 2026-08-25
acquired: 2026-08-25
license: Apache-2.0
security_flags:
  - "Published by Hugging Face org 'ATH-MaaS'; third-party analysis (note.com/ai_driven) identifies ATH-MaaS as a rebranding of the former Alibaba AIDC-AI team (publisher of the earlier 'Ovis' VLM series) following an internal reorg — not independently confirmed by Alibaba itself"
  - 'Model card provides only publisher-reported benchmark numbers (OmniDocBench v1.6, PureDocBench); no independent third-party benchmark reproduction found'
  - "Publisher's own disclaimer: due to real-world document diversity/complexity, the model may still produce incorrect or incomplete outputs (repeated text, invalid table/formula structures, reading-order errors); manual verification recommended for critical applications"
overlaps: [olmocr, opendataloader-pdf, locate-anything]
source: unknown
---

## What it does

OvisOCR2 is an end-to-end vision-language model that converts a document page image directly into a single Markdown document, in natural human reading order, in one forward pass — no separate layout-detection / OCR / table-recognition / formula-recognition pipeline stages. Output covers plain text, HTML-formatted tables (`<table>...</table>`), LaTeX-formatted formulas, and visual (chart/image) regions represented as `<img>` tags with bounding-box coordinates scaled to [0, 1000). It is built by post-training Qwen3.5-0.8B using a data engine that combines real-world documents with synthetic HTML-rendered documents, and a multi-stage training recipe: supervised fine-tuning (SFT), reinforcement learning (RL), and On-Policy Distillation (OPD).

Reported results: 96.58 overall on OmniDocBench v1.6 (publisher states this is the first end-to-end model to top that leaderboard, which was previously dominated by multi-stage pipeline methods) and an Avg3 score of 75.06 on PureDocBench (publisher-reported highest score). An earlier model, ATH-MaaS/OvisOCR, exists in the same HF org.

## Differentiators / Key takeaways

- Single 0.8B model performs the full page→Markdown pipeline (detection, reading-order, OCR, table/formula recognition) in one pass, rather than chaining separate specialist models.
- Small deployment footprint (0.8B params, ~1.7GB safetensors) relative to reported document-parsing accuracy.
- Training combines real documents with synthetic HTML-rendered pages plus SFT+RL+OPD, distinct from pure-SFT OCR fine-tunes.
- A hosted Hugging Face Space (`spaces/ATH-MaaS/OvisOCR2`) allows uploading a PNG/JPEG/WebP/PDF for interactive parsing without local setup.

## Mechanical details

- Base model: post-trained Qwen3.5-0.8B.
- Inference: `pip install "vllm==0.22.1" pillow`; served via vLLM `LLM` class with a fixed prompt template (`apply_chat_template`, `enable_thinking=False`); `max_tokens=16384`, `temperature=0.0`.
- Image preprocessing: `min_pixels=448*448`, `max_pixels=2880*2880`.
- Output post-processing: the model card ships a `_clean_truncated_repeats` helper to strip runaway repeated-token tails from long outputs, and an optional `filter_imgtags` step to drop or keep visual-region `<img>` placeholders (kept version pairs with a helper that crops the source image into per-region files for a renderable Markdown + image bundle).
- Citation: arXiv:2607.13639 ("OvisOCR2 Technical Report"), 13 listed authors.
- License: Apache License 2.0 (SPDX: Apache-2.0), per the model card's License section.

## Security

- **License**: Apache-2.0, permissive.
- **Supply chain**: Weights hosted on Hugging Face under the `ATH-MaaS` org; per third-party reporting this org is understood to be a rebrand of Alibaba's former AIDC-AI team (which published the original "Ovis" VLM series), though this lineage is not confirmed on an official Alibaba channel.
- **Code execution**: Model card ships example Python inference code (vLLM-based); as with any downloaded-model inference snippet, review before running in a production environment.
- **Benchmark provenance**: All headline scores (OmniDocBench v1.6, PureDocBench) are publisher-reported in the model card / technical report; no independent reproduction was found during this review.
- **Known limitations (publisher-disclosed)**: May produce incorrect/incomplete outputs — repeated text, incomplete content, invalid table/formula structures, reading-order inconsistencies — on complex real-world documents; publisher recommends manual verification for critical applications.
