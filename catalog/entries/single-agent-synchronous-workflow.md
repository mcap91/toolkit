---
name: single-agent-synchronous-workflow
title: Single-Agent Synchronous Workflow
category: agent-pattern
summary: "Argument and configuration for denying the Agent tool in Claude Code — single-agent synchronous workflows preserve context evidence (subagent summaries lose the backing data), enable mid-run interruption, and improve cache efficiency; adversarial review via in-repo documentation compliance agents is the endorsed exception"
tags: [single-agent, synchronous, anti-pattern, subagents, context, interruptibility, cost-optimization, code-review, claude-code]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [advisor-strategy, local-model-adversarial-workflow]
license: ""
security_flags: []
source: unknown
---

## What it does

A practitioner-reported workflow philosophy arguing that single-agent synchronous workflows outperform multi-agent orchestration for feature implementation in Claude Code. The core claim: when an orchestrator sends work to a subagent, it takes the returned summary as fact without access to the evidence gathered to support it — there's no way to distinguish "I verified this" from "I concluded this."

Key arguments:

- **Evidence loss**: Subagent context is discarded after summarization. The orchestrator can't audit the prose it receives. In a single-agent session, evidence remains cached and available.
- **Cost accounting**: The discarded subagent context is the real bill — you lose the evidence and pay to re-read it later. Single-agent sessions keep it cached.
- **Interruptibility**: Single-agent work can be stopped when you see a bad premise developing. Parallel subagents are uninterruptible by construction — you find out afterward.
- **Cited research**: Xu et al. "Rethinking the Value of Multi-Agent Workflow" found that running multi-agent workflows through one agent instead of separate instances produced comparable or better results.

The practitioner's configuration denies the Agent tool entirely plus most meta-tools (AskUserQuestion, EnterPlanMode, TaskCreate, Workflow, etc.), achieving ~35% usage of a $100/week subscription while accomplishing 3-6 months of pre-agent work per week.

**Endorsed exception**: Adversarial review agents. Separate agents for architecture boundary compliance, coding guidelines, documentation guidelines, and testing best practices — each inspecting changes against in-repo documentation. The key: review agents check compliance with documented standards, not open-ended assessment. This workflow catches enough defects that human code review rarely finds meaningful issues. Each miss becomes signal that in-repo documentation needs improvement.

The practitioner's desired (but unavailable) feature: per-skill/tool scoping of the Agent tool — adversarial review on, delegated implementation off.

## Assessment

Presents a defensible case against subagent delegation for implementation work, grounded in the evidence-loss problem. The adversarial-review exception is well-reasoned — review agents consume evidence (the diff) but don't need to generate it, so the summarization loss is less harmful. The configuration snippet is directly usable. The desire for per-skill Agent tool scoping reflects a real gap in Claude Code's permission model.

This pattern is in tension with the graph-engineering and multi-agent orchestration patterns also cataloged. The resolution: use single-agent for implementation, multi-agent for review/verification. This is consistent with the advisor-strategy pattern.

## Security

Not applicable — this is a workflow philosophy and Claude Code configuration pattern, not executable code.