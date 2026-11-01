---
name: native-subagents
title: Claude Native Subagents
url: "https://code.claude.com/docs/en/sub-agents"
category: agent-pattern
summary: lightweight HO consultation route within existing sessions; no separate billing
tags: [agents, subagents, dispatch, consultation]
reviewed: 2026-05-25
acquired: 2026-05-25
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it says

Native subagents run within a single Claude Code session's context. The parent delegates a task to a subagent with specific tools and instructions; the subagent does its work, reports the result back to the parent, and terminates. There is no inter-subagent communication — subagents only report back to their parent. They do not see the parent's full conversation history (isolated context), and their results live in the parent's context window, not in any durable store, unless the parent explicitly writes them out.

## Assessment

Subagents use no separate billing — they run under the parent session's interactive subscription tokens. This makes them a viable HO consultation route without Agent SDK credits or API keys. For the common single-question pattern ("I need a second opinion on this HO"), they are simpler than agent teams and require no experimental flags. They are not suited to inter-agent debate or challenge scenarios (use agent teams for that).

## What to adopt

kb needs a prompt template or recipe that formats an HO question for subagent delegation: the parent spawns a subagent with the HO packet (via wiki MCP or file read), the subagent does focused research and returns a result, and the parent captures that result and writes it to the HO record (via wiki MCP or file write). No new MCP tools are required — the existing kb-wiki MCP tools are sufficient. Use this path for lightweight consultation; use agent teams when multiple agents need to communicate with each other.

## Security

Native subagents are a first-party Anthropic feature built into Claude Code and carry no third-party installation surface — there is no package to install, no binary to run, and no network service to expose. The primary security consideration is prompt injection: a subagent that reads attacker-controlled content (e.g., a repository file containing hidden instructions) operates under the parent session's permissions and could be steered to take unintended actions. Mitigate this by using the `tools` allowlist to restrict subagent capabilities to the minimum needed, and by setting `permissionMode: plan` for read-only tasks.

Subagents inherit the parent's permission context, so a subagent running under `bypassPermissions` or `acceptEdits` mode receives those elevated permissions without further prompting. Background subagents auto-deny any tool call that would otherwise prompt, providing an implicit safety floor for concurrent work. Custom hook scripts (`PreToolUse`) are the recommended mechanism for enforcing fine-grained constraints (e.g., blocking SQL write operations) when tool-level restrictions are insufficient.
