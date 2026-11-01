---
name: mergekit
title: mergekit
url: "https://github.com/arcee-ai/mergekit"
category: cli-tool
summary: "Toolkit for merging pre-trained LLMs — 16+ merge methods (SLERP, TIES, DARE, DELLA, task arithmetic, linear, Karcher mean, etc.); out-of-core merging on CPU or with 8GB VRAM; MoE construction from dense models; LoRA extraction; evolutionary merge methods; multi-stage merging; tokenizer transplantation; Frankenmerging (layer assembly); EMNLP 2024 paper; LGPL-3.0"
tags: [model-merging, weight-merging, lora, moe, slerp, ties, dare, llm-tools]
reviewed: 2026-07-06
acquired: 2026-07-06
license: LGPL-3.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Toolkit for merging pre-trained language model checkpoints by operating directly in weight space. Uses an out-of-core approach with lazy tensor loading to perform merges on minimal hardware (CPU-only or 8GB VRAM).

### Merge methods (16+)

| Method | Core idea |
|--------|-----------|
| Linear | Weighted average of parameters |
| SLERP | Spherical linear interpolation (2 models) |
| NuSLERP | Enhanced SLERP with flexible weighting |
| Multi-SLERP | Barycentric SLERP for 3+ models |
| Karcher Mean | Riemannian barycenter on manifolds |
| Task Arithmetic | Combine "task vectors" (diffs from base) |
| TIES | Task arithmetic + sparsification + sign consensus |
| DARE | Task arithmetic + random pruning + rescaling |
| DELLA | Task arithmetic + adaptive magnitude-based pruning |
| Model Breadcrumbs | Task arithmetic + outlier removal |
| SCE | Adaptive matrix-level weighting by variance |
| Model Stock | Geometric weight calculation for interpolation |
| Nearswap | Interpolate where parameters are similar |
| Arcee Fusion | Dynamic thresholding for salient features |
| Passthrough | Direct tensor copy (Frankenmerging) |

### Additional capabilities

- **MoE construction** — merge multiple dense models into a mixture of experts (`mergekit-moe`)
- **LoRA extraction** — extract PEFT-compatible low-rank approximations from fine-tuned models (`mergekit-extract-lora`)
- **Evolutionary merge** — automated merge optimization via evolutionary search
- **Multi-stage merging** — chain multiple merge configs in a single YAML (`mergekit-multi`)
- **Raw PyTorch merging** — merge arbitrary `.pt`/`.safetensors` checkpoints (`mergekit-pytorch`)
- **Tokenizer transplantation** — align vocabularies between models for speculative decoding or distillation (`mergekit-tokensurgeon`)
- **Interpolated gradients** — per-layer parameter interpolation for fine-grained control

### Tokenizer handling

Union, base, or specific-model vocabularies. Per-token embedding source overrides. Automatic embedding matrix alignment across models before merge. Chat template configuration (auto-detect, built-in presets, or custom Jinja2).

## Differentiators

- **Out-of-core architecture** — lazy tensor loading enables merges on machines that can't fit a single model in memory
- **Method breadth** — 16+ merge algorithms from simple averaging to evolutionary optimization
- **MoE from dense** — construct mixture-of-experts models from separate dense checkpoints
- **Tokenizer surgery** — dedicated tool for cross-tokenizer operations (speculative decoding, distillation)

## Mechanical details / What to adopt

- Install: `git clone && pip install -e .`
- Merge: `mergekit-yaml config.yml ./output [--cuda] [--lazy-unpickle]`
- Extract LoRA: `mergekit-extract-lora --model finetuned --base-model base --out-path output`
- MoE: `mergekit-moe` (see docs)
- Upload: `huggingface-cli upload username/model ./output .`
- Hosted: FrankensteinAI provides browser-based merging powered by mergekit

## Security

LGPL-3.0 licensed (mergekit itself). Model weights subject to individual model licenses. No external API calls — all computation is local. Generated README.md model cards for HF Hub uploads.