---
name: nemotron-3-5-bolt
title: NVIDIA Nemotron 3.5 Bolt 74B-A9B (24GB)
url: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB
category: framework
summary: "NVIDIA open-weight vision-language model for local agentic work — 74B total / 9B active Mamba-2–Transformer hybrid LatentMoE with C-RADIO v4-H vision encoder, fine-tuned from Nemotron 3.5 Super VL; natively 2-bit (IQ2) via quantization-aware training so the packed model fits in 24GB; text/image/video in, 256K context, thinking toggle via `enable_thinking`; releases: 24GB vLLM pack, 24GB GGUF (22GB + 1.73GB mmproj) for llama.cpp, BF16 for post-training, and a 1.1B LiLiCorr speculative-decoding drafter; OpenMDW-1.1 license; announced alongside NVIDIA PAIR"
tags:
  - nvidia
  - nemotron
  - open-weights
  - moe
  - mamba
  - vision-language-model
  - quantization-aware-training
  - 2-bit
  - gguf
  - llama-cpp
  - vllm
  - local-inference
  - speculative-decoding
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - nemotron-3-ultra
  - nvidia-pair
license: OpenMDW-1.1
security_flags: []
source: unknown
---

## What it does

Nemotron 3.5 Bolt 74B-A9B is an NVIDIA open-weight model aimed at running everyday agent tasks on local hardware. Its distinguishing feature is native 2-bit precision produced with quantization-aware training (QAT) rather than post-hoc quantization, so the 74B-parameter MoE fits in a 24GB memory budget alongside other applications. It was announced together with NVIDIA's open-source PAIR tool for routing AI workloads across multiple local machines (see `nvidia-pair`).

## Mechanical details

- Architecture: Mamba-2–Transformer hybrid LatentMoE, 74B total / 9B active parameters; C-RADIO v4-H vision encoder. Base lineage: Nemotron 3.5 Super VL 120B-A12B → Bolt 74B-A9B.
- Inputs/outputs: text, image, video in; text out. Up to 256K context. Reasoning toggled with the chat-template `enable_thinking` flag. Recommended sampling for text: temperature 1.0, top_p 0.95.
- Official releases on Hugging Face (`nvidia/`):
  - `...-24GB`: packed IQ2 model for vLLM on Ampere (A100), Hopper (H100-80GB), Blackwell.
  - `...-24GB-GGUF`: llama.cpp format, 22GB main file + 1.73GB mmproj; targets RTX/DGX Spark (64/128GB) or discrete RTX GPUs (32GB+). llama.cpp support landed via PR #30520.
  - `...-BF16`: full precision for customization/post-training.
  - `...-24GB-LiLiCorr-GGUF`: 1.113B-parameter speculative-decoding drafter (released 2026-10-15).
- Community quants exist (Unsloth GGUFs, Sapid Labs NVFP4 W4A16 at 51.4GB — not NVIDIA-reviewed).

## Usage notes

- r/LocalLLM launch thread: commenters question 2-bit for agentic work; note that the 24GB footprint exceeds the 24GB RAM of some RTX Spark machines once OS overhead is included; several suggest running it through Strata-style expert offloading. Linked community benchmarks report roughly 2x the tokens/s of Qwen3.8 27B Q4_K_M on a 3090/5090 but fewer tasks passed, with the gap concentrated in tool calling (480-trial comparison posted to r/LocalLLM).

## Security

Model weights only; no executable code beyond standard inference runtimes. License is OpenMDW-1.1 (NVIDIA open model license; read the repo LICENSE for terms). Third-party quants and fine-tunes are not NVIDIA-reviewed.
