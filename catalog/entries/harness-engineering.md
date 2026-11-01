---
name: harness-engineering
title: Harness Engineering (Fowler / Böckeler)
url: "https://martinfowler.com/articles/harness-engineering.html"
category: reference
summary: "Martin Fowler article defining Agent = Model + Harness — taxonomy of agent controls: guides (feedforward) vs sensors (feedback), computational (deterministic) vs inferential (LLM-based), across three regulation levels (maintainability, architecture fitness, behavior); behavior verification identified as largely unsolved"
tags: [harness, agent-architecture, testing, linting, feedforward, feedback, controls-taxonomy]
reviewed: 2026-07-01
acquired: 2026-07-01
license: unlicensed
security_flags: []
overlaps: []
source: unknown
---

## What it says

Birgitta Böckeler's article on martinfowler.com frames AI agent architecture as Agent = Model + Harness, where the harness is everything except the model itself — the control system that makes model output trustworthy.

The harness taxonomy has two orthogonal dimensions:

**Control direction:**
- **Guides (feedforward)**: Rules that steer the agent before it acts (system prompts, CLAUDE.md rules, templates)
- **Sensors (feedback)**: Checks that verify after the agent acts and enable self-correction (tests, linters, type checkers)

Both are needed: feedback-only means the agent keeps repeating the same mistakes; feedforward-only means you never find out if your rules work.

**Control type:**
- **Computational**: Deterministic and fast — tests, linters, type checkers
- **Inferential**: Semantic, done by an LLM — slower and non-deterministic but understands meaning

**Three regulation levels:**
1. **Maintainability** (code quality) — easiest to regulate
2. **Architecture fitness** (architectural rules via fitness functions) — medium difficulty
3. **Behavior** (functional correctness) — hardest, still largely unsolved; current approaches rely on AI-generated tests + manual checking

## Key takeaways

- The model is still the brain; the harness directs human attention to where it matters instead of everywhere
- Computational controls (tests, linters) are the foundation — fast, deterministic, reliable
- Inferential controls (LLM-based review) fill semantic gaps but are non-deterministic
- Functional correctness verification remains the hardest unsolved problem in agent engineering
- The taxonomy (feedforward/feedback × computational/inferential × three levels) provides a structured way to audit harness coverage

## Security

Article/reference — no code to audit.

## Usage notes

- **Two practical consequences of model-as-cartridge design**: (1) When evaluating models, ensure you're comparing models, not harnesses — a "worse" model in a better harness often beats a stronger model in a naive one; most public agent benchmarks quietly measure both at once. (2) Design your agent so the model is one config line — if tool schemas, prompts, and loop logic are tangled around one vendor's API quirks, you've built a machine you cannot upgrade; a thin adapter layer between loop and model pays for itself the first time a better model ships.
