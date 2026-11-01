---
name: omnigent
title: Omnigent
url: "https://github.com/omnigent-ai/omnigent"
category: framework
summary: "Open-source 'meta-harness' giving a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and custom YAML agents — swap/combine harnesses, mix vendors in one session, drive from terminal/browser/phone, run in cloud sandboxes (Modal/E2B/Daytona/etc.), and enforce approval/spend/tool policies; Python 3.12+, degraded native Windows mode"
tags: [meta-harness, orchestration, multi-agent, claude-code, codex, cursor, sandboxing, policies, mobile]
reviewed: 2026-07-09
acquired: 2026-07-09
license: ""
security_flags: [curl-pipe-sh-installer, license-not-stated-in-readme, degraded-windows-sandbox, runs-multiple-coding-agents]
overlaps: [frontier]
source: unknown
---

## What it is

Omnigent is an open-source meta-harness: a common orchestration layer over multiple coding agents (Claude Code, Codex, Cursor, OpenCode, Hermes, Pi) and custom agents defined in YAML. It lets you swap or combine harnesses without rewriting, mix vendors in one session (e.g. ask one agent to review another's work), and use any model via a first-party API key, a Claude/ChatGPT subscription, or an OpenAI/Anthropic-compatible gateway (OpenRouter, LiteLLM, Ollama, vLLM, Azure).

## What it does

- Multi-device: sessions follow you across terminal, browser (local web UI at `:6767`), phone, and a macOS desktop app; messages, sub-agents, terminals, and files stay in sync.
- Collaboration: share a live session, co-drive a running session (`omnigent attach`), or fork it (`omnigent run --fork`); multi-user accounts via `OMNIGENT_AUTH_ENABLED=1`, invite links, optional OIDC.
- Cloud sandboxes: run sessions in disposable Modal, Daytona, Islo, E2B, CoreWeave, Kubernetes, OpenShell, Boxlite, or Databricks sandboxes; deploy the server via docker compose, Render/Railway/Fly/HF Spaces/Cloudflare/Databricks Apps, or reach a laptop server via Cloudflare tunnel / Tailscale.
- Policies: server-, agent-, and session-level policies (stricter session rules checked first) that allow/block/ask before shell commands or file writes, cap tool calls, and enforce spend budgets.
- Example agents: Polly (multi-agent coding orchestrator delegating to worktree sub-agents and cross-vendor reviewers) and Debby (two-headed Claude+GPT brainstorming partner).

## Install and platforms

`curl -fsSL .../install_oss.sh | sh`, or `uv tool install omnigent` / `pip install omnigent` / Homebrew. Needs Python 3.12+, git, Node 22+ (for npm-installed harnesses), tmux (native terminal wrappers), and bwrap on Linux (mandatory OS sandbox; macOS uses seatbelt). Windows runs natively in a degraded mode: the server, web UI, and SDK-based harnesses (claude-sdk/cursor/codex) work under a Windows Job Object, but the native tmux/PTY terminal wrappers and the bwrap/seatbelt filesystem + network sandbox and L7 egress proxy are unavailable (use Linux/macOS or WSL). Update with `omni upgrade`.

## Security

The README describes the project as open-source but does not state an SPDX license in the fetched content — verify the LICENSE file before adoption. The primary install path is a `curl | sh` bootstrap. On Linux/macOS agents are wrapped in bwrap/seatbelt OS sandboxes with an optional L7 egress proxy; on Windows the Job Object contains the process tree and enforces resource limits but does not isolate filesystem or network. The policy engine (approval gates, tool caps, spend budgets) is the main built-in control surface for constraining orchestrated agents. Because it launches and runs multiple third-party coding agents with their own credentials, credential and egress exposure is inherited from those harnesses.