---
name: terrain-erosion-3-ways
title: terrain-erosion-3-ways
url: https://github.com/dandrino/terrain-erosion-3-ways
category: cli-tool
summary: Daniel Andrino's Python/NumPy demo comparing three procedural terrain-with-erosion techniques — iterative hydraulic-erosion simulation (rain gathers, flows downhill, carries sediment), a GAN trained on ~180k USGS elevation samples, and a river-network-first approach using Poisson disc sampling + Delaunay triangulation; last pushed 2022-11-22; MIT.
tags:
  - terrain-generation
  - erosion-simulation
  - procedural-generation
  - gan
  - poisson-disc-sampling
  - delaunay-triangulation
  - numpy
  - generative-art
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - unmaintained
  - single-maintainer
source: instagram
source_url: https://www.instagram.com/reel/DemMV03uWzP/
---

## What it does

Demonstrates and compares three ways to procedurally generate terrain height maps with erosion-like features:

1. Simulation — iteratively tracks water level, sediment, and height across a grid; rain gathers, runs downhill, and carries soil away, cutting valleys over many rounds. Naturalistic results but parameter-heavy and O(N^3) runtime.
2. Machine learning — trains a GAN (Progressive Growing of GANs, TensorFlow with GPU) on roughly 180,000 USGS elevation samples to generate realistic-looking terrain; training takes 8+ days on the project's own hardware, with little direct control over output.
3. River networks — generates river/stream locations first (Poisson disc sampling + Delaunay triangulation), then derives terrain shape from them; efficient (O(N^2 log N)) and produces convincing ridges, but models sediment deposition only loosely.

The erosion-simulation method takes a height map (normally generated from noise) as its input and runs repeated rounds of simulated rainfall against it.

## Mechanical details

- Python 3.6+, NumPy; the GAN path additionally needs the Progressive Growing of GANs framework and a GPU-equipped TensorFlow install.
- Last pushed 2022-11-22 (per GitHub repo metadata); 963 stars, 63 forks as of this review. The item's own captured on-screen GitHub text shows commits (e.g. "Simulation tweaking", "README.md") dated "6 years ago" relative to the reel's capture.

## Security

Source-available, MIT licensed. The simulation and river-network methods run entirely locally on NumPy arrays with no network calls documented. The GAN method trains against a bundled/downloaded USGS elevation dataset and a third-party GAN framework dependency. Single-maintainer project (Daniel Andrino) with no commits since 2022.

## Usage notes

- Used with its usual noise input replaced: a 2D branch structure grown by Michael Fogleman's dlaf (random walkers sticking into coral-like branches) was converted into a ridge height map — taller where a branch ran longer — and fed to the simulation method in place of noise; 700-716 rounds of simulated rain then carved valleys into it, rendered with three.js (source: https://www.instagram.com/reel/DemMV03uWzP/).

- River-network method mechanics: each river grows upstream from the coast one edge at a time, only accepting an edge that moves uphill and does not reconnect with an existing river graph (so rivers merge but never split going downhill); a configurable "directional inertia" weight biases edge choice toward the previous edge's direction, giving straighter vs. twistier rivers; water volume accumulates along branches so larger, more-fed rivers cut deeper, with terrain height built to fit the resulting network (source: https://www.instagram.com/reel/Dd-WW-AszIG/).
- Suggested uses for the generated height maps: landscapes, 3D terrain, relief prints, or animated erosion visuals (source: https://www.instagram.com/reel/Dd-WW-AszIG/).
