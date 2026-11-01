---
name: pulsarforge
title: PulsarForge
url: "https://github.com/siris9476/pulsarforge"
category: framework
summary: "CPU-only MoE inference engine in C11 — streams 744B-parameter models off SSD via expert-level LRU caching, cross-layer predictive prefetch (80.8% recall), and dynamic-k expert truncation; 21x speedup over naive on i7-8550U/32GB"
tags: [inference, cpu, moe, streaming, c, local-llm]
reviewed: 2026-09-16
acquired: 2026-09-16
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

PulsarForge is a CPU-only inference engine, written in C11, for running large Mixture-of-Experts (MoE) models without loading them fully into RAM. It streams a 744B-parameter model (GLM-5.2, distributed as a 202GB GGUF file) directly off a USB SSD, fetching experts per-token through a custom unbuffered reader rather than relying on OS page cache or mmap.

Experts are quantized to int4 with group size 64; router weights and correction biases are kept at f32 precision.

## Differentiators

- **Cross-layer predictive prefetch**: anticipates which experts an upcoming layer will need and issues fetches ahead of time, reaching 80.8% recall
- **Arrival-order overlap**: compute and IO are not run in lockstep — the engine processes experts as they arrive rather than waiting on a fixed schedule
- **Dynamic-k expert truncation**: router weights correlate with true expert importance at ρ=0.859, which the engine uses to safely skip low-importance experts and reduce work per token
- **Cross-architecture validation**: tested across Qwen3 (0.6B-30B), DeepSeek2 (MLA), and OLMoE-1B-7B, in addition to GLM-5.2

## Mechanical details

- Language: C11
- Quantization: experts int4 group-64; router/correction biases f32
- Streaming: custom unbuffered reader, per-token expert fetch from SSD
- Expert cache: 8GB LRU cache, 40-66% hit rate
- Measured on i7-8550U / 32GB RAM / USB SSD: 196 s/token (naive) to ~9.3 s/token (streaming), a 21x speedup; ~2.9 s/token in 8-stream batch mode
- License: MIT

## Security

No security flags identified from available source material.
