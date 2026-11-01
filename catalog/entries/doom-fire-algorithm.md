---
name: doom-fire-algorithm
title: doom-fire-algorithm
url: https://github.com/filipedeschamps/doom-fire-algorithm
category: cli-tool
summary: Filipe Deschamps's playground of ~70 community reimplementations of the DOOM fire effect across JS/Rust/C++/Python/Go/Unity/Godot/etc. — a grid of 0-36 values mapped to a 37-color palette, bottom row pinned to 36, each cell takes the value below minus a random 0-2 (shifted up to two cells left) so the fire cools and flickers as it rises; 1.5k stars, 304 forks, actively maintained (pushed 2026-10-17); MIT.
tags:
  - doom-fire
  - palette-animation
  - pixel-art
  - procedural-generation
  - generative-art
  - creative-coding
  - javascript
  - fire-effect
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags: []
source: instagram
source_url: https://www.instagram.com/reel/DeRdV4OjhM-/
---

## What it does

A playground of roughly 70 community-contributed reimplementations of the fire effect from the original DOOM video game, started by Filipe Deschamps with a plain JavaScript/HTML-table version (fire.js) and open to pull requests in any language. The algorithm: a grid of integers 0-36, each mapped to one of 37 colors in a palette running black to white; the bottom row is pinned to 36 (hottest/whitest). Each step, a cell's new value is the value of the cell directly below it minus a random amount of 0, 1, or 2 (floored at 0); that same random amount also shifts the written value up to two cells to the left, so the fire leans and flickers as it cools from white to yellow to red to black while rising. Setting the bottom row to 0 lets the fire burn out on its own.

## Mechanical details

- Reference implementation: fire.js plus `playground/1st-implementation-with-tables` (HTML table rendering).
- Roughly 70 community ports across JS/Canvas/PixiJS, Rust (+WASM, terminal), embedded C (STM32F429 + mbed), Lua/Love2D, Kotlin/Android, SDL2, PSP homebrew, C++ (SFML/Qt/raylib), Elixir, Python (PyGame/Kivy/curses), Go/Ebiten, Java/LibGdx, Unity3D, Dart, iOS/SpriteKit, Delphi/Firemonkey, React/React Native, Flutter, Godot (GDScript/shaders), Bash, C# console, SwiftUI+Metal, Excel/VBA, Fortran, and more.
- 1,539 stars, 304 forks as of this review (GitHub API); created 2019-01-04, last pushed 2026-10-17 — actively maintained via community pull requests.
- Inspired by Fabien Sanglard's "How DOOM fire was done" writeup on the original PSX port.

## Security

Source-available, MIT licensed. The core algorithm is pure grid math plus a palette lookup, run entirely client-side/locally with no network calls documented; individual community ports vary by language/runtime and were not independently audited.

## Usage notes

- The captured video's own presentation enlarged the grid to 75x96 cells (page original: 50x46) at 24 steps/second, with a secondary 25x17 debug-size grid at roughly 6 steps/second, labeling cell values against the 37-entry `fireColorsPalette` (fire.js line 5); the enlarged grids, palette layout, annotations, and timing were made for the video, not part of the original repo (source: https://www.instagram.com/reel/DeRdV4OjhM-/).