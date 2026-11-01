---
name: gsap-animation-expert
title: GSAP Animation Expert Skill
url: "https://mcpmarket.com/tools/skills/gsap-animation-expert"
category: skill
summary: "Claude Code skill providing GSAP (GreenSock Animation Platform) animation expertise — timelines, ScrollTrigger, SVG morphing, stagger patterns, easing, and React integration via the useGSAP hook. Covers basic tweens, position parameters, horizontal scroll sections, text split animations, and scroll-reveal patterns. Single SKILL.md file. Attributed to Brookside BI."
license: ""
tags: [gsap, greensock, animation, javascript, react, scrolltrigger, skill, claude-code, web-development]
reviewed: 2026-07-28
acquired: 2026-07-28
overlaps: [motion-design-skill]
security_flags: []
source: unknown
---

## What it is

GSAP Animation Expert is a Claude Code skill that teaches the agent to use the GreenSock Animation Platform (GSAP) for JavaScript animations. It covers the core GSAP API (to, from, fromTo, set), timeline orchestration with position parameters, ScrollTrigger for scroll-driven animations, stagger configurations (simple, grid-based, function-based), easing functions (power, elastic, bounce, custom bezier), and React integration via the `useGSAP` hook with automatic cleanup.

The skill includes ready-to-use patterns for:
- Reveal-on-scroll animations
- Horizontal scroll sections with snap
- Text split character-by-character reveals
- Logo/loading sequence orchestration
- Pin-and-scrub scroll storytelling

It also covers transform properties (x/y/rotation/scale/skew with 3D variants), special properties (autoAlpha, repeat, yoyo), and performance considerations.

## Mechanical details

- **Format:** Single SKILL.md with YAML frontmatter, inline TypeScript/JSX code examples
- **Install:** Listed on mcpmarket.com; copy the SKILL.md into `.claude/skills/`
- **Triggers:** User mentions "GSAP", "GreenSock", "timeline animations", or works with ScrollTrigger/MorphSVG files
- **Dependencies:** `gsap` npm package; `@gsap/react` for React integration
- Attributed to Brookside BI; no GitHub repository found. No license stated.

## Security

No runtime component — instructional Markdown only. No license declared in the observed material; verify terms before use. No security flags observed. Note: GreenSock's official skill pack exists at `greensock/gsap-skills` and may be preferable as the authoritative source.