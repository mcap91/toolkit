---
name: aaa-quality-gate-orchestration
title: AAA Quality-Gate Multi-Agent Orchestration
url: "https://example.com"
category: agent-pattern
summary: "A prompt architecture for orchestrating multi-agent development with built-in quality verification — architecture-first design docs, screenshot-based verification loops, dependency-ordered builder waves, and a critic agent that scores against reference screenshots before passing quality gates"
tags: [multi-agent, orchestration, quality-gates, critic-loop, game-development, 3d-modeling, modular-architecture, verification]
reviewed: 2026-09-02
acquired: 2026-09-02
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it does

A prompt architecture for orchestrating multi-agent development of complex software with built-in quality verification. The pattern was demonstrated building a Cities: Skylines II–class city builder in Three.js, but the structural principles generalize to any multi-subsystem project requiring visual or functional quality gates.

**Architecture-first:** Before any code, agents produce an architecture document defining folder structure, module APIs, events, units, determinism constraints (seeded RNG only), a performance budget, and an asset policy. Module failures are isolated so one broken subsystem never takes the whole project down.

**Verification loop before features:** A headless-Chrome screenshot tool captures the app state with camera presets and time-of-day settings, outputting PNGs plus a JSON log (console errors, fps, draw calls). Every module ships a "showcase" mode for isolated testing. No agent may claim completion without screenshot evidence.

**Fan-out by dependency:** Builder agents each own a single module folder. They run in waves ordered by dependency: (1) terrain, sky, roads, simulation, UI, audio, effects; (2) zoning, buildings, props, traffic, tools; (3) demo integration. Between waves, an integrator agent — the only one allowed to touch shared core code — applies builders' change requests and fixes seams.

**Critic gauntlet:** After each builder round, a separate critic agent (writes no code) takes screenshots at several times of day and zoom levels, checks API contracts and performance, and scores 0–10 against reference screenshots. Pass threshold is 8.5/10 with zero errors. Below that, the builder receives a ranked issue list and iterates, up to 4 rounds.

**Persistent scoring:** Scores and open issues persist to a STATUS.json so each iteration resumes from the weakest module rather than restarting from scratch.

## Mechanical details

- **Module isolation:** One builder agent per subsystem folder, no cross-module edits. Core changes route through the integrator.
- **Quality scoring:** 10 = indistinguishable from reference, 8.5 = AAA with minor nits, 7 = good indie, 5 = programmer art. Pass = ≥8.5 + zero console errors.
- **Blind final gate:** Whole-game screenshots are paired with reference screenshots (labels shuffled A/B) for blind comparison judging.
- **Iteration cap:** Builders get up to 4 rounds to meet the critic's threshold before the loop moves on.
- **Determinism:** Seeded RNG only, ensuring reproducible builds across agent runs.
- **Dev server kept live:** The application stays running throughout so other agents can screenshot it at any time.

## Security

Prompt-only pattern with no installed dependencies. The headless-Chrome screenshot tool requires browser automation access. Asset policy restricts to CC0-licensed sources (Poly Haven, ambientCG, procedural) to avoid licensing issues.