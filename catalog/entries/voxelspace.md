---
name: voxelspace
title: VoxelSpace
url: https://github.com/s-macke/VoxelSpace
category: cli-tool
summary: Sebastian Macke's JavaScript/Python reimplementation of the Comanche (1992) terrain-rendering trick — reads a height map and a pre-lit color map, projects one map point per screen column per scanline, and draws vertical lines front-to-back with distance-scaled sampling steps; no polygons; MIT (game-derived maps excluded from the license); 6.8k stars, 302 forks.
tags:
  - terrain-rendering
  - voxel
  - heightmap
  - retro-graphics
  - computer-graphics
  - creative-coding
  - javascript
  - procedural-generation
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - single-maintainer
source: instagram
source_url: https://www.instagram.com/reel/DeMiEoaP-8i/
---

## What it does

Reimplements the "Voxel Space" terrain-rendering technique used by the 1992 flight-combat game Comanche, in under 20 lines of core algorithm code. The world is represented by two images: a height map (one height value per map position) and a color map with lighting and shadow already baked in — no 3D polygon mesh at all.

For each screen column, the renderer casts outward from the camera one map sample at a time, projecting each sampled point's height to a screen-space vertical line segment drawn in that point's color. It works front-to-back: once a column has drawn up to a given screen height, closer terrain that would occlude farther terrain is skipped, so nearer hills correctly hide more distant ones without a depth buffer. Sampling step size grows with distance from the camera, so far terrain costs less to render per screen column — the core trick that let the original 1992 game render detailed mountains on period hardware with no textured polygons.

## Mechanical details

- Repository mixes a JavaScript/HTML5 canvas demo (the original `VoxelSpace.html`) with Python examples of the core algorithm.
- Advanced variants in the repo add a y-buffer for per-column occlusion tracking and level-of-detail adjustments for performance.
- 6.8k stars, 302 forks (per GitHub, October 2026).

## Security

Source-available, MIT licensed, runs entirely client-side/locally with no network calls. The license explicitly excludes the bundled color/height maps — these are stated to be reverse-engineered from Comanche's game data and are not covered by the MIT grant; the repo's README also notes the underlying Voxel Space technique may still be patented in some jurisdictions. Single-maintainer project (Sebastian Macke).

## Usage notes

- Used with custom-made 1024×1024 height/color maps and a custom camera path (not the repository's excluded game-derived maps) to produce a mountain flyover; separate explanatory diagrams, a separated-column view, and a triangle-based rendering comparison were created independently of the original renderer (source: https://www.instagram.com/reel/DeMiEoaP-8i/).