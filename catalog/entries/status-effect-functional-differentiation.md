---
name: status-effect-functional-differentiation
title: Functional Differentiation of Status Effects (Fire/Poison/Bleed by Role, Not Magnitude)
url: https://www.instagram.com/reel/DfAdjf6ARg9/
source_url: https://www.instagram.com/reel/DfAdjf6ARg9/
source: instagram
category: agent-pattern
summary: "Game-dev design technique for avoiding redundant damage-over-time status effects — when fire, poison, and bleed differ only in how much damage they deal, players converge on the single strongest one and the rest go unused; the fix is giving each effect a distinct mechanical role instead of a different number. Demonstrated with three effects: fire spreads on kill (igniting the three nearest enemies, which can chain further), poison scales (every 10 stacks adds 10% increased damage taken from all sources), and bleed bursts (at 5 stacks, it detonates all remaining stored damage at once) — giving fire a horde-clearing role, poison a sustained-fight role, and bleed a fast single-target-burst role."
tags:
  - game-design
  - status-effects
  - damage-over-time
  - balance
  - game-development
  - roguelike
  - godot
reviewed: 2026-10-29
acquired: 2026-10-29
license: N/A
security_flags: []
overlaps: []
---

## What it does

A game-design technique for avoiding redundant damage-over-time (DoT) status effects. If several DoT effects (e.g. fire, poison, bleed) differ only in the amount of damage they deal, players converge on whichever one hits hardest and the rest become unused "dead weight" — the fix is to make each effect differ in what it does, not just how big its number is.

Demonstrated redesign for three DoT effects in the in-development game Capy of Gods:

- **Fire spreads**: when an enemy dies while burning, the fire jumps to the three nearest enemies, which can themselves ignite further enemies in a chain — effective against groups/hordes.
- **Poison weakens**: every 10 stacks of poison, the affected enemy takes 10% more damage from all sources (not just poison) — a damage-amplifier that compounds in value over a long fight.
- **Bleed bursts**: at 5 stacks, bleed detonates, dealing all of its remaining stored damage in one instant — suited to finishing off a single target quickly.

Each effect's intended use case follows from its mechanic rather than its numbers: fire for hordes, poison for long fights, bleed for fast single-target kills. Demonstrated in a dev-log reel for Capy of Gods, a pixel-art roguelike built in Godot with a free Steam demo.

## Sources

- [Instagram reel, Capy of Gods dev log](https://www.instagram.com/reel/DfAdjf6ARg9/) — caption, transcript, and on-screen text describing the fire/poison/bleed redesign (catalog source)

## Security

N/A — a game design technique description, not software; no code, binary, or service to install.