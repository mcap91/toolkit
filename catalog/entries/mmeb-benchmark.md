---
name: mmeb-benchmark
title: MMEB — Massive Multimodal Embedding Benchmark
url: "https://github.com/TIGER-AI-Lab/VLM2Vec"
category: reference
summary: "Comprehensive benchmark for evaluating omni-modality embedding models — V1 covers 36 image-text datasets across classification/VQA/retrieval/grounding; V2 adds video and visual document tasks (78 total); V3 extends to audio, text retrieval, and agent-centric tasks (190 total); introduced alongside VLM2Vec; TIGER-AI-Lab, ICLR 2025 → TMLR/COLM 2026"
tags: [benchmark, embeddings, multimodal, retrieval, vlm2vec, evaluation, video, audio, agent-retrieval]
reviewed: 2026-09-14
acquired: 2026-09-14
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

MMEB (Massive Multimodal Embedding Benchmark) is an evaluation benchmark for omni-modality embedding models. Each task is reformulated as a ranking problem: given an instruction and a query (text, image, or both), the model selects the correct answer from a candidate set. Evaluation uses Precision@1 with 1,000 candidates per task.

**MMEB-V1** (ICLR 2025): 36 datasets, four meta-task categories — classification, visual question answering, retrieval, visual grounding. 20 training / 16 evaluation datasets.

**MMEB-V2** (TMLR 2026): Expands to 78 tasks. Adds five new task types — visual document retrieval, video retrieval, moment retrieval, video classification, video question answering.

**MMEB-V3** (COLM 2026): 190 tasks across text, image, video, audio, visual documents, and agent-centric scenarios. New categories:
- Audio: classification, cross-modal retrieval, temporal grounding
- Text retrieval: instruction-following, reasoning, long-context, multi-condition, general
- Agent tasks: tool retrieval, GUI control, agent memory retrieval

The companion model VLM2Vec converts vision-language models (Phi-3.5-V, LLaVA-1.6, Qwen2-VL) into embedding models via LoRA tuning, achieving 10–20% improvement over prior multimodal embedding models.

## Mechanical details

- **Organization**: TIGER-AI-Lab
- **Leaderboard**: Models ranked by Overall(V3-ALL) score
- **Evaluation**: Precision@1, 1,000 candidates per task
- **License**: Apache-2.0
- **Publications**: ICLR 2025 (V1), TMLR 2026 (V2), COLM 2026 (V3)

## Security

- **License**: Apache-2.0
- **Governance**: Academic lab (TIGER-AI-Lab), peer-reviewed publications
- **No dangerous patterns** — benchmark datasets and evaluation code