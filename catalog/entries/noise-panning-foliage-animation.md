---
name: noise-panning-foliage-animation
title: Noise-Panning Foliage Animation (Perlin Noise Vertex Displacement)
url: https://www.instagram.com/reel/DeKlghCOQiC/
source_url: https://www.instagram.com/reel/DeKlghCOQiC/
source: instagram
category: agent-pattern
summary: Game-dev technique for animating large numbers of static foliage/vegetation meshes cheaply by driving per-object or per-vertex movement from a Perlin noise texture instead of hand-animating each piece — pixel brightness sets how much an object moves, continuously panning the noise across the environment avoids visible looping, and layering several noise patterns at different speeds adds variation; turns one static art asset into apparently-living foliage across hundreds of instances without per-object animation clips.
tags:
  - procedural-animation
  - perlin-noise
  - shader-technique
  - foliage
  - vegetation
  - wind-animation
  - vertex-displacement
  - game-development
  - unity
reviewed: 2026-10-29
acquired: 2026-10-29
license: N/A
security_flags: []
overlaps: []
---

## What it does

A technique for making large fields of otherwise-static foliage (flowers, leaves, grass patches) read as alive without hand-animating each instance. Instead of displaying a Perlin noise image on screen, its pixel brightness is read as a per-object (or per-vertex) movement amount: darker pixels mean less movement, brighter pixels mean more. The noise pattern is continuously panned across the environment over time rather than sampled once, so the resulting motion has subtle, non-repeating variation instead of a visible loop. Multiple noise layers panned at different speeds can be combined for more organic variation. The net effect: one static mesh (e.g. a single flower) becomes animated-looking across hundreds of placed instances, without authoring an animation clip for each one.

This is a specific, concretely-demonstrated instance of a broader and independently well-documented game-dev technique — panning a noise texture to drive vertex-shader wind/foliage displacement — seen elsewhere as "wind using vertex colors" and world-space-stretched Perlin noise shaders in Unreal Engine 5. It was demonstrated in a dev-log reel for TileShire, an in-development Unity city-builder/tile-merging game by a two-person team, to animate foliage across a procedurally-assembled town.

## Sources

- [Instagram reel, TileShire dev log](https://www.instagram.com/reel/DeKlghCOQiC/) — caption, transcript, and on-screen text walking through the noise-brightness-to-movement mapping, continuous panning, and noise-layering steps (catalog source).
- [Making Foliage React to Wind Using Vertex Colors](https://salivity.github.io/game-development/article/making-foliage-react-to-wind-using-vertex-colors) — independent shader-level breakdown of the same panning-noise-for-wind family of technique.
- [80.lv: Artist shows a useful technique of creating wind in Unreal Engine 5](https://80.lv/articles/artist-shows-a-useful-technique-of-creating-wind-in-unreal-engine-5) — independent example of world-space Perlin noise driving foliage wind in a different engine.

## Security

N/A — a visual/animation technique description, not software; no code, binary, or service to install. No security-relevant claims.
