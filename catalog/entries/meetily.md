---
name: meetily
title: Meetily
url: "https://github.com/Zackriya-Solutions/meetily"
category: framework
summary: "Privacy-first, self-hosted AI meeting assistant (Zackriya Solutions) that captures, transcribes, and summarizes meetings entirely on the local machine. Tauri desktop app (Rust backend, Next.js frontend) with live Whisper/Parakeet transcription, mic+system audio capture, and summaries via Ollama (local) or optional Claude/Groq/OpenRouter/OpenAI endpoints. MIT (Community Edition); a paid PRO tier exists."
license: MIT
tags: [meeting-notes, transcription, whisper, parakeet, local-first, tauri, ollama, privacy]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: [optional-cloud-llm-egress]
source: unknown
---

## What it does

Meetily is a privacy-first AI meeting assistant that runs on the local machine, capturing meetings, transcribing them in real time, and generating summaries without sending data to the cloud by default. It is a single self-contained Tauri application with a Rust backend and Next.js frontend, for macOS, Windows, and Linux. Transcription runs locally with Whisper or Parakeet models; it captures microphone and system audio simultaneously with ducking/clipping prevention, and supports GPU acceleration (Metal/CoreML on Apple Silicon; CUDA on NVIDIA; Vulkan on AMD/Intel). It can import existing audio files to transcribe or re-transcribe with a different model/language. Summaries use a configurable AI provider — Ollama (local, recommended) or Claude, Groq, OpenRouter, or a custom OpenAI-compatible endpoint. The open-source Community Edition is MIT; a separate paid "Meetily PRO" (different codebase) adds higher-accuracy models, custom templates, advanced exports, auto-join, and planned speaker diarization.

## Mechanical details

- **Install:** Windows `…x64-setup.exe`, macOS `meetily_<ver>_aarch64.dmg`, both from GitHub Releases; Linux builds from source
- **Build from source:** needs Rust and Node.js; e.g. `git clone …/meeting-minutes && cd frontend && pnpm install && ./build-gpu.sh`
- Borrows code from whisper.cpp, Screenpipe, and transcribe-rs; uses NVIDIA's Parakeet model (ONNX conversion by istupakov)

## Security

MIT licensed (Community Edition). By design all transcription and storage are local; recordings, transcripts, and models stay on the device. The summarization provider is configurable — the default/recommended Ollama runs locally, but selecting Claude, Groq, OpenRouter, or a custom OpenAI-compatible endpoint sends meeting content to that external service (`optional-cloud-llm-egress`). The README markets privacy/compliance benefits; those are vendor claims, and GDPR-compliance features are attributed to the separate paid PRO edition. Capturing system audio records all participants — recording-consent obligations apply.

## How to use it

desktop installers (Windows .exe / macOS .dmg) from GitHub Releases
