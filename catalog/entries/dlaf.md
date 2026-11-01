---
name: dlaf
title: dlaf
url: https://github.com/fogleman/dlaf
category: cli-tool
summary: Michael Fogleman's C++ command-line tool implementing diffusion-limited aggregation (DLA) — random walkers stick together on contact with a growing cluster, producing coral- or lichen-like branching structures in 2D or 3D; computes roughly one million points per core in ~35 seconds (per its own README) using Boost for spatial indexing, and writes particle ID/parent/coordinate data to CSV, leaving rendering to the caller; last pushed 2020-01-09; MIT.
tags:
  - diffusion-limited-aggregation
  - procedural-generation
  - generative-art
  - creative-coding
  - cplusplus
  - particle-simulation
  - branching-structures
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - unmaintained
  - single-maintainer
  - requires-manual-source-build
source: instagram
source_url: https://www.instagram.com/reel/DemMV03uWzP/
---

## What it does

dlaf (Diffusion-Limited Aggregation, Fast) simulates particles that wander randomly until they touch an already-stuck cluster, then stick in place — repeated over many particles this grows branching, coral- or lichen-like structures in 2D or 3D. Each particle records which particle it stuck to (its parent), so the output is a tree. Parameters (attraction distance, particle spacing, stickiness, "stubbornness") and hooks (starting position, reset condition, join logic, motion vector) are configurable in code. The README's own benchmark claims about one million points computed per core in ~35 seconds; example renders include a 2D run with 1 million particles and a 3D run with 10 million particles ray-traced in ~10 hours at 4096x4096px, 2048 samples per pixel.

## Mechanical details

- Output is a CSV of particle id, parent id, and (x,y[,z]) coordinates — dlaf does no rendering itself; visualization is left to the caller.
- Depends on Boost (used for spatial indexing to find nearby particles efficiently).
- C++, built from source; no packaged binaries documented.
- Last pushed 2020-01-09 (per GitHub repo metadata); 218 stars, 22 forks as of this review.

## Security

Source-available, MIT licensed, no network calls or external data fetches documented — pure local CPU simulation writing a CSV file. Requires building from source with a C++ compiler and Boost; no prebuilt binaries are provided. Single-maintainer project (Michael Fogleman) with no commits since 2020.

## Usage notes

- Used as a pipeline input source: a 2D dlaf run's branch structure was converted into a terrain height map (taller where a branch ran longer) and substituted for the usual noise input of Daniel Andrino's terrain-erosion-3-ways; a separate 3D dlaf run of 6,000 particles had each particle's parent link turned into a capsule shape and blended with Michael Fogleman's sdf library's smooth-union operator to build a mesh, which was then rendered as a hidden-line drawing with Fogleman's ln (source: https://www.instagram.com/reel/DemMV03uWzP/).
