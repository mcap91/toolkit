---
name: agent-teams
title: Claude Agent Teams
url: "https://code.claude.com/docs/en/agent-teams"
category: agent-pattern
summary: "primary interactive dispatch path; subscription billing, no API credits needed"
tags: [agents, teams, dispatch, orchestration]
reviewed: 2026-05-25
acquired: 2026-05-25
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it says

Claude Agent Teams is an experimental feature (requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and v2.1.32+) where one lead session coordinates multiple teammate sessions. Teammates share a task list (pending → in progress → completed, with dependency support) and a mailbox for direct teammate-to-teammate messaging. Each teammate is a separate Claude instance with its own context window; they load the same project context (CLAUDE.md, MCP servers, skills) but not the lead's conversation history. Display modes are in-process (works everywhere, Shift+Down to cycle) and split panes (requires tmux or iTerm2 — not supported in Windows Terminal, VS Code terminal, or Ghostty). Subagent definitions can serve as teammate roles: their `tools` allowlist and `model` are honored and their body is appended to the teammate's system prompt, but `skills` and `mcpServers` frontmatter fields are not applied — teammates load those from project/user settings.

## Assessment

Billing runs under interactive subscription — no API billing or Agent SDK credits needed. This directly satisfies the core kb dispatch constraint introduced by the June 15, 2026 Agent SDK credit change. kb dispatch interoperability is strong: if kb-wiki MCP is configured, teammates have full read/write access to wiki records. Dispatch cannot launch agent teams (interactive-only, no `-p` mode), and the task list is transient, but teammates can write durably via MCP — so the integration surface is MCP, not subprocess launch.

## What to adopt

1. Don't wrap agent teams in dispatch. Teammates call `create-handoff`, `get-response`, and `review` via kb-wiki MCP directly during the team session.
2. Assign a "scribe" teammate to write HO-style summaries as wiki records at session end so outputs survive past the transient task list.
3. Agent teams are operator-directed — dispatch defines the protocol (what an HO is, how responses are structured, where artifacts go) but does not own execution.
4. Use in-process display mode on Windows; reserve split-pane mode for tmux/iTerm2 environments.
5. Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and confirm v2.1.32+ before relying on this path.

**kb dispatch interoperability table**:

| Question | Answer |
|---|---|
| Can teammates read kb wiki? | Yes. If kb-wiki MCP is configured, teammates have full access. |
| Can teammates write to kb wiki? | Yes. Same MCP access. Teammates can create/update WK issues. |
| Can dispatch launch agent teams? | No. Agent teams are interactive-only. No `-p` mode. |
| Can dispatch capture team outputs? | Not directly. Task list is transient. Teammates must write durably via MCP. |
| Is billing acceptable? | Yes. Subscription only. No API credits. |

## Security

Claude Agent Teams is a proprietary Anthropic feature built into Claude Code; there is no open-source license or independently auditable codebase. All team state (config, task list, mailbox) is stored locally under `~/.claude/teams/` and `~/.claude/tasks/` and is removed when the team is cleaned up, so there is no persistent credential or secret exposure from the coordination layer itself. The primary security concern is permission inheritance: all teammates start with the lead's permission mode, and if the lead runs with `--dangerously-skip-permissions`, every teammate inherits that flag with no per-teammate override at spawn time. This means a compromised or misbehaving teammate has the same filesystem and tool access as the lead. Mitigation is to use the most restrictive permission set the task allows before spawning teammates, and to leverage subagent `tools` allowlists to narrow each teammate's effective tool surface.

There are no network-exposure risks specific to the coordination layer — teammates communicate via local IPC (file locking for task claims, local mailbox), not over a network. MCP servers available to the lead are equally available to all teammates, so any MCP tool that has broad write access (e.g. kb-wiki, filesystem MCP) is reachable by every teammate. Hooks (`TeammateIdle`, `TaskCreated`, `TaskCompleted`) run local shell commands and should be treated with the same care as any pre/post-commit hook — avoid embedding secrets or privileged operations in hook scripts.
