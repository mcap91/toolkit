---
name: aperture-cli
title: Aperture CLI
url: "https://github.com/tailscale/aperture-cli"
category: cli-tool
summary: "Tailscale's CLI launcher for coding agents (Claude Code, Gemini CLI, Codex, Copilot CLI, OpenCode) preconfigured for Aperture — manages installation, config, env vars, and model/provider routing; Go, alpha"
tags: [agent-launcher, tailscale, multi-agent, developer-tools, networking]
reviewed: 2026-06-23
acquired: 2026-06-23
license: UNLICENSED
security_flags: [alpha-software, no-stated-license]
overlaps: []
source: unknown
---

## What it does

Aperture CLI is a Go-based launcher that manages installation, configuration, and environment variables for multiple coding agents, preconfigured to work with Tailscale's Aperture service. On first run it connects to `http://ai` (or prompts for an Aperture endpoint).

Supported agents: Claude Code, Gemini CLI, OpenCode, Codex, GitHub Copilot CLI, Claude Cowork.

**Bridge mode**: Lets the CLI reach an Aperture endpoint through an embedded Tailscale node — useful when the full Tailscale client isn't installed, when using another VPN, or when switching tailnets.

## Assessment

Interesting infrastructure for teams using Tailscale to route AI agent traffic through a centralized Aperture endpoint. The bridge mode (embedded Tailscale node) solves a real problem for machines where installing full Tailscale is impractical. However, the tool is alpha, has no stated license in the README, and is tightly coupled to Tailscale's Aperture product.

Relevant as an operational pattern: centralized model routing + agent launcher for teams managing multiple coding agents. Not directly adoptable without Aperture infrastructure.

## Mechanical details

```bash
go install github.com/tailscale/aperture-cli/cmd/aperture@latest
# or build from source
make build
```

Run `aperture` to launch the TUI, configure endpoints and bridges, then select and launch agents.

Flags: `-version` (print version), `-debug` (show env vars before launch).

## Security

- **License**: No SPDX license stated in README — significant adoption blocker
- **Alpha status**: Under active development, may change significantly without notice
- **Tailscale dependency**: Requires Aperture endpoint; bridge mode embeds a Tailscale node
- **Supply chain**: Tailscale-maintained (reputable company), but alpha quality
- **Network**: Routes agent traffic through Aperture endpoint — all LLM API calls go through this proxy