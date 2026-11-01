---
name: anything2explainer
title: anything2explainer
url: "https://github.com/Vincentwei1021/anything2explainer"
category: skill
summary: "Claude Code / Codex skill that turns any topic into a narrated motion-graphics explainer video (1280×720 H.264) — 9-stage pipeline: research → narration → TTS voiceover → storyboard → parallel build agents writing Remotion (React/TS) components per shot → QC; black-canvas white-line-art style, word-boundary-aligned subtitles, chapter progress bar; Chinese and English; 1–3 hours wall clock; PolyForm Noncommercial"
tags: [video, explainer, remotion, tts, motion-graphics, skill, multi-agent, chinese, english]
reviewed: 2026-09-14
acquired: 2026-09-14
license: PolyForm-Noncommercial-1.0.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

A Claude Code / Codex skill that takes a topic (or article/document) and produces a narrated motion-graphics explainer video. Every frame is drawn in code with Remotion (React + TypeScript) — no stock footage, no generative video models.

**Output**: 1280×720 @ 30fps H.264 MP4 with synchronized voiceover, word-boundary-aligned subtitles, chapter cards, top HUD, bottom chapter progress bar, and full paper trail (research doc with source URLs, narration, storyboard, per-shot source code, QC reports).

**Pipeline** (9 stages, 4 human checkpoints):
1. Scaffold Remotion project from template
2. Research agent produces sourced research doc
3. Narration & TTS voiceover with frame-accurate timeline
4. Storyboard: one line per shot with frame range, beat, visuals, motion
5. Overlays & primitives (title, chapter cards, HUD, icons)
6. Pilot: first shot group → 30-second preview cut for approval
7. Parallel build: remaining groups, 5–7 shots per agent, pure-function Remotion components
8. Full render + quantitative frame metrics
9. QC agents per chapter, fix agents per group, re-verification

**Scale by length**:

| Length | Lines/shots | Build agents | Wall clock |
|---|---|---|---|
| 2–3 min | 24–32 | 4–6 | ~1 h |
| 3–5 min | 40–50 | 8 | ~2 h |
| 5–8 min | 60–80 | 10–14 | ~2–3 h |

**Languages**: Chinese (edge-tts Yunxi) and English (kokoro-82m Liam), with alternative TTS engines supported (kokoro-onnx, piper, edge, or bring-your-own audio).

**Visual style**: black canvas, white line art with purple accents, ultra-bold headline type. Two backdrop options (star-field + fog gradient, or dot-field wave). Deterministic rendering — pure functions of frame number with seeded randomness.

## Mechanical details

- **Stack**: Node ≥18, Remotion 4, React 19, ffmpeg, Python 3 (TTS scripts)
- **TTS engines**: edge-tts (cloud, Microsoft), kokoro-82m (local CPU), kokoro-onnx, piper
- **Rendering**: headless Chromium on CPU, no GPU required
- **Reproducibility**: identical frames on re-render (seeded randomness, computed text fitting)
- **Platform**: macOS primary, Linux/ARM verified (Raspberry Pi 5), Windows untested

## Security

- **License**: PolyForm Noncommercial 1.0.0 (commercial use requires author authorization); videos you produce are yours
- **TTS**: edge-tts makes cloud calls to Microsoft; kokoro/piper run fully local
- **No dangerous patterns**: skill reads SKILL.md, runs shell scripts, renders via Chromium