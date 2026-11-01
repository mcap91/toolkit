---
name: manim
title: Manim (3b1b)
url: "https://github.com/3b1b/manim"
category: framework
summary: "Grant Sanderson's (3Blue1Brown) Python animation engine for explanatory math videos — scenes are Python classes composing Mobjects (LaTeX, shapes, graphs, 3D surfaces) with animations rendered via OpenGL, including an interactive live-preview mode; this is the original personal version, distinct from the community-maintained fork ManimCE; MIT, ~94k stars"
tags: [animation, mathematics, visualization, python, latex, opengl, education, video-generation, 3blue1brown]
reviewed: 2026-09-10
acquired: 2026-09-10
license: MIT
security_flags: [personal-project-api-instability]
overlaps: []
source: unknown
---

## What it does

Manim ("mathematical animation") is the animation engine Grant Sanderson wrote and uses to produce 3Blue1Brown videos. A scene is a Python class whose `construct` method builds and animates **Mobjects** — LaTeX/Tex text, geometric shapes, function graphs, vector fields, 3D surfaces — with a rich transformation vocabulary (Transform, FadeIn, Write, morphing between formulas). This repo (ManimGL) renders via OpenGL with an interactive mode: a live window, `self.embed()` IPython breakpoints inside scenes, and camera control during preview.

## Differentiators

- The defining tool of the "explanatory math video" genre; frame-accurate synchronization of formulas, graphs, and geometric intuition.
- Two-lineage ecosystem: this repo is 3b1b's personal, fast-moving version (ManimGL, `manimgl` on PyPI); the **Manim Community Edition** (`manim`, ManimCE) is the separately maintained fork with stabler APIs, better docs, and wider plugin support. Code written for one frequently does not run on the other.
- Heavily used as an LLM/agent target: "generate a Manim animation" is a common code-generation task, and several agent pipelines render Manim scenes as explainer output.
- LaTeX-native: mathematical typography is first-class, not an overlay.

## Mechanical details

- Install: `pip install manimgl` plus system dependencies (FFmpeg, LaTeX distribution, OpenGL); run `manimgl example_scenes.py OpeningManimExample`.
- Interactive workflow: `manimgl -se <line>` drops into a scene at a checkpoint; `-w` writes video files, `-o` opens the result.
- Python, MIT, ~93.7k stars, ~7.7k forks, 498 open issues; created 2015; pushed Sep 2026 (active); wiki, discussions, and GitHub Pages docs (3b1b.github.io/manim).

## Security

- **License:** MIT.
- `personal-project-api-instability` — the README historically warns this version serves 3b1b's own workflow; APIs change without deprecation cycles, and community support concentrates on ManimCE. Not a vulnerability, but a maintenance-planning fact.
- Rendering executes arbitrary Python and shells out to LaTeX/FFmpeg — standard code-execution surface for any scene file from an untrusted source.

## Usage notes

- ManimCE forked from 3b1b/manim in 2020 (source: https://www.instagram.com/reel/DeFTnCdMfC2/).
- Demonstrated example animations: applying z² to a 2D grid bends it, summing odd sine harmonics one by one builds a square wave, and a torus morphs into a sphere in 3D (source: https://www.instagram.com/reel/DeFTnCdMfC2/).
