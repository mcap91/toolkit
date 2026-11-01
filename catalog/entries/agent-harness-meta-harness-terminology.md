---
name: agent-harness-meta-harness-terminology
title: Agent vs Harness vs Meta-Harness (terminology)
url: "https://example.com"
category: reference
summary: "Explainer resolving why Claude Code and Codex are called both 'agents' and 'harnesses' — model is the reasoning engine, agent is the emergent goal-directed behavior, harness is the operational machinery (context assembly, tools, execution, sessions, approvals, sandboxing); introduces 'meta-harness' as Omnigent's term for a layer wrapping multiple harnesses behind one interface with shared orchestration, policy, state, and cost controls"
tags: [terminology, harness, agents, meta-harness, claude-code, codex, subagents, omnigent, architecture]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-forum-content
security_flags: []
overlaps: []
source: unknown
---

## What it says

A short explainer on why "agent" and "harness" both correctly describe Claude Code and Codex — they name different views of one running system:

- **Model** — the reasoning engine (Claude/GPT predicting tokens).
- **Agent** — the goal-directed behavior that emerges when a model can choose steps, use tools, observe results, and continue working.
- **Harness** — the machinery making that behavior operational: assembles context, exposes tools, executes commands, persists sessions, enforces approvals and sandboxing.

Claude Code and Codex bundle harness machinery around models to deliver coding agents. Both can spawn **sub-agents** — separate agent instances with bounded tasks (research, implementation, review) — but multiple sub-agents still live inside one harness.

A **meta-harness** sits one level higher: Omnigent (often misheard as "Omni Agent") wraps different harnesses behind a common interface so a system can switch or combine them while sharing orchestration, policy, state, sandboxes, cost controls, and collaboration.

## Key takeaways

- The useful distinction: sub-agents divide work *inside* a harness; a meta-harness coordinates *across* harness systems.
- The source itself flags that "meta-harness" is emerging terminology — it is the architecture Omnigent describes, not an industry standard.

## Security

- Terminology explainer; no code. The Omnigent framing originates from that product's own architecture description.