---
name: gufo
title: gufo
url: https://github.com/gufo-org/gufo
category: framework
summary: Source-built local inference engine for AMD Strix Halo hardware (Ryzen AI Max+ 395, Radeon 8060S/gfx1151, up to 128GB unified memory) — serves GGUF models (documented against Qwen3.8-Flash-Next and Qwen3.8-27B) over an OpenAI-compatible API with MTP or DFlash2 speculative decoding and vision via a separate mmproj file; Anthropic-style /v1/messages endpoint does not yet support tool calls or streaming; MIT, requires a ROCm toolchain to build
tags:
  - local-inference
  - strix-halo
  - amd
  - rocm
  - gguf
  - speculative-decoding
  - mtp
  - openai-compatible
  - qwen
  - vision
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - strata
  - polystrata
  - llama-cpp-adaptive-kv-streaming
  - qwen38-27b-200k-on-16gb
  - llamastash
  - halogen-flash-server
license: MIT
security_flags:
  - new-project
  - requires-manual-source-build
  - unauthenticated-api-by-default
source: reddit
source_url: https://www.reddit.com/r/LocalLLM/comments/1wxn8r7/daily_driving_qwen_38_flash_instead_of_claude/
---

## What it does

gufo is an inference engine built specifically for AMD's Strix Halo APUs (Ryzen AI Max+ 395 with Radeon 8060S, gfx1151, up to 128GB unified memory). It serves GGUF-format models — in practice Unsloth's quantized builds of Qwen3.8-Flash-Next and Qwen3.8-27B are the models documented in its own setup guides — over an OpenAI-compatible HTTP API, with speculative decoding via either a shared multi-token-prediction (MTP) head bundled with some GGUF releases or a separate DFlash2 draft model. v0.8.0 added an OpenAI Responses endpoint; its Anthropic-style `/v1/messages` endpoint (the shape Claude Code expects) does not yet support tool calls or streaming, per the project's own `docs/SERVER.md`. Vision input goes through a separate `mmproj` projector file; the server checks only that some projector is present for a given model, so a model row can advertise image support even when the matching `mmproj-BF16.gguf` is missing — an image request then fails at request time rather than at startup.

## Mechanical details

- No prebuilt binaries are documented; built from source with CMake + Ninja against a C++20 compiler. The qualified toolchain is GCC 15.3 + ROCm 7.2.3 (system install under `/opt/rocm`), or ROCm 10.x via AMD's pip-installable `rocm` SDK inside a Python venv (`rocm-sdk init`) for a build that doesn't need a system ROCm install.
- CLI: `gufo serve llm --model <gguf> --served-model-name <name> --speculative mtp --mtp-model <gguf>` or `--speculative dflash2 --dflash-model <gguf>`, plus `--top-p`, `--top-k`, `--reasoning-effort`.
- `gufo diagnose` checks the build/runtime environment.
- A community fork (Chiakai-Chang) adds native Windows support (no WSL) via TheRock's ROCm SDK.
- MIT license for gufo's own code; adapted third-party code keeps its own licenses, tracked in NOTICE and THIRD_PARTY_NOTICES.md.

## Security

MIT licensed, source-available. Building it requires a working ROCm toolchain — a non-trivial, hardware- and GCC-version-sensitive build (the project's own docs note GCC 16+ breaks ROCm clang HIP compiles in `<format>`, and no prebuilt binaries are documented). Model weights are a separate download, typically from Hugging Face, and are not bundled with the engine. No authentication is documented on the API port; binding it to a non-localhost address exposes it without credentials unless the operator adds one.

## Usage notes

- A deployment guide runs gufo as a "generic" backend behind LlamaStash's proxy alongside the closed-source Halogen engine on the same Strix Halo box, serving Pi, OpenCode, and Claude Code through one endpoint (source: https://gist.github.com/deepu105/d0b321f3256edf67ebd85e747c0010b9).
