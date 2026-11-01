---
name: motion-design-skill
title: Motion Design Skill
url: "https://github.com/LottieFiles/motion-design-skill"
category: skill
summary: "LottieFiles agent skill teaching universal, implementation-agnostic motion-design principles — timing, easing, choreography, and Disney's 12 principles adapted for UI — so agents choose motion intent before writing animation code. Works with any system (CSS, Framer Motion, GSAP, Lottie, Spring); ships philosophy, pattern recipes, and reference tables. Installs via npx skills add. MIT."
license: MIT
tags: [motion-design, animation, ui, skill, claude-code, css, framer-motion, gsap]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it is

Motion Design Skill (by LottieFiles) is a philosophy-first, implementation-agnostic agent skill that teaches coding agents to "think like motion directors" — choosing timing, easing, choreography, and emotional intent before writing any animation code. It is framework-agnostic, applying to CSS, Framer Motion, GSAP, Lottie, Spring, and others, and states support for 40+ agents including Claude Code, Cursor, Codex, and GitHub Copilot.

The skill activates for UI animations, micro-interactions/feedback, loading/success/error states, scroll- or progress-driven animation, brand motion identity, and multi-element choreography. It is organized into:

- **Core (`SKILL.md`)** — 8-step checklist, motion-personality archetypes, duration/easing tables, property-selection guide, common patterns, quality rules
- **director/** — three pillars, Disney's 12 principles adapted for UI, emotion→motion mapping, choreography, narrative structure, context/accessibility/performance adaptation
- **patterns/** — entrance/exit, state feedback, ambient/continuous, multi-element stagger recipes
- **reference/** — timing/easing tables, property selection, quality checklist, troubleshooting

## Mechanical details

- **Install:** `npx skills add LottieFiles/motion-design-skill`
- Format: a Claude Code / agent skill with a core `SKILL.md` (<500 lines) plus `director/`, `patterns/`, and `reference/` supporting Markdown
- Example prompts include adding entrance animations, building state transitions, and choreographing dashboard entrance sequences

## Security

MIT licensed. The skill is instructional Markdown (motion-design guidance and recipes) with no runtime component of its own; review the files before use. No security flags recorded from the observed material.

## How to use it

npx skills add LottieFiles/motion-design-skill
