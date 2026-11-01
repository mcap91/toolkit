---
name: herdr
title: Herdr
url: "https://github.com/ogulcancelik/herdr"
category: cli-tool
summary: "Terminal-based agent multiplexer (single Rust binary) — real terminal panes for many coding agents at a glance, detach/reattach across terminals or SSH with sessions surviving restarts, tmux-style keyboard + mouse, a plugin marketplace, and a pure socket API that lets agents themselves spawn panes and wait on each other; dual-licensed AGPL-3.0 / commercial"
tags: [terminal-multiplexer, agent-orchestration, tui, rust, session-persistence, socket-api, plugins]
reviewed: 2026-07-09
acquired: 2026-07-09
license: AGPL-3.0-or-later
security_flags: [curl-pipe-sh-installer, dual-license-commercial-required, windows-beta]
overlaps: []
source: unknown
---

## What it is

Herdr is a terminal-native multiplexer purpose-built for running multiple AI coding agents at once. It shows every agent's state (blocked / working / done) as real terminal views rather than a wrapped interpretation, and ships as one Rust binary (no Electron) that runs in whatever terminal you already use.

## What it does

- Detach and reattach: agents keep running after you detach (`ctrl+b q`), reattach from any terminal or over SSH, and sessions survive restarts.
- Agents as users: a pure socket API lets agents themselves spawn panes, read output, and wait on each other (a documented "agent skill" covers this usage).
- Input: tmux-style prefix keybindings plus first-class mouse (click, drag, split).
- Plugins: a marketplace extends panes and workflows.

## Install and build

Install via `curl -fsSL https://herdr.dev/install.sh | sh`, Homebrew (`brew install herdr`), `mise`, or a Windows beta PowerShell one-liner; then run `herdr` where the work lives. Build from source with `cargo build --release` (`just test`, `just check`). Docs live at herdr.dev/docs (quick start, concepts, supported agents, keyboard, configuration, session state, remote, integrations, plugins, socket API). The project states it is built full-time in the open and funded via sponsorship.

## Security

Dual-licensed: AGPL-3.0-or-later (open source) or a commercial license for organizations that cannot comply with AGPL. The primary install path is a `curl | sh` script from herdr.dev (review before running). Windows support is beta. The socket API is designed so that local agents can programmatically spawn and control terminal panes — the intended capability rather than a defect, but it does mean local processes can drive panes.

## Usage notes

- Community consensus (128-comment Reddit thread): Herdr is among the most frequently recommended tools for managing multiple Claude Code sessions. Users report using a "Design/Triage" + "Orchestrator" tab pattern. Other mentioned tools: Orca, cmux, Supacode. Common advice: cap at 2-3 parallel sessions, use strict naming conventions (repo-task), put branch/model info in statusline. The "which pane needs me" problem persists even with good tooling.
