---
name: embeddinggemma-2
title: EmbeddingGemma 2
url: "https://huggingface.co/unsloth/embeddinggemma-2-GGUF"
category: framework
summary: "Google DeepMind's 740M-parameter open multimodal embedding model — maps text, code, images, video, and audio into one 768-dim vector space; modular encoders (270M text-only to 740M full); 8K context window; runs on-device (191MB RAM for text-only on Pixel 11 Pro); Matryoshka truncation to 512/256/128 dims; built on Gemma 4; Apache 2.0"
tags: [embeddings, multimodal, on-device, text, code, image, video, audio, vector-search, rag, google, gemma, apache-2]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

EmbeddingGemma 2 maps five modalities — text, code, images, video, and audio — into a single 768-dimensional embedding space. Built on the Gemma 4 architecture, released by Google DeepMind on 2026-10-06.

Modular design loads only what is needed:

- **Text + code** (270M params): 130M transformer + 140M embedder. 191MB RAM on Pixel 11 Pro.
- **Text + vision** (440M params): adds 170M vision encoder.
- **Text + audio** (570M params): adds 300M audio encoder.
- **Full multimodal** (740M params): all encoders. ~0.5GB RAM.

Context window: 8,192 tokens (4x EmbeddingGemma 1). Fits ~29 images, 58 video frames, or 5.5 minutes of audio per input.

All configurations share one vector space — a text-only query matches documents embedded by the full model.

## Mechanical details

Output dimension: 768, reducible to 512, 256, or 128 via Matryoshka truncation.

Benchmarks (selected):
- MTEB multilingual v2: 61.36
- MTEB Code v1: 78.68 (+9.92 over v1)
- MIEB lite (image): 64.64
- MSEB retrieval (sound): 69.54

GGUF weights available via Unsloth. Also available on HuggingFace and Kaggle in original format. Can run locally via Unsloth Desktop or standard GGUF-compatible runtimes.

## Security

Apache 2.0 licensed. Runs entirely on-device — no network calls required for inference. No known security flags.