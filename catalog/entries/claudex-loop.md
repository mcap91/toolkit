---
name: claudex-loop
title: Claudex-Loop
url: "https://github.com/chaseai-yt/claudex-loop"
category: skill
summary: "Claudex-loop enforces a cross-model review invariant where Claude plans and Codex reviews in a read-only sandbox, through four phases — recon, interrogate, review, and optional build — producing a locked plan and a full round-by-round review transcript"
tags: [cross-model-review, adversarial-review, plan-hardening, codex, claude-code-plugin, multi-model, planning]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [local-model-adversarial-workflow]
license: MIT
security_flags: []
source: unknown
---

## What it does

Claudex-loop enforces a cross-model invariant: whoever made the artifact never checks it.
The workflow has four phases:

1. **RECON (Phase 0):** Claude scouts the codebase or researches greenfield prior art, then
   presents an Assumptions Ledger for batch confirmation — the interview never asks questions
   the code already answered.

2. **INTERROGATE (Phase 1):** A decision map splits open questions into load-bearing (asked
   individually) and cosmetic (batched with veto-by-exception). Each question includes a
   committed recommendation and stakes explanation.

3. **REVIEW (Phase 2):** Codex reviews the locked PLAN.md in a read-only sandbox, issuing
   APPROVED or REVISE verdicts with concrete flaws. Claude arbitrates (can reject bad
   critiques with logged reasons), revises, and resumes the same Codex session. Bounded by
   MAX_ROUNDS (default 5).

4. **BUILD (Phase 3, optional):** User picks the builder. If Codex builds, Claude reads the
   entire diff and runs proof tests. If Claude builds, a fresh Codex session cross-inspects.
   Skipping inspection requires an explicit logged opt-out.

Two artifacts per run: PLAN.md (the spec) and PLAN-REVIEW-LOG.md (the full round-by-round
argument transcript).

## Installation

Marketplace plugin (recommended):
```
/plugin marketplace add chaseai-yt/claudex-loop
/plugin install claudex-loop@claudex-loop
```

Manual: copy `skills/*` to `~/.claude/skills/`.

## Prerequisites

- Codex CLI >= 0.130 (`npm install -g @openai/codex@latest`)
- Authenticated via `codex login` (any ChatGPT account tier)

## Configuration

| Skill | Var | Default | Meaning |
|---|---|---|---|
| claudex-loop | research | ask | none / web / deep — pre-answers the Phase 0 research gate |
| review skills | MAX_ROUNDS | 5 | Hard cap on review rounds |
| review skills | PLAN_FILE | PLAN.md | Where the plan lives |
| all | LOG_FILE | PLAN-REVIEW-LOG.md | The argument transcript |
| codex-build | MAX_FIX_ROUNDS | 2 | Fix rounds before Claude takes over |
| codex-build | PROOF_CMD | from spec | Exact test command that counts as proof |

## Safety Model

Review phases run Codex in read-only mode (`-s read-only` on first call, `-c sandbox_mode="read-only"` on resume). codex-build deliberately grants full write access, gated by: clean git tree requirement, Claude reads every diff line and runs proof, fix rounds bounded, commits human-gated and Claude-authored.