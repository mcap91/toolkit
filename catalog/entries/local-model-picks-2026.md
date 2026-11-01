---
name: local-model-picks-2026
title: Local Model Picks (2026)
url: "https://reddit.com"
category: reference
summary: "Practitioner-curated list of open-source models for local/offline use with RAM requirements — Llama 4 Scout (32GB Q4), Qwen 3.6 7B (16GB, coding), DeepSeek R1 8B (16GB, reasoning), Phi-4 3.8B (8GB, reasoning), Kimi K2.6 1T (API-only, 32B active, matches Claude), Pixtral (VLM), Granite 3 (enterprise/compliance), GPT-OSS 20B/120B"
tags: [local-inference, open-source-models, quantization, offline, model-selection]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [qwen3-6-27b, qwen2-5-coder-32b-instruct, bitnet]
source: unknown
---

## What it says

Practitioner's selection of open-source models for local/offline use, organized by purpose and RAM requirements:

| Model | RAM | Purpose | Notes |
|-------|-----|---------|-------|
| Llama 4 Scout | 32GB (Q4 quant) | General use | — |
| Qwen 3.6 7B | 16GB | Coding | — |
| DeepSeek R1 8B | 16GB | Reasoning | — |
| Phi-4 3.8B | 8GB | Reasoning | Small footprint |
| Kimi K2.6 | 64GB (or API) | Claude replacement | 1T params, 32B active per token |
| Pixtral | — | Vision-language | VLM |
| Granite 3 | — | Enterprise/compliance | "Enterprise and compliance ready" — meaning unclear |
| GPT-OSS 20B / 120B | 24GB (20B) / API (120B) | General / GPT-4 match | 120B reported to match GPT-4 |

## Key takeaways

The list spans from 8GB (Phi-4) to API-only (Kimi K2.6 at 1T params), covering the practical range from laptop inference to server-grade. The "32B active per token" note on Kimi K2.6 refers to mixture-of-experts architecture. Granite 3's "enterprise and compliance ready" claim is noted but not explained by the author.

## Security

N/A — model selection notes, no code or dependencies.

## Notes

### Qwen 3.8 27B setup combos (practitioner reports, Aug 2026)

- **Q4 + Q8 KV cache** is the recommended quantization combo — dynamic/mixed-precision Q4 GGUFs (e.g. Unsloth q4_K_XL) retain near-Q8 accuracy while reclaiming VRAM for context and concurrency.
- **RTX 5090**: runs Qwen 3.8 27B comfortably; also runs Meta Muse 30B with Dflash at ~15 tok/s with 131K context. Meta Muse 30B trades blows with Qwen 3.8 27B — better at agentic work and instruct mode (no thinking), reasoning is brief but good, significantly faster.
- **64GB Mac Mini M4 Pro**: Qwen 3.6 35B (a3b quant) replaced Gemma 4 and was a step-change improvement for coding via Ollama + OpenClaw.

Source: r/LocalLLaMA, r/LocalLLM practitioner threads (unverified).

## Usage notes

- **Qwen 3.8 27B vs 3.6 35B-A3B on 8GB VRAM (r/unsloth, Sep 2026):** With RTX 4060 (8GB) + 64GB DDR5 RAM, user running Qwen3.6 35B-A3B MTP at Q4 128K gets 26-30 t/s. Qwen3.8 27B at Q2 should fit fully in VRAM (faster) but quality at that quant level is questionable. Bonsai's smaller Qwen3.8 variant scores well on benchmarks but reported as poor in practice. Community recommendations for 35B-A3B finetunes: Ornith 1.5-35B-A3B, Ternary Bonsai, Occamy, Tiel-Coder-35B-A3B. Also suggested: empero-ai/Qwen3.8-35B-A3B-Distill-GGUF (but has 8K token limit).

- Very-low-end data point (r/LowEndLocalAI, Oct 2026): GTX 1060 3GB + AMD E2-2000 (2 cores, no AVX) + 8GB DDR3, llama.cpp CUDA with all layers on GPU (`-ngl 99`, batch 256, q8_0 KV cache; any CPU offload unusable). Small models run at 23–37 tok/s generation, 500–1200 tok/s prefill. On an 8-task agentic coding mini-benchmark (one run each, 6-min limit): Qwen3.5-4B no-thinking 7/8 (10 min), Ministral 3 3B 6/8 in 5 min, MiniCPM5-2B 6/8, NeoHorse-1-4B 6/8, Granite 4.1 3B 4/8, Qwen3.5-2B 3/8. Thinking mode did not help these small models (same or worse scores at ~2x time). Commenters suggested LFM2.5 2.6B, FrogNano-4B, Ling 3 Tiny, and Granite 4.2 (author confirmed 4.2 much better than 4.1 on easy tasks).
