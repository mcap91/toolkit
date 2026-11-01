---
name: soup
title: Soup
url: "https://github.com/MakazhanAlpamys/Soup"
category: framework
summary: "LLM fine-tuning CLI — one YAML config, one command; supports SFT, DPO, GRPO, PPO, KTO, ORPO, SimPO, IPO, BCO, pre-training, distillation, vision/audio; layer streaming trains an 8B model on a 4 GB GPU by streaming frozen base from host RAM one decoder layer at a time (bit-exact); auto batch size, GPU detection, quantization (4-bit/8-bit/FP8/QAT); backends: transformers, Unsloth, MLX; web UI dashboard; export to GGUF/ONNX/TensorRT/AWQ; 100+ model recipes; Python 3.10-3.12; Apache-2.0"
tags: [llm, fine-tuning, lora, qlora, sft, dpo, grpo, training, cli, yaml, layer-streaming, python]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: [unsloth, torchtune, trl, axolotl, llamafactory]
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

Soup is a command-line tool for LLM fine-tuning and post-training that wraps the complexity of training infrastructure behind a single YAML configuration file. The goal is zero SSH, zero config debugging — `soup init`, `soup train`, done.

Key capabilities:

- **Training methods**: SFT, DPO, GRPO, PPO, KTO, ORPO, SimPO, IPO, BCO, RLHF, PRM, tool-calling, pre-training, distillation, classification, vision/audio/TTS fine-tuning, unlearning, RAFT/RA-DIT.
- **Layer streaming** (beta): Streams the frozen base model from host RAM to GPU one decoder layer at a time, keeping VRAM usage constant regardless of model size. Trains Llama-3.1-8B-Instruct + NF4 on an RTX 3050 4 GB at 119.6 tok/s, 3.32 GB peak — bit-exact against a normal resident run. Described in a Zenodo preprint (v3, August 2026).
- **PEFT methods**: LoRA, DoRA, LoRA+, rsLoRA, VeRA, OLoRA, NEFTune, PiSSA, ReLoRA, LLaMA Pro, GaLore.
- **Quantization**: 4-bit (NF4/FP4), 8-bit, FP8, QAT, AWQ, GPTQ, BitNet, KV-cache quantization.
- **Auto-configuration**: Automatic batch size selection, GPU detection, quantization defaults. `soup autopilot` for zero-config training with just a model ID, data file, and goal.
- **Backends**: Transformers (default), Unsloth (2-5x faster, `[fast]` extra), MLX (Apple Silicon).
- **Export**: GGUF (for Ollama/llama.cpp), ONNX, TensorRT, AWQ, GPTQ, BitNet. LoRA merge. OpenAI-compatible serving.
- **Web UI**: Local browser dashboard (`soup ui`) for experiments, training setup, live metrics, dataset exploration, and model chat.
- **100+ model recipes**: Ready-made configs for Llama 3.x/4, Qwen 2.5/3, Gemma 3, Mistral, Mixtral, DeepSeek R1/V3, Phi-4, and more.

## Installation

Install via `pipx install "soup-cli[train]"` or `uv tool install "soup-cli[train]"` (preferred for isolation). Light CLI without training deps: `pipx install soup-cli`. Full install with all extras: `pipx install "soup-cli[all]"`. Docker image published to GHCR on every release. Requires Python 3.10-3.12, GPU with CUDA (recommended), Apple Silicon MPS, or CPU (experimental).

VRAM requirements with QLoRA 4-bit: ~7B models on 8 GB, ~14B on 16 GB, ~34B on 24 GB, ~70B on 48 GB.

## Mechanical details

Data formats: Alpaca, ShareGPT, ChatML, preference pairs, vision, audio, ASR, plaintext, embedding, RAFT — auto-detected from JSONL, JSON, CSV, Parquet, or TXT. Config schema defined in `config/schema.py` as single source of truth. Unknown config keys rejected since v0.75 (previously silently ignored). Multi-GPU via DeepSpeed and FSDP. Experiment tracking integration. Supply-chain controls: scan, sign, BOM, attest, audit, airgap. Compliance templates for HIPAA, SOC2, EU AI Act, SR-11-7.

`soup doctor` checks GPU, system resources, dependencies, and version. Tests run without GPU for fast CI.

## Security

Apache-2.0. Telemetry strictly opt-in (`SOUP_TELEMETRY=1`, default off). Built and maintained by a single developer on a 4 GB laptop — all performance numbers measured rather than claimed. v0.75 hardens the web UI: read endpoints and SSE require auth with short-lived single-use tickets, `--public` no longer exposes API docs to the LAN. Community-driven: v0.75 contained 60 pull requests from 22 external contributors.

## How to use it

pipx install "soup-cli[train]"
