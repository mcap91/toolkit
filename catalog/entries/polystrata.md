---
name: polystrata
title: PolyStrata
url: https://github.com/VecSzn/PolyStrata
category: framework
summary: Fork/extension of Strata that adds a second expert-offloading inference engine for more MoE models from ordinary GGUF files — GLM 5.3 Flash, Qwen3.6-35B-A3B, Ornith 1.5, Gemma 4 26B-A4B, Tiel Coder, DeepSeek V4 Flash, LFM2.5, MiniCPM-V and others — beside Strata's unchanged Qwen3.8-Flash-Next engine; GPU caches the most-used experts while the CPU computes the rest from the memory-mapped GGUF, plus draft-token speculation; one-click installer (Windows/Linux), web UI, OpenAI/Anthropic-compatible API on localhost:8080; NVIDIA RTX 20–50 (AMD HIP beta on Linux); author reports ~70–87 tok/s for Qwen3.6-35B-A3B on an 8GB RTX 4070 laptop; MIT
tags:
  - local-inference
  - moe
  - expert-offloading
  - gguf
  - speculative-decoding
  - nvidia
  - cuda
  - amd-hip
  - openai-compatible
  - anthropic-compatible
  - consumer-gpu
  - one-click
  - qwen
  - glm
  - gemma
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - strata
  - lm-studio
  - large-moe-consumer-hardware
license: MIT
security_flags:
  - new-project
  - model-downloads-third-party
  - single-maintainer
source: unknown
---

## What it does

PolyStrata packages the Strata engine (which runs Qwen3.8-Flash-Next on consumer cards) together with a second engine that applies the same idea to other mixture-of-experts models loaded from their standard GGUF files. The model does not need to fit in VRAM: the card holds the experts an answer uses most, the CPU computes the others directly from the memory-mapped GGUF, and the GPU cache follows the experts as an answer is generated. The engine also guesses a few tokens ahead (from the model's own draft block or by matching a repeat of the conversation) and verifies guesses in one pass; with all experts on CPU, outputs are token-identical with and without speculation, and the first 64 tokens are checked against llama.cpp on the same file.

## Mechanical details

- Install: `START-HERE.bat` (Windows; since v0.1.42-poly.1 ships a prebuilt CUDA 13 engine for RTX 20–50, no Visual Studio/CUDA toolkit needed) or `./setup.sh --family <qwen36|glm|...>` (Linux; `--gguf-dir` to reuse an existing file). Interactive setup selects model, context size, image support.
- Endpoints: web UI `http://127.0.0.1:8080`, OpenAI `/v1`, Anthropic `/v1/messages`; works as a Claude Code backend (README includes a Claude Code demo).
- Models (README at review): Qwen3.8-Flash-Next (Strata engine); GLM 5.3 Flash (79–114GB files, mostly in RAM), DeepSeek V4 Flash, LFM2.5-24B-A2B, Flint 40B-A2.5B, Qwen3.6-35B-A3B, Ornith 1.5, Gemma 4 26B-A4B, Tiel Coder 35B-A3B, MiniCPM-V 4.7 35B-A3B, Kolibri 1. Qwen3.6, Ornith and Gemma accept images.
- Hardware: 8–32GB VRAM, 20–96GB RAM depending on model, 11–114GB disk per model. AMD HIP port (community contributed, 0.1.42-poly.4) is Linux-only beta. macOS only for Qwen3.8-Flash-Next.
- Author-reported throughput (short chat / after ~31K prompt / prefill tok/s), v0.1.42-poly.1: Qwen3.6-35B-A3B UD-Q3_K_M 84–87 / 70–73 / ~1,500 on RTX 4070 8GB laptop; 385–393 / 241–246 / ~6,400 on RTX 5090. GLM 5.3 Flash 3.0bit 59–66 tok/s on a 5090 with 120GB RAM (llama.cpp on same PC: ~26). Context costs ~0.7GB VRAM per 32K tokens at fp16, taken from the expert cache.
- Tunables: `STRATA_ROUTE_TAIL_SKIP=0` disables skipping low-ranked experts on cards that can't hold all experts (~9% faster when on, slightly changes outputs); `--kv`, `--vram-reserve-mib`, `--expert-swaps`, `--conversation-cache-mib`.

## Usage notes

- Community reports in the launch thread: Tiel Coder 35B-A3B works unofficially (same qwen35moe arch) with ~4x faster prompt processing (1,000–1,500 tok/s) on an RTX 5060 Mobile 8GB; a ROCm port with INT8 KV cache ran Ornith 1.5 at ~85 tok/s / 200K context on a 20GB 7900 XT. The author recommends raising `--vram-reserve-mib` (e.g. 1024) on HIP rather than disabling the VRAM watchdog.
- The GitHub account/repo was briefly unavailable during the launch period and was mirrored to Hugging Face before being restored.

- AMD HIP port (0.1.42-poly.4, Linux only, contributed by iMilnb, build via `./setup.sh --family qwen36`) measured on an RX 7600 8GB: Qwen3.6 UD-Q2_K_XL 64 tok/s, Ornith Mini 35 tok/s (source: https://www.reddit.com/r/LocalLLM/comments/1x22inc/polystrata_strata_with_four_more_moe_models/)

## Security

MIT (model files carry their own licenses). Binds to localhost by default; `--host 0.0.0.0` requires `--api-key`. README states no data leaves the machine; no telemetry described. Installer downloads engines and model files from GitHub releases and Hugging Face. Most engine code is from the Strata project; the added engine and models are labeled experimental and measured on two machines.
