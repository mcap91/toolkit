---
name: freetoken
title: FreeToken
url: "https://github.com/FlashML-org/FreeToken"
category: framework
summary: "Edge-native MoE inference engine from UC Berkeley/UT Austin — runs 290B+ frontier MoE models on consumer hardware by keeping experts in system RAM and LRU-caching active experts to GPU; bandwidth-adaptive Q* scheduling, double-buffered prefill streaming, semantic anchor checkpoints for agentic context reuse, elastic VRAM reallocation; 3-4x faster decode and 6-30x faster prefill vs Ollama/llama.cpp on VRAM-oversubscribed MoE workloads; OpenAI/Anthropic-compatible API; desktop app + CLI; supports RTX 30/40/50 series; Apache-2.0"
tags: [moe, local-inference, edge-inference, vram-oversubscription, expert-caching, consumer-hardware, gpu, llm-inference, openai-compatible, apache-2]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [large-moe-consumer-hardware, on-prem-llm-deployment-architecture, cpubrrr]
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

FreeToken is an inference engine purpose-built for running Mixture-of-Experts (MoE) models that exceed available GPU VRAM. Instead of loading the entire model onto the GPU, it keeps most expert weights in system RAM and dynamically loads only the experts needed for each token via LRU caching.

Key capabilities:

- **Bandwidth-adaptive Q* scheduling**: Dynamically decides CPU-GPU co-execution policy based on available bandwidth, optimizing expert loading vs. compute overlap.
- **Double-buffered prefill streaming**: Full-layer streaming for prefill phase, hiding memory transfer latency.
- **Global LRU expert caching**: Frequently-used experts stay GPU-resident; rarely-used experts evict to system RAM. When VRAM can't spare capacity, falls back to on-demand loading rather than oversubscribing.
- **Semantic anchor checkpoints**: Caches recurrent state and KV caches at semantic breakpoints, allowing agentic context edits (tool calls, thinking blocks) to skip redundant recomputation.
- **Elastic memory management**: Runtime VRAM reallocation between expert caches and KV memory without engine restarts.
- **FTW fast weight format**: Custom weight format optimized for edge serving.

**Benchmarks (August 2026):**
- Qwen3.6-35B at ~39 tok/s on 8GB RTX 4060 laptop
- DeepSeek-V4-Flash (284B) on RTX 5090 desktop
- GLM-5.2 (753B) on a single workstation GPU
- 3-4x faster decode, 6-30x faster prefill vs Ollama/llama.cpp on equivalent MoE models

**When to use vs alternatives:** FreeToken wins when the MoE model exceeds VRAM — its purpose-built scenario. If the model fits in VRAM, llama.cpp is faster for single requests and vLLM is faster for parallel serving.

Supported models: DeepSeek-V4, GLM-5.2/4.7, Qwen3.6/3.5 MoE, gpt-oss, Gemma-4, MiniMax-M2.5, Muse-Glimmer. Quantization formats: MXFP4, NVFP4, FP8, BF16.

## Mechanical details

Install via `uv pip install "freetoken[accel]"` or build from source. Desktop app available at flashml.ai with GUI for model management and chat. Serves OpenAI- and Anthropic-compatible APIs for integration with Claude Code, Codex, OpenCode, OpenClaw, DeepSeek Harness. Requires NVIDIA RTX 30/40/50 series GPU. Research paper: arXiv:2608.16157.

Inspired by mini-sglang; reuses code from SGLang, vLLM, FlashInfer, flash-linear-attention, LightLLM, and llama.cpp.

## Security

Apache-2.0 licensed. Academic project from UC Berkeley and UT Austin (Ion Stoica, Song Han, Matei Zaharia among authors). No telemetry documentation found. Desktop app is a separate closed-source download from flashml.ai.

## How to use it

uv pip install "freetoken[accel]"
