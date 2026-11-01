---
name: lm-studio
title: LM Studio
url: "https://lmstudio.ai/"
category: framework
summary: "Desktop application for downloading, managing, and running local LLMs with GUI chat, OpenAI/Anthropic-compatible API server (localhost:1234), MLX and llama.cpp engines, built-in model search with VRAM fit estimation, GPU offload controls, voice transcription, and Bionic agentic assistant; JS/Python SDKs, MCP client support, headless daemon (llmster), LM Link encrypted remote inference; free for personal and commercial use; macOS/Windows/Linux"
tags: [local-inference, llm, api-server, openai-compatible, mlx, llama-cpp, gui, model-management, voice, agent, mcp-client, privacy, desktop]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [on-prem-llm-deployment-architecture]
license: Proprietary (free for personal and commercial use)
security_flags: [closed-source]
source: unknown
---

## What it does

LM Studio is a desktop application (v0.4.23, August 2026) that lets users download GGUF-quantized LLMs from Hugging Face, manage them locally, and run inference entirely on their own hardware. It ships two inference backends — llama.cpp (CPU/NVIDIA/AMD) and MLX (Apple Silicon) — switchable per model.

Key capabilities:

- **Model discovery and management**: Built-in search across Hugging Face GGUF repositories with up-front VRAM/RAM fit estimation before download. Per-model parameter tuning (temperature, top-p, context length) and GPU layer offload controls via GUI.
- **Chat interface**: Conversation history, file/image attachments, vision model support, and real-time local voice transcription (audio never leaves device).
- **Bionic agent**: Built-in agentic assistant for document creation/editing, coding tasks, automations, and computer control. Works with local or frontier open models (GLM 5.2, Kimi K3, DeepSeek V4 Pro via ZDR cloud).
- **Local API server**: Serves OpenAI-compatible endpoints (`/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, `/v1/models`) and Anthropic-compatible endpoints at `localhost:1234`. Tool calling supported. Any OpenAI SDK-based tool (LangChain, LlamaIndex, Continue.dev, Claude Code) works by pointing its base URL.
- **Developer tooling**: JavaScript and Python SDKs, CLI tool (`lms`), headless daemon (`llmster`) for server deployments, MCP client support.
- **LM Link**: Encrypted remote inference — run models on a GPU server while the API appears at localhost on a laptop.

## Mechanical details

Requires macOS 14+ (Apple Silicon), Windows 10+, or Linux. Models stored locally in a configurable directory. GPU memory allocation adjustable from 10–100% of VRAM. Context window configurable up to model limits (trades VRAM for context length). Enterprise tier available for organizations.

Privacy-first: all local inference stays on-device. Cloud features (frontier model access via Bionic) use Zero Data Retention (ZDR) — no data stored server-side.

## Security

Proprietary closed-source application. Free for personal and commercial use. No telemetry details publicly documented. Local inference data stays on-device. Cloud ZDR policy for any server-routed requests. The closed-source nature means the privacy claims cannot be independently verified from source code.

## How to use it

Download from https://lmstudio.ai/
