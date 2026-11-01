---
name: free-claude-code
title: Free Claude Code
url: "https://github.com/Alishahryar1/free-claude-code"
category: framework
summary: "Drop-in proxy routing Claude Code (Anthropic Messages API) and Codex (OpenAI Responses API) traffic to 24 provider backends — per-model-tier routing, Admin UI, Discord/Telegram bot wrapper, voice-note transcription via local Whisper or NVIDIA NIM; Python/FastAPI, MIT"
tags: [proxy, claude-code, codex, model-routing, llm-gateway, multi-provider]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: [litellm, openrouter]
source: unknown
---

## What it does

FastAPI proxy server that intercepts Claude Code's Anthropic API calls (`/v1/messages`, `/v1/models`) and Codex's OpenAI Responses API calls (`/v1/responses`), routing them to any of 24 provider backends. Includes launcher scripts (`fcc-claude`, `fcc-codex`) that configure environment variables and launch the real CLI tools pointed at the local proxy.

**24 providers:** NVIDIA NIM, OpenRouter, Google AI Studio (Gemini), DeepSeek, Mistral La Plateforme, Mistral Codestral, OpenCode Zen, OpenCode Go, Vercel AI Gateway, Hugging Face Inference Providers, Cohere, GitHub Models, Wafer, Kimi, MiniMax, Cerebras, Groq, SambaNova, Fireworks AI, Cloudflare, Z.ai, LM Studio, llama.cpp, Ollama.

**Per-tier routing:** `MODEL_OPUS`, `MODEL_SONNET`, `MODEL_HAIKU` can each target a different provider, with `MODEL` as fallback. Codex uses the `MODEL` default through `fcc-codex`.

## Differentiators

- **Dual-protocol proxy** — handles both Anthropic Messages and OpenAI Responses protocols in one server, normalizing thinking blocks, tool calls, token usage metadata, and provider errors into the shape each client expects
- **Native model picker support** — Claude Code's `/model` picker works through the proxy's `/v1/models` endpoint; Codex gets a generated local model catalog
- **Admin UI** — local-only web UI at `/admin` for editing proxy settings, validating changes, and checking provider health
- **Discord/Telegram bot wrapper** — runs remote Claude Code sessions with streaming progress, reply-based conversation branches, `/stop` and `/clear` commands
- **Voice-note transcription** — optional integration with local Whisper (CPU/CUDA) or NVIDIA NIM Riva gRPC for voice messages in Discord/Telegram
- **Request optimizations** — answers trivial Claude Code probes locally to save latency and quota
- **Auto-compaction** — sets `CLAUDE_CODE_AUTO_COMPACT_WINDOW` to 190K tokens

## Mechanical details / What to adopt

- **Install:** `curl -fsSL ... | sh` (macOS/Linux) or `irm ... | iex` (Windows PowerShell); installers also install Claude Code and Codex when missing
- **Run:** `fcc-server` starts proxy, `fcc-claude` / `fcc-codex` launch clients
- **VS Code:** set `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` in extension settings; Codex uses `~/.codex/config.toml`
- **JetBrains ACP:** edit `installed.json` with proxy env vars
- **Architecture:** FastAPI routes + service layer, provider transports (OpenAI-chat and Anthropic-messages), SSE normalization, per-provider rate limiting
- **Extending:** add OpenAI-compatible providers via `OpenAIChatTransport`, Anthropic-compatible via `AnthropicMessagesTransport`

## Security

MIT licensed. Local-only Admin UI (loopback access). Auth token configurable but optional — when blank, proxy injects `fcc-no-auth` sentinel. Installer runs `curl | sh` which carries standard pipe-to-shell risk. Proxy sits in MITM position for all API traffic — all prompts and responses pass through it. No credential storage beyond `~/.fcc/.env`. CI pipeline includes Ruff linting, type checking (ty), and pytest.