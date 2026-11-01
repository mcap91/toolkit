---
name: deny-env-reads
title: Deny .env Reads via Permissions
url: "https://code.claude.com/docs/en/settings"
category: reference
summary: Useful security hygiene tip for Claude Code projects; documents a built-in feature rather than a new tool
tags: [security, permissions, claude-code, env-files, secrets]
reviewed: 2026-06-10
acquired: 2026-06-10
license: UNLICENSED
security_flags: []
overlaps: [claude-code-remote-prompt-hardening]
source: unknown
---

## What it says

A practical tip for preventing Claude Code from reading sensitive environment files (`.env`, `.env.*`, `secrets/`). Even with explicit steering prompts telling Claude not to read `.env` files, the agent may still occasionally access or modify them. The reliable solution is to add deny rules to `.claude/settings.local.json`:

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  }
}
```

This uses Claude Code's built-in permission system to enforce the restriction at the harness level, making it impossible for the agent to read those paths regardless of prompt behavior.

## Assessment

**Note.** This documents a built-in Claude Code feature — there's nothing to install or adopt as external tooling. It's worth recording as a reference because: (1) the failure mode it addresses (agent reading `.env` despite prompt instructions) is real and common, (2) the fix is non-obvious to users who haven't read the settings docs, and (3) it complements the existing "Claude Code Remote Prompt Hardening" entry. Not elevated to `adopt` because it's a single config snippet, not a tool or pattern to integrate.

## Mechanical details / What to adopt

- Add deny rules to `.claude/settings.local.json` (user-local, not committed to repo) for any sensitive file patterns
- The deny list uses glob syntax relative to the project root
- Covers `Read` operations; consider also denying `Edit` and `Write` for the same paths
- This is a harness-level enforcement — it cannot be overridden by prompt content

## Security

- **License**: N/A — this is a configuration tip referencing official Claude Code documentation
- **Dangerous patterns**: None — the tip itself improves security posture by preventing secret exposure
- **Supply chain**: N/A — no dependencies, no code to install
- **Assessment**: Clean. The tip is straightforward and aligns with security best practices for AI coding assistants