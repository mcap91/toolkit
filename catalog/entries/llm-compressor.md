---
name: llm-compressor
title: LLM Compressor
url: "https://github.com/vllm-project/llm-compressor"
category: framework
summary: "Transformers-compatible model quantization/compression library for optimized vLLM deployment — GPTQ, AWQ, SmoothQuant, AutoRound, rotation-based (SpinQuant, QuIP), and REAP expert pruning; weight/activation/KV-cache/attention quantization (INT8, FP8, NVFP4, MXFP4, MXFP8); saves in compressed-tensors format; DDP and disk offloading for large-model compression; maintained by Red Hat AI and the vLLM Project"
tags: [quantization, compression, vllm, gptq, awq, fp8, nvfp4, mxfp4, inference-optimization, model-deployment, huggingface]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Apache-2.0
security_flags: []
overlaps: [unsloth, axolotl, llamafactory, turboquant]
source: unknown
---

## What it does

llmcompressor is a Transformers-compatible library from Red Hat AI and the vLLM Project for applying post-training compression algorithms to LLMs, producing checkpoints optimized for deployment with vLLM. It quantizes weights, activations, KV cache, and attention to reduced precision while preserving accuracy, and integrates directly with Hugging Face models/repositories.

### Supported precisions and types

- **Activation quantization**: W8A8 (int8 and fp8), W4AFP8, Microscale (NVFP4, MXFP4, MXFP8)
- **Mixed precision**: W4A16, W8A16, MXFP8A16, MXFP4A16, NVFP4A16
- **Attention and KV cache quantization**: FP8, NVFP4
- **Low/arbitrary-bit quantization**: WNA4, WNA8, WNA16

### Supported algorithms

Simple PTQ (round-to-nearest), GPTQ, AWQ (derived from AutoAWQ, built with AutoAWQ's original maintainer), SmoothQuant, AutoRound, rotation-based transforms (SpinQuant, QuIP), and REAP expert pruning (prunes least-salient MoE experts before quantization).

### Workflow

Models are quantized via a one-shot API (`llmcompressor.oneshot`) using a `QuantizationModifier` recipe that targets layers (e.g. `Linear`), a quantization scheme (e.g. `FP8_BLOCK`), and ignore-list (e.g. `lm_head`). Output is saved via standard Hugging Face `save_pretrained` in the compressed-tensors format (a safetensors extension), which vLLM loads natively.

### Scale and hardware support

- DDP (distributed data parallel) and disk offloading support for compressing very large models with limited hardware
- Non-uniform quantization (different schemes per layer/module)
- Architecture-specific support for MoE LLMs, Vision-Language Models, and Audio-Language Models
- Model-free definition quantization (models without a Hugging Face model class definition)
- Batched GPTQ with a Triton kernel (~15x faster than the prior eager path; up to ~30x end-to-end on MoE workloads via same-shape layer batching)

## Mechanical details

- Install: `pip install llmcompressor`
- Quick tour: load a model with `transformers.AutoModelForCausalLM`, build a `QuantizationModifier` recipe, call `oneshot(model=model, recipe=recipe)`, then `save_pretrained` — output loads directly in vLLM via `LLM("path/to/quantized-model")`
- Red Hat AI publishes pre-quantized production checkpoints under the `RedHatAI` Hugging Face org (e.g. GLM-5.3 MXFP4, Kimi-K3 NVFP4/FP8, Qwen3.8 INT4/NVFP4/MXFP4) as reference outputs of this pipeline
- Companion library `vllm-project/compressed-tensors` defines the on-disk storage format and handles checkpoint conversion between formats (AutoAWQ, ModelOpt NVFP4, FP8 block)

## Security

Apache-2.0. Actively maintained under the vllm-project GitHub org with Red Hat AI backing; frequent releases tied to vLLM version compatibility (e.g. MXFP4 weight-only support requires vLLM v0.14.0+). No installer pipe-to-shell pattern — standard `pip install`. No credential handling or network calls beyond standard Hugging Face Hub model/dataset downloads.
