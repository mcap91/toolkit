---
name: open-weight-models-june-2026
title: Open Weight Models That Matter (June 2026)
url: "https://openrouter.ai/blog/insights/the-open-weight-models-that-matter-june-2026/"
category: reference
summary: "OpenRouter analysis of the four open-weight models that matter as of June 2026 — DeepSeek V4 Flash (best cost/performance, 79% SWE-bench, $0.05/$0.24 per M tokens), GLM 5.2 (#1 open-weight intelligence index, Opus-class planning), MiniMax M3 (multimodal image/video, 1M context, MiniMax Sparse Attention), NVIDIA Nemotron 3 Ultra (US-built, hybrid Mamba-2+Transformer MoE, 550B/55B-active, free route available)"
tags: [open-weight-models, model-selection, deepseek, glm, minimax, nemotron, pricing, benchmarks]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [openrouter, local-model-picks-2026]
source: unknown
---

## What it says

OpenRouter's June 2026 analysis of the four most impactful open-weight models, positioned as the field maintains a consistent 3–6 month gap behind closed frontier labs without that gap widening.

### DeepSeek V4 Flash

- ~284B params / ~13B active MoE, 1M context, MIT licensed
- 79.0% SWE-bench Verified (Pro variant: 80.6%, matching GPT-5.5-class)
- First-party pricing: $0.14/$0.28 per M tokens (in/out), $0.029/M with caching — ~150x cheaper than GPT-5.5 output
- Western no-train hosts at ~2x first-party price
- Text-only; first-party API routes through China and permits training on data
- Best for: frontier-class agentic/coding at lowest cost

### GLM 5.2

- #1 open-weight on Artificial Analysis Intelligence Index v4.1 (score 51)
- Level with GPT-5.5 xhigh on GDPval-AA real-world agentic benchmark
- Pricing: $0.447/$3.31 per M tokens (weighted average)
- Token-hungry — high thinking output can consume budget quickly
- Released days after U.S. export controls disabled Anthropic Fable 5/Mythos 5 broadly
- Best for: planning quality, long-horizon coding, Opus-class replacement

### MiniMax M3

- ~428B params / ~23B active MoE, 1M context
- Only model in group with native image and video input
- MiniMax Sparse Attention (blockwise sparse over real K/V blocks)
- Pricing: $0.098/$1.21 per M tokens (rises above 512K context)
- MiniMax Community License (commercial use requires attribution; large products need authorization)
- Best for: UI automation, screenshot-to-code, diagram/document understanding, video-grounded agents

### NVIDIA Nemotron 3 Ultra

- 550B / 55B-active hybrid Mamba-2 + Transformer MoE, 1M context, NVFP4 trained
- AA Intelligence Index score 48 — strongest U.S. open-weight entry
- Pricing: $0.423/$2.61 per M tokens + popular free route
- OpenMDW license; NVIDIA released data, recipes, eval tooling, RL infrastructure
- Strategic incentive: more open-model usage drives Blackwell/Hopper/NIM/CUDA demand
- Best for: enterprise workflows, RAG, orchestration where U.S. origin and NVIDIA stack matter

### Summary table

| Model | AA Index | Price (in/out/M) | Throughput | Use case |
|-------|----------|-------------------|------------|----------|
| DeepSeek V4 Flash | 40 | $0.054/$0.242 | ~84 tok/s | Cost/performance frontier |
| GLM 5.2 | 51 | $0.447/$3.31 | ~78 tok/s | Planning + long-horizon coding |
| MiniMax M3 | 44 | $0.098/$1.21 | ~59 tok/s | Multimodal + long context |
| Nemotron 3 Ultra | 48 | $0.423/$2.61 | ~75 tok/s | U.S.-built + NVIDIA stack |

## Key takeaways

Open-weight models maintain a 3–6 month gap behind closed frontier, with no acceleration of the gap. Cost savings for moving workloads from frontier to open-weight are significant. The gap between the four models is about which corner of cost/quality/modality/vendor to optimize for, not whether open-weight is viable.

## Security

N/A — analysis article, no code or dependencies.