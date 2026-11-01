---
name: parallax
title: Parallax
url: "https://github.com/GradientHQ/parallax"
category: framework
summary: "Fully decentralized distributed LLM inference engine by Gradient — pipeline-parallel model sharding across heterogeneous devices (CUDA/Metal/CPU, mixed platforms, phones), P2P communication via Lattica, GPU backend via SGLang/vLLM, Mac backend via MLX LM, paged KV cache and continuous batching; supports DeepSeek, Qwen, GLM, Kimi-K2, gpt-oss, MiniMax; cross-platform"
tags: [distributed-inference, local-inference, pipeline-parallelism, decentralized, cross-platform, mlx, vllm, sglang, model-sharding, cluster]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: ""
security_flags: []
source: unknown
---

## What it does

Parallax is a decentralized inference engine that distributes LLM inference across multiple heterogeneous devices via pipeline parallelism. It slices a model's layers across every node on the network — GPU machines (via SGLang/vLLM), Macs (via MLX LM), and even phones — with P2P communication powered by Lattica.

Key capabilities:

- **Pipeline parallel sharding**: splits model layers across devices with varying hardware. An RTX 3060 mini PC, a Mac mini, MacBooks, a Windows laptop, and an Android phone can collectively run a 120B model that none could load individually.
- **Dynamic scheduling**: routes requests and balances load across heterogeneous nodes.
- **Paged KV cache & continuous batching**: on Mac backend for efficient serving.
- **Self-healing**: if a node drops, the cluster redistributes its shard to remaining devices without downtime.
- **OpenClaw integration**: supported as of February 2026.

Supported model families: DeepSeek (V3.2, R1), MiniMax (M3, M2.7), GLM (5.2, 5.1, 4.7), Kimi-K2 (Thinking, Instruct), Qwen (3.6-35B-A3B), gpt-oss (120B, safeguard-120B), Step (3.5-Flash).

## Mechanical details

Install via git clone + `install.sh`. Serve with `parallax serve -m <model>`. Backend architecture: Lattica for P2P, SGLang/vLLM for GPU, MLX LM for Mac. Demonstrated running gpt-oss-120b (4-bit, ~60GB) across 6 devices at ~1.1 t/s — proof of concept for consumer hardware clusters. Won #1 Product of the Day on Product Hunt (October 2025). v0.0.1 released October 2025.

## Security

License not specified in README. Distributed architecture requires network trust between nodes — P2P via Lattica. No telemetry mentioned. Standard open-source build-from-source trust model; depends on SGLang, vLLM, and MLX LM as backends.