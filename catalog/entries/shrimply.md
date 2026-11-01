---
name: shrimply
title: Shrimply
url: "https://github.com/soirihiroka/shrimply"
category: cli-tool
summary: "Cross-platform GPU-accelerated video editor in Rust — GTK 4 / libadwaita UI, Skia + wgpu + Slang + CUDA rendering, FFmpeg media, PipeWire audio, Python compute server; requires NVIDIA or Apple Silicon GPU; pre-alpha; GPL-3.0+"
tags: [video-editor, rust, gtk4, gpu, cuda, ffmpeg, cross-platform]
reviewed: 2026-09-14
acquired: 2026-09-14
license: GPL-3.0-or-later
security_flags: []
overlaps: []
source: unknown
---

## What it does

Shrimply is a cross-platform video editor written in Rust. Currently pre-alpha.

Tech stack:
- **Interface**: GTK 4 + libadwaita
- **Rendering**: Skia, wgpu, Slang, CUDA
- **Media**: FFmpeg, PipeWire
- **Compute**: Python server

Requirements: NVIDIA or Apple Silicon GPU, Wayland or macOS 15+.

Pre-alpha status means expected issues: build difficulties, undocumented footguns, performance regressions, project file breakage, crashes and resource leaks.

## Security

- **License**: GPL-3.0-or-later (core); NVIDIA CUDA Toolkit, OptiX SDK, Optical Flow SDK, Video Codec SDK retain their own proprietary license terms
- **Pre-alpha**: not production-ready