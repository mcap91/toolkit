---
name: deepseek-and-destroy
title: DeepSeek and Destroy
url: "https://github.com/frozenpepper/deepseek-and-destroy"
category: skill
summary: "Portable, multi-harness coding-agent skill in which an expensive orchestrator model decomposes and gates a multi-phase implementation plan while routing survey, implementation, review, and verification work to cheap DeepSeek-v4-flash workers via OpenCode CLI, using a worker proof-obligation discipline meant to catch tests that pass for the wrong reason."
tags: [multi-agent, orchestration, deepseek, opencode, cost-optimization, plan-execution, worker-pattern, codex, claude-code, kilocode]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: []
overlaps: [architect-loop]
source: unknown
---

## What it does

DeepSeek and Destroy (DSD) is a coding-agent skill for executing large, multi-phase implementation plans while reserving an expensive orchestrator model (e.g. Opus) for plan-wide judgment and routing repository-scale grunt work — survey, discovery, bounded implementation, verification, independent review, repair, and evidence synthesis — to cheap worker models. The default worker backend is `opencode-go/deepseek-v4-flash`, dispatched via the OpenCode CLI. The core loop: plan → phase survey/discovery when needed → a bounded task with stable acceptance-criteria IDs (AC-001, etc.) and "Proof Obligations" → a fresh implementer → a fresh independent reviewer → pass/fail gate (fixer loop on fail) → phase-level verification workers and a fresh phase auditor → orchestrator phase gate → next phase. It runs until the plan is complete, a genuine human-level blocker is reached, or the user pauses/abandons it — a finished task or phase, or a review failure, is explicitly not treated as a stopping condition.

## Differentiators

A "worker proof layer" (`worker/PROOF-PATTERNS.md`) supplies optional proof recipes — NEGATIVE-GATE, CARDINALITY, IDENTITY, DURABILITY, DERIVED-EVIDENCE — aimed at a specific failure class the author calls "green for the wrong reason" (e.g. a negative test that aborts before the guard it claims to test, a single-member fixture hiding a "last parent wins" bug). Reviewers fill in a Proof Matrix per acceptance criterion and must be able to name a plausible broken implementation the current evidence would fail to catch. A fast-path acceptance rule lets a credible fresh-reviewer PASS with a complete Decision Packet skip re-review by the orchestrator, to avoid paying twice for verification. Defect-honesty rules forbid relabeling a correctness defect as "known limitation" or "tech debt" to preserve a PASS. Durable run state lives under `DeepSeekAndDestroy/plans/<plan-id>/runs/<run-id>/` (state.json, HANDOVER.md, Proof Matrices, phase audits, findings/fixes log) with a defined context-checkpoint policy (checkpoint due at 65% context, compact before 75%, no new phase-level reasoning at 80%) and crash/resume support. Supports Codex, Claude Code, OpenCode (default), and Kilo Code (via two installed subagent profiles, `dsd-mutating-worker` and `dsd-readonly-worker`).

## Mechanical details

- Install: copy the repository folder intact into the harness's skill location.
- Quick start: "Use DeepSeek and Destroy to execute the authoritative plan at DOCS/Plans/implementation-plan.md."
- Optional overrides in `CONFIG.example.md`: worker harness/model/endpoint, role routing/fallback workers, review/transport budgets, project-specific rules, live/destructive test policy, context-checkpoint behavior.
- OpenCode workers use one disposable external SQLite DB per DSD run (never the project's or the user's interactive DB); parallel execution uses one external DB per concurrency lane. `scripts/opencode_probe.py` reconciles ambiguous possibly-live workers before relaunch.
- `scripts/check_review_contract.py` checks structural completeness/consistency of reviewer reports (not software-semantic correctness).
- Author (source Reddit post) reports the skill works well with Claude Opus as orchestrator + DeepSeek-flash workers, but explicitly does **not** work well with SOL (Codex's model) as orchestrator/implementer — SOL ignores the skill's hard rules, re-reviews everything itself, inspects worker context, and micromanages, defeating the delegation model.

## Security

MIT licensed, copyright 2026 FrozenPepper. Single-author, early-stage project (author describes ongoing active changes and an in-progress automatic context-compaction/resume protocol as of the source post) — no independent audit, star count, or adoption signal found via web search at review time beyond the author's own account. The skill dispatches external `opencode` CLI child processes to run worker agents with tool/shell access; scope of what those workers can touch is governed by the harness's own permissions, not by DSD itself. No credentials or network calls beyond what the underlying harness (Claude Code/Codex/OpenCode/Kilo Code) and OpenCode CLI already require.
