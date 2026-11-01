---
name: nanogpt
title: nanoGPT
url: "https://github.com/karpathy/nanogpt"
category: reference
summary: "Karpathy's canonical minimal GPT training repo (~600 lines total); deprecated Nov 2025 in favor of nanochat but remains the clearest educational reference for transformer training loops"
tags: [gpt, training, transformer, karpathy, deep-learning, educational]
reviewed: 2026-06-17
acquired: 2026-06-17
license: MIT
security_flags: [deprecated]
overlaps: [zero-to-mastery-ml]
source: unknown
---

## What it does

The simplest, fastest repository for training/finetuning medium-sized GPTs. The entire implementation is ~600 lines: `train.py` (~300 lines, boilerplate training loop) and `model.py` (~300 lines, GPT model definition with optional GPT-2 weight loading). Reproduces GPT-2 (124M) on OpenWebText using a single 8xA100 node in ~4 days.

Supports: character-level and BPE tokenization, DDP multi-GPU/multi-node training, PyTorch 2.0 `torch.compile`, finetuning from GPT-2 checkpoints, CPU/GPU/MPS (Apple Silicon) inference.

**Deprecated as of Nov 2025** — Karpathy recommends nanochat as the successor.

## Assessment

As a reference for understanding transformer training, nanoGPT is unmatched in clarity-to-capability ratio. The code is intentionally readable and hackable. However, it's explicitly deprecated and not under active development.

For this catalog's purposes, it's a learning reference rather than something to build on. The successor (nanochat) would be the actionable project if training custom models becomes relevant. The patterns (minimal training loop, clean model definition, config-file-driven hyperparameters) are worth studying for anyone building agent-driven ML training workflows.

## Mechanical details

- Install: `pip install torch numpy transformers datasets tiktoken wandb tqdm`
- Quick start: `python data/shakespeare_char/prepare.py && python train.py config/train_shakespeare_char.py`
- Sampling: `python sample.py --out_dir=out-shakespeare-char`
- Windows: needs `--compile=False` (PyTorch 2.0 compile not fully supported)
- Successor: nanochat (same author)

## Security

- **License**: MIT
- **Maintenance**: Deprecated Nov 2025. No further updates expected
- **Dependencies**: Standard PyTorch ML stack (torch, numpy, transformers, datasets, tiktoken, wandb, tqdm)
- **Supply chain**: Karpathy (former OpenAI founding member, high-trust author). 13k+ GitHub stars