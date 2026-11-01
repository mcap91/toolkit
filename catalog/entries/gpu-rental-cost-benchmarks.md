---
name: gpu-rental-cost-benchmarks
title: GPU Rental Cost-Per-Token Benchmarks
category: reference
summary: "A detailed cost and performance breakdown from renting 4x RTX 4080 Super GPUs to run a 120B MoE model via vLLM, showing cost per token drops 6-8x by batching requests and documenting throughput/latency across concurrency levels"
tags: [gpu-rental, cost-optimization, local-inference, vllm, benchmarking, vram, concurrency]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: ""
security_flags: []
source: unknown
---

## What it covers

A detailed cost and performance breakdown from renting cloud GPUs (4x RTX 4080 Super 32GB,
128GB total VRAM) to run a 120B MoE model (gpt-oss-120b, native MXFP4) via vLLM with TP=4.

## Key Numbers

| Concurrency | Aggregate tok/s | Per-request tok/s | TTFT p50 | $/1M output tokens |
|---|---|---|---|---|
| 1 | 195.6 | 195.7 | 1.24s | $1.42 |
| 16 | 1,165.5 | 73.1 | 3.23s | $0.238 |
| 64 | 1,633.9 | 26.7 | 8.70s | $0.17 |

Total cost: $2.38 for 1h42m session (~$0.25/GPU/hour).

## Takeaways

- Cost per token drops 6-8x by batching requests (concurrency 16-64 vs single-user)
- Single-user local GPU setups pay ~8x more per token than batched workloads
- The metric that drives rent-vs-buy is $/M tokens at your actual concurrency, not $/hr
- Model download gotcha: HuggingFace repos may contain 3x the needed data (original/metal
  checkpoint formats) — exclude unnecessary directories to save bandwidth
- Long-context (32K, 64K input tokens) worked with zero OOM using ~58GB KV cache headroom
- CPU offload to half the GPUs works but is ~38x slower