---
name: sana-wm
title: SANA-WM (NVIDIA)
url: https://github.com/NVlabs/Sana
category: framework
summary: 2.6B-parameter open-source text+image-to-video diffusion transformer world model from NVIDIA/MIT (Haoyi Zhu, Song Han, Enze Xie, et al.) — given one image, a text prompt, and a 6-DoF camera trajectory, generates an explorable, controllable, minute-long 720p video on a single GPU via Hybrid Linear Attention (Gated DeltaNet + periodic softmax attention) and an LTX-2 refiner; Apache-2.0 code and weights, trained in 15 days on 64 H100 GPUs
tags:
  - world-model
  - video-generation
  - text-to-video
  - image-to-video
  - diffusion-transformer
  - camera-control
  - nvidia
  - open-weights
reviewed: 2026-10-30
acquired: 2026-10-30
license: Apache-2.0
security_flags: []
overlaps: []
source_url: https://www.instagram.com/reel/De2LjyNNS4H/
source: instagram
---

## What it does

SANA-WM is a 2.6-billion-parameter text+image-to-video (TI2V) diffusion transformer "world model" from NVIDIA and MIT researchers (Haoyi Zhu, Song Han, Enze Xie, et al.), described in "SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer" (arXiv:2605.15178, May 2026). Given one input image, a text prompt, and a 6-DoF camera trajectory, it generates an explorable, controllable, minute-long (60s) 720p video on a single GPU. It uses Hybrid Linear Attention — frame-wise Gated DeltaNet (GDN) recurrent blocks combined with softmax attention at every 4th layer (block indices 3, 7, 11, 15, 19) — for memory-efficient long-context video generation, paired with an LTX-2 refiner for high-fidelity decoding. Trained on roughly 213K public video clips with metric-scale pose supervision, completing in 15 days on 64 H100 GPUs. NVIDIA reports 36x higher throughput than the nearest open-source baseline; a distilled variant using NVFP4 quantization runs on a single consumer RTX 5090.

## Mechanical details

- Code: github.com/NVlabs/Sana (same repo also hosts SANA, SANA-1.5, SANA-Sprint, SANA-Video, Sol-RL)
- Install: `git clone https://github.com/NVlabs/Sana.git && cd Sana && ./environment_setup.sh sana`
- Weights: `Efficient-Large-Model/SANA-WM_bidirectional` and `Efficient-Large-Model/SANA-WM_streaming` on Hugging Face — Apache-2.0, ungated, load directly
- Project page: nvlabs.github.io/Sana/WM/

## Security

Apache-2.0 license covering code and weights; no gating or token required to download. Runs locally once weights are downloaded; no network calls documented at inference time.
