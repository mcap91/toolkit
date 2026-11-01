---
name: twine
title: Twine
url: https://github.com/klembot/twinejs
source_url: https://www.instagram.com/reel/De8mEDavJu2/
source: instagram
category: framework
summary: Open-source tool (since 2009, by Chris Klimas) for writing choice-based, state-tracking interactive fiction as linked "passages" shown as boxes on a map, connected by [[double-bracket]] links that become both player choices and map arrows; variables and if-checks gate content on player choices (e.g. a trust variable). Ships as a desktop/browser/Electron app (klembot/twinejs, GPL-3.0, ~2.9k stars); default story format is Harlowe (Leon Arnott, Zlib license), with SugarCube, Snowman, and Chapbook as alternatives. "Publish to File" exports a single self-contained HTML file playable in any browser or uploadable to itch.io; "Export as Twee" produces a plain-text passage format a separate parser can read into another engine. Netflix's "Black Mirror" episode Bandersnatch was written in Twine. Current release 2.12.1 (2026-10-06).
tags:
  - interactive-fiction
  - twine
  - harlowe
  - choice-based-narrative
  - hypertext-fiction
  - twee
  - game-development
  - open-source
  - gpl
reviewed: 2026-10-29
acquired: 2026-10-29
license: GPL-3.0
security_flags: []
overlaps: []
---

## What it does

Twine is an open-source tool, created by Chris Klimas in 2009, for writing interactive, nonlinear stories without code. A story is a set of linked "passages" — text blocks shown as boxes on a visual map. Writing a link in `[[double square brackets]]` both creates a player-facing choice and draws an arrow between the two passages on the map. Variables can record player choices (e.g. `(set: $trust to 0)`, then `(set: $trust += 1)` when the player brings tea to a character) and `(if:)` macros gate later content on those variables (e.g. a secret is shown only `(if: $trust >= 1)`), so earlier choices can be remembered and change later outcomes. Netflix's interactive film "Black Mirror" episode Bandersnatch was written in Twine.

Twine ships as a desktop/Electron app and a browser-based editor (source at `klembot/twinejs`, GPL-3.0, ~2.9k GitHub stars). Stories are written in a story format — a scripting language for passage content. Harlowe, maintained separately by Leon Arnott under the Zlib license, is Twine 2's default format; SugarCube, Snowman, and Chapbook are the other built-in formats.

Two export paths matter for using a Twine story outside the editor: "Publish to File" produces one self-contained HTML file that runs in any browser and can be uploaded as-is to a host like itch.io; "Export as Twee" produces Twee, a plain-text passage format (passage names, tags, and body text) that a separate parser can read into another runtime, such as a game engine.

## Mechanical details

- Current release: 2.12.1 (2026-10-06); 2.12.0 shipped 2026-04-10.
- License: Twine itself (`klembot/twinejs`) is GPL-3.0. Harlowe 3.3.9, the default story format, is licensed separately under Zlib by its maintainer Leon Arnott — the editor and the story-format language it ships with are not under one license.
- Twee is a plain-text serialization of a story's passages (e.g. `:: PassageName [tag] ... [[Link->Target]]`) plus a `StoryData` header naming the story format and version; it is meant to be read by external tooling, not rendered directly.
- No official or first-party integration connects Twine/Harlowe output to any game engine; any engine-side reader of Twee or Harlowe macros is third-party and typically scoped to the macros a given project actually uses, not the full Harlowe language.

## Security

No security-relevant behavior identified — Twine produces static HTML or plain-text story data; it does not execute arbitrary code or require elevated access to run.

## Sources

- [klembot/twinejs — GitHub](https://github.com/klembot/twinejs) — source, license, contributor list, star count
- [Twine (software) — Wikipedia](https://en.wikipedia.org/wiki/Twine_(software)) — history, creator, story formats, Bandersnatch connection
- [twinery.org](https://twinery.org/) — official site
- [Instagram reel](https://www.instagram.com/reel/De8mEDavJu2/) — catalog source; demonstrates a trust-variable/if-check passage flow, Publish to File vs. Export as Twee, and a one-off non-official Godot 4.3 parser written for that episode that reads Twee output, turns links into choices, and lights a lamp on a tagged passage — the parser supports only the passages, links, and Harlowe macros used in that specific story, not general Harlowe or an official Twine/Godot integration