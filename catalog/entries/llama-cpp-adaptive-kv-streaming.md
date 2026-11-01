---
name: llama-cpp-adaptive-kv-streaming
title: llama.cpp Adaptive KV Streaming
url: "https://github.com/RaymondHuang210129/llama.cpp-adaptive-kv-streaming"
category: framework
summary: "llama.cpp fork that streams KV cache pages from pinned host RAM to GPU on demand — runs Qwen3.8-27B at full 256K context on 16GB VRAM (RTX 5070 Ti) without UVM thrashing; phase arena multiplexes prefill/decode workspaces, adaptive policy adjusts resident/ring split in real time, V2 adds MTP (speculative decoding) with shared ring; CUDA-only, experimental, MIT"
tags: [llama-cpp, kv-cache, long-context, vram-optimization, cuda, streaming, local-inference, speculative-decoding, mtp, phase-arena]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: [qwen38-27b-200k-on-16gb]
license: MIT
security_flags: [experimental, single-config-qualified]
source: unknown
---

## What it does

A focused fork of llama.cpp that solves one problem: when model weights consume most of the VRAM and a long context needs a KV cache that no longer fits, CUDA Unified Memory pages migrate in an uncontrolled way that thrashes. This fork takes explicit control: authoritative KV tensors live in pinned host RAM, a bounded GPU pool is split between resident KV pages and a transfer ring, and while one attention layer computes, the pages needed next are prefetched via a separate CUDA stream.

V2 rebuilds V1's streaming, cross-layer prefetch, and phase arena on explicit memory ownership and adds long-context MTP (Multi-Token Prediction) without a second full GPU KV allocation.

Key engineering:

- **Phase arena**: one fixed GPU allocation multiplexed between prefill (large graph + gather workspace, smaller KV pool) and decode (smaller graph, larger KV pool). Prefill and decode never need peak buffers simultaneously.
- **Adaptive policy**: resident/ring split adjusted in real time based on context length and measured prefetch behavior — not a static setting. Hysteresis prevents oscillation.
- **Ordered attention**: streaming changes physical addresses but preserves the logical tile order — resident pages, ring tiles before wrap, ring tiles after wrap, then stock-style final reduction. No approximate per-chunk normalization.
- **MTP integration**: MTP is layer 17 sharing the target's physical pool via a complete-layer lease. Ring is protected during catch-up/draft, returned to target before verification. Recurrent rollback via bounded two-slot GPU stage into pinned host snapshots.
- **Benchmark driver**: automatically probes largest workable arena per context size, generates CSV, PNG, SVG results. Reproducible rather than asserted.

## Mechanical details

Build from source (cmake, CUDA required). Qualified configuration: RTX 5070 Ti 16GB, Qwen3.8-27B UD-IQ4_XS, 256K context, Flash Attention on, Q8_0 K / Q4_0 V, one server slot. V2 measured 8.73 t/s without MTP and 19.12 t/s with draft length 3 at 256K context; 41.04 and 101.05 t/s at 32K. Backend-neutral memory contracts exist (views for CPU, CUDA/HIP, OpenCL, SYCL, Vulkan) but the complete streamed-attention adapter is CUDA-specific. ~290 GitHub stars.

Current limits: one serial target/MTP pair, one CUDA GPU, Qwen3.8-style 256-token page geometry, no parallel slots, no multi-GPU split, no mmproj.

## Security

MIT licensed (inherited from llama.cpp). Experimental research code — primarily validated on one specific hardware/model/quant configuration. Being a fork, long-term maintenance and upstream merging are uncertain. C++ codebase with CUDA kernels; standard build-from-source trust model.