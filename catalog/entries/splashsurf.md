---
name: splashsurf
title: splashsurf
url: https://github.com/InteractiveComputerGraphics/splashsurf
source_url: https://www.instagram.com/reel/DexwNYhhf-k/
source: instagram
category: cli-tool
summary: Rust surface reconstruction library and CLI (Fabian Löschner, Interactive Computer Graphics) that converts SPH particle data (e.g. from [[splishsplash]]) into a smooth triangle mesh for rendering — loads formats including .bgeo and .vtk; 309 stars, 29 forks; MIT.
tags:
  - surface-reconstruction
  - sph
  - particle-to-mesh
  - rust
  - cli
  - mesh-generation
  - vfx
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

splashsurf reconstructs a continuous triangle-mesh surface from raw SPH (smoothed particle hydrodynamics) particle data. Simulators like [[splishsplash]] output only particle positions each timestep, which look like loose sand/grains rather than a liquid; splashsurf fits a smooth surface around the particle cloud so it can be rendered as a fluid. It reads particle data formats including `.bgeo` and `.vtk` and writes mesh output for import into renderers or 3D tools (e.g. Mitsuba, Blender, Maya).

## Mechanical details

Written in Rust, distributed as both a library and a command-line binary. 309 GitHub stars, 29 forks, MIT licensed, maintained by Fabian Löschner under the Interactive Computer Graphics organization (the same group that maintains [[splishsplash]]). Users on SPlisHSPlasH's own GitHub discussions recommend it as the standard next step after simulation, noting the raw reconstruction can look bumpy and benefits from smoothing before import into a DCC tool. In the demonstrated pipeline (SPlisHSPlasH → splashsurf → Mitsuba), splashsurf is the middle, mesh-reconstruction stage between simulating 71,346 particles and rendering the final water footage.

## Security

MIT licensed. Offline Rust CLI/library — reads local particle files and writes local mesh files, no network calls or telemetry observed in its stated function. Standard build-from-source/crates.io trust model.

## Sources

- [GitHub: InteractiveComputerGraphics/splashsurf](https://github.com/InteractiveComputerGraphics/splashsurf) — README, license
- [Instagram reel](https://www.instagram.com/reel/DexwNYhhf-k/) (@hyun2xyz) — names splashsurf as the surface-reconstruction stage between SPlisHSPlasH simulation and Mitsuba rendering, credits splashsurf (commit 56d3e6a), MIT