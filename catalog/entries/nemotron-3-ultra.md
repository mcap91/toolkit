---
name: nemotron-3-ultra
title: NVIDIA Nemotron 3 Ultra
url: "https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/"
category: framework
summary: "NVIDIA's most capable open model — 550B total / 55B active parameters, Mixture-of-Experts Hybrid Mamba-Attention architecture with LatentMoE and MTP speculative decoding; 1M context length; 5.9x throughput vs GLM-5.1, 4.8x vs Kimi K2.6; open checkpoints (base, post-trained, NVFP4 quantized, GenRM) and training datasets released"
tags: [nvidia, open-weights, moe, mamba, large-language-model, inference, speculative-decoding]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [qwen3-6-27b]
source: unknown
---

## What it does

NVIDIA's flagship open-weight LLM — 550 billion total parameters with 55 billion active per token via Mixture-of-Experts. Uses a hybrid Mamba-Attention architecture combining state-space models with attention layers, plus LatentMoE for improved accuracy and MTP (Multi-Token Prediction) layers for native speculative decoding.

**Key specs:**
- 550B total / 55B active parameters (MoE)
- Hybrid Mamba-Attention architecture
- Up to 1M token context length
- Pretrained in NVFP4 (4-bit floating point)
- Post-trained with SFT + RL + Multi-teacher On-Policy Distillation (MOPD)
- Inference-time reasoning budget control

## Differentiators

- **Throughput** — 5.9x higher than GLM-5.1-754B-A40B, 4.8x vs Kimi K2.6-1T-A32B, 1.6x vs Qwen-3.5-397B-17B at 8K input / 64K output
- **Accuracy** — on-par with state-of-the-art open LLMs across diverse benchmarks; outperforms on RULER at 1M context length
- **Mamba-Attention hybrid** — combines state-space model efficiency with attention's precision
- **LatentMoE** — improved accuracy over standard MoE routing
- **Native speculative decoding** via MTP layers — faster inference without separate draft models
- **Full open release** — base model, post-trained model, NVFP4 quantized model, GenRM (reward model for RLHF), and training datasets all released

## Mechanical details / What to adopt

**Checkpoints released:**
- Nemotron 3 Ultra 550B-A55B NVFP4 (post-trained + quantized)
- Nemotron 3 Ultra 550B-A55B BF16 (post-trained)
- Nemotron 3 Ultra 550B-A55B Base BF16
- Nemotron 3 Ultra 550B-A55B GenRM

**Datasets released:**
- Nemotron-Pretraining-Code-v3 (173B tokens, GitHub through Sept 2025)
- Nemotron-Pretraining-Legal-v1 (synthetic legal data)
- Nemotron-Pretraining-Specialized-v1.2 (factual recall, moral scenarios, QA)
- Nemotron-Posttraining-v3 (agentic, reasoning, general capabilities for SFT/RL)

Published June 4, 2026.

## Security

Open checkpoints and datasets released. License not explicitly stated on the research page — check HuggingFace model cards for specific SPDX identifiers. NVIDIA research release.