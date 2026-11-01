---
name: fable-orchestrator-model-split
title: Fable as Orchestrator — Role-per-Model Split with Ticketed Review Loop
url: "https://reddit.com"
category: agent-pattern
summary: "Practitioner workflow for stretching Claude Fable usage limits by making Fable the orchestrator, not the worker — Haiku scouts locations, Sonnet researches and builds from specs, Opus refutes/reviews and debugs; extended with a ticket loop where an ephemeral Opus hand implements in a worktree, a cold Fable reviewer issues ACCEPT/REWORK verdicts, green-suite merges auto-revert on red, and the lead cuts releases"
tags: [orchestration, model-routing, claude-fable, opus, sonnet, haiku, cost-optimization, worktree, code-review, ticket-loop, multi-agent]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-forum-content
security_flags: []
overlaps: [local-model-adversarial-workflow, deepseek-and-destroy, single-agent-synchronous-workflow]
source: unknown
---

## What it says

A practitioner's account of running Claude Fable "on High basically all the time" (90% Fable usage) without burning through limits, by making Fable the orchestrator rather than the worker. The role split:

- **Fable — orchestrator:** plans, writes specs, spins up agents, reads their reports, makes architecture/judgment calls, integrates.
- **Haiku — scout:** finds files, symbols, call sites; reports locations instead of dumping whole files.
- **Sonnet — researcher:** reads docs/source and reports facts; anything unverifiable is marked unverified.
- **Sonnet — builder:** codes from a clear spec and runs tests.
- **Opus — refuter:** reviews the builder's diff and reruns tests itself — a "done" claim is not trusted.
- **Opus — debugger:** reserved for hard root-cause debugging.

Fable never reads large code volumes, does bulk refactors, or writes docs — anything a cheaper model can handle.

The extended ticket loop: Fable (lead) writes the spec and files a ticket; the loop mints a branch, worktree, and seat; an ephemeral Opus "hand" boots in the worktree, implements, runs the suite, commits, and marks DONE with a short report (deviations flagged). A cold Fable reviewer then receives the diff plus spec, writes an ACCEPT or REWORK verdict, and is retired. REWORK feeds must-fixes back to the same hand (context intact); ACCEPT merges to master with the full suite run behind it — a red suite reverts the merge and escalates. On acceptance the hand is retired, worktree removed, branch deleted; the lead titles the changelog and cuts the release.

## Key takeaways

- The expensive model's leverage is judgment density: specs, verdicts, integration — not token throughput.
- Verification is structurally separated from implementation: the reviewer is a *cold* instance with only diff + spec, and merges are guarded by an independent full-suite run with automatic revert.
- Rework preserves the implementer's context while keeping the reviewer stateless — fresh eyes each round, warm hands throughout.

## What to adopt

- The scout/researcher/builder/refuter/debugger role taxonomy maps directly onto subagent model selection.
- The cold-reviewer + auto-revert-on-red-merge mechanics are reusable in any orchestrated pipeline.

## Security

- Forum content; a workflow description with no code. Claims are one user's self-reported usage ratios.