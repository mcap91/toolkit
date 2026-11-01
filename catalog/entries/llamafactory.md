---
name: llamafactory
title: LLaMA Factory
url: "https://github.com/hiyouga/LlamaFactory"
category: framework
summary: "Unified fine-tuning framework for 100+ LLMs and VLMs — zero-code web UI (LLaMA Board) and CLI; supports SFT, LoRA/QLoRA (2–8 bit), DPO/KTO/ORPO/PPO, reward modeling, pretraining; multimodal (image/video/audio); vLLM/SGLang inference; NVIDIA/AMD/Ascend NPU/CPU; used by Amazon, NVIDIA, Aliyun; ACL 2024; Apache 2.0"
tags: [fine-tuning, lora, qlora, dpo, ppo, multimodal, web-ui, distributed-training, vllm]
reviewed: 2026-07-06
acquired: 2026-07-06
license: Apache-2.0
security_flags: []
overlaps: [unsloth, axolotl, trl]
source: unknown
---

## What it does

Unified framework for fine-tuning 100+ LLMs and VLMs with both a zero-code Gradio web UI (LLaMA Board) and CLI. Single YAML config drives dataset prep, training, evaluation, and inference.

### Training methods

- **Supervised fine-tuning** — full, freeze-tuning, LoRA, QLoRA (2/3/4/5/6/8-bit via AQLM/AWQ/GPTQ/LLM.int8/HQQ/EETQ), OFT/QOFT
- **Preference tuning** — DPO, IPO, KTO, ORPO, SimPO
- **Reinforcement learning** — PPO, GRPO (via companion EasyR1 framework)
- **Reward modeling** — outcome RM and process RM (PRM)
- **Pretraining** — continual pretraining

### Optimizers and techniques

GaLore, BAdam, APOLLO, Adam-mini, Muon, DoRA, LongLoRA, LLaMA Pro, Mixture-of-Depths, LoRA+, LoftQ, PiSSA, NEFTune, rsLoRA, FlashAttention-2, Unsloth integration, Liger Kernel, KTransformers, Scalable Softmax

### Model support

100+ models: LLaMA 1–4, DeepSeek (including R1), Qwen 2–3.6, Gemma 1–3n, Mistral/Mixtral, GLM 4–4.5, Phi 3–4, Falcon, InternLM/InternVL, MiniCPM, and many more. Day-0/Day-1 support for new releases.

### Multimodal

Vision (LLaMA-Vision, Qwen2-VL/3-VL, Pixtral, LLaVA, InternVL, GLM-4.6V, Gemma 3n), audio (Qwen2-Audio, Voxtral, MiniCPM-o), video (Qwen3-VL)

### Inference

OpenAI-style API deployment via vLLM or SGLang backends. Gradio chat UI. Ollama modelfile export.

## Differentiators

- **Zero-code web UI** — LLaMA Board (Gradio) covers the full train/eval/inference pipeline with no code
- **Broadest model support** — 100+ models with day-0/day-1 releases, including rare architectures (Yuan, TeleChat, Ling)
- **Hardware breadth** — NVIDIA CUDA, AMD ROCm, Ascend NPU, CPU; Docker images for each
- **Quantization depth** — 2-bit through 8-bit QLoRA with 6 quantization backends
- **KTransformers integration** — fine-tuning 1T+ models on 2x 4090 GPUs + CPU offloading
- **Megatron-core backend** — via mcore_adapter for large-scale pretraining

## Mechanical details / What to adopt

- Install: `git clone && pip install -e .` or Docker (`hiyouga/llamafactory:latest`)
- Train: `llamafactory-cli train examples/train_lora/qwen3_lora_sft.yaml`
- Chat: `llamafactory-cli chat examples/inference/qwen3_lora_sft.yaml`
- Web UI: `llamafactory-cli webui`
- API: `llamafactory-cli api examples/inference/qwen3.yaml infer_backend=vllm`
- Export/merge: `llamafactory-cli export examples/merge_lora/qwen3_lora_sft.yaml`
- Cloud: Google Colab (free), Alibaba PAI-DSW (free trial)
- Experiment tracking: TensorBoard, W&B, MLflow, SwanLab

## Security

Apache 2.0 licensed. Model weights subject to individual model licenses. Docker images available for CUDA, ROCm, and Ascend NPU. Datasets loaded from HuggingFace, ModelScope, Modelers Hub, local disk, or cloud storage.