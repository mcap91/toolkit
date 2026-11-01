---
name: awesome-gamedev-agent-skills
title: awesome-gamedev-agent-skills
url: https://github.com/gamedev-skills/awesome-gamedev-agent-skills
category: plugin
summary: A library of 77 Agent Skills for game development spanning 12 engines (Godot, Unity, Unreal, Ebitengine, Phaser, PixiJS, three.js, Bevy, pygame, LOVE, Defold, Roblox), plus cross-engine discipline, genre-template, and workflow skills, installed via a router that detects the project's engine from project files and loads only the matching skills
tags:
  - agent-skills
  - game-development
  - godot
  - unity
  - unreal
  - claude-code-plugin
  - router
  - skill-library
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: Apache-2.0
security_flags: []
source: instagram
source_url: https://www.instagram.com/reel/De8q9xDETx-/
---

## What it does

awesome-gamedev-agent-skills is a curated library of Agent Skills (SKILL.md files, Anthropic's
open Agent Skills standard) for game development. It contains 77 skills:

- **Engine skills (across 12 engines):** Godot (16), Unity (8), Unreal (6), plus Ebitengine,
  Phaser, PixiJS, three.js, Bevy, pygame, LOVE, Defold, and Roblox
- **15 cross-engine discipline skills:** AI, procedural generation, audio, shaders, physics, etc.
- **9 genre template skills:** platformer, roguelike, RPG, FPS, tower defense, card games,
  visual novels, survival-crafting, puzzle
- **4 workflow skills:** game jams, prototyping, Steam/itch publishing

A router detects the project's engine from project files (`project.godot`, `*.uproject`, etc.),
analyzes the user's request for task/genre/concept, and loads only the matching skills in
priority order (engine basics, then discipline, then genre) — e.g. "add a double jump to my
Godot player" loads just `godot-2d-movement` and `platformer`.

A separate `create-game-assets` skill is an art-direction/production pipeline: it locks a visual
target, builds asset families, normalizes outputs deterministically, and checks them in-game to
keep art style consistent across a project.

Skills are version-pinned to specific engine releases (Godot 4.7, Unity 6.3 LTS, Unreal 5.8,
etc.) and claimed to be sourced from official engine docs. All skills pass a Python validator
(`validate-skills.py`) before merge.

## Installation

```bash
npx skills add gamedev-skills/awesome-gamedev-agent-skills
```

Detects the installed agent (Claude Code, Cursor, Windsurf, Cline, Copilot, Gemini CLI, etc.)
and installs skills to that agent's local skill directory. Manual installation by copying
folders into an agent's skills directory is also supported.

## Security

Skills are plain Markdown data files with no bundled scripts observed in the repo structure, so
there is no code execution surface in the repo itself beyond what any loaded SKILL.md instructs
the host agent to do. Apache-2.0 license, ~5.6k GitHub stars, ~531 forks, maintained by Abhishek
Barali as of 2026-10-29.

## Usage notes

- A promoted Instagram reel describes the pack as "74 skills"; the README (checked 2026-10-29)
  states 77 skills — the reel's figure is out of date or imprecise (source: https://www.instagram.com/reel/De8q9xDETx-/)