---
name: axolotl
title: Axolotl
url: "https://github.com/axolotl-ai-cloud/axolotl"
category: framework
summary: "Open-source LLM post-training framework — YAML-driven pipeline for SFT, LoRA/QLoRA, DPO/KTO/ORPO, GRPO, reward modeling, pretraining, multimodal (vision/audio); ND parallelism (CP+TP+FSDP), ScatterMoE fused LoRA, MoE expert quantization, QAT, sequence parallelism; built-in agent docs CLI; Apache 2.0"
tags: [fine-tuning, lora, qlora, dpo, grpo, moe, multimodal, distributed-training, post-training]
reviewed: 2026-07-06
acquired: 2026-07-06
license: Apache-2.0
security_flags: []
overlaps: [unsloth, llamafactory, trl]
source: unknown
---

## What it does

Framework for LLM post-training and fine-tuning with a single YAML config file covering the full pipeline: dataset preprocessing, training, evaluation, quantization, and inference.

### Training methods

- **Supervised fine-tuning** — full, LoRA, QLoRA, GPTQ, QAT (quantization-aware training)
- **Preference tuning** — DPO, IPO, KTO, ORPO, SimPO, GDPO (Generalized DPO)
- **Reinforcement learning** — GRPO
- **Reward modeling** — outcome RM and process RM (PRM)
- **Pretraining** — continual pretraining with text diffusion support
- **Multimodal** — LLaMA-Vision, Qwen2-VL, Pixtral, LLaVA, SmolVLM2, GLM-4.6V, InternVL 3.5, Gemma 3n, Voxtral (audio)

### Performance optimizations

- Multipacking, Flash Attention 2/3/4, Xformers, Flex Attention, SageAttention, Liger Kernel, Cut Cross Entropy
- ScatterMoE LoRA (custom Triton kernels on MoE expert weights)
- MoE expert quantization (`quantize_moe_experts: true`) for reduced VRAM with FSDP2
- Sequence Parallelism (SP) for context length scaling
- ND Parallelism (CP + TP + FSDP within and across nodes)
- Multi-GPU (FSDP1, FSDP2, DeepSpeed), multi-node (Torchrun, Ray)
- EAFT (Entropy-Aware Focal Training), Scalable Softmax for long context
- Distributed Muon optimizer for FSDP2 pretraining

### Model support

GPT-OSS, LLaMA 1–4, Mistral/Mixtral, Qwen 2–3.6, Gemma 1–4, DeepSeek, GLM, Phi, Granite, and many more. Day-0/Day-1 support for new model releases.

## Differentiators

- **YAML-first pipeline** — one config file drives the entire training pipeline including dataset prep
- **ScatterMoE fused LoRA** — LoRA directly on MoE expert weights via custom Triton kernels
- **ND Parallelism** — composable CP + TP + FSDP within a single YAML config
- **Agent docs CLI** — `axolotl agent-docs` ships bundled documentation optimized for AI coding agents, no repo clone needed
- **Text diffusion training** — alternative to autoregressive training

## Mechanical details / What to adopt

- Install: `uv pip install --no-build-isolation axolotl[deepspeed]` (requires Python 3.12, PyTorch 2.12+, NVIDIA Ampere+)
- Docker: `axolotlai/axolotl:main-latest`
- Train: `axolotl train examples/llama-3/lora-1b.yml`
- Fetch examples: `axolotl fetch examples`
- Agent docs: `axolotl agent-docs sft` / `axolotl agent-docs grpo` / `axolotl agent-docs --list`
- Config schema: `axolotl config-schema`
- Cloud: RunPod, Vast.ai, PRIME Intellect, Modal, Novita, JarvisLabs, Latitude.sh

## Security

Apache 2.0 licensed. Opt-out telemetry (system info, model types, error rates — no personal data or file paths); disable with `AXOLOTL_DO_NOT_TRACK=1`. Datasets loaded from HuggingFace, local disk, or cloud storage (S3/Azure/GCP/OCI).