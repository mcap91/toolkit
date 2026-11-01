---
name: ovis-vl-embedding
title: Ovis-VL-Embedding
url: "https://huggingface.co/ATH-MaaS/Ovis-VL-Embedding-2B"
category: framework
summary: "Omni-modal embedding model (2B and 9B variants) built on Qwen3.5 backbone — encodes text, images, visual documents, and video frames in a shared representation space; 77.46 overall on MMEB-v2 (78 datasets), 80.47 on visual document retrieval; no modality-specific projection heads, last-token hidden state as embedding; for multimodal RAG, cross-modal search, document retrieval"
tags: [embeddings, multimodal, visual-document-retrieval, qwen, rag, cross-modal-search, vision-language, video-retrieval]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: ""
security_flags: [trust-remote-code]
source: unknown
---

## What it does

Ovis-VL-Embedding is a multimodal embedding model that encodes text, images, visual documents, and sampled video frames as one interleaved sequence. The final-layer hidden state at the last non-padding token becomes the retrieval embedding, with no modality-specific projection heads.

Built on Qwen3.5's native text and vision encoders with a shared multimodal language backbone. Two sizes: 2B (initialized from Qwen3.5-2B) and 9B (from Qwen3.5-9B). Unlike approaches that bolt separate modality towers together, Ovis-Embedding starts from a pretrained omni-modal understanding model with natively aligned front-ends.

Intended use cases:

- Semantic text search and cross-modal retrieval (text-to-image, image-to-text, image-to-image)
- Multimodal RAG indexing and retrieval
- Visual document and page retrieval (e.g., searching for an underwriting fee in a scanned table, or a location on a map)
- Text-to-video and video retrieval
- Recommendation and nearest-neighbor matching

## Mechanical details

Ovis-VL-Embedding-2B scores 77.46 overall on MMEB-v2 (78 datasets spanning image, video, and visual-document tasks), outperforming the strongest compared baseline by 2.04 points. On visual document retrieval: 80.47 vs 79.86 baseline. Produces d=2048-dimensional embeddings. Part of the broader Ovis-Embedding family which also includes audio-capable omni-modal variants. arXiv: 2609.25165 (September 2026).

## Security

License not specified on the model card. Requires `trust_remote_code=True` for loading via Transformers (executes arbitrary Python from HuggingFace snapshot). Published by ATH-MaaS group.