---
name: orca-ade
title: Orca (ADE)
url: "https://github.com/stablyai/orca"
category: cli-tool
summary: "Agent Development Environment for running parallel coding agents (Claude Code, Codex, OpenCode, Pi, 30+ others) side-by-side — each in its own git worktree, tracked in one place; Ghostty-class terminal splits, Design Mode (Chromium click-to-prompt), annotate AI diffs, GitHub/Linear integration, SSH worktrees, mobile companion (iOS/Android), CLI for scripting; Electron, MIT"
tags: [agent-orchestration, worktrees, parallel-agents, claude-code, codex, terminal, design-mode, github, linear, mobile, ssh, diff-review]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: MIT
security_flags: [telemetry-opt-out]
source: unknown
---

## What it does

Orca is an Agent Development Environment (ADE) that runs multiple coding agents in parallel, each in its own isolated git worktree, with results tracked in a unified UI. It works with any CLI agent — Claude Code, Codex, OpenCode, Pi, Grok, Cursor, Devin, and 30+ others.

Key capabilities:

- **Parallel worktrees**: fan one prompt across five agents, each in its own worktree. Compare results and merge the winner.
- **Terminal splits**: Ghostty-class terminals with WebGL rendering, infinite splits, scrollback surviving restarts.
- **Design Mode**: click any UI element in a real Chromium window to send its HTML, CSS, and a cropped screenshot into the agent prompt.
- **Diff annotation**: drop comments on any diff line and ship them back to the agent. Review, edit, and commit without leaving Orca.
- **GitHub & Linear native**: browse PRs, issues, and project boards in-app. Open a worktree from any task.
- **SSH worktrees**: run agents on remote machines with full file editing, git, terminals, auto-reconnect, and port forwarding.
- **Mobile companion**: iOS/Android apps to monitor and steer agents from phone — notifications when agents finish, follow-ups from anywhere.
- **Orca CLI**: script workflows with `orca worktree create`, `snapshot`, `click`, `fill`.
- **Computer Use**: agents operate desktop apps and visible UI when a workflow needs real interaction.

## Mechanical details

Desktop app for macOS (Apple Silicon + Intel), Windows, Linux (AppImage). Also available via Homebrew. Mobile apps pair with desktop via relay server (included in repo under `cloud/`). Ships daily. VS Code editor with autosave. Quick-open search across worktrees, files, agents, commands. Account switcher with Claude/Codex usage tracking and rate-limit resets.

## Security

MIT licensed. Collects anonymous usage telemetry with opt-out available (documented in privacy & telemetry docs). Windows builds signed via SignPath.io. The tool runs agents using the user's own CLI subscriptions — no API keys stored by Orca itself.

## How to use it

brew install --cask stablyai/orca/orca
