---
name: repowire
title: Repowire
url: "https://github.com/prassanna-ravishankar/repowire"
category: framework
summary: "Compelling multi-agent mesh for cross-repo coordination, but macOS/Linux only and default spawn config ships dangerous permission flags"
tags: [multi-agent, orchestration, mcp, claude-code, codex, gemini-cli, daemon, mesh, tmux, telegram, slack]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [spawn-ships-dangerously-skip-permissions, optional-external-relay, curl-pipe-sh-installer, macos-linux-only]
overlaps: [claude-peers-mcp]
source: unknown
---

## What it does

Repowire is a local daemon that gives named identities to agent sessions (Claude Code, Codex, Gemini CLI, OpenCode, Pi) running in different tmux windows or machines, then lets them exchange typed messages — non-blocking asks with explicit ack replies, fire-and-forget notifications, scheduled wake-ups, and broadcasts. A browser dashboard, Telegram, and Slack can participate as "service peers." A single session can be designated an orchestrator that dispatches work, polls status, and coordinates reviews across other agent peers. The daemon stores state in SQLite at `~/.repowire/state.db`; a hosted relay (repowire.io) is opt-in for remote access and cross-machine bridging.

## Assessment

The agent-to-agent ask pattern and orchestrator-peer model solve a real problem in multi-repo workflows: today you copy-paste between terminal windows to move context across agents. Repowire's approach — hooks + MCP tools wired automatically by `repowire setup`, with a named address book and lifecycle-tracked threads — is cleaner than ad-hoc file-based handoffs. However, several factors justify watching rather than piloting now: (1) **macOS/Linux only** (tmux requirement; no Windows support), which excludes this project's primary platform; (2) the default spawn configuration ships with `--dangerously-skip-permissions` (Claude Code), `--dangerously-bypass-approvals-and-sandbox` (Codex), and `--yolo` (Gemini) baked into `config.yaml`, which is a significant footgun even if these are user-configurable; (3) the architecture is explicitly in flux toward "session-native" in v0.14, meaning the API surface is still stabilizing; (4) the optional relay introduces an external service dependency and outbound WebSocket that needs trust evaluation. Watch for a stable v1.0 with safer spawn defaults and Windows/WSL support before adopting.

## Mechanical details

- **Transport per runtime:** Claude Code and Codex use hooks + MCP JSON tools; Gemini CLI uses normalized BeforeAgent/AfterAgent hook events; OpenCode uses a TypeScript plugin + WebSocket; Pi uses the Repowire extension path.
- **Daemon:** Python 3.10+ process bound to `127.0.0.1:8377`; SQLite for durable state; launchd (macOS) or systemd --user (Linux) service.
- **Install:** `curl | sh` installer detects uv/pipx/pip in order; `repowire setup` auto-wires detected runtimes.
- **MCP surface:** Exposes ask, notify, broadcast, schedule, and jobs tools; optional Streamable HTTP MCP at `/mcp` (localhost-only, bearer-auth, off by default).
- **Relay:** Opt-in outbound WebSocket to `wss://repowire.io` with an API key; not required for local routing.
- **Key commands:** `repowire peer list/new`, `repowire schedule self`, `repowire telegram start`, `repowire slack start`, `repowire doctor`, `repowire update`.
- **Overlap with catalog:** Overlaps with "Claude Peers MCP" (agent communication via MCP), but Repowire is substantially broader in scope (daemon, jobs, schedules, human surfaces, relay).

## Security

- **License:** MIT — no restrictions.
- **spawn-ships-dangerously-skip-permissions:** The documented default `config.yaml` sets `claude-code: "claude --dangerously-skip-permissions"`, `codex: "codex --dangerously-bypass-approvals-and-sandbox"`, and `gemini: "gemini --yolo"` as the spawn commands. Any workflow that uses `repowire peer new` with these defaults removes all agent safety prompts. Users must consciously override these to safer invocations.
- **optional-external-relay:** When `relay.enabled: true`, Repowire establishes an outbound WebSocket to `wss://repowire.io` and authenticates with an API key. Traffic routing, data retention, and key management at repowire.io are not audited here.
- **curl-pipe-sh-installer:** The quickstart installs via `curl ... | sh` from the repo's raw GitHub URL, which is a supply-chain risk if the repo or CDN is compromised. `uv tool install repowire` from PyPI is a safer alternative.
- **Local daemon auth:** `daemon.auth_token` is available but not enforced by default; the MCP HTTP endpoint is off by default and localhost-only when enabled.
- **Spawn path allowlist:** `spawn.allowed_paths` restricts which directories can be targeted by `repowire peer new`, which limits blast radius if the daemon is abused.
- **No Windows support:** macos-linux-only is a hard platform limitation, not a security issue, but relevant for deployment decisions.
