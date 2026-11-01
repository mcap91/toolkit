---
name: internal-agent-permission-sprawl
title: Internal Bot Leaked the Unannounced Reorg Plan (permission sprawl)
url: "https://reddit.com"
category: reference
summary: "Incident writeup — an internal Q&A assistant scoped 'to read the wiki' answered with a confidential reorg spreadsheet including salary bands, because a broad Drive grant at setup indexed the HR folder; a follow-up audit found another wiki-summarizer bot holding inherited delete access and send-as-mail rights from its creator's account; thesis: over-broad access is itself the incident — 'an agent that can read everything will eventually read the thing it shouldn't'"
tags: [agent-security, least-privilege, permissions, oauth-scopes, data-leak, internal-tools, access-audit, inherited-permissions]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-forum-content
security_flags: []
overlaps: []
source: unknown
---

## What it says

A discussion post recounting two related findings at one company:

1. **The leak.** An internal assistant meant to answer from an approved knowledge base responded to a team-structure question with details from an unannounced reorg spreadsheet, including salary bands. Root cause: at setup, the bot requested Drive file access and someone clicked yes; that scope indexed everything, including the confidential HR folder. The asker had no idea the material was confidential — "they just got an answer."
2. **The audit.** A week-long review of what internal agents could reach found one bot whose entire job was summarizing a few wikis, yet it held **delete access on the shared drive** and could **send mail as its creator** — permissions nobody granted deliberately; they were inherited from the account that set it up.

The author's framing: nothing attacked them — the access itself was the problem.

## Key takeaways

- Consent-screen grants at agent setup time become the agent's permanent effective scope; "read the wiki" intent does not constrain a Drive-wide token.
- Service accounts inherit their creator's permissions unless explicitly narrowed — the most dangerous grants are the ones nobody made.
- The failure mode needs no attacker and no prompt injection: a helpful agent + over-broad read scope = eventual disclosure of the most sensitive reachable document.

## What to adopt

- Periodically audit effective (not intended) permissions of every internal agent: what can it read, delete, and impersonate.
- Scope agent identities separately from their creators; never let an agent run on a human's inherited credentials.

## Security

- Forum content; a first-person incident report, unverifiable but internally consistent and representative of a well-documented failure class.