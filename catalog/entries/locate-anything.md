---
name: locate-anything
title: LocateAnything
url: "https://research.nvidia.com/labs/lpr/locate-anything/"
category: framework
summary: novel parallel box decoding for vision-language grounding; 3B model on HuggingFace; evaluate for spatial/histology image analysis when pipeline matures
tags: [vision, grounding, object-detection, nvidia, spatial, histology, image-analysis]
license: Apache-2.0 (code); NVIDIA non-commercial research license (model weights)
reviewed: 2026-05-27
acquired: 2026-05-27
overlaps: []
security_flags: [trust_remote_code]
source: unknown
---

## What it does

A unified vision-language grounding model from NVIDIA that predicts bounding boxes and point coordinates for visual grounding and object detection tasks. The key innovation is Parallel Box Decoding (PBD) — predicting complete bounding boxes as atomic units in a single forward pass rather than sequential token generation, achieving 12.7 boxes per second (10x faster than Qwen3-VL's textual approach). Architecture: Moon-ViT vision encoder with Qwen2.5 language decoder connected via MLP projector. Three inference modes: Fast Mode (MTP) for speed, Slow Mode (NTP) for precision, and Hybrid Mode that detects format irregularities and falls back to autoregressive generation. Handles general object detection, GUI element grounding, referring expression comprehension, OCR localization, layout understanding, and point-based localization. 3B parameter model.

## Assessment

Potentially relevant for spatial transcriptomics workflows — grounding arbitrary text descriptions to regions in H&E or fluorescence images. The model is available on HuggingFace (`nvidia/LocateAnything-3B`) with an interactive demo, and code is on GitHub (`NVlabs/Eagle/tree/main/Embodied`). However, this is a general-purpose vision-language model, not trained on histology or biomedical images. The blocker is evaluating whether it generalizes to tissue morphology and cell-type localization tasks without fine-tuning. Dataset listed as "incoming" suggests the project is still maturing.

## Mechanical details

Model: `huggingface.co/nvidia/LocateAnything-3B`. Code: `github.com/NVlabs/Eagle/tree/main/Embodied`. Demo: `huggingface.co/spaces/nvidia/LocateAnything`. Paper: arXiv:2605.27365 (Wang et al., 2026). Pilot trigger: when spatial transcriptomics pipeline includes an image grounding step, evaluate on a representative H&E image with tissue-type text queries.

- [2026-06-25 update] ECCV 2026 accepted. LoRA fine-tuning and visual prompt fine-tuning scripts released. Batch inference CLI (`batch_infer.py`) with optional `la_flash` sparse-range FlashAttention runtime for non-Hopper GPUs (A100, RTX 4090). On A100 4K image: `la_flash` cuts peak memory from 35 GB to 12 GB with comparable latency. License confirmed as NVIDIA non-commercial research (not Apache-2.0 as previously noted for code).

## Security

The model weights (`nvidia/LocateAnything-3B`) are released under NVIDIA's non-commercial research license — commercial use is prohibited except by NVIDIA and its affiliates, making this unsuitable for production or commercial pipelines without a separate agreement. The code repository (NVlabs/Eagle) is Apache 2.0, but the model incorporates Qwen2.5-3B-Instruct (Qwen Research License) and MoonViT-SO-400M (MIT), so the most restrictive upstream term (Qwen Research License) applies to derived deployments. NVIDIA explicitly labels this model as "for research and development only."

Loading the model requires `trust_remote_code=True`, which executes arbitrary Python from the HuggingFace model card at load time — verify the model revision is pinned and the remote code reviewed before use in any automated pipeline. No known CVEs or prompt-injection disclosures were identified at time of review; the model processes image and text inputs only and does not make network calls at inference time.
