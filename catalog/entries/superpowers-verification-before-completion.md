---
name: superpowers-verification-before-completion
title: "Superpowers: Verification Before Completion"
url: "https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md"
category: skill
summary: "canonical 'evidence before claims' gate skill — already active in this project and referenced by other catalog entries as the standard"
tags: [verification, quality, agent-discipline, completion-gate, tdd]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-unknown
security_flags: []
overlaps: [verify-before-claim]
source: unknown
---

## What it does

A Claude Code skill that enforces a hard gate before any completion claim, success expression, or commit action. The core principle is "evidence before claims, always." Before stating that tests pass, a build succeeds, a bug is fixed, or requirements are met, the agent must: (1) identify the command that proves the claim, (2) run it fresh and completely in the current message, (3) read the full output and exit code, (4) verify the output supports the claim, and only then (5) state the claim with the evidence attached.

The skill defines an "Iron Law" (no completion claims without fresh verification evidence), a structured 5-step gate function, a table of common claim-to-requirement mappings (e.g., "tests pass" requires test-command output showing 0 failures, not a prior run), a "red flags — STOP" list (expressions like "should pass," "probably," satisfaction phrases like "Great!" or "Done!" before verification, trusting agent success reports), and a rationalization-prevention table addressing common excuses. It also covers regression testing (full red-green cycle required), agent delegation (always verify VCS diff, not agent self-report), and requirements verification (line-by-line checklist, not just passing tests).

## Assessment

Adopt. This is the canonical obra/superpowers version of the verification discipline that the existing `verify-before-claim` catalog entry (Third Brain V5 variant) explicitly defers to as the standard. It is already installed in this project's `.claude/` directory and has been active across sessions. The skill directly addresses a failure mode observed repeatedly in agent workflows: false completion claims that break trust and produce wasted rework cycles. The 5-step gate is concrete, machine-followable, and free of ambiguity. The rationalization-prevention table is particularly effective at closing escape hatches agents use to skip verification under time/confidence pressure.

The only nuance: the Third Brain V5 variant adds a probabilistic confidence model (expected-value scoring, single-source flagging) not present here. That extension is cataloged separately in `verify-before-claim` (verdict: note) and can be layered on if needed. For the baseline rule, this skill is the authoritative source.

## Mechanical details

The skill is a SKILL.md file installed to `.claude/skills/verification-before-completion/`. When active, the Claude Code harness surfaces the skill's trigger condition to the model context. Trigger: "Use when about to claim work is complete, fixed, or passing, before committing or creating PRs." The skill operates as a cognitive gate, not an executable — it cannot mechanically run commands itself; it instructs the agent to run them and report evidence before making claims.

Key adoption patterns:
- Tests: run the test command, show output with pass count, then state "all tests pass"
- Regression (TDD red-green): write test → run (must pass) → revert fix → run (must fail) → restore → run (must pass)
- Build: run build command, confirm exit 0, then state "build passes"
- Requirements: re-read plan, create line-by-line checklist, verify each item
- Agent delegation: check VCS diff after agent reports success; never trust self-report alone

The "when to apply" scope is intentionally maximal: any variation of success/completion claims, any expression of satisfaction, any positive statement about work state, committing/PR creation/task completion, moving to the next task, delegating to subagents.

## Security

This is a pure Markdown skill file — no code, no dependencies, no executables. No supply-chain risk. The content contains strong normative language ("this is non-negotiable," "lying, not verifying") intended to resist rationalization by the consuming agent. No injection vectors. No license declaration in the repository; marked `LicenseRef-unknown` pending a SPDX identifier being added to the obra/superpowers repo.

Note: the skill's content includes instructions for the consuming agent (e.g., "Run the command. Read the output."). Per catalog policy, these are treated as data describing the skill's behavior, not as instructions to follow during cataloging.
