---
name: brogue-ce
title: "Brogue: Community Edition"
url: https://github.com/tmewett/BrogueCE
category: cli-tool
summary: Community-maintained fork of Brian Walker's Brogue roguelike — seeded procedural dungeon generator that places rooms by sliding candidates until a door meets an existing wall without overlap, cuts extra doors between far-apart floor areas to add loops, and shapes lakes with a 5-round cellular-automaton smoothing pass gated by a connectivity check; C, SDL2, 26 playable levels, 1.5k stars/197 forks; AGPL-3.0.
tags:
  - procedural-generation
  - dungeon-generation
  - roguelike
  - cellular-automaton
  - game-dev
  - seeded-random
  - c
  - sdl2
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: AGPL-3.0
security_flags:
  - requires-manual-source-build
source: instagram
source_url: https://www.instagram.com/reel/DegQ9xiIESl/
---

## What it does

Brogue: Community Edition continues development of Brian Walker's Brogue, a single-player roguelike where the player descends 26 dungeon levels to retrieve the Amulet of Yendor, with randomly-generated floors and permadeath. CE is maintained by tmewett under a benevolent-dictator model, with contributions from testers and developers coordinated via GitHub issues and a Discord server. Builds exist for Windows, macOS, and Linux (SDL2/SDL2_image), plus a separately-maintained Android port.

## Mechanical details

- Dungeon generation (`src/brogue/Architect.c`, `createDungeon(grid)`) starts from solid rock, carves one room, then generates candidate rooms and slides each across the map until one of its doors meets an existing wall without overlapping any placed room; a capped number of candidate attempts (`roomAttempts(grid, n)`) are tried per floor — a reel-captured example ran 35 attempts after the first room and kept 20 rooms.
- Once rooms are placed, doors are added between adjacent floor areas that are more than a fixed walking-distance threshold apart, creating loops instead of only dead-end connectivity.
- Lakes are generated from random noise smoothed by repeated rounds of an eight-neighbor cellular-automaton fill rule (a cell fills if enough of its neighbors are filled), then accepted only if the floor remains fully connected with the lake in place — rejected lake placements are discarded.
- Liquid type in a lake varies with dungeon depth (e.g., lava at deeper floors).
- Generation is deterministic: the same seed number produces the same dungeon for a given dungeon-version build.
- 990 commits on master, 1.5k stars, 197 forks, 161 open issues, 46 open PRs as of this review.

## Security

Source-available under AGPL-3.0-or-later; builds from C source with SDL2/SDL2_image. No prebuilt binaries are referenced as the primary distribution path for all platforms (macOS build is unsigned). No network calls or telemetry documented — a local, offline game.

## Usage notes

- A reel visualized the generator by redrawing BrogueCE's own game-generated map data for a single seeded floor with players, monsters, and items stripped out, adding color/labels to the room-placement, door/loop, and lake-smoothing steps for explanation (source: https://www.instagram.com/reel/DegQ9xiIESl/).
