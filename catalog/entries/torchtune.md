---
name: torchtune
title: torchtune
url: "https://github.com/meta-pytorch/torchtune"
category: framework
summary: "PyTorch-native post-training library by Meta — composable building blocks (not trainers) for SFT, LoRA, QLoRA, DPO, GRPO, quantization, evaluation; YAML-driven recipes under 600 LOC; composable parallelism (FSDP2, TP, SP, CP, expert parallel for MoE); in-backward optimizer fusion; works on single 24GB GPU to multi-node clusters; v0.6 stable; Apache 2.0"
tags: [fine-tuning, pytorch, lora, qlora, dpo, fsdp, distributed-training, post-training, meta]
reviewed: 2026-07-06
acquired: 2026-07-06
license: Apache-2.0
security_flags: []
overlaps: [unsloth, axolotl, llamafactory, trl]
source: unknown
---

## What it does

PyTorch-native post-training library built around composable building blocks rather than monolithic trainers. Each training recipe is self-contained (under 600 lines of code), designed to be read and modified directly.

### Training workflow

- **Dataset preparation** — download and prepare datasets from HF Hub or local storage
- **Fine-tuning** — full fine-tune, LoRA, QLoRA with hackable model builders
- **Preference optimization** — DPO, GRPO
- **Quantization** — post-training quantization via torchao (4-bit, 8-bit)
- **Evaluation** — integrated with EleutherAI's LM Evaluation Harness
- **Inference** — local inference testing, ExecuTorch export for mobile/edge

### Parallelism stack

Composable parallelism built on PyTorch DTensor: FSDP2, tensor parallel, sequence parallel, context parallel, expert parallel (MoE), loss parallel. The same components scale from a single GPU to multi-node clusters without rewriting the training loop.

### Performance

- In-backward optimizer fusion reduces gradient-buffer lifetime for large models
- Memory-efficient recipes tested on single 24GB consumer GPUs
- YAML-driven configs (Hydra-inspired) with orthogonal optimization switches

### Model support

Llama 1–4, Gemma 2, Qwen 2.5, and others. Checkpoint compatibility with HF Hub and production inference systems.

## Differentiators

- **No-abstraction recipes** — each recipe is under 600 LOC with no trainer framework; full visibility into the training loop
- **PyTorch-native parallelism** — composable DTensor-based parallelism stack, not wrapping external libraries
- **Correctness-first** — high bar on proving correctness of components; "PyTorch just works, so should torchtune"
- **ExecuTorch export** — direct path to mobile/edge inference after fine-tuning
- **May 2026 paper** — arxiv:2605.21442 benchmarks against Axolotl and Unsloth

## Mechanical details / What to adopt

- Install: `pip install torchtune` (v0.6 stable)
- Download model: `tune download` CLI
- Train: `tune run <recipe> --config <config.yaml>`
- Evaluate: built-in evaluation recipe with EleutherAI harness
- Quantize: post-training recipe via torchao
- Requires PyTorch 2.x, Python 3.x

## Security

Apache 2.0 licensed. Part of the official PyTorch ecosystem (meta-pytorch org). Models downloaded from HF Hub. Integrations with W&B for experiment tracking (optional).