---
name: disney-animation-principles-game-vfx
title: Disney's Animation Principles Applied to Game VFX (Anticipation, Squash & Stretch, Follow Through, Timing, Arcs)
url: https://www.instagram.com/reel/DejpGOctoHu/
source_url: https://www.instagram.com/reel/DejpGOctoHu/
source: instagram
category: agent-pattern
summary: Game-dev technique for making a combat VFX effect (demonstrated on a thrown fireball) read as satisfying by applying five of Disney's twelve classical animation principles instead of adding more particles or better shaders — anticipation (the hero leans back while the fire gathers, then throws), squash and stretch (the fireball stretches in flight, the enemy squashes on hit), follow through (the hero's body settles after the throw, the trail lags behind, the burst flies on), timing (freeze the game for a few frames on the hit, i.e. hit-stop), and arcs (the fireball, sparks, and damage numbers travel on curved rather than straight paths). Framed as the same underlying asset read as flat or alive purely based on which of these principles are layered on top, independent of particle count or shader quality.
tags:
  - game-design
  - game-feel
  - juice
  - animation-principles
  - squash-and-stretch
  - anticipation
  - follow-through
  - hit-stop
  - vfx
  - game-development
reviewed: 2026-10-30
acquired: 2026-10-30
license: N/A
security_flags: []
overlaps: []
---

## What it does

Demonstrates, via a before/after fireball VFX comparison, that five of Disney's classical animation principles — not particle count or shader quality — are what make a game effect feel alive. The reel pairs each principle with a concrete application to a thrown-fireball attack: (1) **anticipation** — the hero leans back while the fire gathers before throwing, signaling the action before it happens; (2) **squash and stretch** — the fireball stretches along its flight path, and the enemy squashes on impact, communicating velocity and force; (3) **follow through** (and overlapping action) — the hero's body continues settling after the throw, the fireball's trail lags behind the head of the effect, and the burst continues expanding after the main impact; (4) **timing** — the game briefly freezes on the hit (a hit-stop/freeze-frame), giving the impact weight; (5) **arcs** — the fireball, its sparks, and the resulting damage numbers all travel on curved rather than straight paths. The claimed takeaway is that the same base asset (particles, glow, fireball shape) reads as flat in the "before" version and satisfying in the "after" version purely from applying these five principles, and that the principles themselves are roughly 90 years old (attributed to Disney animators of the 1930s) and still apply directly to real-time game VFX.

## Sources

- [Instagram reel, "The Disney Secret to Juicy, Satisfying Animation"](https://www.instagram.com/reel/DejpGOctoHu/) — caption, transcript, and before/after demonstration walking through the five principles applied to a fireball effect (catalog source).
- [Open Culture, "Disney's 12 Timeless Principles of Animation"](https://www.openculture.com/2014/05/disneys-12-timeless-principles-of-animation.html) — independent coverage of the full 12-principle set.
- Frank Thomas and Ollie Johnston, *The Illusion of Life: Disney Animation* (1981) — the principles were developed as practical technique by Disney's animation team through the 1930s (including on *Snow White and the Seven Dwarfs*) and later formally codified and named in this book by two of Disney's "Nine Old Men" animators.
- [mygamedesign.com, "How Do You Make Melee Combat Feel Crunchy and Satisfying?"](https://mygamedesign.com/how-do-you-make-melee-combat-feel-crunchy-and-satisfying/) — independent game-design coverage describing hit-stop (brief simulation freeze on impact, commonly a handful of frames to roughly 35–90ms) and squash-and-stretch as the same Disney animation principles applied directly to combat-hit feedback, distinct from the `health-bar-chip-damage-feedback` and `boss-fight-entrance-design` catalog entries, which cover other game-feel techniques (UI damage feedback and encounter staging, respectively).

## Security

N/A — an animation/VFX design technique description, not software; no code, binary, or service to install. No security-relevant claims.
