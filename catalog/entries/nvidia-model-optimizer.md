---
name: nvidia-model-optimizer
title: NVIDIA Model Optimizer
url: https://github.com/NVIDIA/Model-Optimizer
source_url: https://www.instagram.com/reel/DdrPPALI9iA/
source: instagram
category: framework
summary: NVIDIA's open-source library (formerly TensorRT Model Optimizer, rebranded Dec 2025) of LLM/VLM compression techniques — post-training quantization (NVFP4/FP8/INT8/INT4 via SmoothQuant, AWQ, SVDQuant), quantization-aware training/distillation, pruning, distillation, speculative-decoding draft training, and sparsity; takes Hugging Face/PyTorch/ONNX checkpoints, exports quantized checkpoints deployable on TensorRT-LLM, TensorRT, vLLM, or SGLang; publishes pre-quantized checkpoints (DeepSeek-R1-FP4, Llama-3.3-70B-FP4, Nemotron NVFP4) on Hugging Face; pip install nvidia-modelopt[all]; pre-1.0 (0.x), Apache-2.0.
tags:
  - nvidia
  - quantization
  - pruning
  - distillation
  - speculative-decoding
  - sparsity
  - model-compression
  - tensorrt-llm
  - vllm
  - nvfp4
  - fp8
  - inference-optimization
reviewed: 2026-10-30
acquired: 2026-10-30
license: Apache-2.0
security_flags: []
overlaps:
  - llm-compressor
---

## What it does

NVIDIA Model Optimizer (ModelOpt, formerly "TensorRT Model Optimizer" before a December 2025 rebrand) is a library of model optimization techniques for accelerating LLM and VLM inference: post-training quantization (PTQ), quantization-aware training (QAT) and quantization-aware distillation, pruning, knowledge distillation, speculative-decoding draft-module training, and sparsity. It consumes Hugging Face, PyTorch, or ONNX checkpoints and exposes Python APIs to compose these techniques, exporting a checkpoint ready for downstream deployment on TensorRT-LLM, TensorRT, vLLM, or SGLang. It integrates with NVIDIA Megatron-Bridge, Megatron-LM, and Hugging Face Accelerate for training-required optimization steps.

Quantization support covers NVFP4, FP8, INT8, and INT4 formats using algorithms including SmoothQuant, AWQ, SVDQuant, and Double Quantization, with both PTQ and QAT workflows. NVIDIA publishes pre-quantized checkpoints built with ModelOpt on Hugging Face (e.g. DeepSeek-R1-FP4, Llama-3.3-70B-Instruct-FP4, Llama-3.1-405B-Instruct-FP4, Nemotron 3 Ultra NVFP4, Nemotron-3-Super FP8/NVFP4), and documents customer uses: Domyn compressed Colosseum-355B to 260B with Minitron pruning+distillation, Bielik.AI built a 7B Minitron model (33% smaller, 50% faster, 90% quality retained), and Adobe reports a 60% diffusion-latency reduction and 40% TCO reduction combining ModelOpt with TensorRT.

## Mechanical details

Install via `pip install -U nvidia-modelopt[all]`, or clone `github.com/NVIDIA/Model-Optimizer` and `pip install -e .[dev]`. Ships pre-installed in NVIDIA's `nvcr.io/nvidia/pytorch`, `nvcr.io/nvidia/nemo`, and `nvcr.io/nvidia/tensorrt-llm/release` container images. Open-sourced January 2025; still pre-1.0 (0.x versioning) with a documented deprecation policy (~1-release/~1-month migration window per deprecated feature). Ships agent-tooling skills installable via a Claude Code or Codex plugin marketplace (`claude plugin marketplace add https://github.com/NVIDIA/Model-Optimizer.git`).

## Security

Apache-2.0 licensed, source public on GitHub. A local optimization/export library, not a network service — no telemetry or network calls beyond standard package/model downloads (PyPI, Hugging Face). Pre-1.0 versioning means breaking API changes can land in minor releases.

## Sources

- [GitHub: NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer) — README, techniques table, release notes
- [Instagram reel](https://www.instagram.com/reel/DdrPPALI9iA/) — creator describes using ModelOpt's quantization to run a ~27B-parameter Qwen model locally on a laptop, claiming it cut their coding costs to near zero