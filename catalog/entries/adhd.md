---
name: adhd
title: ADHD
url: "https://github.com/UditAkhourii/adhd"
category: skill
summary: "parallel divergent ideation via isolated cognitive frames; overlaps with superpowers:brainstorming but the frame isolation and scoring mechanics are worth studying"
tags: [ideation, brainstorming, parallel, divergent-thinking, cognitive-frames, subagents]
reviewed: 2026-05-27
acquired: 2026-05-27
overlaps: [superpowers-brainstorming]
license: MIT
security_flags: []
source: unknown
---

## What it does

A Claude Code skill that implements parallel divergent ideation by spawning N isolated reasoning branches under deliberately distorted cognitive frames, then applying a separate critic pass to evaluate and converge. Two-phase architecture: Phase 1 (Diverge) selects 5 of 14 cognitive frames (hardware engineer, regulator, 10-year-old, competitor, biology, logistics, game design, markets, inversion, extreme budget/timeline, speedrunner, ant colony, 3am on-call) and spawns parallel Agent calls where each generates 6 ideas in structured JSON with zero shared context. Phase 2 (Focus) scores ideas 0-10 on novelty/viability/fit (weighted 0.35/0.40/0.25), clusters by underlying angle, and deepens top 3 with mechanics sketches, load-bearing risks, first concrete steps, and child ideas. Default run: 5 frames x 6 ideas = 30 candidates, ~10 LLM calls, ~$0.30.

Also available as a CLI (`npm install -g adhd-agent; adhd "your problem"`) and TypeScript library. MIT licensed, requires Node 18+.

## Assessment

The `superpowers:brainstorming` skill already covers divergent ideation in our stack. ADHD's distinguishing mechanics — strictly isolated parallel branches with zero shared context during divergence, a fixed frame library, and quantitative scoring with trap detection — are worth studying as potential enhancements to the brainstorming skill. The frame isolation invariant (serialization collapses the method) is the strongest novel contribution. However, installing it alongside superpowers:brainstorming would create routing ambiguity for the same trigger conditions.

## Mechanical details

Install: `npx skills add UditAkhourii/adhd` or manual curl of `SKILL.md`. Trigger: user types `/adhd` or conditions match (open-ended answer space, high cost of wrong obvious answer, open phrasing). Anti-patterns documented: convergence disguised as divergence, weird-for-weird's-sake, unstructured prose, refusing to commit, simulating parallel branches sequentially. If piloting, disable or rename the brainstorming skill to avoid conflicts.

## Security

Licensed MIT — permissive, no copyleft obligations. No security flags apply.

This is a Claude Code skill (a SKILL.md prompt file) installed via `npx skills add`. It runs entirely as prompt instructions inside the agent harness — no external code execution, no network calls, no credential storage. The optional CLI (`npm install -g adhd-agent`) and library (`npm install adhd-agent`) are Node.js packages that make LLM API calls using the caller's existing API key; no new credential surface is introduced beyond what the host agent already holds. Dependency risk is low: the package is small and MIT-attributed by all known forks and adopters. Audit `package.json` before installing the npm package if that surface matters.

## How to use it

npx skills add UditAkhourii/adhd
