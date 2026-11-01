---
name: turboquant
title: TurboQuant — Extreme KV Cache Compression
url: "https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/"
category: reference
summary: Foundational Google Research algorithm (ICLR 2026) for 3-4 bit KV cache compression with zero accuracy loss; growing downstream ecosystem but no single canonical package yet
tags: [quantization, kv-cache, compression, inference, memory-optimization, google-research]
reviewed: 2026-06-16
acquired: 2026-06-16
license: Apache-2.0
security_flags: []
overlaps: [airllm, rtk]
source: unknown
---

## What it does

TurboQuant (ICLR 2026) compresses the key-value cache in transformer models to 3–4 bits with zero accuracy loss. It combines two sub-algorithms:

- **PolarQuant** (AISTATS 2026): Randomly rotates data vectors, converts to polar coordinates, then quantizes on a predictable circular grid — eliminates the normalization constants that bloat traditional quantization.
- **QJL** (Quantized Johnson-Lindenstrauss): A 1-bit error-correction pass that removes bias from the PolarQuant stage using a sign-bit projection trick. Zero memory overhead.

Results on Gemma and Mistral across LongBench, Needle-in-Haystack, ZeroSCROLLS, RULER, and L-Eval: 6x memory reduction, up to 8x speedup on H100 GPUs, no training or fine-tuning required. Also applicable to vector search (superior recall vs. PQ and RabbiQ baselines).

## Assessment

**Watch.** The algorithm is proven and the research is from Google, but the ecosystem is fragmented. Downstream implementations include TurboAgents (RAG/agent middleware), vLLM TurboQuant Plugin, turboquant-pytorch, turboquant ggml (llama.cpp), and the mlx-vlm PR for Apple Silicon. No single canonical package has emerged as the standard integration path. Worth tracking as implementations mature.

## Mechanical details

Agent integration routes documented in the wild:

1. **Inference engine backends:** vLLM and llama.cpp plugins replace the attention backend (`--attention-backend CUSTOM`).
2. **Agent middleware:** TurboAgents attaches to existing RAG/agent systems, compressing vector search payloads and KV cache without altering agent source code.
3. **Python/HuggingFace:** Drop-in `TurboQuantCache(bits=4)` replacement passed as `past_key_values` to any HuggingFace model's generate loop.

## Security

Google Research publication — no installable code to audit directly. Downstream implementations each carry their own security profiles. Apache-2.0 is the standard Google Research license.