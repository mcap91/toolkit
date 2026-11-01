---
name: cpubrrr
title: cpubrrr
url: "https://github.com/arizqi/cpubrrr"
category: cli-tool
summary: "From-scratch CPU-only LLM inference engine in Rust that beats llama.cpp's CPU path on MoE models. Hand-written NEON/SME kernels, quad-interleaved weight layout, integer-accumulation Q8_K, worker-driven execution. Runs gpt-oss:20b at ~77 tok/s and Qwen3-Coder-30B at ~92 tok/s on Apple M4 Max (CPU only). OpenAI-compatible API server included. Dual MIT/Apache-2.0."
license: MIT
tags: [llm-inference, cpu, rust, neon, arm, apple-silicon, moe, quantization, performance, llama-cpp-alternative]
reviewed: 2026-07-28
acquired: 2026-07-28
overlaps: []
security_flags: []
source: unknown
---

## What it is

cpubrrr is a research-grade CPU-only LLM inference runtime written in Rust. It links nothing but the C standard library, so it physically cannot touch the GPU. It targets mixture-of-experts (MoE) models on Apple Silicon and achieves higher decode throughput than llama.cpp's CPU path on both MXFP4 and Q4_K/Q6_K quantization formats.

Measured on Apple M4 Max (CPU only):
- gpt-oss:20b (MXFP4): ~77 tok/s vs llama.cpp ~14 tok/s (~5x)
- Qwen3-Coder-30B (Q4_K/Q6_K): ~92 tok/s vs llama.cpp ~82 tok/s (~1.1-1.2x)

Supported models (config-driven, same-family models run with zero code changes):
- gpt-oss:20b and gpt-oss-120b (MXFP4)
- Qwen3-Coder-30B and Qwen3-30B (Q4_K/Q6_K)

Key techniques: hand-written ARM NEON SIMD integer kernels (sdot/tbl for exact 4-bit arithmetic), quad-interleaved weight layout for sequential memory access, integer-accumulation Q8_K kernel adopted from llama.cpp's algorithm, worker-driven execution with yielding spin-barriers, MoE-aware scheduling, and mmap'd weights.

## Mechanical details

- **Build:** `cargo build --release` (uses target-cpu=native)
- **Setup:** `./scripts/setup_model.sh <model>` reads weights from local Ollama install (no weights copied)
- **API server:** `python3 scripts/openai_server.py` serves OpenAI-compatible API at localhost:8643
- **Demo:** `python3 scripts/demo_server.py` for side-by-side cpubrrr vs llama.cpp comparison with live tok/s
- **Requirements:** Apple Silicon Mac (M-series, ARMv9+SME), Rust stable, Python 3, Ollama with model pulled
- **Correctness:** Verified bit-exact against gguf library; GSM8K parity with llama.cpp (89% vs 87% on Qwen3-Coder-30B Q4_K, within noise)
- **Honest limits:** Research engine, not production server. No cross-user batching. Apple M4 only — x86 (AVX-512) port is the #1 open contribution request. Prefill throughput still behind llama.cpp.

## Security

Dual MIT/Apache-2.0. No model weights included or redistributed. Research engine with no serving hardening. The extensive benchmark-integrity documentation (contaminated baselines, unverified GPU placement, thermal throttling, unreproducible peaks) is unusually thorough and transparent. No security flags observed.

## How to use it

cargo build --release
