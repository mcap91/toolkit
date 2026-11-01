---
name: starnet
title: StarNet
url: https://starnetos.com/
category: framework
summary: Local-first, MIT-licensed multi-agent harness (Tauri/Rust desktop shell + Node.js sidecar) for Windows/macOS that runs several AI agents in parallel with a live pixel-art visualization of agent state, delegation (team.dispatch), chat integration (Telegram, Discord, Slack, Signal, Matrix), persistent memory, BYOK model backends (OpenRouter, Anthropic, OpenAI, Google, Ollama, Claude Code CLI), and per-job/per-day spend budgets enforced against a real cost ledger
tags:
  - agent-harness
  - multi-agent
  - local-first
  - desktop-app
  - tauri
  - byok
  - orchestration
  - cost-ledger
  - open-source
  - windows
  - macos
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags: []
overlaps: []
source: web
source_url: https://starnetos.com/
---

## What it does

StarNet is a local-first AI agent harness: its own Node.js sidecar process runs the agent loop, executes tools, routes work between agents, schedules runs, enforces budgets, and keeps memory — it does not sit on top of another agent framework. The desktop shell is built with Rust/Tauri (vanilla JS frontend) and communicates with the Node sidecar over local HTTP/NDJSON/SSE.

Agents are organized visually as a pixel-art space station: each occupied "bay" is a running agent, and placed "gear" (a signal dish, a filing cabinet, a workbench) grants that room's agents web access, file access, or a terminal respectively. An "overseer" agent can delegate to specialist workers via a `team.dispatch` call; each worker runs independently with its own tools and returns its result to the lead. Users direct the crew from a "COMMS" interface and can interrupt the current task with Stop.

Model backends are bring-your-own-key: OpenRouter, Anthropic, OpenAI, a ChatGPT sign-in, the Claude Code CLI, Gemini, Grok, Kimi, Mistral, DeepSeek, Groq, or fully local Ollama. Chat/control surfaces extend to Telegram, Discord, Slack, Signal, and Matrix. The project also ships a terminal CLI (`starnet`) for headless station management and can import agents from the OpenClaw and Hermes Agent projects.

Spend is bounded by a per-job budget (default $2, $50 ceiling), optional per-day caps, a default $25/day global limit (adjustable or disposable), and a limit on unattended jobs per day — all enforced against a real cost ledger, not advisory. Local data (station state, transcripts, memory, ledgers) stays on the user's machine; network/model calls happen only when an agent runs or a network tool/connector is explicitly granted.

## Mechanical details

- Current stable version: v0.14.1; ~1.6k GitHub stars, ~338 forks, 16,000+ commits on main (as of October 2026)
- Repo: `https://github.com/androoAGI/starnet` (code MIT-licensed; branding/artwork excluded)
- Run from source: Node.js 18+, `git clone https://github.com/androoAGI/starnet.git && cd starnet && npm install && npm start`, opens station UI at `http://localhost:8787`
- Installers: Windows `.EXE` (Authenticode-signed) and macOS `.DMG` (Apple Silicon and Intel, notarized); Linux has no public installer target
- Headless station management via a `starnet` terminal CLI
- Desktop shell: Rust/Tauri; sidecar: Node.js; frontend: vanilla JavaScript; local HTTP/NDJSON/SSE between them
- Delegation primitive: `team.dispatch`, called by an overseer agent to hand work to a specialist worker

## Security

- **License**: MIT (code); branding/artwork separately owned, not licensed
- **Dependency health**: Node.js 18+ sidecar, Tauri/Rust desktop shell — standard, actively maintained toolchains
- **Code quality signals**: Active repo (16,000+ commits), full-history secret scanning reported in its test pipeline
- **Supply chain**: Windows installer is Authenticode-signed (SmartScreen may still warn while certificate reputation builds); macOS DMG is Developer ID-signed and notarized (a Gatekeeper trust failure is flagged as reportable, not expected)
- **Dangerous patterns**: API keys stored in OS keychain when using the installer (never in the frontend); running from source stores keys in a local file instead, a weaker-than-keychain posture; grants web/file/terminal capability to agents on explicit placement of "gear," and tool execution is described as consent-based with "Task Briefs" requiring explicit approval for ambiguous tasks
- **Maintenance**: Active as of October 2026 (v0.14.1 stable, source build ahead of it)
