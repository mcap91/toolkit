---
name: pilotfish
title: Pilotfish
url: "https://github.com/Nanako0129/pilotfish"
category: skill
summary: "Multi-model orchestration layer for Claude Code — six agent roles (haiku scouts, sonnet executor, opus judgment, adversarial verifier, security) that delegate from a frontier orchestrator; one-prompt install to ~/.claude/, benchmarked at 96% of all-Fable performance for 46% cost"
tags: [claude-code, multi-model, orchestration, subagents, cost-optimization, fable, skill]
reviewed: 2026-07-12
acquired: 2026-07-12
license: MIT
security_flags: [writes-to-user-home]
overlaps: [claude-code-fable-cost-playbook, advisor-strategy, native-subagents]
source: unknown
---

## What it is

Pilotfish is an installable orchestration layer for Claude Code that implements the "frontier model plans, cheaper models execute" pattern. It defines six agent roles pinned to cost-appropriate model tiers, with a CLAUDE.md policy that delegates by task type. One-prompt install; writes only to `~/.claude/`.

## Architecture

- **Tier 0 — Fable/frontier.** Intent, architecture, decomposition, tradeoffs, final review, synthesis.
- **Tier 1 — Opus.** Complex implementation, deep debugging, cross-module reasoning, security-sensitive work, reviewing cheaper agents' output.
- **Tier 2 — Sonnet.** Scoped implementation, tests, medium debugging, local refactors, following patterns.
- **Tier 3 — Haiku.** Repo discovery, file summaries, log summaries, checklist verification, edge-case scanning.
- **Verification role.** Independent fresh-context verifier (adversarial, not self-critique).
- **Security role.** Kept off Fable because its classifiers misfire on benign security work.

## Benchmark backing

Anthropic's first-party numbers (July 2026): Fable 5 orchestrator + Sonnet 5 workers achieves 96% of all-Fable performance at 46% of the cost (BrowseComp: 86.8% vs 90.8% accuracy, $18.53 vs $40.56 per problem). The inverse pattern (Sonnet executor consulting Fable advisor) hits ~92% at ~63% on SWE-bench Pro.

## Installation

Claude reads the install runbook, inspects existing config, shows a merge plan, applies after approval. Idempotent — re-running upgrades in place. No files touched outside `~/.claude/`. Uninstall is three reversible steps documented in the README.

## Related: fable-chief-agent skill

The community also produced a standalone skill (`fable-chief-agent`) encoding the same philosophy in a single SKILL.md — Fable owns intent/architecture/tradeoffs/final-gate, delegates discovery/implementation/verification to cheaper tiers. Same operating loop: decide → define success → delegate → review evidence → decide → verify → answer.

## Security

Passed SkillsLLM automated security scan (dependency audit + prompt-injection heuristics, no high-severity issues). Installs only under `~/.claude/` — no system-wide changes. The README provides a tag-pinned variant and lists which files to read first. Model-agnostic policy text (never names a specific model) means the stack survives model deprecation without breaking.