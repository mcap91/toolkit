---
name: llmfit
title: llmfit
url: "https://github.com/AlexsJones/llmfit"
category: cli-tool
summary: "Terminal tool that detects local hardware (RAM/CPU/GPU/VRAM) and scores LLM models across fit, speed, quality, and context to report which will run well locally; ships an interactive TUI and a JSON-emitting CLI for agent/script use."
tags: [llm-inference, hardware-detection, model-selection, rust, tui, ollama, llama-cpp, mlx, local-llm]
reviewed: 2026-07-22
acquired: 2026-07-22
license: MIT
security_flags: [curl-pipe-sh-install, community-submitted-benchmark-data]
overlaps: []
source: unknown
---

## What it does

llmfit is a Rust terminal tool that right-sizes LLM models to the local machine. It detects hardware (RAM, CPU, GPU/VRAM, and backend), then scores every model in its catalog across four dimensions — memory fit, estimated speed, quality, and context length. It ships an interactive TUI (default) and a classic CLI mode, and handles multi-GPU setups, MoE architectures, and dynamic quantization selection. Supported local runtime providers are Ollama, llama.cpp, MLX, Docker Model Runner, and LM Studio. Speed estimates come from a memory-bandwidth model grounded in runtime sampling and community measurements; `llmfit info` reports the inputs behind each estimate plus commands to verify it on the local machine. A benchmarking feature (`llmfit bench`) measures real tok/s and time-to-first-token against a running provider — results are saved locally and can be contributed back as PRs to a community leaderboard directly from the TUI.

## Assessment

Packaged through many channels (Scoop, a Homebrew tap and homebrew-core, MacPorts, uv/pip, Docker/Podman, a curl installer, and `cargo build` from source), indicating broad packaging maintenance. Windows release binaries are Authenticode-signed via SignPath.io using a SignPath Foundation certificate, with signing restricted to GitHub Actions artifacts built from this repository and approved by the maintainer (@AlexsJones). The README documents sister projects (sympozium, llmserve, llama-panel) and an alternative (llm-checker, noted to lack MoE support). The JSON output of `llmfit recommend --json` and `docker run … recommend | jq` positions the tool for agent and script consumption.

## Mechanical details

- **Install:** `scoop install llmfit` (Windows); `brew install AlexsJones/llmfit/llmfit` or `port install llmfit` (macOS/Linux); `curl -fsSL https://llmfit.axjns.dev/install.sh | sh` (add `-s -- --local` for `~/.local/bin` without sudo); `uv tool install -U llmfit` / `uvx llmfit`; `docker run ghcr.io/alexsjones/llmfit`; or `cargo build --release` from source
- **TUI:** bare `llmfit` (pass `--tui` under Docker)
- **CLI:** `llmfit fit` (ranked table), `recommend --json` (top picks as JSON), `info "<model>"` (per-model fit analysis + verify commands), `bench` (measure tok/s and TTFT), `doctor` (hardware-detection report for bug reports)
- Docker/Podman invocation prints JSON from `recommend` for `jq` querying
- **Contributing:** run `cargo fmt` before PRs; new models can be added locally (no rebuild) or to the built-in catalog

## Security

License is MIT. Primary adoption surfaces observed in the README: (1) a `curl -fsSL … | sh` install path that pipes a remote script to a shell — offered with a `--local` variant to install without sudo; the Scoop/Homebrew/MacPorts/uv package-manager paths avoid the pipe-to-shell pattern. (2) The community-benchmark feature merges user-submitted measurements into the fit table via PRs, so the estimates shipped for a given hardware profile depend on community-contributed data reviewed at merge time. Windows binaries are Authenticode-signed via SignPath, with signing limited to GitHub Actions builds from this repository. The README states the program contacts external services only on explicit user action (model downloads, runtime-provider queries, the leaderboard). No eval/shell-injection patterns are documented in the README; CI beyond the release-signing pipeline was not verified. `security_flags` reflect the curl-pipe install option and the reliance on community-submitted benchmark data.