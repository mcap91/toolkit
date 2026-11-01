---
name: hyperframes
title: HyperFrames
url: https://github.com/heygen-com/hyperframes
source_url: https://www.reddit.com/r/vibecoding/comments/1wyxpef/look_what_i_built/
category: framework
summary: Open-source, agent-native HTML-to-video rendering system by HeyGen — "write HTML, render video"; seek-based deterministic rendering (window.__hf object exposing duration + seek()) captured headlessly via Puppeteer/CDP and encoded with FFmpeg; three-method FrameAdapter interface (init/getDurationFrames/seekFrame) plugs in GSAP, CSS/WAAPI, Lottie, Three.js, Anime.js, or a custom runtime, so e.g. Three.js scenes seek on hf-seek events and a window.__hfThreeTime clock instead of wall-clock time; CLI (`npx hyperframes init`) plus modular packages (core, engine, producer, browser studio editor, embeddable player, aws-lambda distributed render); migration skill from Remotion/Motion Canvas/Lottie/canvas verified frame by frame; installs as a Claude Code plugin-marketplace entry or standalone skill (`npx skills add heygen-com/hyperframes`); Node.js 22+ and FFmpeg required; Apache-2.0; ~75.5k stars/6.9k forks
tags:
  - video-generation
  - html-to-video
  - puppeteer
  - ffmpeg
  - three-js
  - agent-skill
  - claude-code-plugin
  - heygen
  - cli
  - remotion-alternative
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - brag
license: Apache-2.0
security_flags: []
source: reddit
---

## What it does

HyperFrames is an open-source, agent-native rendering system that turns HTML into video. Core design principle: "seek, don't play" — every composition exposes a `window.__hf` object with a duration and a `seek()` function that positions every clip, tween, and video at a given timestamp instead of relying on real-time playback. A headless renderer drives the same `window.__hf` interface via Puppeteer and Chrome DevTools Protocol: scrubbing the timeline in the browser-based studio editor calls `seek()`; capturing a frame for render calls `seek()` at that frame's timestamp, making output deterministic regardless of system speed.

Animation libraries integrate through a three-method FrameAdapter interface (`init`, `getDurationFrames`, `seekFrame`). Adapters ship for GSAP, CSS/WAAPI, Lottie, Three.js, and Anime.js, or a custom runtime. The Three.js adapter makes Three.js scenes seekable by driving them from `hf-seek` events and a `window.__hfThreeTime` clock instead of wall-clock time, so a Three.js animation (e.g. an exploding 3D object) can be captured frame-accurately.

The CLI (`npx hyperframes init my-video`) scaffolds a project; FFmpeg encodes the captured frames into video. A `/remotion-to-hyperframes` migration skill ports existing Remotion, Motion Canvas, Lottie, canvas, or other renders over, verified frame by frame. It installs as a Claude Code plugin-marketplace entry or standalone skill (`npx skills add heygen-com/hyperframes`), positioning it for agent-driven video generation — an agent writes the HTML/CSS/JS composition, HyperFrames renders it.

## Mechanical details

- Packages: `hyperframes` (CLI), `@hyperframes/core` (types/parsers/runtime), `@hyperframes/engine` (Puppeteer+FFmpeg capture engine), `@hyperframes/producer` (capture/encode/audio-mix pipeline), `@hyperframes/studio` (browser composition editor), `@hyperframes/player` (embeddable web component), `@hyperframes/shader-transitions` (WebGL shader transitions), `@hyperframes/aws-lambda` (distributed cloud rendering).
- Requirements: Node.js 22+, FFmpeg; development requires Git LFS (~240MB of test fixtures).
- Maintained by HeyGen (`heygen-com` org); Apache-2.0; ~75.5k stars / 6.9k forks at review.
- Reported usage (r/vibecoding, Oct 2026): a marketing video for an unrelated tool (salt.md) was built by prompting Claude Code (Opus 5.5) with a one-line brief ("Make a HyperFrames marketing video...30-45 seconds...modern with a wow effect"), then iterated over three feedback rounds; the exploding-cube effect was real Three.js 3D, the rest HTML composited from the target site's real screenshots, muxed to mp4 with ElevenLabs-generated voiceover/music (source: https://www.reddit.com/r/vibecoding/comments/1wyxpef/look_what_i_built/).

## Security

Apache-2.0. Headless rendering executes arbitrary HTML/CSS/JS (including fetched resources) inside a Puppeteer-controlled browser — the same class of risk as any headless-browser render pipeline (local file/network access from rendered pages, resource exhaustion on untrusted compositions). Repo ships a SECURITY.md for report intake; no disclosed CVEs or incident reports found in review.