---
name: mitsuba3
title: Mitsuba 3
url: https://github.com/mitsuba-renderer/mitsuba3
source_url: https://www.instagram.com/reel/DexwNYhhf-k/
source: instagram
category: framework
summary: Research-oriented, retargetable forward/inverse renderer from EPFL — Python-first, JIT-compiled and differentiable via the Dr.Jit backend, supports monochromatic/RGB/spectral and polarized light transport, CPU and GPU execution; ~3k stars, 374 forks; BSD-3-Clause.
tags:
  - rendering
  - differentiable-rendering
  - physically-based-rendering
  - python
  - drjit
  - jit-compilation
  - spectral-rendering
  - vfx
reviewed: 2026-10-30
acquired: 2026-10-30
license: BSD-3-Clause
security_flags: []
overlaps: []
---

## What it does

Mitsuba 3 is a research rendering system for forward (image synthesis) and inverse (parameter recovery from images) light transport simulation, developed at EPFL. It is "retargetable": the same scene description and core library can be recompiled or re-dispatched to act as a scalar CPU renderer, a vectorized/GPU renderer, or a differentiable renderer that computes derivatives of the rendered image with respect to scene parameters (camera pose, geometry, BSDFs, textures, volumes). Materials, textures, and even full rendering algorithms can be written in Python, which Mitsuba JIT-compiles (and optionally differentiates) at runtime via the Dr.Jit backend.

## Mechanical details

Core library plus a plugin system covering materials, light sources, and rendering algorithms; supports monochromatic, RGB, and spectral rendering, including polarized light transport. Python-first API; Dr.Jit (a separate EPFL project, 813 stars) provides the JIT compilation and automatic differentiation that execute on both CPU and GPU. Tested on Linux (x86_64), macOS (aarch64/x86_64), and Windows (x86_64). ~3k GitHub stars (2,964 at last check), 374 forks, actively maintained (last updated 2026-10-25); the org also maintains the older Mitsuba 1 (C++, 1.1k stars) and Mitsuba 2 (2.1k stars) repos that Mitsuba 3 supersedes. Recent releases report roughly 2x faster tracing/compilation and reverse-mode differentiation of symbolic loops. In the demonstrated pipeline, Mitsuba is the final rendering stage, turning a splashsurf-reconstructed mesh of a 71,346-particle SPlisHSPlasH simulation into the final water footage.

## Security

BSD-3-Clause licensed. Rendering library/CLI that compiles and executes user-supplied Python scene code and shaders via its own JIT (Dr.Jit); treat untrusted scene files with the same care as any code execution, since scene scripts run as Python. No network calls or telemetry in its core rendering function.

## Sources

- [GitHub: mitsuba-renderer/mitsuba3](https://github.com/mitsuba-renderer/mitsuba3) — README, releases
- [Instagram reel](https://www.instagram.com/reel/DexwNYhhf-k/) (@hyun2xyz) — names Mitsuba 3.9.1 as the rendering stage after SPlisHSPlasH simulation and splashsurf reconstruction, credits BSD-3-Clause license