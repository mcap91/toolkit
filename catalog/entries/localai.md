---
name: localai
title: LocalAI
url: "https://github.com/mudler/localai"
category: framework
summary: "Open-source local AI engine — drop-in OpenAI/Anthropic/ElevenLabs API compatibility across 60+ backends (llama.cpp, vLLM, whisper.cpp, stable-diffusion, MLX, etc.); supports LLMs, vision, voice, image, video on any hardware (NVIDIA/AMD/Intel/Apple/Vulkan/CPU); multi-user auth with quotas, built-in agents with MCP/RAG/tool use, distributed cluster mode, fine-tuning UI, WebRTC realtime audio; MIT"
tags: [local-inference, openai-compatible, multi-modal, self-hosted, llm-server, mcp, agents, tts, asr, image-generation]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: [ollama, open-webui]
source: unknown
---

## What it does

Self-hosted AI engine that runs any model locally with drop-in API compatibility for OpenAI, Anthropic, and ElevenLabs endpoints. Modular backend architecture — each backend (llama.cpp, vLLM, SGLang, transformers, whisper.cpp, diffusers, MLX, etc.) is pulled as a separate OCI image only when needed.

### Modalities

- **Text generation** — llama.cpp, vLLM, SGLang, transformers, MLX
- **Speech-to-text** — whisper.cpp, parakeet.cpp (NeMo port), vibevoice.cpp, voxtral.c
- **Text-to-speech** — Piper (60 voices / 42 languages), vibevoice.cpp (voice cloning)
- **Image generation** — stable-diffusion, diffusers, Ideogram4
- **Vision** — VLM support, llama.cpp video input
- **Object detection** — rf-detr.cpp, locate-anything.cpp
- **Audio** — realtime speech-to-speech API with WebRTC, voice activity detection (Silero-VAD), audio event classification (ced.cpp)

### Platform features

- **Multi-user** — API key auth, OIDC, per-user quotas with predictive analytics, usage attribution
- **Agents** — built-in autonomous agents with tool use, RAG, MCP support, skills, SSE streaming, Agent Hub
- **Distributed mode** — horizontal scaling with PostgreSQL + NATS, VRAM-aware routing, autoscaling, prefix-cache-aware routing
- **Fine-tuning** — in-UI fine-tuning with TRL, auto-export to GGUF, on-the-fly quantization
- **Biometric backends** — voice-detect.cpp (speaker recognition), face-detect.cpp (face detection/recognition/anti-spoofing) — native C++/ggml, no Python at inference

## Differentiators

- **Modular backend gallery** — 60+ backends as OCI images pulled on demand; no monolithic install
- **Hardware breadth** — NVIDIA CUDA 12/13, AMD ROCm, Intel oneAPI/SYCL, Apple Silicon Metal, Vulkan, NVIDIA Jetson L4T, CPU-only
- **Native C/GGML backends** — team-built parakeet.cpp, voxtral.c, vibevoice.cpp, rf-detr.cpp, etc. with no Python/onnxruntime at inference
- **apex-quant** — per-tensor/per-layer MoE quantization recipe producing GGUFs matching Q8_0 quality on stock llama.cpp

## Mechanical details / What to adopt

- Install: Docker (`localai/localai:latest`), macOS DMG, or build from source
- Load models: `local-ai run ollama://gemma:2b`, `local-ai run huggingface://...`, or from model gallery
- API endpoint: `http://localhost:8080` — OpenAI-compatible `/v1/chat/completions`, `/v1/embeddings`, etc.
- Interactive chat: `local-ai chat --model <name>`
- GPU auto-detection: automatic backend selection based on available hardware
- Kubernetes: Helm chart available

## Security

MIT licensed. Privacy-first — no data leaves local infrastructure. Multi-user auth via API keys and OIDC. Per-user quotas and usage tracking. PII redaction tier via privacy-filter.cpp. Backend OCI images signed with cosign. macOS DMG is unsigned (requires `xattr -d` quarantine removal).