---
name: taste-skill
title: Taste Skill
url: "https://github.com/leonxlnx/taste-skill"
category: skill
summary: "Collection of portable SKILL.md files (design-taste-frontend and variants) that give AI coding agents layout/typography/motion/spacing guidance intended to reduce generic-looking generated UI, plus separate image-generation skills for design reference boards"
tags: [frontend, design, anti-slop, ui-generation, claude-code-skill, codex, motion-design, typography, skill-bundle]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: [sponsored-content]
overlaps: [impeccable, suede-creator-skills, ui-ux-pro-max-skill]
source: unknown
---

## What it does

Taste Skill is a repository of `SKILL.md` instruction files positioned as an "anti-slop frontend framework" — portable guidance meant to shift AI-generated interfaces away from generic/templated-looking layout, typography, motion, and spacing. The primary skill, `design-taste-frontend` (v2, described as an "experimental" rewrite of v1), infers a design language from the user's brief, maps it against a design-system reference, and applies three numeric 1-10 dials: `DESIGN_VARIANCE` (layout experimentation), `MOTION_INTENSITY` (animation depth), and `VISUAL_DENSITY` (information per viewport). The prior version is preserved separately as `design-taste-frontend-v1` for projects depending on its exact behavior.

Additional variants in the same repo: `gpt-taste` (stricter rules tuned for GPT/Codex), `image-to-code` (generate reference images, then implement from them), `redesign-existing-projects` (audit-then-fix for existing UIs), `high-end-visual-design`/`minimalist-ui`/`industrial-brutalist-ui` (fixed visual-direction variants), `full-output-enforcement` (targets agents that truncate or leave placeholder code), and `stitch-design-taste` (compatible with Google Stitch's `DESIGN.md` export format). Three further skills (`imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`) produce reference images only (no code), intended for use with image-generation tools before handing results to a coding agent.

## Differentiators

- Ships multiple narrow variants (style-locked, model-specific, redesign-vs-greenfield, image-vs-code) rather than one general skill, letting a user pick a specific behavior instead of one skill trying to cover every case.
- Framework-agnostic by design intent — rules target visual/design decisions rather than a specific component API, per the README (React, Vue, Svelte cited as tested).
- Distributed both as installable skills (`npx skills add`, a third-party skill-installer CLI) and as copy-paste `SKILL.md` files for direct use in a repo or pasted into a chat session.

## Mechanical details

- Install all skills: `npx skills add https://github.com/Leonxlnx/taste-skill`
- Install one skill by its `name:` frontmatter value (not folder name), e.g. `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`
- A `CHANGELOG.md` documents the v1-to-v2 diff and rationale for the default skill.
- Background research notes referenced (not fully reproduced in the fetched README) live in a `research/` directory in the repo.

## Security

MIT licensed (repo copyright 2026 Leonxlnx). Content is instructional Markdown consumed as agent context — no executable code ships with the core skills, so there is no install-time code-execution surface beyond whatever the `npx skills add` installer itself does. The README embeds paid sponsor placements for unrelated third-party products (a WordPress-access tool and a "launch kit" template service) directly in the project's front matter/marketing sections; since `SKILL.md` files are loaded into an agent's context on every session, any repo that mixes promotional or unreviewed third-party content into its documentation is worth reviewing before installing, even though the sponsor content observed here sits in the README rather than inside the skill files themselves. The README also explicitly disclaims any official cryptocurrency token bearing the project's name, noting unaffiliated tokens have been created using the author's name/image. Maintenance is credited to two individuals (`lexnlin`, `blueemi99`) with feedback channels via GitHub issues/PRs, Discord-style DMs, and email — a small, informal maintainer base for a fast-growing repo.