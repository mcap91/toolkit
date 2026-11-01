---
name: splishsplash
title: SPlisHSPlasH
url: https://github.com/InteractiveComputerGraphics/SPlisHSPlasH
source_url: https://www.instagram.com/reel/DexwNYhhf-k/
source: instagram
category: framework
summary: Open-source C++ library (Jan Bender et al.) for physically-based fluid simulation using smoothed particle hydrodynamics (SPH) — 2D/3D, CPU/GPU neighborhood search, AVX vectorization, Python bindings, multiple pressure solvers (WCSPH, PCISPH, PBF, IISPH, DFSPH, PF), viscosity/surface-tension/vorticity methods, multi-phase and rigid-fluid coupling; 1.9k stars, 339 forks; MIT.
tags:
  - fluid-simulation
  - sph
  - smoothed-particle-hydrodynamics
  - dfsph
  - physics-simulation
  - cplusplus
  - python-bindings
  - vfx
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

SPlisHSPlasH simulates fluids (and deformable solids, with rigid-fluid coupling) by representing the fluid as particles and computing their motion with smoothed particle hydrodynamics (SPH): each particle's density is estimated by summing the mass of nearby particles within a kernel radius, weighted by a smooth falloff function, and an implicit pressure solver corrects local compression toward the fluid's rest density every step before gravity and viscosity are applied and particles are advanced. It implements several interchangeable pressure solvers (WCSPH, PCISPH, PBF, IISPH, DFSPH, PF — the DFSPH solver is divergence-free SPH, which iterates the pressure correction until average compression drops below a configurable tolerance), plus explicit/implicit viscosity, surface tension, vorticity methods, drag-force computation, and multi-phase simulation. Output is raw particle position/velocity data per timestep, which downstream tools (e.g. [[splashsurf]]) convert into a renderable mesh surface.

## Mechanical details

C++ core with CPU or GPU neighborhood search and AVX vectorization for performance; Python bindings and embedded Python scripting (contributed by Stefan Jeske) let scenes and solver parameters be scripted rather than only configured via JSON scene files. Builds are tested on Linux, Windows, and macOS (CI badges for build-linux, build-windows-wheels, build-macos, build-mac-wheels). 1.9k GitHub stars, 339 forks. Maintained by Jan Bender's group (Interactive Computer Graphics) alongside an academic Eurographics tutorial on SPH methods; recent releases (e.g. 2.13.0) have added published research techniques such as implicit surface tension (Jeske et al., ACM TOG 2023) directly into the solver. A documented demonstration run: a 71,346-particle dam-break scene, 41 neighbors per particle for density estimation, DFSPH achieving 0.010% average compression, took 3,052 timesteps (4 simulated seconds) and about 14 minutes on one CPU core, excluding rendering.

## Security

MIT licensed. Offline C++/Python simulation library with no network calls, external services, or telemetry — it reads scene/config files and writes particle data locally. Standard build-from-source trust model; GPU neighborhood search path depends on the user's own CUDA/OpenGL stack.

## Sources

- [GitHub: InteractiveComputerGraphics/SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH) — README, releases, license
- [Instagram reel](https://www.instagram.com/reel/DexwNYhhf-k/) (@hyun2xyz) — dam-break demo walkthrough (particle count, DFSPH compression figure, step/runtime figures), credits SPlisHSPlasH 2.18.1