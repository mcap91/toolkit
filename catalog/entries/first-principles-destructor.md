---
name: first-principles-destructor
title: First Principles Destructor
url: "https://github.com/reshadat/first-principles-destructor"
category: skill
summary: "6-stage assumption-destruction skill — inventories hidden assumptions, strips to physics/math/logic floor, calculates 'convention tax', removes non-load-bearing conventions, rebuilds from reality; multi-platform (Claude Code, Codex, Gemini, Cursor, Kiro); MIT"
tags: [first-principles, reasoning, skill, multi-platform]
reviewed: 2026-06-22
acquired: 2026-06-22
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

A SKILL.md-based prompt skill that runs a structured 6-stage process on any statement, belief, or process:

1. **Assumption Inventory** — surfaces 5–15 hidden assumptions
2. **Reality Floor** — strips convention; what do physics/math/logic actually require?
3. **Convention Tax Calculator** — quantifies the cost of maintaining each assumption
4. **Assumption Removal Test** — what breaks, what costs more, what's purely optional?
5. **Rebuilt Version** — reconstruct from reality, not habit
6. **First Mover Question** — if this rebuilt version is possible, why doesn't it exist yet?

Multi-platform installer covers Claude Code (global/project), Gemini CLI, Codex CLI, Cursor (.mdc rules), Kiro (.kiro/steering), and Claude.ai (.skill ZIP upload).

## Assessment

Well-structured thinking framework packaged as a portable skill. The "convention tax" framing is the novel contribution — forcing quantification of what each assumption costs rather than just listing assumptions. The multi-platform packaging (install.sh with flags for each agent) is a good reference for cross-platform skill distribution.

Useful for strategic/architecture decisions and challenging "we've always done it this way" patterns. The 6-stage pipeline is rigid enough to be repeatable but open enough to apply to technical, business, or process questions.

## Mechanical details

- Install: `./install.sh --claude-global` (or `--claude-project`, `--gemini`, `--codex`, `--cursor`, `--kiro`, `--all-global`)
- Trigger: `/first-principles [statement]` or natural language ("destroy this assumption", "what's the convention tax on")
- Core file: `SKILL.md` — portable to any SKILL.md-compatible agent
- Cursor: `.cursor/rules/first-principles.mdc`
- Kiro: `.kiro/steering/first-principles.md`

## Security

- **License**: MIT
- **Content**: pure prompt skill, no code execution, no dependencies
- **Install script**: shell script that copies files to agent skill directories — review before running
- **Single contributor**: small repo, but the skill is just a markdown file