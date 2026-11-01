---
name: pixel-agents
title: Pixel Agents
url: "https://github.com/pixel-agents-hq/pixel-agents"
category: framework
summary: "Animated pixel-art office that visualizes AI coding agents as characters — renders live activity (editing, reading, waiting for input) via Claude Code hooks or transcript heuristics; ships as VS Code extension and standalone CLI (npx pixel-agents); agent-agnostic HookProvider interface with Claude Code as reference integration; office layout editor, sub-agent/team visualization, areas mapped to workspace folders; React 19 + Canvas 2D; MIT"
tags: [visualization, claude-code, vscode-extension, hooks, pixel-art, agent-orchestration]
reviewed: 2026-09-26
acquired: 2026-09-26
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Pixel Agents renders AI coding agents as animated pixel-art characters in a virtual office. Each agent terminal gets its own character that walks to a desk, sits, types when editing, reads when searching, and raises a speech bubble when waiting for user input or permission. Ships two forms from one codebase:

- **VS Code extension** (Marketplace + Open VSX) — agents launch into VS Code terminals; characters render in the panel area.
- **Standalone CLI** (`npx pixel-agents`) — starts a local Fastify server serving the office as a browser app; works with tmux, remote, and non-VS Code workflows.

Supports sub-agents and Claude teammate visualization as separate characters with lifecycle tracking. Office layouts persist across sessions and can be imported/exported as JSON.

## Differentiators

- **Agent-agnostic architecture**: a typed `HookProvider` interface defines the integration boundary — adding a new AI tool is a single subdirectory. Claude Code is the reference; Codex, Gemini, Cursor on roadmap.
- **Dual detection**: hooks mode receives Claude events (SessionStart, PreToolUse, PermissionRequest, Stop); heuristic mode infers status by scanning JSONL session transcripts as fallback.
- **Areas**: named zones painted onto the office grid, mapped to workspace folders — new agents auto-seat in the area matching their folder.
- **Coexistence**: extension and standalone CLI run simultaneously with separate agent state but shared office layout, using per-server registration under `~/.pixel-agents/servers/`.

## Mechanical details

- **Install (extension)**: VS Code Marketplace or Open VSX. Panel opens beside terminal.
- **Install (CLI)**: `npx pixel-agents` or `npm install --global pixel-agents`. Binds `127.0.0.1` by default; `0.0.0.0` exposes to LAN.
- **Auth model**: CLI prints a `?token=` URL — bearer capability controlling hook install/remove permission. Untokened clients can view but not modify hooks.
- **Hook integration**: configures hooks in `~/.claude/settings.json`; persistent data in `~/.pixel-agents/`.
- **Stack**: React 19, Vite, Canvas 2D with pathfinding and character state machines. Bundled with esbuild (extension/CLI) and Vite (webview). Tests via Vitest + Node test runner; e2e via Playwright.
- **Asset system**: bundled characters (6), pets, furniture, floors, walls, carpets under `webview-ui/public/assets/`. External asset directories loadable via settings. Visual manifest editor at `scripts/asset-manager.html`.
- **Requirements**: Claude Code CLI, VS Code 1.105+ (extension) or Node 20+ (CLI), Windows/Linux/macOS.

## Security

- MIT license, no commercial restrictions.
- Token-based auth for hook management — treated as bearer capability; docs warn against sharing URLs.
- Binds localhost by default; explicit opt-in for network exposure.
- Does not modify Claude Code — reads hooks events and transcripts only.
- No eval patterns or credential handling observed in the README description.
- Active development with CI (GitHub Actions), Allure test reports, Playwright e2e coverage.