---
name: halogen-flash-server
title: Halogen (halogen-flash-server)
url: https://github.com/peonist-ai/halogen-flash-server
category: framework
summary: Closed-source, hardware-specific local inference server for running Qwen3.8-Flash-Next on AMD Strix Halo (gfx1151) silicon — distributed as a container image behind an open deployment-tooling repo; serves OpenAI- and Anthropic-compatible APIs on one port, supports MTP speculative decoding, and can route small models to the Ryzen AI NPU alongside the main model; the engine binary itself is proprietary, licensed by Peonist, LLC, separately from the public deployment scaffolding
tags:
  - local-inference
  - strix-halo
  - amd
  - closed-source
  - docker
  - openai-compatible
  - anthropic-compatible
  - qwen
  - npu
  - speculative-decoding
  - mtp
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - gufo
  - strata
  - polystrata
  - qwen38-27b-200k-on-16gb
  - llamastash
license: proprietary
security_flags:
  - closed-source-binary
  - new-project
  - unauthenticated-internal-port
source: reddit
source_url: https://www.reddit.com/r/LocalLLM/comments/1wxn8r7/daily_driving_qwen_38_flash_instead_of_claude/
---

## What it does

Halogen (distributed as `halogen-flash-server`) is a local inference server built exclusively for running the Qwen3.8-Flash-Next model family on AMD Strix Halo (gfx1151) hardware. The GitHub repository is deployment scaffolding only — container orchestration files, entrypoint scripts, benchmarking utilities, and documentation; the inference engine itself ships as a closed-source binary inside the container image and is not visible or patchable from the repo. It serves both an OpenAI-compatible and an Anthropic-compatible API on one port, with configurable reasoning-effort levels (none/low/medium/xhigh, overridable per request) and MTP speculative decoding at a configurable depth. It can also run small models on the device's Ryzen AI NPU alongside the main Flash model, selecting between them by the model name in each request. Weights (~118GB) are distributed separately on Hugging Face as a derivative of Qwen3.8-Flash-Next, under that base model's license.

## Mechanical details

- Distributed as a Docker/Podman image (`ghcr.io/peonist-ai/halogen-flash-server`); a typical launch mounts the GPU devices (`/dev/kfd`, `/dev/dri`) and a local weights directory.
- Checkpoint format is a native `.hgn` file plus an n-gram lookup table rather than GGUF.
- Configuration is via `HALOGEN_*` environment variables (e.g. `HALOGEN_CTX`, `HALOGEN_MTP_DEPTH`, `HALOGEN_REASONING_EFFORT`, `HALOGEN_NPU_MODELS`); the project's own `AGENTS.md` documents two ports — an internal `HALOGEN_PORT` (8730) with no authentication, meant to stay unpublished, and `HALOGEN_API_PORT` (8731) as the only port meant for clients.
- A project contributor stated on a public forum that the engine is closed for now, with work ongoing toward opening the harness so third parties can add their own model packs; no inbound license exists for code contributions to the engine itself.

## Security

The inference engine binary is closed-source and proprietary, licensed separately by Peonist, LLC (per the repo's own LICENSE.md/EULA and trademark notice) from the public deployment-tooling repository; the public repo does not contain code that can be inspected, audited, or patched for the engine itself. The project's own documentation flags its internal port (8730) as unauthenticated and states it must not be published — a misconfiguration risk if that guidance is missed when deploying the container. Model weights are a separate Hugging Face download under the base Qwen model's license.

## Usage notes

- A deployment guide runs Halogen as a "generic" backend behind LlamaStash's proxy alongside gufo on the same Strix Halo box, with LlamaStash's `integrations` command pointing Claude Code's `ANTHROPIC_MODEL`/`ANTHROPIC_SMALL_FAST_MODEL` at a Halogen-served preset (source: https://gist.github.com/deepu105/d0b321f3256edf67ebd85e747c0010b9).
