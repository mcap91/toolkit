---
name: armorocr
title: ArmorOCR
url: "https://github.com/ant-research/ArmorOCR"
category: framework
summary: "Two-stage adversarial OCR framework built on Qwen3-VL-8B — trains robust grounded text perception via on-policy self-distillation from transformed observations, then refines with GRPO and task-conditioned rewards for localization, recognition, spotting, and VQA; includes AdvSpot benchmark (390 images, 13 adversarial OCR types)"
tags: [ocr, adversarial-robustness, vision-language-model, qwen, grpo, self-distillation, benchmark, grounded-ocr, document-parsing]
reviewed: 2026-09-03
acquired: 2026-09-03
license: Apache-2.0
security_flags: []
overlaps: [ovisocr2]
source: unknown
---

## What it does

ArmorOCR addresses the vulnerability of large multimodal models to adversarial visual text — text that humans can read but models fail to localize and recognize. It is a two-stage post-training framework built on Qwen3-VL-8B-Instruct that produces a single model capable of single-pass inference on the original image without inference-time visual transformations or tool assistance.

Stage 1 — On-Policy Self-Distillation (OPSD): the model learns adversarial OCR perception from privileged transformed observations (augmented views of the same image that make the text easier to read). Knowledge is transferred from these "easy" observations to the model's perception of the original image via on-policy distillation.

Stage 2 — GRPO with task-conditioned rewards: Group Relative Policy Optimization refines grounded OCR perception using separate reward signals for localization (bounding box IoU), recognition (text accuracy), full spotting (combined), and visual question answering.

The framework includes AdvSpot, the first benchmark for grounded adversarial OCR evaluation: 390 images with region-level annotations (bounding boxes, transcriptions, perception-type labels, region-grounded VQA pairs), spanning 5 primary categories and 13 fine-grained adversarial OCR types organized by failure mechanism — Spatial Manipulation, Glyph Variation, Visual Encoding, Contextual Blending, and Imaging Degradation.

## Differentiators

- Targets adversarial OCR specifically — rotated, mirrored, tiny, stylized, handwritten, encoded, blended, and degraded text — rather than clean document or natural-scene OCR
- Single-pass inference on the original image; no test-time augmentation, ensemble, or tool pipeline required
- Introduces the AdvSpot benchmark, the first region-grounded adversarial OCR evaluation set
- GGUF quantized weights available (Q8_0, Q4_K_M) for deployment without full-precision GPU memory
- Trained with ms-swift; inference via standard Transformers or llama.cpp

## Mechanical details

- Base model: Qwen3-VL-8B-Instruct
- Training framework: ms-swift (two-stage post-training)
- Inference: Python (Transformers + accelerate) or GGUF via llama.cpp / llama-server
- Hardware: single GPU inference; GGUF variants reduce memory requirements
- Evaluation script (`advspot_infer.py`) supports multi-GPU data-parallel inference, resume, and outputs predictions, metrics (VQA accuracy + IoU), and badcases
- Weights on Hugging Face: inclusionAI/ArmorOCR (full), inclusionAI/ArmorOCR-GGUF (quantized)

## Security

- Repository contains inference code and an evaluation script; no web-facing components
- Dependencies are standard ML stack (torch, transformers, accelerate, pillow) with pinned versions
- No eval(), shell injection vectors, or credential handling observed
- From Ant Group (Ant Research); small contributor base typical of research releases
- License not explicitly stated in README; repository appears Apache-2.0 based on Hugging Face model card conventions for Ant/inclusionAI releases