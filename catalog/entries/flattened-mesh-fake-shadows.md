---
name: flattened-mesh-fake-shadows
title: Flattened Secondary Mesh as a Stylized Fake Shadow (Instead of Dynamic Shadow Rendering)
url: https://www.instagram.com/reel/DezJsUWuQqo/
source_url: https://www.instagram.com/reel/DezJsUWuQqo/
source: instagram
category: agent-pattern
summary: "Game-dev shadow technique that replaces an engine's built-in dynamic shadow system with a hand-controlled stand-in: a second, simplified version of the character mesh is flattened onto the floor via a material, and that flattened silhouette is used as the character's shadow. Reported benefits are twofold — it saves the performance cost of real-time shadow/lighting calculations, and it gives the artist direct control over the shadow's shape and softness so it can be made 'punchy' and stylized to match the game's art style rather than looking like a physically-accurate soft/dynamic shadow. Demonstrated in Unreal Engine by the two-person dev team of the upcoming roguelike 'Barrow and Blade' as one of three non-standard optimization techniques."
tags:
  - game-design
  - stylized-rendering
  - shadows
  - performance-optimization
  - material-technique
  - game-development
  - unreal-engine
reviewed: 2026-10-30
acquired: 2026-10-30
license: N/A
security_flags: []
overlaps: []
---

## What it does

A technique for producing a character's ground shadow without using the engine's real-time dynamic shadow system. A second, simplified mesh of the character (distinct from the render mesh) is used as the shadow's shape source; a material flattens that mesh onto the floor plane, projecting its silhouette as a 2D shape on the ground beneath the character. This flattened shape stands in for a cast shadow.

Reported motivations (from the source): it saves performance that would otherwise go to real-time shadow and lighting calculations, and it gives the team direct authorial control over the shadow's look — described as letting them create "punchy," stylized shadows that match the rest of the environment's art style, rather than the shadow looking like whatever the engine's dynamic lighting model happens to produce. Demonstrated in Unreal Engine by the two-person dev team of the hack-and-slash roguelike "Barrow and Blade," alongside two other non-standard optimization techniques, as part of an effort to run well across a wide range of hardware including the Steam Deck.

## Mechanical details

The source (a short dev-log reel) names the two ingredients — a simplified second character mesh, and "a material to flatten this onto the floor" — but does not show the material graph or explain how the flattening is done (e.g. a vertex shader collapsing the mesh's vertical axis, a planar projection, or an orthographic render-to-texture of the simplified mesh).

This sits in a known spectrum of ground-shadow techniques of increasing shape accuracy and cost: a simple decal/blob shadow (cheapest, least accurate — usually a generic circle or capsule shape projected under the character, independent of actual pose), a flattened stand-in mesh as here (shape follows the character's silhouette via a second mesh, no real shadow-map lookup), and full dynamic shadow casting from the render mesh (most accurate, most expensive, pose-correct down to limb detail). Unreal Engine developer forum discussions document a closely related "fake AO/shadow plane" pattern — a flattened plane with a dedicated fake-shadow material standing in for real shadow casting — and note that static shadows, dynamic shadows, and collision must be disabled on the stand-in geometry to avoid it double-shadowing or physically colliding alongside the real shadow/character.

## Sources

- [Instagram reel, Barrow and Blade dev team](https://www.instagram.com/reel/DezJsUWuQqo/) — caption, transcript, and on-screen text describing the flattened-mesh shadow technique as one of three optimization tricks (catalog source)
- [Epic Developer Community Forums: How do you fake dynamic shadows? — Let's share techniques](https://forums.unrealengine.com/t/how-do-you-fake-dynamic-shadows-lets-share-techniques/58423) — community-documented decal, flattened-plane, and capsule-shadow variants of the same fake-shadow problem space
- [unofficial-modding-guide.com: Practical Hacks to Wrangle Unreal Engine's Static Lighting](https://unofficial-modding-guide.com/posts/UE5LightingHacks/) — related Unreal lighting-performance workarounds

## Security

N/A — a game-rendering technique description, not software; no code, binary, or service to install.