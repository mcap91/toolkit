---
name: mapgen4
title: mapgen4
url: "https://github.com/redblobgames/mapgen4"
category: cli-tool
summary: "Procedural wilderness map generator — real-time terrain regeneration as you paint; Delaunay/Voronoi mesh with 25K+ cells; elevation, rivers, rainfall, biomes; oblique projection rendering; TypeScript/JavaScript; Apache 2.0"
tags: [procedural-generation, map-generation, terrain, voronoi, delaunay, rivers, biomes, typescript, creative-coding, game-dev]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

Mapgen4 generates procedural wilderness maps in the browser with real-time terrain regeneration as you paint. Built on a Delaunay+Voronoi mesh supporting 25K+ cells (up to 1M+), with detailed river networks.

Features: elevation via distance fields, rainfall/biomes/evaporation/wind simulation, oblique projection rendering (not standard rotate+translate+scale), outline rendering.

Continuation of mapgen2 ideas (2010) at larger scale. Designed to look pretty rather than generate realistic terrain. Extensive blog post series documenting the algorithms.

## Mechanical details

Install: `npm install -g esbuild && npm install && ./build.sh`. Serve: `python3 -m http.server 8000`, visit `localhost:8000/embed.html`.

TypeScript with esbuild (no type checking in build — IDE only). Uses Delaunator (MapBox), fast-2d-poisson-disk-sampling, simplex-noise, flatqueue, gl-matrix.

By Red Blob Games (Amit Patel), author of extensive game programming tutorials.

## Security

Apache 2.0 licensed. Helper libraries (dual-mesh, prng) also Apache 2.0. Dependencies are ISC/MIT. Runs entirely client-side.