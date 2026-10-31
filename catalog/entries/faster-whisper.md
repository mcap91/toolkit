---
name: faster-whisper
title: Faster Whisper
url: "https://github.com/SYSTRAN/faster-whisper"
category: framework
summary: "CTranslate2-based Whisper reimplementation — 4x faster than openai/whisper at same accuracy, int8 quantization, batched inference, VAD filtering, word-level timestamps; core ASR runtime for caption-less audio/video ingestion"
tags: [asr, whisper, transcription, audio, speech-to-text, ctranslate2, gpu]
workflows: []
reviewed: 2026-06-19
acquired: 2026-06-19
license: MIT
security_flags: []
supersedes: []
overlaps: []
source: unknown
---

## What it does

Reimplementation of OpenAI's Whisper speech-to-text model using CTranslate2 for fast inference. Key capabilities:

- **4x faster** than openai/whisper with identical accuracy, lower memory usage
- **Batched transcription**: 13 min audio in 16-17s with batch_size=8 on RTX 3070 Ti
- **Quantization**: int8 on both CPU and GPU — halves VRAM (2.9 GB vs 4.5 GB for large-v2)
- **Word-level timestamps** via built-in support
- **VAD filtering**: integrated Silero VAD to skip silence, configurable thresholds
- **Distil-Whisper compatible**: works with distil-large-v3 for even faster inference
- **No FFmpeg dependency**: uses PyAV for audio decoding (bundles FFmpeg libs)

Python API — `WhisperModel.transcribe()` returns a generator of timestamped segments.

## Assessment

The standard high-performance Whisper runtime. Massive community adoption — WhisperX, speaches, whisper-streaming, and 15+ other projects build on it. Benchmarks are solid and reproducible. SYSTRAN (the maintainer) is a commercial MT company with decades of NLP history — not a single-contributor hobby project.

In this catalog's context: this is the ASR engine for transcribing lectures, conference talks, and video tutorials that lack captions. Pairs with mcp-server-youtube-transcript (for captioned videos) to cover the full video-to-text pipeline.

GPU requirement note: CUDA 12 + cuDNN 9 required for current versions. RTX 50-series / Blackwell needs CUDA 12.8+ builds — verify ctranslate2 compatibility before deploying on newest hardware.

## Mechanical details

- **Install**: `pip install faster-whisper`
- **Python**: 3.9+
- **GPU**: CUDA 12 + cuDNN 9 (cuBLAS + cuDNN); CPU mode also supported with int8
- **Models**: auto-downloads from HuggingFace Hub by size name (`large-v3`, `turbo`, `distil-large-v3`)
- **Model conversion**: `ct2-transformers-converter` script for fine-tuned models
- **Docker**: works with `nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04`

## Security

- **License**: MIT — no restrictions
- **Dependencies**: ctranslate2, PyAV, huggingface_hub, tokenizers, Silero VAD (bundled ONNX)
- **Code quality**: benchmarks with reproducible methodology, large community test surface
- **Supply chain**: SYSTRAN (commercial NLP company), multiple contributors, 13k+ GitHub stars
- **Dangerous patterns**: none — pure inference library, no network services, no credential handling
- **Maintenance**: actively maintained, responsive to issues, regular releases