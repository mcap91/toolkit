---
name: imageio-ffmpeg
title: imageio-ffmpeg
url: https://github.com/imageio/imageio-ffmpeg
category: framework
summary: Pure-Python FFmpeg subprocess wrapper that reads/writes video frames via pipes as generator functions, bundling platform-specific ffmpeg binaries in its wheels; maintainers now recommend PyAV instead for speed and features
tags:
  - ffmpeg
  - video
  - python
  - subprocess
  - pipes
  - video-io
  - imageio
reviewed: 2026-10-29
acquired: 2026-10-29
license: BSD-2-Clause
security_flags: []
overlaps: []
source: web
source_url: https://github.com/imageio/imageio-ffmpeg
---

## What it does

imageio-ffmpeg is a dependency-free Python library that wraps the `ffmpeg` command-line tool for reading and writing video files. It exposes two generator functions, `read_frames()` and `write_frames()`, that call `ffmpeg` in a subprocess and stream frame data over pipes, reliably terminating the process when done. It forms the basis of the ffmpeg plugin in the broader `imageio` library (which adds a higher-level API, camera support, and seeking), but can be used standalone.

Published wheels on PyPI bundle a platform-specific `ffmpeg` binary (Windows 7+, Linux kernel 2.6.32+, OSX 10.9+), so no separate ffmpeg install is required via `pip install imageio-ffmpeg`. The conda-forge package instead depends on the `ffmpeg` conda-forge package. Works with Python 3.7+, including PyPy.

## Differentiators

- **Pure-Python subprocess wrapper**: calls the ffmpeg binary over pipes rather than binding to the C library, trading speed for simpler packaging and distribution
- **Bundled binaries**: pip wheels ship the ffmpeg executable per platform, avoiding a separate system-level ffmpeg install
- **Generator-based streaming API**: `read_frames()` yields a metadata dict (codec, size, fps, duration) followed by raw frame bytes; `write_frames()` accepts frames via `.send()`
- Also exposes `count_frames_and_secs()`, `get_ffmpeg_exe()`, and `get_ffmpeg_version()` utility functions
- **Maintainers explicitly recommend PyAV instead**: the README states this library predates PyAV's binary wheels and "you should probably use PyAV instead; it is faster and offers more features," since PyAV binds ffmpeg at the C level instead of shelling out

## Mechanical details

Install with `pip install --upgrade imageio-ffmpeg` or `conda install imageio-ffmpeg -c conda-forge`. `read_frames(path, pix_fmt="rgb24", ...)` only accepts file paths, not file-like objects, because frames are piped from a subprocess. `write_frames(path, size, pix_fmt_in="rgb24", pix_fmt_out="yuv420p", fps=16, quality=5, codec=None, macro_block_size=16, audio_path=None, ...)` writes frames sent via the generator's `.send()` method, optionally muxing in an audio track from `audio_path`. The `IMAGEIO_FFMPEG_EXE` environment variable overrides which ffmpeg binary is used (bundled binary, conda ffmpeg, or system ffmpeg, checked in that order); `IMAGEIO_FFMPEG_NO_PREVENT_SIGINT=1` disables the library's default SIGINT-blocking behavior around the ffmpeg subprocess.

## Security

BSD-2-Clause licensed. No network access or credential handling — operates purely on local files by spawning a local ffmpeg subprocess. Commercial support available via a Tidelift Subscription; security reports are coordinated through Tidelift rather than a repo-native security policy.