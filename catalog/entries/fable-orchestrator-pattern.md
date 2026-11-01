---
name: fable-orchestrator-pattern
title: Fable Orchestrator Pattern (Multi-Model Delegation)
category: agent-pattern
summary: "Workflow pattern using Claude Fable as principal orchestrator with cheaper models (Sonnet, Opus, Codex/GPT-5.6) as execution workers — Fable plans and judges, workers implement and review in loops; achieves ~92–96% of Fable-solo quality at 40–63% of the cost; implemented via Claude Code agents, Codex CLI persistent threads, or the advisor tool"
tags: [claude-code, fable, orchestration, multi-model, cost-optimization, codex, sonnet, opus, delegation]
reviewed: 2026-07-15
acquired: 2026-07-15
license: unlicensed
security_flags: []
overlaps: [advisor-strategy, frontier, native-subagents]
source: unknown
---

## What it says

A multi-model orchestration pattern where Fable (Claude's most capable model, $10/$50 per million tokens input/output) serves as the principal orchestrator — planning, decomposing tasks, reviewing diffs, and making judgment calls — while cheaper models handle volume work:

**Core flow (from practitioner report):**
1. Fable plans the work
2. Sonnet 5.6 Sol reviews the plan in a loop until approved
3. Sonnet 5.6 Luna implements
4. Fable reads the full diff, fixes what it doesn't like directly, runs tests
5. Sol reviews the code against the plan
6. Loop until approved
7. Fable handles release (changelog, tag, merge)

**Implementation:** Bash scripts around Codex CLI with persistent threads, called from Claude Code skills. No framework, no MCP server, no multi-agent library — just shell orchestration.

**Variant patterns documented in the ecosystem:**
- **Advisor pattern:** Single Claude Code session where Sonnet runs tools and Fable consults at decision points via the built-in advisor tool
- **Orchestrator pattern:** Fable decomposes into subagent briefs; Opus handles deep reasoning, Sonnet handles mechanical work, Codex CLI provides cross-vendor perspective
- **Cross-vendor variant (fable-advisor v3+):** Replaces Sonnet/Opus implementers with Grok 4.5 (default) or GPT-5.6 Sol (optional) for vendor-diverse implementation — different model families catch different blind spots

## Key takeaways

- Fable's value is in planning and judgment; ~80–90% of tokens are mechanical work that cheaper models handle equally well
- Benchmarked: Sonnet 5 executor + Fable 5 advisor achieves ~92% of Fable solo on SWE-bench Pro at ~63% of the price; Fable orchestrator + Sonnet workers reaches 96% on BrowseComp at 46% cost
- Persistent Codex CLI threads maintain context across the plan→implement→review loop without re-injecting history
- Fable runs safety classifiers on cybersecurity and biology content — if tripped, Claude Code silently reroutes to Opus 4.8; check with `/model` if results seem degraded
- If a pinned Claude model isn't available on the account, Claude Code silently falls back to the session model — the pattern degrades quietly rather than erroring
- The cross-vendor approach (Claude as architect, Grok/GPT as implementers) provides architectural review diversity at the cost of added toolchain complexity

## Security

Pattern itself has no security concerns beyond standard multi-model trust boundaries. Cross-vendor variants send code context to multiple AI providers. Codex CLI requires separate authentication.