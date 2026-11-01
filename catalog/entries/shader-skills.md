---
name: shader-skills
title: Shader Skills
url: https://github.com/gokayfem/shader-skills
source_url: https://www.instagram.com/reel/Der53z2kchV/
source: instagram
category: skill
license: MIT
summary: Agent skill (gokayfem) teaching Claude Code, Codex, Cursor, Copilot, and Gemini CLI to write procedural GLSL/Shadertoy shaders that compile on the first try. Ships a 186-function GLSL library across 20 modules (hashing, noise, SDFs, raymarching, shading, water, volumetrics, color/tonemapping, cameras, debugging), each function WebGL2-compiled and GPU-tested (90 property tests across 16,384 samples), plus a Python bundler that inlines only the functions a given shader uses into one Shadertoy-ready file, and a checker that catches common WebGL-vs-desktop-GLSL mistakes. v2.0.0 tagged 2026-10-23; MIT; 410 stars, 36 forks at time of review.
tags:
  - glsl
  - shadertoy
  - webgl2
  - shaders
  - procedural-generation
  - claude-code-skill
  - raymarching
  - generative-art
  - skill
reviewed: 2026-10-30
acquired: 2026-10-30
overlaps:
  - threejs-skills
security_flags: []
---

## What it does

Shader Skills is an agent skill that teaches coding agents (Claude Code, Codex, Cursor, Copilot, Gemini CLI) to write procedural GLSL shaders targeting WebGL2/Shadertoy that compile successfully and render as intended on the first attempt. Its core is a library of 186 GLSL functions spread across 20 modules — hashing, ten noise variants, patterns, 2D/3D signed distance functions (SDFs), operators, domain transformations, raymarching, shading, water simulation, color/tonemapping, volumetrics, cameras, and debugging utilities. Each function is compiled in WebGL2 and numerically verified on the GPU rather than assumed correct from desktop-GLSL conventions. The README frames the problem it targets as agents writing shaders "blind": they cannot see rendered output, misremember exact formulas, and WebGL2 rejects constructs (e.g. struct ternaries) that desktop GLSL accepts, producing GPU-varying hash results, SDFs with wrong signs, double gamma correction, or fog that ignores the sky.

A Python bundler inlines only the dependency functions a given shader actually calls into a single self-contained file that pastes directly into Shadertoy, and a separate checker script scans for the known WebGL2 failure patterns above before the agent presents a result. The repo ships 11 ready-to-run example shaders (SDF still-life with PBR materials/soft shadows/AO/AgX tonemapping, volumetric cumulus clouds with energy-conserving integration and Beer-Powder/dual-lobe phase functions, a physically-based sky with aerial perspective, a 2D distance-field poster using Oklab gradients, texture-free procedural materials — marble, Voronoi cracks, hex tiles, Truchet patterns, filtered checker — and a dispersive-wave ocean with analytic curvature foam and Fresnel sky), each with a paste-ready source file under `skills/shader-art-coding/templates/`. A separate "Video 2 GLSL" workflow (promoted by the author on X/Twitter, not verified firsthand here) reconstructs a short reference video clip as a single procedural GLSL fragment shader.

## Mechanical details

- Install via the skills CLI: `npx skills add gokayfem/shader-skills`; also distributed as a Claude Code plugin (`claude plugin marketplace add gokayfem/shader-skills` then `claude plugin install shader-skills@shader-skills`) and as a Gemini CLI extension.
- Repository layout: `skills/shader-art-coding/` (the skill definition plus the GLSL function library and reference docs), `tests/` (WebGL2 test harness and GPU property tests), `gallery/` (rendered example outputs with linked source shaders), `adapters/` (prompt adapters for ChatGPT and Gemini Gems).
- Quality gating per the README: glslang validation, WebGL2 compilation checks, Lipschitz-bound checking on SDFs, and derivative/noise validation, backed by 90 GPU property tests run across 16,384 samples.
- First tagged release v2.0.0 (2026-10-23), aligned with the plugin and Gemini-extension version numbers. At least one third-party fork exists (`calrizien/metal-shader-skills`), porting the approach to native Metal Shading Language 4.1 for Apple platforms.

## Security

MIT licensed. The library and skill are static GLSL source plus Python validation/bundler scripts; no network calls or runtime service are described. The bundler and checker are local scripts operating on shader text. No independent security audit found; no security flags observed from the fetched material.

## How to use it

npx skills add gokayfem/shader-skills
