---
name: helm-session-manager
title: Helm (gamepad-driven multi-agent session manager)
url: https://github.com/PetePeter/helm
category: cli-tool
summary: Electron desktop app (Windows .exe, macOS universal .dmg) for running and switching between multiple AI coding CLI sessions (Claude Code, Copilot CLI, Codex CLI, etc.) as embedded terminals (node-pty + xterm.js), controlled with a game controller or keyboard; includes an opt-in per-session prompt-cache keep-warm heartbeat (auto-off after 8 hours), a Helm MCP server so agents can control sessions programmatically, cross-machine "Fleet" pairing with deny-by-default per-peer allow-lists, a Telegram bot for remote control, a per-folder plan graph, pattern-matched auto-fire on terminal output, scheduled prompts, a project memory knowledge graph with scheduled "dreaming" maintenance, and session mission/todo/ETA tracking with compaction handover notes; an Android companion app is sideloaded via APK. No LICENSE file in the repository. Single-repo project.
tags:
  - claude-code
  - codex
  - copilot-cli
  - session-manager
  - electron
  - gamepad
  - multi-agent
  - mcp-server
  - telegram-bot
  - prompt-caching
  - cache-warming
  - remote-control
  - android
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - cold-cache-session-resume
  - multi-session-management-strategies
  - cloud-session-context-repo
license: unspecified
security_flags:
  - no-license-file
  - network-listener-feature-fleet-mode
source: reddit
source_url: https://www.reddit.com/r/ClaudeCode/comments/1x1ybwb/best_way_to_handle_cold_cache_hits_you_overpay_5x/
---

## What it does

A session manager for running several AI coding CLIs side by side, built as an Electron desktop
app. Each CLI (Claude Code, Copilot CLI, Codex CLI, or others configured by the user) runs as an
embedded terminal via `node-pty` + `xterm.js` — no external windows. Primary control surface is a
game controller (Xbox or generic/DirectInput gamepad): D-pad switches sessions and auto-selects
the terminal, triggers spawn new sessions for configured CLIs, and the right stick scrolls the
buffer. Keyboard shortcuts duplicate every binding. An Android companion app (sideloaded APK,
paired over Bluetooth LE or local network) mirrors session control, chat, plans, and artifacts,
with voice calls and notifications.

Relevant to prompt-cache cost management: a per-session opt-in toggle sends a short heartbeat
before a supported CLI's prompt cache expires, turning itself off automatically after 8 hours
(`docs/session-freeze.md` covers prompt-cache status, session freezing, and keep-warm controls).

Other features: a Helm MCP server (starts automatically with the app) exposing tools so Claude
Code or other agents can send text between sessions, read terminal output, and manage plans
programmatically; a Telegram bot with one forum topic per session for remote control
(`/sessions`, `/status`, `/spawn`, `/send`, `/close`), with activity-gated output batching; a
per-working-directory plan graph (planning/ready/coding/review/blocked/done states) with
dependency-aware chips surfaced near the terminal; a regex pattern matcher that auto-fires
scripted input sequences on PTY output, with per-session cooldowns; one-time and recurring
scheduled prompts; LLM-directed notification routing between sessions, Telegram, or OS toasts;
session recovery across app crashes with a 30-day recycle bin keyed to each session's resume id;
a cross-machine "Fleet" mode pairing two Helm instances over LAN (off by default; TCP 47474 +
mDNS discovery; 6-digit pairing code confirmation; deny-by-default per-peer tool allow-lists with
a rolling 7-day audit log; `helm_restart`, `session_close`, and `session_group_close` are never
remotely invocable); a per-project memory knowledge graph with auto-save/auto-recall and a
scheduled "dreaming" maintenance run that prunes and merges memories; and per-session mission/
todo/ETA tracking plus a compaction handover note carried across a session's own `/compact`.

Quick start is `npm install && npm start`. Current macOS builds are not notarized (first launch
needs a Gatekeeper override). Surfaced in an r/ClaudeCode comment linking to a specific commit
demonstrating the session-freeze (cache-cooldown) feature, in a thread about handling cold
prompt-cache hits.

## Security

No LICENSE file is present in the repository — terms for reuse or redistribution are
unspecified. The MCP server and Fleet mode both open local/network control surfaces: the MCP
server lets any connecting agent send text and manage plans in every open session, and Fleet
(disabled by default) opens a TCP listener plus mDNS once a user enables it, mitigated by its
pairing-code confirmation and deny-by-default per-peer allow-list. The Telegram bot and Android
companion both relay session control over the network/Bluetooth. Review the MCP server's and
Fleet's trust model before enabling either on a machine running sessions with repo write access.
