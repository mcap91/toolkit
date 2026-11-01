---
name: ai-work-receipt
title: AI Work Receipt
url: "https://instagram.com/agenticengineering"
category: agent-pattern
summary: "Concept for an agent skill that generates structured AI work receipts — two arms: time-saved estimates (human baseline vs AI-assisted time) and artifact metrics (lines of code, functions/modules shipped, bugs logged/closed); aimed at giving managers and stakeholders visibility into AI productivity gains"
tags: [productivity, metrics, time-tracking, agent-patterns, accountability]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [codeburn]
source: unknown
---

## What it says

Concept from @agenticengineering (Instagram) for a skill/prompt that asks the agent to review completed work and generate a structured "AI work receipt" with two measurement arms:

**Arm 1 — Time saved:**
- Human baseline: how long this would have taken manually
- AI-assisted time: how long it actually took with the agent
- Final value estimate: small assist, major time saver, or not worth using AI for
- Instruction to be conservative and not count drafts, ideas, or unused output as completed work
- Requires access to date/time tools (or git/file modified timestamps) for actual time measurement

**Arm 2 — Artifacts produced:**
- Lines of code written
- Functions/modules shipped
- Bugs and issues logged and closed

**Goal:** provide users, managers, and key opinion leaders with visibility on how AI improves productivity.

## Key takeaways

The two-arm structure (time + artifacts) addresses a real gap — most AI productivity claims are anecdotal. The conservative estimation instruction ("do not count drafts, ideas, or unused output") is a useful guard against inflated metrics. Git timestamps and file modification times provide objective time boundaries. The pattern could be implemented as a Claude Code skill using `git log`, `git diff --stat`, and file timestamps.

## Security

N/A — concept description, no code or dependencies.