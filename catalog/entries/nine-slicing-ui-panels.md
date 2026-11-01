---
name: nine-slicing-ui-panels
title: Nine Slicing (9-Slice) for Scalable UI Panels
url: https://www.instagram.com/reel/DZqZpQbtQ79/
source_url: https://www.instagram.com/reel/DZqZpQbtQ79/
source: instagram
category: agent-pattern
summary: "Game-dev UI technique for resizing a panel/box sprite to any dimension without distorting its border art. Naively scaling a textured panel along an axis stretches the corners and looks worse the more it's scaled. Nine slicing splits the source image into a 3x3 grid — four corners, four edges, one center — and scales each region differently when the panel resizes: corners are repositioned but never scaled (so border art stays crisp), each edge stretches along only its own axis to connect the corners, and the center stretches on both axes to fill the middle. Requires only that the edge/center art be drawn so it tiles or stretches cleanly; built into most major engines as a first-class primitive (Godot's NinePatchRect/StyleBoxTexture, Unity's Sliced Sprite image type, and CSS's border-image-slice), so adopting it needs no custom tooling."
tags:
  - game-design
  - nine-slice
  - nine-patch
  - ui
  - sprite-scaling
  - game-development
  - godot
  - unity
reviewed: 2026-10-29
acquired: 2026-10-29
license: N/A
security_flags: []
overlaps: []
---

## What it does

A standard game-UI technique for resizing a bordered panel sprite (dialog box, button, menu frame) to any target size without stretching or blurring its corner/border art. Scaling a flat textured sprite along one axis stretches every pixel uniformly, so decorative corners warp and the distortion compounds with more scaling — the naive fix (hand-drawing a separate art asset per panel size) doesn't scale and makes every later UI tweak require redoing art.

Nine slicing instead divides the source image into a 3x3 grid of nine regions — four corners, four edges, and one center — and scales each region by a different rule when the panel is resized:

- **Corners** are repositioned to the panel's new extents but never scaled, so their art stays pixel-perfect regardless of panel size.
- **Edges** (top/bottom/left/right) stretch or tile along only their own axis (horizontal edges scale horizontally, vertical edges vertically) to span the gap between corners.
- **Center** stretches or tiles on both axes to fill the remaining middle area.

The only requirement on the source art is that the edge and center strips be drawn so they scale or tile cleanly (e.g. a repeating pattern or a flat gradient), since those are the regions actually being stretched.

The technique (also called 9-slice or 9-patch) is a built-in primitive in most major engines rather than something developers implement by hand: Godot exposes it via the `NinePatchRect` node (or a `StyleBoxTexture` margin set on a `Theme`), Unity via the Sprite Editor's border handles plus the UI `Image` component's "Sliced" image type, and CSS via `border-image-slice`. Because engine support is first-class, adopting the technique for a given panel is a matter of setting margin/border values on an existing node or sprite, not writing custom scaling code.

## Sources

- [Instagram reel, Isadora's Edge dev log](https://www.instagram.com/reel/DZqZpQbtQ79/) — caption, transcript, and on-screen text describing the corner-distortion problem and the corner/edge/center scaling rules (catalog source)
- [Godot Engine docs: NinePatchRect](https://docs.godotengine.org/en/stable/classes/class_ninepatchrect.html) — Godot's built-in node for nine-patch panels, patch margins, and axis stretch modes
- [spritelab.dev: 9-Slice Game UI — How It Works in Godot, Unity and CSS](https://spritelab.dev/guides/9-slice-game-ui) — cross-engine comparison of the same 3x3-grid technique and each engine's setup workflow

## Security

N/A — a game design/UI technique description, not software; no code, binary, or service to install.