---
name: beam-reflection-ai
title: Beam (Reflection AI)
url: https://huggingface.co/reflection/Beam-1.0-501B-A23B
category: framework
summary: 501B-total/23B-active sparse mixture-of-experts open-weight model from Reflection AI (a Brooklyn lab founded by two ex-Google-DeepMind researchers) for coding, reasoning, and agentic workloads — 1M-token effective context, pretrained on 23.8T tokens plus 100M+ RL rollouts; vendor-reported benchmarks include 81.6% SWE-bench Verified, 80.1% Terminal-Bench 2.1, 90.6% GPQA Diamond, 97.7% AIME 2026; weights (BF16/FP8/NVFP4) and a DFlash2 speculative-decoding drafter released under Apache-2.0 on 2026-10-16 with a 40+ partner hosting ecosystem
tags:
  - llm
  - coding-agent
  - mixture-of-experts
  - open-weights
  - reflection-ai
  - agentic
reviewed: 2026-10-30
acquired: 2026-10-30
license: Apache-2.0
security_flags: []
overlaps: []
source_url: https://www.instagram.com/reel/De2LjyNNS4H/
source: instagram
---

## What it does

Beam is Reflection AI's first open-weight model: a sparse mixture-of-experts (MoE) architecture with 501 billion total parameters and 23 billion active per token, pretrained on 23.8 trillion tokens and tuned with more than 100 million reinforcement-learning rollouts. Reflection AI is a Brooklyn-based lab founded in 2024 by two former Google DeepMind researchers. Beam targets coding, reasoning, and agentic workloads — resolving software issues, modifying code, calling tools, and acting on intermediate results — with an effective context length of 1 million tokens. Vendor-reported benchmarks (BF16 weights, temperature 0.7): 81.6% SWE-bench Verified, 80.1% Terminal-Bench 2.1, 43.3% DeepSWE v1.1, 80.8% MCP Atlas, 90.6% GPQA Diamond, 97.7% AIME 2026.

Announced October 5, 2026 as an open-weight release; weights were not initially downloadable (waitlist only) and went fully live under Apache-2.0 on October 16, 2026, in collaboration with an ecosystem of 40+ hosting/serving partners (e.g. Baseten).

## Mechanical details

- Hugging Face org: huggingface.co/reflection; primary model page huggingface.co/reflection/Beam-1.0-501B-A23B
- Weight formats and sizes: NVFP4 (273 GiB), FP8 (468.72 GiB), BF16 (933.81 GiB); speculative-decoding drafter `reflection/Beam-1.0-501B-A23B-DFlash2`
- Download: Hugging Face CLI, e.g. `hf download reflection/Beam-1.0-501B-A23B-FP8`
- Developer docs: developers.reflection.ai/serving-weights

## Security

Apache-2.0 license (weights, tokenizer, reference implementation, developer tooling). Open weights publicly downloadable from a verified Hugging Face organization; no gating. Running the model locally requires multiple high-memory GPUs even at NVFP4 precision (273 GiB) — a deployment-scale consideration, not a disclosed vulnerability.
