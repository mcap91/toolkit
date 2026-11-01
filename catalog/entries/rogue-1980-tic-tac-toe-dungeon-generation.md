---
name: rogue-1980-tic-tac-toe-dungeon-generation
title: Rogue's 3x3 Grid ("Tic-Tac-Toe") Dungeon Generation Algorithm
url: https://www.instagram.com/reel/DfAALtXkvNs/
source_url: https://www.instagram.com/reel/DfAALtXkvNs/
source: instagram
category: agent-pattern
summary: Procedural dungeon-layout algorithm from Rogue (1980, by Michael Toy and Glenn Wichman, later joined by Ken Arnold), the game that gave the roguelike genre its name. Rather than placing rooms at arbitrary positions — which collide and can leave rooms unreachable — Rogue's source (version 5.4, files rooms.c and passages.c) divides its 80x24 terminal screen into a fixed 3x3 grid of nine cells. Each cell gets at most one room, randomly sized and positioned but confined to its cell so rooms can never overlap or share a wall; up to three cells (equally likely to be 0-3) are left empty, acting only as a point corridors pass through. Cells are then linked one at a time, each new link joining an already-connected cell to an unconnected neighbor, until all nine are reachable from the starting room, plus up to four extra random links so the layout isn't a single unique path. The result is a layout that is random but always fully connected and always resolvable within a single draw call's worth of simple grid math.
tags:
  - procedural-generation
  - dungeon-generation
  - roguelike
  - grid-based-generation
  - level-design
  - game-development
  - history
reviewed: 2026-10-30
acquired: 2026-10-30
license: N/A
security_flags: []
overlaps: []
---

## What it does

Rogue (1980) is the game that gave the roguelike genre its name; it was written by Michael Toy and Glenn Wichman, later joined by Ken Arnold, who took over much of the ongoing development. Most adventure games of the era were "canned" — the same fixed layout on every playthrough — so Rogue's authors had the program generate a new dungeon layout each time instead.

A naive approach — dropping rooms at arbitrary positions on the screen — causes rooms to overlap each other, and can leave some rooms with no path in. Rogue's solution, implemented in its C source (version 5.4, primarily `rooms.c` and `passages.c`), is to divide the fixed 80-column by 24-line terminal screen into a 3x3 grid of nine equally sized rectangular cells (a "tic-tac-toe board," in Wichman's own description):

- Up to three of the nine cells are randomly marked "gone" before room placement — the code picks `goneCount = random(0, 4)`, so 0, 1, 2, or 3 empty cells are equally likely outcomes, each removing one cell from the room-eligible set.
- Each remaining cell gets exactly one room. The room's width and height are each chosen randomly first (from 4 up to one less than the cell's width/height), and only then is the room positioned inside the cell using the leftover "slack" space, with a reserved one-column-left and one-row-bottom gutter always kept clear. Because a room can never grow or be placed outside its own cell, two rooms can never overlap or touch.
- Cells (whether they hold a room or are "gone," in which case a random point inside the empty cell stands in for a room) are then linked into corridors: starting from one random cell, the algorithm repeatedly links an already-connected cell to an adjacent still-unconnected cell until every one of the nine cells is reachable from the start. Up to four more random links between already-adjacent cells are added on top of that minimum spanning connection, specifically — per a comment in the source — "so that there isn't always just one unique passage through it," producing loops instead of a single critical path.
- Each corridor between two linked cells is dug as a straight run in the primary direction, a single sideways turn to realign, then a second straight run to the target wall or empty-cell point, so every corridor has at most two bends.

The result is a layout that is different every run, cannot produce an unreachable room, and is computed with only simple grid arithmetic and small-integer random draws, which was necessary on the limited hardware the game targeted. Wichman later said of the approach, "We landed on it early because we weren't smart enough to know how to do anything clever" — yet it was influential enough that the entire roguelike genre of randomly-generated dungeon games is named after it. Wichman and Toy also reportedly wanted more free-form, less grid-locked levels but never found a way to generate them; the later game Hack (an early roguelike) solved that differently.

The captured Instagram reel that surfaced this item is a third party's own code reimplementation of Rogue 5.4's documented rules (plus a separately-labeled "naive" demo of the room-collision problem the grid solves) — it is explicitly not the original Rogue codebase, and the reel states it is not affiliated with or endorsed by Rogue's creators. The original Rogue binary's source was not published at the time; the source referenced here and mirrored on GitHub is the later official Rogue 5.4.4 release under a BSD-style license.

## Sources

- [Instagram reel on Rogue's dungeon generation](https://www.instagram.com/reel/DfAALtXkvNs/) — caption, transcript, and on-screen text describing the 3x3 grid, empty-cell count, room placement, and corridor-linking rules, citing Rogue 5.4.4's `rooms.c`/`passages.c` and Wichman's "A Brief History of Rogue" (1997) (catalog source)
- [How did Rogue Generate its Random Dungeons? (howtomakeanrpg.com)](https://howtomakeanrpg.com/r/a/rogue-dungeon-generation.html) — line-by-line breakdown of the same algorithm from Rogue's C source, including the `goneCount = random(0, 4)` empty-cell draw, room-slack positioning, cell-linking, and corridor-digging pseudocode, plus the 2002 Wichman quote about wanting more free-form levels
- [Davidslv/rogue on GitHub](https://github.com/Davidslv/rogue) — archived mirror of the official Rogue 5.4.4 C source (including `rooms.c` and `passages.c`) under a BSD-style license; maintainer states it is an archive, not an official project repository
- [Rogue (video game) — Wikipedia](https://en.wikipedia.org/wiki/Rogue_(video_game)) — background on Toy, Wichman, and Arnold's roles and the game's history and influence

## Security

N/A — a description of a 1980s game's level-generation algorithm, not software to install. No security-relevant claims.