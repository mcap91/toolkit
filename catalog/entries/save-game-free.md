---
name: save-game-free
title: Save Game Free
url: https://github.com/BayatGames/SaveGameFree
source_url: https://www.instagram.com/reel/DeuQdK6THpz/
source: instagram
category: framework
summary: Bayat Games' free Unity save/load library — serializes game data to Binary, JSON, or XML with optional encryption via a static SaveGame.Save/Load API, supports serializable complex/custom classes, works across Windows/Linux/macOS/Android/iOS/tvOS/Samsung TV/WebGL, and persists state across scene loads without reinitialization; a paid Save Game Pro tier adds support for saving native Unity types (GameObjects, Transforms) directly; 672 stars, 65 forks; MIT.
tags:
  - unity
  - save-system
  - serialization
  - persistence
  - game-development
  - csharp
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

Save Game Free is a save/load library for Unity that persists game data (player progress, scores, custom serializable classes) to disk using a simple static API — e.g. `SaveGame.Save("score", score)` / a matching `Load` call — with no per-scene reinitialization required, since it keeps its state in static properties. It supports three storage formats (Binary, JSON, XML) and optional encryption so saved files aren't trivially editable, and serializes any class marked `[Serializable]`, though it does not support serializing native Unity types (e.g. `GameObject`, `Transform`) directly — that capability is reserved for the paid "Save Game Pro" upgrade. Ships cross-platform support for Windows, Linux, macOS, Android, iOS, tvOS, Samsung TV, and WebGL.

## Mechanical details

672 GitHub stars, 65 forks, 24 watchers; latest listed Asset Store version 2.4.0. Distributed via the Unity Asset Store, GitHub releases, or direct source download; documentation hosted at docs.bayat.io/savegamefree. Supports async/await file operations and reports Unity 6 compatibility in its current release notes.

## Security

MIT licensed. Local file-based persistence library — reads/writes save files on-device; the optional encryption feature is for protecting save-file integrity against casual tampering, not a cryptographic security guarantee. No network calls or telemetry observed.

## Sources

- [GitHub: BayatGames/SaveGameFree](https://github.com/BayatGames/SaveGameFree) — README, feature list, license
- [Instagram reel](https://www.instagram.com/reel/DeuQdK6THpz/) — named the tool as one of eight repos used to build a Claude-assisted farm game (catalog source; no link given in the reel itself)