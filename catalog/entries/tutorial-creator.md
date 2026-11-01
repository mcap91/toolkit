---
name: tutorial-creator
title: Tutorial Creator
category: skill
summary: good for knowledge retention and onboarding
tags: [tutorials, onboarding, knowledge-retention]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it does

Converts code sessions and Claude conversations into structured tutorials with vocabulary, a pre-test, a step-by-step walkthrough, common mistakes, and a post-test. Transforms work that would otherwise be lost after a session into reusable learning material. Useful for capturing non-obvious workflow decisions, pipeline quirks, and tool-specific gotchas discovered during active development.

## Assessment

Bioinformatics workflows accumulate tacit knowledge — why a particular normalization approach was chosen, what a cryptic error message means, how to interpret QC plots. Tutorial Creator makes that knowledge explicit and transferable. Good for onboarding collaborators to established pipelines or creating reference materials from exploratory analysis sessions.

## Mechanical details

Source is a Reddit r/claudeskills post. No public repo URL confirmed at review time. Pilot by running it on one completed analysis session to evaluate output quality and tutorial structure before broader adoption.

## Security

Tutorial Creator is a Claude Code skill implemented as a SKILL.md prompt file with no associated binary, package dependency, or network component. Its attack surface is limited to the prompt text itself: a malicious or tampered SKILL.md could influence model behavior through injected instructions, so the file should be reviewed before installation and sourced only from trusted channels. No external data is fetched at runtime and no code is executed outside the normal Claude Code conversation context, so supply-chain and execution risks are negligible.
