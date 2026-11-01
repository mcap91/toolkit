---
name: sparse-memory-lm
title: sparse-memory-lm (product-key memory on a 21M model)
url: https://github.com/re133/sparse-memory-lm
category: framework
summary: Hobby research repo testing product-key memory layers (Lample et al. 2019; Meta 'Memory Layers at Scale') on a small model — a 21M-parameter Llama-style decoder plus a learned table of up to 16.8M rows × 384 dims (6.4B values, ~384 rows / 33M values read per token) matches a ~114M dense model's perplexity on 500M Wikipedia tokens; 4-bit table memory-mapped from NVMe generates ~114–140 tok/s using 0.4GB VRAM (prompt prefill slow from page faults); portable Triton kernels verified on RX 9070, MI350X, H100/H200; bolting a table onto pretrained Qwen3.5-0.8B did not help; Apache-2.0
tags:
  - memory-layers
  - product-key-memory
  - sparse-memory
  - language-model
  - research
  - triton
  - rocm
  - ssd-offload
  - mmap
  - small-models
  - pretraining
  - pytorch
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - engraft-ngram
license: Apache-2.0
security_flags:
  - single-maintainer
  - research-code
source: unknown
---

## What it does

Tests what a huge, sparsely read lookup table is worth to a small language model, what it costs, and whether the table must live in VRAM. Each token's hidden state selects rows via product keys and reads only a few hundred of them, so compute per token stays nearly constant while parameter count grows with the table.

Results (single seed for the large runs; success criteria written before each run, failures included in the repo):

| Variant | Table values | Perplexity (500M tokens) | Dense-equivalent size |
|---|---|---|---|
| B-1M | 0.4B | 21.84 | ~60M |
| B-4M | 1.6B | 20.80 | ~83M |
| B-16M | 6.4B | 19.96 | ~114M |

At 3B training tokens B-16M matched a ~152M dense model. Advantage is in tokens-per-quality more than wall-clock GPU training time. Attaching a table to a finished Qwen3.5-0.8B gave no gain over a dense add-on of equal compute (+2.4 points factual recall), suggesting the table must be present from pretraining.

## Mechanical details

- Inference offload: 4-bit table (3.2GB for B-16M; 192 bytes/row, ~21 rows per 4KB page) memory-mapped from NVMe via the Linux page cache with `MADV_RANDOM` and targeted `MADV_WILLNEED`; generation 114–138 tok/s on RX 9070 using ~0.4GB VRAM; prefill 1,500–6,500 tok/s because each missed row costs a 4KB page read. Rows are currently stored in product-key order; reordering by co-activation (suggested in the thread) is untested.
- Training memory: ~16 bytes per table parameter (fp32 value, gradient accumulator, two Adam moments) + ~4.5GiB; measured peaks 10.4 GiB (B-1M), 28.5 GiB (B-4M), 101 GiB (B-16M).
- Triton kernels give matching training curves on AMD RDNA4 (RX 9070), CDNA4 (MI350X), and NVIDIA Hopper (H100/H200). Large runs cost ~$70 on Runpod.
- Run: `pip install -r requirements.txt`, `python -m pytest tests`, `python scripts/demo_generate.py --table nvme`. Model: `huggingface.co/fechyy/sparse-memory-lm-B-16M`; interactive explorer at `re133.github.io/sparse-memory-lm/explorer/` shows which table rows a token reads.
- Related approach: Engram-style n-gram hashing selects rows from input tokens (prefetchable before the layer runs); product keys select from the hidden state, which is why SSD prefill is harder here.

## Usage notes

- Model writes fluent Wikipedia-style English with fabricated facts (no instruction tuning, 21M params). The author's next step is factual-recall tests and row-level fact editing at ~1B scale.

## Security

Apache-2.0 research code with a pytest suite; built with Claude Code assistance (visible in commits); single author, ~16 stars. No network or credential handling beyond model download.
