---
name: wave-function-collapse
title: WaveFunctionCollapse
url: https://github.com/mxgmn/WaveFunctionCollapse
source_url: https://www.instagram.com/reel/DeuQdK6THpz/
source: instagram
category: framework
summary: C# algorithm (by Maxim Gumin) that generates bitmaps/tilemaps locally similar to a single input example — picks the lowest-entropy region, collapses it to one of the input's NxN patterns weighted by their input frequency, and propagates that constraint outward, repeating until the whole output is determined or a contradiction forces a retry; used for procedural terrain, dungeon, and texture generation; 25.5k stars, 1.4k forks; MIT (sample images/tiles excluded from the license).
tags:
  - procedural-generation
  - wave-function-collapse
  - tile-generation
  - constraint-propagation
  - csharp
  - game-development
  - unity
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps:
  - markov-junior
---

## What it does

WaveFunctionCollapse (WFC) generates output bitmaps or tilemaps that are "locally similar" to a single input sample: every NxN pixel pattern that appears in the output also appears somewhere in the input, and the output's pattern frequencies approximate the input's. It runs an observation/propagation loop borrowed in name only from quantum mechanics: the output starts in a "superposition" where every cell could be any input pattern; the algorithm repeatedly finds the cell with the lowest Shannon entropy (fewest remaining valid patterns), collapses it to one pattern chosen at random weighted by input frequency, then propagates that constraint to neighboring cells, removing patterns that would no longer be consistent. The loop continues until every cell is resolved (success) or a contradiction leaves a cell with no valid patterns (the implementation restarts). Two input modes are supported: the "overlapping" model (learns patterns directly from a sample image) and the "tiled" model (uses a hand-authored tileset with explicit adjacency rules).

## Mechanical details

C#, no external dependencies. Runs on Windows/Linux/macOS as a standalone command-line program producing image output. 25.5k GitHub stars, 1.4k forks (as of this entry). The algorithm is intentionally sequential/local-propagation based, which the author notes makes it hard to parallelize compared to techniques like Perlin noise. It has been ported to numerous other languages/engines (Godot 4, Rust, Python with OpenCL acceleration, Go, a C CLI, and others) and used in shipped tools for dungeon/terrain/texture generation, including as one of the composable node types inside [[markov-junior]], the same author's later rewrite-rule-based successor.

## Security

MIT licensed (Maxim Gumin, 2016); the license text excludes the bundled sample images/tiles, which are not covered by the MIT grant. Standalone offline tool — no network calls, no credentials, no telemetry. Standard build-from-source trust model.

## Sources

- [GitHub: mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) — README, algorithm description, license
- [Instagram reel](https://www.instagram.com/reel/DeuQdK6THpz/) — named the tool as one of eight repos used to build a Claude-assisted farm game (catalog source; no link given in the reel itself)