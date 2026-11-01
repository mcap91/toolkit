---
name: markov-junior
title: MarkovJunior
url: "https://github.com/mxgmn/MarkovJunior"
category: framework
summary: "Probabilistic programming language where programs are ordered lists of rewrite rules and inference is constraint propagation — generates dungeons, mazes, architecture, puzzles, and simulations on 2D/3D grids; C#/.NET, 153 examples, supports WFC and ConvChain nodes; MIT"
tags: [procedural-generation, rewrite-rules, constraint-propagation, markov-algorithms, wave-function-collapse, grid-generation, csharp, dotnet]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

MarkovJunior is a probabilistic programming language based on Markov algorithms — ordered lists of rewrite rules applied to grids. On each step the interpreter finds the first rule with a match, selects a random match, and applies it. Programs compose rules into sequence nodes (run one after another) and Markov nodes (loop back to the first matching child). Inference via constraint propagation allows imposing constraints on future state, generating only runs that reach the constrained goal.

Core capabilities:

- **Rewrite rules on grids**: `(RBB=WWR)` is a self-avoiding walk. `(WBB=WAW)` generates mazes. Rules work in any number of dimensions without modification.
- **Inference**: connects two states via rewrite rule chains using unidirectional or bidirectional constraint propagation. Generalizes Dijkstra fields to arbitrary rules. Solves Sokoban puzzles, generates grid-covering paths, connects points with constrained paths.
- **Composability**: sequence nodes, Markov nodes (with nesting à la REFAL), forall-nodes (from Imagegram), WFC and ConvChain custom nodes.
- **153 examples**: maze generation, dungeon generation (including Bob Nystrom's algorithm), architecture (ModernHouse, Apartemazements), puzzles, growth models, percolation.

## Mechanical details

C# console application, .NET Core, no dependencies beyond standard library. Runs on Windows/Linux/macOS. Models defined in XML (`models.xml`). Output as PNG or .vox (MagicaVoxel). Fast pattern matching via multidimensional Boyer-Moore; incremental match tracking avoids full grid scans. Notable ports: TypeScript (web), JavaScript, Rust (Python library), Python, Julia. Funded by Embark Studios, Oskar Stålberg, Freehold Games.

## Security

MIT licensed. No security flags. Standalone offline tool, no network calls, no credentials. Standard .NET build-from-source trust model.

## Usage notes

- Name origin and theory: named after Andrei Markov Jr. (son of the Markov-chains Markov), whose 1951 string-rewriting "normal algorithms" (find the first matching rule, replace, repeat) were proved Turing-complete; MarkovJunior lifts this to grids, where a rule can match in many places at once, so the interpreter picks one match at random. Illustrated: at one step the maze rule `WBB → WAW` matches in 38 places and the maze finishes after 284 replacements with no match left; with two ordered rules the first digs forward and the second backtracks only when the first no longer matches (MazeBacktracker); the same program runs unchanged in 3D; ModernHouse emerges from ~500 lines of rules in 764 steps (recorded at commit 42aaf24, examples MazeGrowth, MazeBacktracker, ModernHouse) (source: https://www.instagram.com/reel/DebFucxs5Xp/)
