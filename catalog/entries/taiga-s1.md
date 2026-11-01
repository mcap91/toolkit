---
name: taiga-s1
title: Taiga-S1
url: "https://github.com/mckeown12/taiga-s1"
category: framework
summary: "1.2M-parameter System-1 decision model for building CAD parts in FreeCAD — ~1ms per decision on CPU, no LLM/GPU/screenshots; covers PartDesign workflows (sketch, pad, pocket, hole, revolve, pattern, fillet, chamfer, shell); generalizes to 17-feature parts (95%) despite training on ≤5-feature; 86-100% recovery from 20% random action corruption; part of the Biome-S1 family; 4.9 MB model file"
tags: [cad, freecad, decision-model, system-1, computer-use, tiny-model, cpu, agent-executor, manufacturing, 3d-modeling]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: unknown
security_flags: []
source: unknown
---

## What it does

Taiga-S1 is a 1.2M-parameter model trained from scratch to build 3D parts in FreeCAD one command at a time. It serves as a fast executor for computer-use agents: a planner decides what to build, Taiga-S1 handles step-by-step FreeCAD PartDesign execution.

No LLM, no vision model, no screenshots, no GPU. ~1ms per decision on CPU. 4.9 MB model file.

Capabilities cover FreeCAD PartDesign: sketches (rectangle, circle, hexagon), pad, pocket, hole, revolve, linear/polar patterns, mirror, fillet, chamfer, shell.

Key properties:
- **Length generalization**: trained on ≤5-feature goals, completes 100% of 11-feature goals (~55 commands) and 95% of 17-feature goals.
- **Error recovery**: with 20% of actions replaced by random ones, recovers and finishes 86-100% of parts.
- **Unseen combinations**: feature pairings never in training data: 90-100% success.

Part of the Biome-S1 family (by shhivv/Shiv Shanmugam). Related model: Mesa-S1, which operates FreeCAD's GUI (toolbar buttons, dialogs, dropdowns) at 1.2M params with 97-100% accuracy.

## Mechanical details

Weights on HuggingFace: shhivv/taiga-s1. Reproduction scripts available for environment setup, synthetic data generation in headless FreeCAD, training, and evaluation.

Community demo: 19-part twin-cylinder engine modeled on Android (Termux + Debian proot + Termux:X11), every part at volumetric IoU 1.0.

Launched 2026-09-26.

## Security

License not stated in source content. Model weights hosted on HuggingFace. Runs entirely locally on CPU.

## Usage notes

- Independent third-party test: built a part in 47 clicks in 3 seconds, every click correct; ~2ms per decision on a Mac CPU (vs. the ~1ms figure above, platform unspecified there) (source: https://www.instagram.com/reel/DeFJd9AHPVS/)
- Same test: 3 custom parts built exactly as specified; a plate with 11 holes took 89 clicks, all correct (source: https://www.instagram.com/reel/DeFJd9AHPVS/)
- Same test, failure modes: asked for 22 holes, it stopped 9 short — yet the repo's own automated check still passed the result, a validation gap; asked to round corners before other features, it looped (round, undo, round, undo) (source: https://www.instagram.com/reel/DeFJd9AHPVS/)
- Reviewer states it only handles plates, holes, and patterns, not complex objects like an engine block — this conflicts with the entry's own community-demo claim of a 19-part twin-cylinder engine at IoU 1.0; unresolved discrepancy (source: https://www.instagram.com/reel/DeFJd9AHPVS/)
