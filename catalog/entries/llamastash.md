---
name: llamastash
title: LlamaStash
url: https://github.com/llamastash/llamastash
category: framework
summary: Terminal-native manager and daemon for local LLM runtimes — TUI + CLI, routes llama.cpp (GGUF) or any declared OpenAI-compatible server behind one proxy endpoint (default http://127.0.0.1:11435/v1), auto-discovers models cached by Hugging Face/Ollama/LM Studio, and patches Pi/OpenCode/Claude Code configs to route through it; MIT, Rust, single core maintainer (Deepu K Sasidharan)
tags:
  - local-inference
  - llm-manager
  - proxy
  - openai-compatible
  - tui
  - cli
  - rust
  - model-management
  - generic-backend
  - cuda
  - claude-code-integration
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - lm-studio
  - nvidia-pair
  - nemo-switchyard
  - qwen38-27b-200k-on-16gb
  - gufo
  - halogen-flash-server
license: MIT
security_flags:
  - new-project
  - model-downloads-third-party
  - single-maintainer
  - config-patching-other-tools
source: reddit
source_url: https://www.reddit.com/r/LocalLLM/comments/1wxn8r7/daily_driving_qwen_38_flash_instead_of_claude/
---

## What it does

LlamaStash is a terminal-native manager for local LLM runtimes — a TUI and CLI built around a daemon that launches, supervises, and routes backend inference servers behind one OpenAI-compatible proxy endpoint (`http://127.0.0.1:11435/v1` by default). It auto-discovers models already cached by Hugging Face, Ollama, and LM Studio instead of requiring its own model directory. Built-in support covers llama.cpp (GGUF) directly; a "generic" backend (added in v0.5.0) lets a user declare any other OpenAI-compatible server — binary, flags, env vars, and a readiness path — in `config.yaml`, and LlamaStash then manages that process's lifecycle the same way it manages llama.cpp: reserving a port, waiting on readiness, routing the proxy to it, and stopping it with a grace-period SIGTERM. This is the mechanism documented for folding third-party engines such as Halogen and gufo into the same daemon and proxy. v0.6.0 added per-preset idle TTL, automatic unloading of idle models to make room for a request that doesn't fit, optional preload-at-boot, and CUDA support (`llamastash init` installs llama.cpp's CUDA build and runtime libraries).

An `integrations` subcommand patches other agent tools' configuration to route through the LlamaStash proxy: it writes a provider entry into Pi's `models.json`, patches OpenCode's config with the proxy URL and model list, and for Claude Code writes a standalone env script (`~/.config/llamastash/claude-code.sh`, without touching `~/.claude/settings.json` directly) that sets `ANTHROPIC_MODEL` and `ANTHROPIC_SMALL_FAST_MODEL` to a LlamaStash-served model id — sourcing that script before `claude` points Claude Code at a local model instead of Anthropic's API.

## Mechanical details

- Install: `curl -fsSL https://llamastash.dev/install.sh | sh` (macOS/Linux), `irm https://llamastash.dev/install.ps1 | iex` (Windows), a Homebrew tap, `cargo install llamastash`, or the AUR (`yay -S llamastash`). `llamastash init` on first run installs llama-server and writes the config.
- Config lives at `~/.config/llamastash/config.yaml`; a `model_paths:` list lets it scan non-default Hugging Face cache locations.
- `llamastash favorites add <model>` then `llamastash integrations <tool>...` registers one entry per model/preset combination (`<id>@<preset>`) with each connected tool.
- Written in Rust; developed by Deepu K Sasidharan. MIT license.

## Security

MIT licensed; GitHub activity shows a single core maintainer. Downloads model weights from Hugging Face and other third-party hosts on request — standard supply-chain exposure for any model-pulling tool. The proxy binds to localhost by default. The `integrations` command writes into other tools' configuration files and, for Claude Code, a separate env script meant to be sourced into the shell — review what it writes before sourcing it, as with any tool that patches another CLI's configuration or environment.

## Usage notes

- A deployment guide pairs LlamaStash's generic backend with the closed-source Halogen engine and with gufo on the same AMD Strix Halo box, serving Pi, OpenCode, and Claude Code through one proxy (source: https://gist.github.com/deepu105/d0b321f3256edf67ebd85e747c0010b9).
- Already referenced for an agentic-coding benchmark pairing LlamaStash with the Pi harness to run Qwen 3.8 27B/Flash-Next locally against Claude Opus on a Strix Halo laptop — see the `qwen38-27b-200k-on-16gb` entry's Usage notes.
