---
name: deepseek-v4-flash-kv-cache-architecture
title: DeepSeek V4.1 Flash KV Cache Architecture
url: "https://arxiv.org/abs/2505.09343"
category: reference
summary: "DeepSeek V4.1 Flash transformer architecture redesign targeting KV cache reduction — Cross-layer Encoder-Decoder (CED) splits 20 encoder + 20 decoder layers so prompt tokens skip decoder entirely; cross-layer attention sharing (Full/Reindex/Reuse modes) shares KV across layers; global cache compressed to FP4 with 128-token bounded replay for local states; 4x smaller global cache, 8x smaller persistent cache vs V4 Flash"
tags: [deepseek, kv-cache, transformer-architecture, inference-optimization, fp4, attention-sharing]
reviewed: 2026-09-14
acquired: 2026-09-14
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it does

Documents DeepSeek V4.1 Flash's transformer architecture redesign focused on reducing KV cache memory for long-context and persistent agent memory workloads. Three key innovations:

**1. Cross-layer Encoder-Decoder (CED)**: Splits the model into 20 encoder layers and 20 decoder layers. Encoder layers read the prompt and build the global cache. Prompt tokens skip the decoder layers entirely, nearly halving prompt-processing compute.

**2. Cross-Layer Attention Sharing**: Three attention modes share memory across decoder layers:
- **Full**: builds and selects cache
- **Reindex**: shares cache with a fresh selection
- **Reuse**: shares both cache and selection
- Local attention still handles nearby tokens separately

**3. 4-Bit Global Cache & Bounded Replay**: The global cache is compressed to FP4 (4-bit floating point). Missing local attention states are approximately reconstructed by replaying just 128 tokens.

Results: 4x smaller global cache and 8x smaller persistent cache compared to V4 Flash. Enables massive context windows and persistent agent memory without exhausting GPU VRAM.

## Security

No security concerns — this is a reference about a model architecture design.

## Usage notes

- The architecture this entry documents backs a 552B-total-parameter MoE backbone with 16B parameters active during decode (8B during prefill) — confirmed total/active parameter counts for DeepSeek V4.1 Flash (source: https://www.instagram.com/reel/De2LjyNNS4H/)
- DeepSeek added live Search and Fetch APIs (api.deepseek.com) for agent/RAG tool use around the V4.1 Flash-1017 snapshot, with a fee waiver for Claude Code/Codex web-search calls through 2026-11-01 (source: https://www.instagram.com/reel/De2LjyNNS4H/)
