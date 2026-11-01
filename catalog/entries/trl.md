---
name: trl
title: TRL (Transformers Reinforcement Learning)
url: "https://huggingface.co/docs/trl/en/index"
category: framework
summary: "Hugging Face full-stack post-training library — SFT, GRPO, DPO, reward modeling, PPO, and more; vLLM integration for online RL; Harbor sandboxed agent training; vision-language model alignment; co-located vLLM for GPU efficiency; integrated with transformers/PEFT/DeepSpeed/Liger Kernel; Apache 2.0"
tags: [fine-tuning, rlhf, dpo, grpo, ppo, reward-modeling, huggingface, vllm, post-training]
reviewed: 2026-07-06
acquired: 2026-07-06
license: Apache-2.0
security_flags: []
overlaps: [unsloth, axolotl, llamafactory]
source: unknown
---

## What it does

Full-stack library for post-training transformer language models, integrated with Hugging Face transformers. Provides trainers for supervised fine-tuning, reinforcement learning, and preference optimization.

### Training methods

- **SFT** — supervised fine-tuning
- **GRPO** — Group Relative Policy Optimization (with vLLM support)
- **DPO** — Direct Preference Optimization
- **PPO** — Proximal Policy Optimization
- **Reward modeling** — train reward models for RLHF
- **Harbor** — train agents against sandboxed task suites (instruction + sandbox image + in-sandbox verifier) via GRPOTrainer's `environment_factory`

### Key features

- vLLM integration for online RL with co-located inference (no separate GPU allocation)
- Vision-language model alignment
- PEFT/LoRA integration
- DeepSpeed and Liger Kernel support
- Dataset format documentation and training FAQ

## Differentiators

- **Native transformers integration** — built on top of HF transformers, seamless with the HF ecosystem (Hub, datasets, PEFT)
- **Harbor** — sandboxed agent training environment with verifiers, unique among fine-tuning libraries
- **Co-located vLLM** — runs vLLM inference alongside training on the same GPUs, no dedicated inference server needed
- **VLM alignment** — first-class support for vision-language model preference optimization

## Mechanical details / What to adopt

- Install: `pip install trl`
- SFT: `SFTTrainer` with standard HF training arguments
- GRPO: `GRPOTrainer` with `environment_factory` for agent training
- DPO: `DPOTrainer` with preference datasets
- Learn: HF smol course covers post-training with TRL
- TRL v1 is the current major version (March 2026)

## Security

Apache 2.0 licensed. Part of the Hugging Face ecosystem. Models and datasets loaded from HF Hub or local storage.