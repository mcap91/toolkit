---
name: penecho
title: PenEcho
url: "https://github.com/penecho/penecho"
category: framework
summary: "Local-first AI canvas: put a question, equation, diagram, or half-formed idea anywhere on an infinite canvas and PenEcho reads the marks and their spatial relationships and answers beside them. Node server + browser UI; pluggable LLM source (Claude CLI, Codex CLI, Kimi CLI, or OpenAI/Anthropic API). A Kimi Open Source Friend. AGPL-3.0-only."
license: AGPL-3.0-only
tags: [ai-canvas, handwriting-recognition, diagrams, whiteboard, local-first, claude-cli, codex-cli, agpl]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: [binds-all-interfaces-by-default, plaintext-credentials-at-rest, launches-local-cli-processes]
source: unknown
---

## What it does

PenEcho is an open-source "think with AI beyond the chat box" tool: a shared canvas where handwriting, equations, diagrams, and spatial context become part of the conversation. It runs as a local Node.js server with a browser canvas UI. A user draws or writes anywhere on a large (20,000×20,000) canvas and pauses; PenEcho sends only the relevant canvas crop and geometry to the selected model, which returns a movable draft (answers, hints, formulas, plots, diagrams) placed beside the marks and kept separate from confirmed ink until accepted. It supports images, sandboxed HTML/animation widgets, Mermaid flowcharts, image search, and local snapshot/PNG export. The model executor is pluggable: Claude Code CLI, Codex CLI, Kimi CLI, or an OpenAI-compatible / Anthropic-compatible API endpoint, each with a reasoning-effort control. It is an official member of Moonshot AI's "Kimi Open Source Friends" program.

## Mechanical details

- **Install:** `npm install -g penecho` (Node.js 20.3+), then `penecho configure` and `penecho`; or run from source with `npm install && npm start`; desktop app on GitHub Releases
- **Config:** `~/.penecho/config.env` (or `--config <file>`); keys include `AI_PROVIDER` (api/codex-cli/claude-cli), `AI_API_URL`/`AI_API_KEY`/`AI_API_MODEL`, `AI_EFFORT`, `HOST`/`PORT`
- **UI:** defaults to `http://localhost:3888`; CLI modes use isolated `claude -p` / `codex exec` turns with tools/agents/MCP disabled

## Security

AGPL-3.0-only: if you modify PenEcho and provide it to users over a network, you must offer them the corresponding source (a separate commercial license is available). PenEcho listens on `0.0.0.0:3888` by default so localhost and trusted-LAN access work immediately (`binds-all-interfaces-by-default`); each process starts undecided and requires either a shared six-digit code (stored only as a salted in-memory hash, rate-limited) or an explicit choice to run without one before granting a session — the code is described as a trusted-LAN guard, "not Internet-grade authentication." API credentials are stored in plaintext in the local `config.env` (owner-only permissions on POSIX, never sent to browser code) (`plaintext-credentials-at-rest`). The CLI executor modes launch a local `claude`/`codex`/`kimi` process per valid request and should be used only on the local machine or a trusted LAN, never exposed directly to the public internet (`launches-local-cli-processes`); PenEcho checks Host, client network, exact Origin, session cookie, and content type before launching. Optional request tracing writes request/response artifacts under `~/.penecho/logs/requests`.

## How to use it

npm install -g penecho
