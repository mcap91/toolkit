---
name: procedura
title: Procedura
url: "https://github.com/SpatiaOS/Procedura"
category: framework
summary: "Agentic text-to-3D modeling pipeline — turns a text prompt into an editable parametric OpenSCAD program with named parts joined by typed mates; optional per-part PBR materials, articulation export to OpenUSD/URDF with Isaac Sim validation; part-by-part generation with LLM reasoning, 3D feedback loop, and refine critic; any OpenAI-compatible endpoint; MIT"
tags: [3d-modeling, procedural-generation, openscad, text-to-3d, agent, llm, parametric, cad, blender, usd, urdf]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

Procedura turns a text prompt into an editable parametric 3D program — not a point cloud or triangle soup, but OpenSCAD source code you can open, edit, and recompile. Parts are named and joined by typed mates (pegs/sockets, bolt patterns, snaps).

Pipeline stages:
1. **Plan**: decompose prompt into named parts
2. **Draft**: build parts one at a time, optionally with 3D feedback (Blender renders of build-so-far)
3. **Refine**: render → critic → patch → gate loop (2 LLM calls per cycle, default 6 cycles)
4. **Paint** (optional): vision call assigns per-part PBR materials
5. **Motion** (optional): articulation planning, exported to OpenUSD + URDF, validated in Isaac Sim

Outputs: `.scad` source, `.obj` mesh (unit-normalized), Blender renders, optional STL, materials JSON, URDF.

Works with any OpenAI-compatible endpoint (OpenAI, OpenRouter, vLLM, Ollama, LM Studio) or native Gemini. No 3D training data used — frozen LLM reasoning only.

## Mechanical details

Install: `git clone && bash scripts/install-deps.sh`. Requires Bun 1.3+, OpenSCAD with Manifold backend, Blender. Isaac Sim only needed for `--motion` physics validation.

Web Studio: `cd web && bun install && bun run start` (localhost:8080). Batch processing via `scripts/batch.ts`.

Key flags: `--image` (reference image, biggest quality gain), `--3d-feedback`, `--assembly`, `--paint`, `--motion --motion-urdf`, `--max-steps N`.

## Security

MIT licensed. Ships no API keys. Requires user-configured endpoint. Blender scripts are MIT (GPL-compatible). OpenSCAD/Blender invoked as external programs, not redistributed.