---
name: ui-ux-pro-max-skill
title: UI/UX Pro Max Skill
url: "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill"
category: skill
summary: comprehensive design system generation but focused on general web/mobile UI; evaluate when dashboard/report aesthetics become a priority
tags: [ui, ux, design-system, typography, color-palettes, dashboards, visualization]
license: MIT
security_flags: []
reviewed: 2026-05-25
acquired: 2026-05-25
overlaps: [web-artifacts-builder]
source: unknown
---

## What it does

An AI skill that enhances Claude Code with professional UI/UX design capabilities. Uses 161 industry-specific reasoning rules to generate complete design systems (styles, colors, typography, components) matched to product type. Includes databases of 67 UI styles, 161 color palettes, 57 typography pairings, 25 chart types, and 99 UX/accessibility guidelines. Supports React, Next.js, Vue, Svelte, Angular, SwiftUI, Flutter, and more. Generates via MASTER.md persistence file with page-specific overrides. 82.7k stars, MIT licensed.

## Assessment

We already have Web Artifacts Builder for interactive HTML reports/dashboards. UI/UX Pro Max goes much deeper into design systems — its 25 chart types and dashboard-specific guidance could improve data visualization quality for bioinformatics QC reports and analysis dashboards. However, our primary output is scientific data visualization, not consumer-facing UI. The skill's strength (industry-matched design systems for web/mobile products) doesn't align with our core need. Revisit if we build user-facing tools or need polished dashboards beyond what Web Artifacts Builder provides.

## Mechanical details

- CLI install: `npm install -g uipro-cli` then `uipro init --ai claude` in project
- Marketplace: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`
- Generates MASTER.md design system file persisting across sessions
- Supports page-specific override files for targeted customization
- Anti-pattern awareness (e.g., "no AI purple/pink gradients for banking")

## Security

UI/UX Pro Max is MIT-licensed and ships no server-side components — all design intelligence is bundled as local CSV data files and a Python search script. The `uipro-cli` npm package performs a one-time download from GitHub to install skill assets into the project's `.claude/skills/` directory; after that initial fetch the skill runs fully offline and makes no network calls during normal use. The `--offline` flag can be passed to `uipro init` to skip the GitHub download entirely and use the bundled assets from the npm package.

The main supply-chain surface is the `uipro-cli` npm package itself and the Python script it installs (`scripts/search.py`). No credentials, tokens, or environment secrets are read or exposed by the skill. The skill does not execute arbitrary code at install time beyond copying files; however, as with any third-party Claude Code skill, the installed SKILL.md is loaded into the agent context on every session, so any prompt-injection payload embedded in a malicious update would be in-context. Pin to a reviewed version (`uipro versions`) and audit updates before upgrading in sensitive environments.

## How to use it

npm install -g uipro-cli && uipro init --ai claude
