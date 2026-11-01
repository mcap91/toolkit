---
name: icca-harness
title: ICCA Harness
url: "https://github.com/BernhardJackiewicz/icca-harness"
category: plugin
summary: "Evidence-gated maker-checker-auditor workflow for Claude Code — separates Implementer, Checker, Control, and Auditor roles so the agent that writes code never decides whether it's accepted; mechanical enforcement via Git hooks (frozen acceptance tests, content-fingerprinted commit gates, bounded repair loops); measured 28% reduction in expensive-model tokens on implementation-heavy tasks at identical success rate (total tokens increase 37%); optional stage gates for static analysis, coverage, mutation testing, property tests, dependency structure, e2e scenarios; MIT"
tags: [claude-code, maker-checker, evidence-gated, code-review, verification, delegation, token-optimization, git-hooks, testing, skill]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [fable-agent-orchestration, agent-skills-osmani]
license: MIT
security_flags: []
source: unknown
---

## What it does

ICCA is a Claude Code skill that enforces a maker-checker-auditor separation for agentic development. The central rule: the agent that implements never decides whether its own implementation is accepted.

**Four roles:**
- **Implementer**: Writes production code in a fresh delegated context. Cannot stage, commit, touch frozen tests, or accept its own work.
- **Checker**: Independent fresh-context agents that execute declared stage gates (tests, static analysis, coverage, mutation). Never see Implementer transcripts. Never repair.
- **Control**: Optional. Reviews a completed cycle against its contract on larger plans.
- **Auditor**: Fresh context, interprets original requirements independently. Never receives "all done" summaries. Runs tests and builds its own probes.

**Mechanical enforcement (Git hooks):**
- Production code edits blocked before an active cycle or logged exemption exists
- Acceptance tests frozen by patch fingerprint before implementation — modifications detected mechanically
- Commits blocked without a passed commit gate
- Commits blocked after verified code state changes (content fingerprinting)
- Single-use gates: one passed gate authorizes exactly one commit
- Bounded repair: 2 attempts per defect, then re-planning

**Self-triage (Part 0):** The workflow classifies tasks as solo (no harness), light (core cycle), or full (cycle + declared stage gates). Small well-scoped work runs directly; delegation is for implementation-heavy work.

**Measured results (16 paired runs, 100% success rate):**
- Large task: -28% expensive-model tokens, +37% total tokens across both models
- Small task: +7% expensive-model tokens, +119% total tokens (delegation loses)
- Conclusion: delegate implementation-heavy work when the strongest model is scarce; do small work directly

**Optional stage gates:** static analysis, quality ceilings, coverage floors, mutation testing, seed-pinned property tests, dependency-structure checks, end-to-end scenarios. Each runs in an independent Checker context.

## Mechanical details

Installs as a Claude Code skill + hook pair. Requires Python 3.8+, Git, Claude Code. Gate CLI (`red_proof.py`) is dependency-free. 347 pytest tests + 21 smoke checks. Benchmark reproducible for ~$2.55 total. Tested on macOS. English default; German translation maintained in sync.

Inspired by Uncle Bob Martin's "gauntlet" concept (July 2026 tweet) — surrounding agents with extreme constraints rather than reading their code.

## Security

MIT licensed. Hooks are process CI, not a security boundary — they fail open on internal errors and can be disabled locally. Plain-terminal commits outside Claude Code are not intercepted. Repository resolution has shell-parsing limits for multi-repo scenarios.

## How to use it

git clone https://github.com/BernhardJackiewicz/icca-harness.git && cd icca-harness && ./install.sh
