---
name: cloud-session-context-repo
title: Cloud Session Context Repository Pattern
category: agent-pattern
summary: "Pattern for persistent multi-session Claude Code cloud workflows — shared context repo (CLAUDE.md + .gitmodules + session handoff notes + skills), launcher webapp generating parameterized session URLs, status feed for monitoring; git as the sync layer, no backend"
tags: [claude-code, cloud-sessions, context, handoff, session-resume, git, orchestration, multi-repo]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [agent-session-resume]
license: ""
security_flags: []
source: unknown
---

## What it does

A practitioner-reported pattern for productive use of Claude Code's cloud sessions (disposable Linux VMs included with Pro/Max subscriptions). Solves the problem that every new cloud session starts with no context about the user's work.

Two components:

1. **Context repository** (private git repo opened by every cloud session first):
   - `CLAUDE.md` — maps repos, architecture, conventions, workflows
   - `.gitmodules` — references actual project repos without copying code (keeps context repo tiny)
   - `sessions/` — short handoff notes from previous agents (what changed, what was discovered, what needs work)
   - `skills/` — skills that should be available in cloud sessions (they don't auto-appear)

2. **Launcher website** (small self-hosted page):
   - Generates `claude.ai/code` URLs with pre-filled repositories and initial prompt
   - User picks a project, types a task, and it opens Claude Code with context repo + project repos + prompt
   - Agents send one-line status updates back to the site (working/quiet/done feed)
   - Requires enabling custom network access and allowlisting the website domain
   - No credentials stored — repo access uses Anthropic's existing GitHub integration

Workflow: Open site from phone → pick project → give small testable task → close laptop → review diff/PR later.

Community-validated best practices from discussion:
- Have agents report a "blocked" status for stuck-on-input situations
- Gate context repo changes through PRs to prevent agents overwriting each other
- Always run project tests before reporting "done"

## Assessment

Addresses a real gap: Claude Code cloud sessions are stateless and skills don't persist across sessions. The .gitmodules approach for referencing project repos without duplicating code is elegant. The session handoff notes in `sessions/` parallel this project's own handoff skill concept. The launcher website is the novel contribution — parameterized session URLs with status monitoring.

Limitations noted by the community: cloud session reliability is inconsistent, sessions stall, and network restrictions limit some workflows. The original post was flagged as promotional (BlitzOS), but the underlying pattern was validated independently by multiple commenters.

## Security

Not applicable — this is a workflow pattern, not executable code. The launcher website requires custom network access allowlisting in Claude's settings. No credentials are stored in the launcher — all repo access goes through Anthropic's GitHub integration.