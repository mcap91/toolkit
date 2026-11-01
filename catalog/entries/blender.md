---
name: blender
title: Blender
url: https://www.blender.org/
source_url: https://www.instagram.com/reel/DeuMK6FJhoc/
source: instagram
category: framework
summary: Free, open-source 3D creation suite (modeling, sculpting, UV/texturing, rigging, animation, simulation, the Cycles and EEVEE render engines, compositing, video editing, and Grease Pencil 2D-in-3D drawing); scriptable via a Python API that drives the entire tool including a built-in Python console and add-on system; cross-platform (Linux, Windows, macOS); GPL-licensed (sources vary between citing GPL-2.0-or-later and GPL-3.0), free since 1.0 and open-source since 2002 after a community buyout from the original commercial owner (NaN); maintained by the Blender Foundation with an LTS release track (5.2 LTS released 2026-07-14); third-party MCP servers exist that let AI agents drive Blender's Python API over the Model Context Protocol, which is the specific integration referenced (and dismissed) in this entry's source item.
tags:
  - 3d-modeling
  - sculpting
  - animation
  - rendering
  - cycles
  - python-scripting
  - open-source
  - gpl
  - blender-foundation
  - game-development
reviewed: 2026-10-29
acquired: 2026-10-29
license: GPL
security_flags:
  - python-scripting-arbitrary-code
  - third-party-mcp-code-execution-surface
overlaps: []
---

## What it does

Blender is a free, open-source 3D creation suite covering the full content pipeline: modeling, sculpting (multi-resolution and dynamic subdivision, texture-brush painting), UV/texturing, rigging and animation, physics/particle simulation, two render engines (Cycles for path-traced photorealism, EEVEE for real-time/viewport rendering), node-based compositing, basic video editing, and Grease Pencil for 2D drawing directly inside a 3D viewport. It is scriptable end-to-end through a Python API — most of Blender's own UI is itself built on that API — with a built-in Python console and a community add-on ecosystem for extending or automating the tool.

Originally built in-house by a Dutch animation studio (1994), Blender became free and open-source in 2002 after a community fundraiser bought the rights from the original commercial owner (NaN) for roughly €100,000. It now runs cross-platform (Linux, Windows, macOS) under the Blender Foundation, which maintains a Long-Term-Support release track alongside regular releases (5.2 LTS released 2026-07-14).

Because Blender exposes its full feature set through Python, third-party Model Context Protocol (MCP) servers exist (community projects, not shipped by the Blender Foundation) that let an AI agent drive Blender — creating/editing geometry, materials, and scenes — by calling that same Python API over MCP. This Blender-via-MCP integration pattern is the specific thing referenced (and dismissed as not worth the effort, in favor of agent-written procedural-generation code) in this entry's source item; no specific MCP server product was named in that item.

## Mechanical details

- License: sources disagree on the exact GPL version cited (GPL-2.0-or-later vs. GPL-3.0); Blender itself is unambiguously copyleft/free-software, and this covers Blender's own source, not content created with it.
- Distribution: official builds for Linux/Windows/macOS from blender.org, plus Steam and package-manager distributions; add-ons installed as Python packages/scripts.
- Python API covers nearly every editable property in the application, which is also how both official and community tooling (render farms, pipeline automation, MCP bridges) control Blender headlessly (`blender --background --python script.py`).

## Security

- `python-scripting-arbitrary-code` — Blender's add-on and scripting system runs arbitrary Python with the permissions of the user running Blender; `.blend` files can embed scripts that execute on open unless disabled in preferences. Treat untrusted `.blend` files and add-ons like any other untrusted executable code.
- `third-party-mcp-code-execution-surface` — Blender-driving MCP servers are community-built, not from the Blender Foundation; by design they let a connected AI agent execute Python inside Blender, which inherits the same arbitrary-code-execution surface as any Blender scripting access. Vet the specific MCP server implementation and its auth/exposure model before granting agent access.

## Sources

- [Blender — The Free and Open Source 3D Creation Software](https://www.blender.org/) — official site
- [Blender (software) — Wikipedia](https://en.wikipedia.org/wiki/Blender_(software)) — license and history background
- [Instagram reel](https://www.instagram.com/reel/DeuMK6FJhoc/) — catalog source; creator groups Blender (used via MCP) with Meshy and prebuilt engines as "a waste of time" for AI-accelerated game development, preferring agent-written procedural-generation code instead

## Usage notes

- Gradient-map texturing workflow: a single low-resolution gradient-map image (found by searching "gradient" on itch.io, or made by hand) can texture an entire game's mesh set, relying on Blender's built-in linear interpolation to smooth the pixelated gradient when sampled at different UV positions. Steps: add the gradient image as a texture in the Shader Editor (Ctrl+T adds the texture-coordinate/mapping node chain), set Roughness to 1; in the UV Editor, lock the 3D viewport to front orthographic (Numpad 1), select all, `U` > Project from View, then in the UV editor press `S` `X` `0` to flatten the UV map onto the X axis, and scale/move it to sample a specific color from the gradient strip. Different mesh parts can be selected in Edit Mode and re-unwrapped individually to pick different colors from the same gradient map. For a radial gradient (e.g. a sword blade), rotate the model 90°, project from view, scale/position, then add a Mirror modifier to get a gradient radiating out from the center. (source: https://www.instagram.com/reel/DfAykyuuEpk/)
