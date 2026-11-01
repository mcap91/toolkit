---
name: img2threejs
title: img2threejs
url: "https://github.com/img2threejs/img2threejs"
category: skill
summary: "Image-to-3D reconstruction skill for Claude Code/Codex/OpenCode that turns a single reference image into a quality-gated, animation-ready TypeScript THREE.Group factory via a staged sculpting pipeline, using stdlib-only Python scripts for validation/gating so model tokens are spent only on visual judgment"
tags: [image-to-3d, threejs, procedural-generation, claude-code-skill, token-efficient, typescript, python, 3d-modeling]
reviewed: 2026-08-09
acquired: 2026-08-09
license: Apache-2.0
security_flags: []
overlaps: [threejs-skills]
source: unknown
---

## What it does

img2threejs takes one reference image of an object and produces a `THREE.Group` factory (TypeScript) that reconstructs it from primitives, procedural shaders, and generated geometry, including a runtime hierarchy of pivots, sockets, and colliders so the result is animation-ready rather than a static mesh. It runs as a skill under Claude Code, Codex, or OpenCode and is described as agent-agnostic for vision/browser capabilities, using whatever the host agent provides (native image reading, a browser MCP, a project preview, or a user-supplied screenshot).

A staged sculpting pipeline generates and vision-reviews one build pass at a time — blockout → structural → form → material → surface → lighting → interaction → optimization — self-correcting against reference-image comparison at each stage before advancing. Before code generation, a "detail inventory" step enumerates identity-defining small details (bevels, screws/rivets, engraved/painted linework, wear); every listed detail must map to a real modeled component, and a strict-quality gate blocks generation until the inventory is complete. Subjects are classified as object, character, or hybrid; characters route through a separate anatomy-aware track (proportions, facial landmarks, pose). Optional capabilities include multi-view silhouette carving (intersecting orthographic silhouettes into a voxel mesh), a projection-first likeness path for a specific person/character, and CS2-weapon-specific review gates with family-specific component contracts (documented for the Glock-18 and knife families).

## Differentiators

- Deterministic, stdlib-only Python 3.10+ scripts (no pip dependencies — PNG parsing via `struct`/`zlib`) handle validation, spec authoring, and pass-gating; per the README, model tokens are spent only on judging a single packaged reference-vs-render comparison sheet per pass rather than re-reading state or scoring pixels.
- Fail-closed generation: the factory generator repeats the strict-quality gate and returns a `BLOCKED` result with the spec artifact, failure metrics, and next action instead of emitting an underspecified model; a documented `--allow-nonstrict` override exists only for legacy test fixtures.
- A resumable local-state workflow (`forge/state.py` / `forge/next.py`) supports multi-session reconstructions by tracking an ordered, evidence-backed intake/pass checklist.
- Explicitly states its own limits: a single image cannot reveal hidden sides or guarantee exact geometry, unseen faces are inferred by mirroring visible ones (not invented), and character output is described as stylized reconstruction rather than photoreal likeness.
- Optional (non-authoritative) integrations — SAM2, Depth Anything V2, MediaPipe, Chrome DevTools, Three.js scene inspection, Playwright, Context7 — can supply evidence to the pipeline but per the README never approve a gate or silently provide geometry themselves.

## Mechanical details

- Install: `git clone https://github.com/img2threejs/img2threejs.git ~/.claude/skills/img2threejs`; for use with more than one agent host, keep a single checkout and symlink it into each host's skills directory (e.g. `~/.codex/skills/img2threejs`) to avoid drift.
- Invoke in Claude Code via `/img2threejs` with an attached/referenced image; the skill self-classifies the subject and runs its own gates without further configuration.
- Multi-session state: `python3 forge/state.py init --reference <image> --profile character --spec object-sculpt-spec.json` then `python3 forge/next.py --state .img2threejs/state.json` to resume.
- Individual pipeline stage scripts (intake, spec authoring/validation, material analysis, pass orchestration, factory generation, review/comparison, CS2-specific review) are documented per-script in `docs/ARCHITECTURE.md`.
- The GitHub org hosting this repo (`img2threejs`) mirrors what third-party coverage identifies as the author's personal repository at `github.com/hoainho/img2threejs` (author credited elsewhere as Hoài Nhớ); a separate `img2threejs/img2threejs-showcase` repo holds the live demo gallery source.
- Roadmap (per the README): v1.0–v1.4.1 shipped (object pipeline through CS2 weapon hardening); v1.5 (character update) in progress; v1.6 onward targets environments, game-engine exporters, rigging, and a longer-term "procedural world" v2.0.

## Security

Apache 2.0 licensed. The core pipeline is local: Python 3.10+ standard library only for the deterministic validation/gating scripts, with no required third-party pip packages, and output is diffable TypeScript plus a JSON spec rather than binary mesh files. The optional reference-fidelity tooling (SAM2, Depth Anything V2, MediaPipe, Playwright, Context7, etc.) is explicitly opt-in and documented as evidence-only, not gate-approving, which limits how much those add-ons can silently affect output if enabled. Third-party star-count trackers report rapid, inconsistent growth (roughly 3.6k to 9.7k+ stars across snapshots within about two weeks in July 2026), consistent with a young, fast-growing project; no independent security audit is referenced in the fetched material. The repo includes a sponsor section (a named AI-inference-platform sponsor plus VietQR/MoMo/PayPal donation links) separate from the pipeline code itself.