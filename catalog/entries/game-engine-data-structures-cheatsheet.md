---
name: game-engine-data-structures-cheatsheet
title: Game Engine Data Structures Cheat Sheet
category: reference
summary: "Practitioner cheat sheet on six data structures used in game engines for performance: contiguous arrays (C++ vector, Unreal TArray) over linked lists for CPU cache locality during entity iteration; quad trees/octrees for spatial partitioning (frustum culling, raycasting) cutting O(n) scans to O(log n); bounding volume hierarchies (BVH) for fast ray tracing and broad-phase collision detection; ring buffers/circular queues for fixed-length event logs, input, and audio buffers; graphs with A* for pathfinding; spatial hashmaps for constant-time grid-based lookups."
tags:
  - data-structures
  - game-development
  - cache-locality
  - data-oriented-design
  - spatial-partitioning
  - octree
  - bvh
  - ring-buffer
  - pathfinding
  - spatial-hashing
reviewed: 2026-10-30
acquired: 2026-10-30
overlaps:
  - navmesh-plus
license: N/A
security_flags: []
source: instagram
source_url: https://www.instagram.com/reel/Dez02K2qND3/
---

## What it does

Six data structures, each matched to a specific game-engine performance problem:

1. **Contiguous arrays over linked lists** (data-oriented design): a `std::vector` (C++) or `TArray` (Unreal Engine) stores elements sequentially, letting CPU L1/L2 caches prefetch upcoming elements during iteration. Linked lists scatter nodes across the heap — each traversal step is a likely cache miss. Measured effects reported elsewhere: linked-list-heavy code can see 70-90% cache-miss rates versus 5-15% for array-based equivalents, and over 96% of linked-list cache misses are heap misses specifically. Trade-off: contiguous arrays make insertion/deletion in the middle more expensive than a linked list's O(1) splice, which is usually outweighed by the iteration-speed win in hot loops (entity updates, render passes).
2. **Quad trees (2D) / octrees (3D)**: recursively subdivide space into four or eight child regions, each wrapped in a bounding box. A spatial query (frustum culling, raycasting, nearest-object lookup) descends only the branches whose bounding box intersects the query, cutting a naive O(n) scan over every object to roughly O(log n).
3. **Bounding Volume Hierarchies (BVH)**: a tree of nested bounding boxes around geometry, used for ray tracing and collision broad-phase. For ray tracing, a BVH cuts expected per-ray cost from O(n) triangle tests to O(log n) — a 10-million-triangle scene needs roughly 23 box tests plus a handful of triangle tests per ray. For collision detection, which traverses two BVHs simultaneously and collects every overlapping pair (no early exit), query cost is closer to O(log n + k), where k is the number of overlaps returned.
4. **Ring buffers (circular queues)**: fixed-capacity buffers that wrap writes back to index 0 once full, overwriting the oldest entry. Used for data with a natural fixed-length window and no need for dynamic growth: input command history, event logs, audio sample buffers.
5. **Graphs with A***: game worlds are modeled as a graph of connected nodes (navmesh polygons, tile grids); A* search finds a shortest path by combining actual path cost with a heuristic estimate to the goal, avoiding the need to explore the whole graph.
6. **Spatial hashmaps**: bucket world-space coordinates into a hash of grid-cell IDs, giving O(1) average lookup for "what's in this cell" or "what's near this point" — used for grid-based inventories and broad-phase neighbor checks without building a tree.

## Sources

- [Instagram reel — gamedev data structures overview](https://www.instagram.com/reel/Dez02K2qND3/) — the captured item itself (caption, transcript, on-screen text).
- [Why Arrays have better cache locality than Linked List? — GeeksforGeeks](https://www.geeksforgeeks.org/dsa/why-arrays-have-better-cache-locality-than-linked-list/) — array vs. linked-list cache locality mechanics.
- [Data-Oriented Design for Games: Complete ECS Architecture Guide](https://generalistprogrammer.com/tutorials/data-oriented-design-games-complete-architecture-guide) — 70-90% vs. 5-15% cache-miss rate comparison for OOP vs. data-oriented layouts.
- [Bounding volume hierarchy — Wikipedia](https://en.wikipedia.org/wiki/Bounding_volume_hierarchy) — BVH definition and use in collision/ray queries.
- [BVH for Collision Detection: From AABB to Optimal Hierarchies — DEV Community](https://dev.to/mayank_mayam03/bvh-for-collision-detection-from-aabb-to-optimal-hierarchies-21k6) — O(log n) ray cost, O(log n + k) broad-phase collision cost, two-BVH traversal for collision vs. single-BVH for ray tracing.

## Security

N/A — reference content describing general data structures, not software this entry ships or installs.