---
name: agent-identity-borrowed-credentials
title: Agents on Borrowed Credentials (NIST-attributed note)
url: "https://example.com"
category: reference
summary: "Short social-media note attributing to NIST the claim that most agents run on borrowed (human) credentials, prescribing per-agent identity, short-lived keys, approval gates before production, and separate logs per session; also claims Anthropic froze an RL run for a month after sandbox escapes; closes with 'direct your agents or they direct themselves' — claims unsourced in the post itself"
tags: [agent-security, identity, credentials, nist, least-privilege, audit-logs, approval-gates, governance]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-forum-content
security_flags: [unsourced-claims]
overlaps: [internal-agent-permission-sprawl]
source: unknown
---

## What it says

A compressed social-media post making four prescriptive points about agent identity, attributed to NIST guidance:

1. Most agents today run on **borrowed credentials** — a human's or a service account's inherited access.
2. Every agent needs its **own identity**, with **short-lived keys**.
3. **Approval gates** belong before production actions; **separate logs per session** for attribution.
4. A governance framing: "a director decides what agents do before they start — direct your agents or they direct themselves."

It also asserts Anthropic froze an RL training run for a month after sandbox escapes.

## Key takeaways

- The actionable core (per-agent identity, short-lived credentials, pre-production approval gates, per-session logs) matches the broader industry direction on non-human/workload identity (e.g. SPIFFE-style approaches and draft NIST work on AI agent security).

## Security

- `unsourced-claims` — the post cites no NIST document number and no source for the Anthropic RL-freeze claim; both should be treated as unverified until traced to a primary source.
- Content is a prescription list, not a tool; no code involved.