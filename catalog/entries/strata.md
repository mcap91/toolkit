---
name: strata
title: Strata
url: "https://github.com/Niko1221/Strata"
category: framework
summary: "One-click inference engine for Qwen3.8-Flash-Next (125B MoE) on consumer NVIDIA GPUs (12-24GB) — expert offloading between GPU/RAM/SSD, speculative decoding via built-in MTP, 60-95 t/s on RTX 5070; multi-GPU pipeline, OpenAI/Anthropic-compatible API, vision support, browser UI with live monitor; built on ggml; MIT"
tags: [local-inference, qwen, moe, expert-offloading, speculative-decoding, one-click, nvidia, cuda, openai-compatible, consumer-gpu]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: [llama-cpp-adaptive-kv-streaming, qwen38-27b-200k-on-16gb]
license: MIT
security_flags: []
source: unknown
---

## What it does

Strata runs Qwen3.8-Flash-Next (125B parameters, 6B active per token, 24,576 experts) on a consumer gaming PC. It shares work across GPU, RAM, and SSD: the GPU handles per-token computation and caches hot experts, RAM holds all experts for CPU fallback, and the SSD stores the 29GB engram lookup table with small row reads per token. GPU and CPU work in parallel so neither waits.

Key capabilities:

- **Expert offloading**: only ~10 of 24,576 experts needed per token. GPU keeps the most-requested experts and learns which ones to retain during use.
- **Speculative decoding**: built-in MTP helper guesses next words, big model verifies in one pass — 1.6-1.8x speedup with identical output quality.
- **One-click install**: `START-HERE.bat` (Windows) or `./setup.sh` (Linux) handles Python, engine, and model download (~70GB). Calibration mode optimizes for specific hardware.
- **Multi-GPU**: pipeline parallelism across 2-3 NVIDIA cards (RTX 20+, 8GB+ each). 18-20% faster prompt processing on dual-GPU vs single.
- **API compatibility**: OpenAI (`/v1`) and Anthropic (`/v1/messages`) endpoints on localhost:8080. Thinking mode (off/low/medium/high).
- **Vision**: optional image input support.
- **AMD HIP**: experimental Radeon RX 7900 XT/XTX support on Linux.

## Mechanical details

Performance on RTX 5070 (12GB), Ryzen 5 7600, 64GB RAM:

| Quant | Decode (short) | Decode (128K) | Prompt (32K) | RAM needed |
|-------|---------------|---------------|-------------|-----------|
| Q2_0 | 93 t/s | 74 t/s | 2,170 t/s | 37.6 GB |
| IQ2_XS | 79 t/s | 63 t/s | 2,090 t/s | 39.2 GB |
| IQ3_XXS | 62 t/s | 49 t/s | 1,750 t/s | 47.0 GB |
| IQ3_S | 53 t/s | 46 t/s | 1,620 t/s | 54.8 GB |

Also supports ISTA-DASLab Coder variant (half experts pruned, 91% SWE-bench Verified score, fits 32GB RAM) and Swift 1.5 fine-tune (shorter thinking). Built on ggml (from llama.cpp). Ideas from Splash, ninfer, HyperQwen.

## Security

MIT licensed. Runs entirely local — no telemetry, no cloud calls. Model files carry their own licenses (Qwen Community License 1.0 for original). Listens on localhost by default; `--host 0.0.0.0` exposes the API with user-specified `--api-key`.

## Usage notes

- Strata update (Oct 2026): users report 200-230+ tok/s on dual 5090s with Flash Next IQ3 model, up from 170-190 tok/s pre-update. Hardware: Epyc 7402p, 256GB DDR4 3200 ECC, 192GB allocated to AI server VM in Proxmox. Q4 with vision support pending.
- Dual RTX 3090 (24GB each), Ryzen 7 9800, 64GB DDR5-5200, Linux/Proxmox: Qwen3.8-Flash-Next-OrcaRouter IQ4_XS with vision. 100+ t/s decode short context. Extended context results: 200K prompt → 2,004 t/s PP / 73 t/s decode; 400K → 1,633 t/s PP / 46 t/s decode; 900K → 1,110 t/s PP / 44 t/s decode. Machine runs notably cooler than prior vLLM setup (60-70 t/s).
- Orca 3.8 Flash Next uncensored variant: 75-80 t/s output on a 4090 via Strata. Compared to 180 t/s for a 3.6 35B censored model via llama.cpp. User reports the 180B Orca version runs with as little as 12GB VRAM via Strata's expert offloading.

- Reddit thread (r/Qwen_AI, Oct 2026) on self-hosting Qwen 3.8 27B: one commenter reports ~160 tok/s running Qwen 3.8 Flash Next IQ3_S via Strata on a single 48GB GPU, using ~60GB of RAM. Another reports Strata working well on 24-32GB VRAM given more RAM and a fast SSD, full 256K context, and (on a cloud RTX6000) ~200 tok/s at 7K prefill when all experts fit, with 512K context support. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)

- ykarout ported Strata's optimizations to Qwen3.6-35B-A3B (previously tuned mainly for Flash Next), published as a UD_Q4_K_XL GGUF fine-tune at huggingface.co/ykarout/Strata-Qwen3.6-35B-A3B and a Sage-based variant at huggingface.co/ykarout/Strata-Sage-A1.5-GGUF; required a one-line engine patch for a missing `ev_route` event on the all-experts-in-VRAM path (unpatched engine build q36-r2 crashed on first prompt on any ≥32GB card), since fixed upstream. (source: https://www.reddit.com/r/unsloth/comments/1xdzfnf/for_qwen3635b_lovers_ud_q4_k_xl_now_runs_in/)
- Benchmark on a single Tesla V100 32GB (AMD EPYC 7282, 64GB RAM) running Qwen3.6-35B-A3B UD-Q4_K_XL (22.9GB, 262K native context, MTP-2 speculative decoding): decode +37-77% vs a llama.cpp baseline of 109 tok/s; MTP acceptance rose from 47% (llama.cpp) to 68-100% depending on workload, with agent/tool-call traffic (near-perfect context echo) the best case. Prompt processing collapses with context length (3,126 tok/s at a 14K-token prompt down to 285 tok/s at 216K) while decode degrades more gently (169 → 45 tok/s). VRAM peak ~29.6/32GB at 65K context with 2 concurrent streams. `--draft-vocab 16384` measured +4-12% decode. Concurrent streams are serialized (one resident sequence, FIFO), not batched — N streams run at full single-stream speed each but total wall time is roughly the sum, not improved aggregate throughput. (source: https://www.reddit.com/r/unsloth/comments/1xdzfnf/for_qwen3635b_lovers_ud_q4_k_xl_now_runs_in/)
- Strata enforces specific per-layer quantization levels by default; a fine-tune's GGUF (e.g. UD_Q8_K_XL) can fail to load if some layers aren't in an accepted precision — fix is requantizing just those layers with llama.cpp's `llama-quantize`. Separately, expert-profile tuning (distinct from the kernel/memory/resource optimizations that do most of the work) gives a 1-5% perf boost and transfers across fine-tunes of the same base model (tested: Qwen3.6-35B-A3B base and the Sage fine-tune gave near-identical results from the same expert profile). (source: https://www.reddit.com/r/unsloth/comments/1xdzfnf/for_qwen3635b_lovers_ud_q4_k_xl_now_runs_in/)
