---
name: colibri
title: colibri
url: https://github.com/JustVugg/colibri
category: framework
summary: Pure-C, zero-dependency inference engine that runs very large open-weight mixture-of-experts (MoE) LLMs (up to ~2.8T parameters) on ordinary hardware by keeping the small per-token-active dense part resident in RAM/VRAM and streaming the inactive routed experts from disk; ships a `coli` CLI, OpenAI- and Anthropic-compatible HTTP API, an MCP server for AI-assisted setup, and a non-generative "System One" classification endpoint backed by three purpose-built decision models
tags:
  - local-inference
  - moe
  - expert-offloading
  - cpu-inference
  - vulkan
  - cuda
  - metal
  - openai-compatible
  - anthropic-compatible
  - mcp-server
  - decision-model
  - safetensors
  - pure-c
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - strata
  - polystrata
  - gufo
  - halogen-flash-server
  - cpubrrr
  - large-moe-consumer-hardware
license: apache-2.0
security_flags:
  - new-project
  - unauthenticated-by-default
source: web
source_url: https://github.com/JustVugg/colibri
---

## What it does

colibri is a from-scratch C inference engine (one .c file per model family, no BLAS, no Python at runtime) for running mixture-of-experts LLMs whose routed experts change on every token but whose dense/shared layers do not. It keeps the dense part and a learned cache of frequently-used experts resident in RAM or VRAM and reads the remaining experts from disk on demand through a per-layer LRU cache plus a usage-learned pinned set (`.coli_usage`, updated every turn). Ten engines run chat/tool-calling language models (GLM-5.2/5.3, GLM-5.3-Flash, Kimi K3, DeepSeek V4/V4.1 Flash, MiMo-V2.6 Flash/Pro, Qwen3.6/Qwen3-Coder/Qwen3.8-Flash-Next, the dense Qwen3.8-27B, and OLMoE), one draws images (Qwen-Image-2.1), and three answer classification-style questions instead of chatting (Laya, GLiNER2.5-Decide, and Clef, the last of which also chats). A one-step setup script (`start-here.sh`/`START-HERE.bat`) profiles the host's RAM, disk, CPU and GPU, recommends a model that fits, downloads it with resumable progress, and builds or downloads the matching engine (CPU, Vulkan for any GPU vendor, CUDA for NVIDIA, Metal for Apple Silicon).

## Mechanical details

- Model weights use a custom int4/int8 safetensors-derived container (not GGUF); conversion commands from each model's original FP8/bf16 release are documented per model family.
- `coli` CLI subcommands: `chat`, `web`, `serve`, `plan` (shows where weights will live: VRAM/RAM/disk), `doctor` (read-only readiness check), `tune` (measures and saves the fastest safe settings for the host), `convert`, `status`, `stop`, `logs`, `mcp` (starts an MCP server exposing hardware-detect/recommend/install/start/stop/check tools).
- `coli serve`/`web` expose an OpenAI-compatible API (`/v1/chat/completions`, `/v1/completions`, `/v1/models`) and an Anthropic-compatible `/v1/messages`, so Claude Code and the Anthropic SDKs point at it unmodified; the repo also claims base-URL-only compatibility with TypeSafe's Jev API clients.
- `POST /v1/systemone` answers typed yes/no, multiple-choice, or scored questions about a given text/JSON state by returning a calibrated probability per allowed option instead of generating free text, either by scoring token probabilities on any chat model colibri runs or natively on Laya, GLiNER2.5-Decide, or Clef.
- Multiple concurrent conversations share one process via `coli serve --kv-slots N` (up to 16), each with its own KV cache, decoded together.
- `COLI_MODEL_MIRROR` reads a model from a second local drive to add disk bandwidth; `COLI_NUMA=1` spreads resident weights across a multi-socket host's memory controllers; a cluster mode can run routed experts on other machines.
- CI checks every engine's output against the reference Hugging Face `transformers` implementation and, for the Vulkan path, against the CPU path on a software driver.
- Apache 2.0, by Vincenzo Fornaro; each model keeps the license its own authors gave it (e.g. GLM-5.2 weights are MIT per Z.ai; Qwen-Image-2.1 is non-commercial-use-only).

## Security

The engine and setup scripts are fully open source (Apache 2.0) and build from source or download prebuilt binaries per platform; model weights are separate third-party Hugging Face downloads, each under its own upstream license. The local HTTP server (`coli serve`/`web`) accepts any non-empty API key when started without `COLI_API_KEY` set, i.e. it enforces no real authentication by default — a risk if the port is exposed beyond localhost. `docs/AI_SETUP.md` is written to instruct an AI coding assistant through unattended setup and explicitly tells it to ask the user before downloading a model or installing a system package, implying the authors anticipated agentic/unattended use of the installer. The project is new and solo-maintained (started as a one-person project), with benchmark numbers crowdsourced via GitHub issues rather than independently verified.