---
name: claude-code-cross-session-pitfalls
title: Claude Code Cross-Session Communication Pitfalls
category: reference
summary: "Documentation of Claude Code's cross-session SendMessage behavior — agents in one CLI session can discover and message stale sessions via ListAgents/SendMessage, triggering context consumption and cache invalidation across all open sessions; mitigations: crossSessionInbound: refuse in settings (preferred), or deny SendMessage/ListAgents (but this also disables subagent and team messaging)"
tags: [claude-code, cross-session, sendmessage, listagents, settings, pitfall, token-consumption, configuration]
reviewed: 2026-09-25
acquired: 2026-09-25
license: N/A
security_flags: []
overlaps: []
source: unknown
---

## What it does

Documents a Claude Code behavior where agents in one CLI session discover and message other open sessions on the same machine (r/ClaudeCode, Sep 2026).

**The problem:** A Claude session starting work on a feature used SendMessage to contact 6+ other open sessions to "claim" file paths and check for conflicts. This triggered all stale sessions, consumed tokens across all of them (one empty session hit 60K tokens on Opus medium), and burned through usage quotas.

**Root cause:** SendMessage serves three purposes — subagent communication, agent-team messaging, and cross-session messaging. All use the same tool.

**Mitigations (in settings.json):**
1. **Preferred:** `"crossSessionInbound": "refuse"` — refuses inbound messages from other sessions while preserving subagent and team messaging
2. **Nuclear:** `"permissions": { "deny": ["SendMessage", "ListAgents"] }` — but this also kills subagent communication (not recommended)
3. **Middle ground:** `"isolatePeerMachines": true` — requires approval before messages leave the machine

**Important:** Do NOT deny SendMessage — it also removes messaging to subagents and agent-team teammates. Use `crossSessionInbound: refuse` instead.

## Assessment

Directly relevant to any multi-session Claude Code workflow. The recommended setting (`crossSessionInbound: refuse`) should be default for most users running multiple sessions.