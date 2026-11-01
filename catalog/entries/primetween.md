---
name: primetween
title: PrimeTween
url: https://github.com/KyryloKuzyk/PrimeTween
source_url: https://www.instagram.com/reel/DeuQdK6THpz/
source: instagram
category: framework
summary: Allocation-free Unity tweening library — animates Transform, RectTransform, SpriteRenderer, AudioSource, Light, Materials, UI Toolkit elements, and generic float/Color/Vector values in one line of code with sequences, delays, and coroutine/async-await support (delays allocate as part of C# async, nothing else does); tunable from the Inspector; pitched as a faster, allocation-free alternative to DOTween; a paid PRO tier adds visual Inspector-authored animation; free tier license is source-available but restricts repackaging/resale, not OSI-approved MIT/Apache; 2.0k stars, 83 forks.
tags:
  - unity
  - tweening
  - animation
  - performance
  - game-development
  - csharp
reviewed: 2026-10-30
acquired: 2026-10-30
license: custom (source-available; free use in apps/games, no repackaging or resale)
security_flags:
  - non-standard-license
overlaps: []
---

## What it does

PrimeTween is a Unity animation ("tweening") library that animates object properties — position, rotation, scale, color, UI/UI Toolkit values, material properties, camera properties, audio volume, and generic `float`/`Color`/`Vector` values — in a single line of code, with support for delays, sequences, coroutines, and async/await. All animation parameters are also exposed in the Inspector for designer tuning without code. The library is marketed as allocation-free at runtime (the one exception being that `async`/`await` itself allocates a small amount of garbage in C#, independent of PrimeTween), and as a drop-in, easier-to-learn replacement for the popular commercial DOTween library — PrimeTween ships migration documentation for teams switching from DOTween. A separate paid PrimeTween PRO tier adds an Inspector-based visual animation authoring tool (`TweenAnimation`) and claims faster runtime performance.

## Mechanical details

Installable via the Unity Asset Store or Unity Package Manager (UPM) through npm's scoped-registry mechanism (`com.kyrylokuzyk.primetween`). Over 250 automated tests per the project's own documentation. 2.0k GitHub stars, 83 forks. The free library's license is a custom, source-available license (not MIT/Apache): it permits using and modifying PrimeTween inside free or commercial apps/games distributed as binaries, and permits internal team/company redistribution, but prohibits distributing PrimeTween's own source/tarball inside derivative libraries or templates (use the npm install path instead) and prohibits reselling PrimeTween itself, modified or not.

## Security

Source-available but not OSI-approved (custom license terms above) — flagged as a non-standard license rather than a security defect. No evidence of network calls or telemetry in the free library; it is a local animation/tweening utility.

## Sources

- [GitHub: KyryloKuzyk/PrimeTween](https://github.com/KyryloKuzyk/PrimeTween) — README, features, license terms
- [Instagram reel](https://www.instagram.com/reel/DeuQdK6THpz/) — named the tool as one of eight repos used to build a Claude-assisted farm game (catalog source; no link given in the reel itself)