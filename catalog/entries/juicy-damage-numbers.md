---
name: juicy-damage-numbers
title: Nine-Step Juicy Damage Number Technique (Pop, Float, Fade, Arc, Scale, Color, Crit FX, Stack, Randomize)
url: https://www.instagram.com/reel/DcDs7f9uaqo/
source_url: https://www.instagram.com/reel/DcDs7f9uaqo/
source: instagram
category: agent-pattern
summary: Game-dev technique for upgrading a default floating-damage-number label into "juicy" feedback through a stack of independent, optional tweaks rather than one fix — pick a legible display font (the reel uses Bungee from Google Fonts), pop the number in on spawn instead of just appearing, float it upward as it arrives, fade it out at the end of its lifetime, give each digit an arc-like falling offset instead of a straight rise, scale its size by the damage value so bigger hits read as bigger, shift its color over time based on which action produced it, layer particles and screen shake onto critical hits using the same logic, experimentally stack numbers on very fast multi-hit attacks, and randomize each number's spawn offset so a burst of hits doesn't render as a single overlapping stack. Framed as a menu of optional, independently-applicable steps rather than a required pipeline, and as engine-agnostic (the creator states it applies to any game engine).
tags:
  - game-design
  - damage-numbers
  - game-feel
  - juice
  - ui-feedback
  - vfx
  - screen-shake
  - particles
  - game-development
reviewed: 2026-10-30
acquired: 2026-10-30
license: N/A
security_flags: []
overlaps: []
---

## What it does

A checklist of independent visual tweaks for turning a bare floating-damage-number label into "juicy" feedback, demonstrated by upgrading a default implementation (a plain number that appears and disappears with no animation) step by step: (1) choose a legible display font first — the reel uses Bungee from Google Fonts; (2) pop the number in with a scale/spawn animation rather than having it appear instantly; (3) float it upward as it arrives; (4) fade it out once its on-screen lifetime ends; (5) give it an arc-like falling offset per digit/number instead of a straight vertical path; (6) scale its size based on the damage value, so larger hits render larger; (7) shift its color over time based on the action that produced it (e.g. normal hit vs. heal vs. DoT); (8) apply the same particle-and-screen-shake treatment used elsewhere in the game to critical hits specifically; (9) on very fast multi-hit attacks, experiment with stacking numbers rather than showing each individually; (10) randomize each number's spawn offset so a cluster of near-simultaneous hits doesn't render as one illegible overlapping stack. Presented explicitly as an optional menu — "you don't have to follow all or apply all, whichever suits your feel" — and as implementable in any game engine, not tied to one toolchain.

## Sources

- [Instagram reel, "How to make juicy damage numbers"](https://www.instagram.com/reel/DcDs7f9uaqo/) — caption, transcript, and key-claims walkthrough of the nine-step technique (catalog source).
- [GameJuice, "Damage Numbers: Turning Abstract Stats into Satisfying Feedback"](https://www.gamejuice.co.uk/articles/damage-numbers-satisfying-feedback) — independent design article on damage-number legibility (font weight, stroke/outline), handling high-frequency/AoE hit volume, and tiering feedback intensity by event significance.
- [Acagamic, "Show Juicy Feedback to Indicate Player Damage in Video Games"](https://acagamic.com/newsletter/2022/03/08/show-juicy-feedback-to-indicate-player-damage-in-video-games/) — independent newsletter piece on floating combat text as one channel of "juicy" feedback for player damage, and the immersion/feedback tradeoff that motivates it.
- Martin Jonasson & Petri Purho, "Juice It or Lose It" (GDC 2012) — the commonly cited origin talk for the general "juice" vocabulary (squash, particles, color, sound layered onto an unchanged core loop) that this technique applies specifically to damage numbers.

## Security

N/A — a UI/VFX design technique description, not software; no code, binary, or service to install. No security-relevant claims.