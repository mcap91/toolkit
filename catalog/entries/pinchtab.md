---
name: pinchtab
title: PinchTab
url: "https://github.com/pinchtab/pinchtab"
category: framework
summary: "Standalone Go HTTP server (~16MB single binary) that gives AI agents control of Chrome via a CLI and HTTP API: token-efficient text extraction (~800 tokens/page), headless/headed profiles, multi-instance orchestration, an MCP server, and a dashboard. Local-first by default (binds 127.0.0.1, sensitive endpoints off). MIT."
license: MIT
tags: [browser-automation, ai-agents, chrome, cdp, go, http-api, mcp, headless]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: [browser-use]
security_flags: [privileged-control-surface, curl-pipe-sh-install, network-exposure-if-misconfigured]
source: unknown
---

## What it does

PinchTab is a standalone HTTP server, distributed as a ~16MB self-contained Go binary, that gives AI agents direct control over Chrome. Agents navigate pages, extract structured content, and interact with the DOM through a CLI (`pinchtab nav/snap/click/fill/press/text`) or an HTTP API, using stable accessibility element refs rather than coordinates. It emphasizes token efficiency (~800 tokens/page via text extraction, which it benchmarks as cheaper than screenshots). Features include headless and headed modes, named browser profiles with persistent sessions (cookies/logins/extensions), multi-instance orchestration with isolated profiles, external-Chrome attach (advanced), site audits and visual comparison (`pinchtab audit`/`compare`), an MCP server, a dashboard, and a background daemon. Windows support is best-effort; macOS/Linux are the primary tested targets.

## Mechanical details

- **Install:** `npm install -g pinchtab`; `brew install pinchtab/tap/pinchtab`; `curl -fsSL https://pinchtab.com/install.sh | bash`; or Docker (`pinchtab/pinchtab`, published bound to `127.0.0.1:9867`)
- **Run:** `pinchtab daemon install` (background daemon), `pinchtab server` (foreground control plane), or `pinchtab bridge` (single instance; recommended on Windows)
- **Default endpoint:** `http://localhost:9867`; profiles/instances/tabs managed via REST (`/profiles`, `/instances/start`, `/tabs/{id}/...`)

## Security

MIT licensed; no telemetry, local-first by default. The server binds `127.0.0.1`, disables sensitive endpoint families and `attach` by default, and restricts browsing to a local-only allowlist (IDPI) until the operator explicitly widens it. The project's own documentation flags the dashboard, HTTP API, MCP server, and remote CLI integrations as privileged operator control surfaces not designed for untrusted users, multi-tenant use, or public-internet exposure (`privileged-control-surface`); any non-local deployment (binding beyond loopback, publishing ports, remote bridges) is an operator-secured advanced setup requiring tokens, TLS, and network boundaries (`network-exposure-if-misconfigured`). One documented install path pipes a remote script to a shell (`curl … | bash`, `curl-pipe-sh-install`); npm/Homebrew/Docker paths avoid it. Optional CloakBrowser stealth support launches a user-supplied binary that is not bundled. Enabling headed profiles lets an agent act inside authenticated sessions.

## How to use it

npm install -g pinchtab
