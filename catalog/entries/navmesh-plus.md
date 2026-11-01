---
name: navmesh-plus
title: NavMeshPlus
url: https://github.com/h8man/NavMeshPlus
source_url: https://www.instagram.com/reel/DeuQdK6THpz/
source: instagram
category: framework
summary: Unity package extending Unity's NavMeshComponents with a 2D extensions system — auto-generates a navigation mesh from scene geometry (tilemaps, sprites, Collider2D) for top-down 2D pathfinding, letting characters and AI navigate around obstacles without hand-authored waypoints; 2.4k stars, 269 forks; MIT.
tags:
  - unity
  - navmesh
  - 2d-pathfinding
  - ai-navigation
  - game-development
  - csharp
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

NavMeshPlus extends Unity's built-in NavMesh system (designed for 3D) to generate navigation meshes from 2D scene geometry — tilemaps, sprite colliders, and Collider2D components — so top-down 2D games can use standard pathfinding/avoidance instead of hand-rolled waypoint graphs. Usage: add a `NavigationSurface` component to an empty GameObject, add a `NavMeshCollectSources2d` component to collect 2D geometry as sources, click "Rotate Surface to XY" to orient the baked mesh toward a standard 2D camera, then bake. Obstacles/areas can be tagged with a `NavMeshModifier` to override walkability per object (e.g. marking fences as unwalkable so AI-controlled characters route around them).

## Mechanical details

Forked from and extends Unity's official NavMeshComponents samples. Implements its own world-bounds calculation, 2D source collection (tiles/sprites/colliders), and conversion into the format Unity's `NavMeshBuilder` expects. Supports runtime (re)baking via an async `BuildNavMeshAsync` call on the `NavigationSurface` component, so navmeshes can regenerate as 2D levels change at runtime. 2.4k GitHub stars, 269 forks. Distributed as a Unity package (Package Manager git-URL install) or by copying the repo into `Assets`.

## Security

MIT licensed. Unity package/library with no network calls, external services, or telemetry — it only reads scene geometry and bakes navmesh data locally.

## Sources

- [GitHub: h8man/NavMeshPlus](https://github.com/h8man/NavMeshPlus) — README, wiki how-to, license
- [Instagram reel](https://www.instagram.com/reel/DeuQdK6THpz/) — named the tool as one of eight repos used to build a Claude-assisted farm game (catalog source; no link given in the reel itself)