---
name: tailscale-mobile-approval
title: Tailscale Mobile Approval Workflow
url: "https://tailscale.com/"
category: agent-pattern
summary: "Pattern for approving Claude Code permission prompts from a mobile device via Tailscale SSH + tmux — attach to a persistent session from any device on the tailnet, review diffs and approve remotely"
tags: [tailscale, remote-access, tmux, mobile, workflow, claude-code]
reviewed: 2026-06-23
acquired: 2026-06-23
license: N/A
security_flags: []
overlaps: [remote-control]
source: unknown
---

## What it says

A workflow for approving Claude Code permission prompts from an Android phone (or any remote device) using Tailscale SSH and tmux, as an alternative to Claude's built-in `/remote` feature.

### Setup

1. **Enable Tailscale SSH on the host**: `tailscale up --ssh` (macOS: also enable Remote Login in System Settings)
2. **Create a persistent tmux session** in the project directory: `tmux new -s claude-session`, then launch `claude` inside it
3. **Connect from mobile**: SSH into the host via Tailscale IP or MagicDNS name (`ssh username@100.x.y.z`), then `tmux attach -t claude-session`
4. Review diffs and approve/reject prompts directly from the mobile terminal

### Key advantage over /remote

Available on-demand at any time — not predetermined like `claude /remote`. Just SSH in and attach to the existing tmux session whenever needed.

## Assessment

Practical operational pattern that solves a real pain point: wanting to check on and approve long-running Claude Code sessions from a phone without pre-planning. Requires Tailscale on both devices (free for personal use) and a terminal app on the phone (Termius, Blink, etc.).

The original content mentions `--dangerously-skip-permissions` as a "pro tip" — this is actively harmful advice and should not be followed. The value is in the Tailscale SSH + tmux attachment pattern, not in bypassing safety controls.

## What to adopt

The tmux + Tailscale SSH pattern is sound and composable with existing workflows. No new tools needed beyond Tailscale (already common) and tmux.

## Security

- The pattern itself is secure — Tailscale provides encrypted, authenticated connections via WireGuard
- **Do not use `--dangerously-skip-permissions`** despite it being suggested in the source material — this bypasses all safety controls
- Tailscale MagicDNS avoids exposing SSH to the public internet