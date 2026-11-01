---
name: tuios
title: TUIOS — Terminal UI OS
url: "https://github.com/Gaurav-Gosain/tuios"
category: cli-tool
summary: "Terminal multiplexer and window manager built in Go on Charm's Bubble Tea v2 — vim-like modal interface, BSP/scrolling/master-stack tiling, 9 workspaces, kitty graphics protocol passthrough (flicker-free video, sixel experimental), daemon mode with session resurrection, vim-style copy mode with 10K-line scrollback, tape scripting DSL for automation, command palette, app launcher, SSH server mode, web terminal mode; event-driven rendering (zero idle CPU); MIT"
tags: [terminal-multiplexer, tui, go, bubble-tea, tiling, kitty-graphics, tmux-alternative, vim, daemon, session-management, automation]
reviewed: 2026-09-18
acquired: 2026-09-18
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

TUIOS is a terminal multiplexer combining tmux session management with i3/sway-style tiling window management. Built in Go on Charm's Bubble Tea v2 and Lipgloss v2.

Core capabilities:
- Modal interface: Window Management mode (vim-like navigation) and Terminal mode; Ctrl+P command palette
- Tiling: BSP (binary space partitioning) with spiral layout, scrolling layout (niri-style infinite horizontal strip), master-stack layout; preselection for controlling split placement
- 9 workspaces with independent isolation and instant switching
- Kitty graphics: full image rendering with flicker-free video (image ID reuse + mode 2026 sync); sixel passthrough experimental; supports mpv --vo=kitty
- Daemon mode with detach/reattach (like tmux), session resurrection across daemon restarts/reboots
- Vim-style copy mode over 10,000-line scrollback with search, yank, mouse wheel scrolling, interactive scrollbar
- Tape scripting DSL for recording and replaying terminal workflows; headless execution against daemon sessions
- App launcher (Alt+Space, frecency-ranked with desktop app icons), aggregate view across all workspaces, multifocus broadcast typing
- TOML config, customizable keybindings, hooks (shell commands on window events), themes

Installable via Homebrew, AUR, Nix, Go, Docker, or install script.

## Security

- License: MIT
- SSH server mode available for remote terminal multiplexing
- Multiple install methods including curl-pipe install script