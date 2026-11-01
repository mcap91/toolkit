---
name: qwopus38-27b-flash
title: Qwopus3.8-27B-Flash
category: reference
summary: "Post-trained efficiency variant of Qwen3.8-27B (hybrid DeltaNet + attention architecture) focused on reducing unnecessary reasoning while preserving capability — +12.8% decoder throughput, MTP acceptance 66.1% to 80.7%, ~9.9% less total output with significantly fewer P95 runaway-reasoning cases; trades 1.45pp on MMLU-Pro (92.73% to 91.28%); 13/14 agent tasks passed at 99 tok/s on RTX 5090; trained with high-quality SFT (top 10% of 1.5M samples) + NVIDIA NeMo-RL GSPO; GGUF format"
tags: [qwen, local-inference, efficiency, mtp, speculative-decoding, reasoning, gguf, agent-workloads, post-training, deltanet]
reviewed: 2026-09-18
acquired: 2026-09-18
license: ""
security_flags: []
overlaps: [qwen38-27b-200k-on-16gb]
source: unknown
---

## What it does

Qwopus3.8-27B-Flash is a post-trained variant of Qwen3.8-27B optimized for inference efficiency, reasoning efficiency, and agent workloads. The goal is not higher benchmark accuracy but reducing unnecessary compute while preserving most capability.

Base architecture (Qwen3.8-27B): 64 layers in a hybrid pattern — 48 Gated DeltaNet layers + 16 Gated Attention layers. DeltaNet layers act as recurrent state updates for efficient long-context processing; attention layers provide periodic precise retrieval. 262K native context, native Multi-Token Prediction (MTP) support.

Post-training: high-quality SFT filtered to top ~10% of 1.5M teacher-generated samples, then GSPO via NVIDIA NeMo-RL to reinforce effective reasoning trajectories and better termination behavior.

Measured improvements over base Qwen3.8-27B (Q5_K_M + MTP, MMLU-Pro math/physics/chemistry):
- Decoder throughput: +12.8%
- MTP acceptance: 66.1% to 80.7% (+14.6pp)
- Output reduction: ~9.9% fewer total characters; P95 extreme outputs decreased 13-40%
- Accuracy trade-off: MMLU-Pro 92.73% to 91.28% (-1.45pp)

Agent evaluation (14 held-out SW engineering tasks, RTX 5090): 13/14 tasks passed, 99 tok/s average, 88.8% MTP acceptance, 26 minutes total.

Known issue: abnormal Python indentation in some nested block structures.

## Security

- Available as GGUF for local inference
- No specific security concerns beyond standard local model deployment