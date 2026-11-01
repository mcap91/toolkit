---
name: claude-skill-steelman
title: Claude Skill Steelman
url: "https://github.com/techiejd/claude-skill-steelman"
category: skill
summary: "Single-purpose /steelman skill that pressure-tests decisions by arguing strongest alternatives at full strength — anti-sycophancy focused, context-specific; overlaps with doubt-driven-development (agent-skills) and superpowers:brainstorming"
tags: [decision-making, anti-sycophancy, claude-code, skill]
reviewed: 2026-06-25
acquired: 2026-06-25
license: MIT
security_flags: []
overlaps: [agent-skills-osmani]
source: unknown
---

## What it does

A single Claude Code skill invoked via `/steelman`. When a user states a direction (e.g., "We're going with Postgres"), the skill makes Claude genuinely argue for the 2–3 strongest alternatives — not devil's advocate theater, but real arguments rooted in the specific project context. Outputs: blind spots in the current choice (2–4 bullets), full-strength alternative arguments, an honest assessment of whether the original choice survived scrutiny, and a decision prompt (proceed/reconsider/investigate).

Claude may also auto-suggest invoking the skill when it detects high-stakes decisions in context (architecture, technology selection, strategic pivots), but never auto-triggers.

## Assessment

Well-scoped single skill solving a real problem: momentum bias in architecture and technology decisions. The anti-sycophancy focus is explicit — the README calls out that if Claude returns a generic pros/cons list or "your choice is still solid," the skill didn't load properly.

However, this is a narrow slice of what doubt-driven-development (from agent-skills-osmani) and superpowers:brainstorming already cover. Doubt-driven-development provides a full CLAIM → EXTRACT → DOUBT → RECONCILE → STOP pipeline with optional cross-model escalation. The steelman skill's value is in its simplicity — one slash command, one purpose — but it doesn't add capability beyond what's already available.

Single contributor, small repo, no tests or CI. Useful as a pattern reference for anti-sycophancy skill design.

## Mechanical details

- Install: `git clone` into `~/.claude/skills/steelman/` or `curl` the SKILL.md
- Single file (SKILL.md), no dependencies
- Requires user to state a direction first — not for open-ended "X or Y?" questions
- Tested primarily on Opus/Sonnet; smaller models may revert to hedging

## Security

MIT license, single Markdown file, no code execution, no dependencies. No security concerns.