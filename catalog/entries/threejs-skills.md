---
name: threejs-skills
title: Three.js Skills
url: "https://github.com/CloudAI-X/threejs-skills"
category: skill
summary: "Skill bundle (CloudAI-X) shipping 10 Three.js SKILL.md sub-skills for AI coding agents: fundamentals, geometry, materials, textures, lighting, loaders, animation, interaction, shaders, and post-processing — each triggering on the matching 3D/WebGL task. Installs via npx skills add. MIT."
license: MIT
tags: [threejs, 3d, webgl, skill-bundle, web-development, claude-code, shaders, animation]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it is

Three.js Skills (by CloudAI-X) is an agent skill bundle that ships 10 individual `SKILL.md` files, each teaching a coding agent one area of the Three.js 3D/WebGL library and activating when a prompt matches that area:

- **threejs-fundamentals** — scene setup, cameras, renderer, Object3D hierarchy, transforms
- **threejs-geometry** — built-in shapes, BufferGeometry, custom geometry, instancing
- **threejs-materials** — PBR/basic/phong/shader materials and properties
- **threejs-textures** — texture types, UV mapping, environment/cube maps
- **threejs-lighting** — light types, shadows, image-based lighting
- **threejs-loaders** — GLTF, textures, models, async loading
- **threejs-animation** — keyframe/skeletal animation, morph targets, mixing
- **threejs-interaction** — raycasting, controls, mouse/touch input, selection
- **threejs-shaders** — GLSL, ShaderMaterial, uniforms, custom effects
- **threejs-postprocessing** — EffectComposer, bloom, DOF, screen effects

The bundle is indexed on the agenticskills.io directory (MIT, ~2.3K stars on the source repo).

## Mechanical details

- **Install:** `npx skills add CloudAI-X/threejs-skills`
- Format: 10 Claude Code / agent `SKILL.md` files with `name`/`description` frontmatter and progressive-disclosure trigger descriptions
- Source repo: `CloudAI-X/threejs-skills`

## Security

MIT licensed. These are instructional Markdown skill files (guidance/patterns for writing Three.js code), with no runtime component of their own. As with any installed skill, review the `SKILL.md` contents before use. No security flags recorded from the observed material.

## How to use it

npx skills add CloudAI-X/threejs-skills
