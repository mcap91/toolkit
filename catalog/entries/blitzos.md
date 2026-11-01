---
name: blitzos
title: BlitzOS
url: "https://github.com/blitzdotdev/blitzos"
category: plugin
summary: "Context-repo system for Claude Code cloud VMs — generates a private GitHub repo (CLAUDE.md map + git submodule references + sessions log) so every new cloud agent boots knowing your repos, conventions, and what previous agents did; one-click multi-repo launch via blitzos.com, self-hostable on Cloudflare; MIT"
tags: [claude-code, cloud-sessions, context-management, multi-repo, github, session-persistence, self-hosted]
reviewed: 2026-07-15
acquired: 2026-07-15
license: MIT
security_flags: []
overlaps: [claude-mem]
source: unknown
---

## What it says

Addresses the cold-start problem of Claude Code cloud sessions: every new VM boots knowing nothing about the user's repos, conventions, or prior work. BlitzOS generates a "context repo" — a private GitHub repository that serves as the bootstrap payload for cloud agents:

```
your-context-repo/
  CLAUDE.md      # repo map, inter-repo relationships, conventions, work loop
  .gitmodules    # member repos pinned by reference (no code copied in)
  sessions/      # each cloud agent commits a record of what it did
  docs/          # optional power-mode setup
```

**Three deployment modes:**
- **Browser (blitzos.com):** Sign in with GitHub, pick repos, get one-click launches and a live agent feed showing status (working/quiet/done) across all running cloud agents
- **Local:** Skill builds everything on the user's machine, nothing touches BlitzOS servers
- **Self-host:** Run the portal on your own Cloudflare account (your OAuth app, database, domain) via a single setup script (~10 minutes)

**Security model:** Default flow uses zero credentials. The launch link selects repos through Anthropic's native GitHub proxy. Source code is never copied into the context repo (submodule references only) and never touches BlitzOS servers.

**Managed version (waitlist):** Company-wide context with role-based agent launches, scoped tool access (Google Workspace, Slack, Linear, Stripe), per-role credential grants, and audit trails.

## Key takeaways

- The core insight is that agent context should live in a versioned repo, not on a local machine — making it portable, reviewable, and available in unlimited parallel copies
- The sessions log creates compounding context: each cloud agent records what it did, so later agents can read the history
- Git submodule references avoid duplicating code into the context repo
- Requires Claude Code, Git, gh (authenticated), jq, Node 18+
- Roadmap includes: steering running agents from the web feed, skills traveling with the context repo, self-updating context (agents propose PRs back), and Codex support for vendor portability

## Security

MIT licensed. Default flow touches no credentials — all repo access goes through Anthropic's GitHub rail. Self-hosted mode runs entirely on the user's Cloudflare infrastructure. Managed version introduces credential scoping per role and per agent, with audit trail. The blitzos.com SaaS path does involve signing in with GitHub OAuth.