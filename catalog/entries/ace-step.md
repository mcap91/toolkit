---
name: ace-step
title: ACE-Step 1.5
url: https://github.com/ace-step/ACE-Step-1.5
source_url: https://www.instagram.com/reel/De369jptIw-/
source: instagram
category: framework
summary: Open-source local music-generation foundation model (successor to the original ACE-Step) — a hybrid architecture where a language model plans a song blueprint (metadata, lyrics, captions via chain-of-thought) that guides a Diffusion Transformer decoder; generates a full song in under 2 seconds on an A100 and under 10 seconds on an RTX 3090, runs locally on under 4GB VRAM (base models; the newer 4B-parameter XL variants need 12-20GB+), supports 10-second to 10-minute durations, batch generation of up to 8 songs, cover generation, repaint/edit, track separation, vocal-to-BGM, reference-audio-guided generation, LoRA personalization from a handful of songs, and 50+ languages; ships a Gradio UI, REST API, Python API, CLI, and a C++/GGML VST3 plugin; co-led by ACE Studio and StepFun; MIT, with a usage disclaimer about copyright/cultural-sensitivity risk in generated output.
tags:
  - music-generation
  - text-to-music
  - diffusion-transformer
  - audio
  - local-inference
  - gradio
  - lora
  - open-source
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

ACE-Step 1.5 is an open-source music foundation model aimed at bringing commercial-grade music generation to consumer hardware. Its architecture pairs a language model (LM), which acts as a planner that expands a simple user query into a full song blueprint — scaling from short loops to 10-minute compositions while generating metadata, lyrics, and captions via chain-of-thought — with a Diffusion Transformer (DiT) decoder that the LM's blueprint guides during synthesis. The LM/DiT alignment is trained with intrinsic reinforcement learning using only the model's own internal signals, without an external reward model or human-preference data, per the project's abstract. Beyond straight text-to-music synthesis, it supports cover generation, selective repaint/edit of part of a track, stem/track separation, multi-track layering, automatic vocal-to-backing-track (Vocal2BGM) generation, reference-audio-guided style control, metadata control (duration, BPM, key/scale, time signature), audio-understanding (extracting BPM/key/caption from an existing track), automatic lyric-timestamp (LRC) generation, and one-click LoRA personalization — a user-specific style trained from as few as 8 songs in about an hour on a 12GB-VRAM RTX 3090.

## Mechanical details

- **Performance**: under 2 seconds per full song on an A100, under 10 seconds on an RTX 3090 (0.5-10s on A100 depending on "think mode" and diffusion-step count); supports 10-second to 600-second (10-minute) output; batch generation up to 8 songs at once.
- **Hardware tiers**: base 2B DiT models run on as little as ~6GB VRAM (LM disabled, INT8 quantization, full CPU offload); the newer 4B-parameter "XL" DiT variants (`acestep-v15-xl-base/sft/turbo`, released 2026-04-02) need ≥12GB VRAM with offload or ≥20GB without, for higher audio quality (~9GB bf16 weights vs ~4.7GB for the 2B models); an LM companion model (0.6B/1.7B/4B, built on Qwen3) adds query rewriting, audio understanding, and composition capability at increasing VRAM cost.
- **Install**: `uv sync` after `git clone https://github.com/ACE-Step/ACE-Step-1.5.git`; launches a Gradio UI (`uv run acestep`, port 7860) or REST API server (`uv run acestep-api`, port 8001); portable pre-bundled packages exist for Windows and macOS. Supports CUDA, Apple MPS, AMD ROCm, Intel XPU, and CPU backends.
- **Other interfaces**: a standalone C++/GGML VST3 plugin for DAW integration, a Python API, and an interactive CLI wizard.
- **Benchmark tooling**: `profile_inference.py` measures LM/DiT/VAE timing per device/configuration in single-run or configuration-matrix mode.
- Supports 50+ languages for lyrics with structure/style control; claims quality "between Suno v4.5 and Suno v5" on the project's own evaluation.
- MIT license; the README carries a usage disclaimer flagging unintentional copyright infringement from stylistic similarity and inappropriate cultural-element blending as acknowledged risks, placing responsibility on the user to verify originality, disclose AI involvement, and obtain permissions when adapting protected styles.

## Security

Local-inference tool — model weights download from Hugging Face on first run; no network service is exposed by default beyond the local Gradio/REST ports the user starts. No code-execution or credential-handling risk pattern observed beyond standard model-weight-download trust (verify checksums/source if downloading weights in a security-sensitive environment). MIT licensed for the code; generated-output risk (copyright/cultural-sensitivity) is a content-policy concern the project's own README flags, not a software vulnerability.

## Sources

- [GitHub: ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) — README: abstract, features, performance figures, model zoo, license, disclaimer
- [Instagram reel](https://www.instagram.com/reel/De369jptIw-/) — named "ACE-Step 1.5" as one of five repos that "turn Claude into an entire game studio," citing a soundtrack generated "in under 10 seconds" (catalog source; no link given in the reel itself)