---
name: yarn-spinner
title: Yarn Spinner
url: https://github.com/YarnSpinnerTool/YarnSpinner-Unity
source_url: https://www.instagram.com/reel/DeuQdK6THpz/
source: instagram
category: framework
summary: "Open-source dialogue system (Secret Lab) for writing and running branching game dialogue in a screenplay-like scripting language — the Yarn Spinner compiler/runtime is engine-agnostic, with an official Unity integration (YarnSpinner-Unity) sending lines, player-choice options, and in-scene commands from scripted conversations to the game; used in shipped titles including Night in the Woods, A Short Hike, and Dredge; Unity integration repo: 845 stars, 129 forks; MIT."
tags:
  - dialogue-system
  - narrative-scripting
  - unity
  - game-development
  - csharp
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

Yarn Spinner is a dialogue system for writing interactive, branching conversations in Yarn, a simple screenplay-like markup language, then running them inside a game. At runtime the Yarn Spinner engine sends the host game lines of dialogue to display, options for the player to choose between, and commands that trigger in-scene behavior (e.g. playing an animation or setting a game-state flag) as the conversation plays out. The core compiler/runtime is engine-agnostic (C#); `YarnSpinner-Unity` is the official Unity integration package wiring that runtime into Unity's UI and scene systems.

## Mechanical details

Developed by Secret Lab with community contributions and support from NYU Game Center. 845 GitHub stars / 129 forks on the Unity integration repo (the core `YarnSpinnerTool/YarnSpinner` compiler repo is separate). Distributed via the Unity Asset Store, an Itch.io store page, or Package Manager git-URL install. Version 3.x introduced "Dialogue Presenters," a new model for how dialogue/options are shown on screen, replacing the deprecated presentation code from 2.x. Used in shipped commercial games including Night in the Woods, A Short Hike, Lost in Random, Dredge, Frog Detective, Button City, Escape Academy, Baladins, and Unbeatable.

## Security

MIT licensed. Local scripting/dialogue runtime with no network calls or telemetry — it only reads authored Yarn scripts and drives in-game UI/events.

## Sources

- [GitHub: YarnSpinnerTool/YarnSpinner-Unity](https://github.com/YarnSpinnerTool/YarnSpinner-Unity) — README, license, notable games
- [Instagram reel](https://www.instagram.com/reel/DeuQdK6THpz/) — named the tool as one of eight repos used to build a Claude-assisted farm game (catalog source; no link given in the reel itself)