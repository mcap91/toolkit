---
name: yt-dlp
title: yt-dlp
url: https://github.com/yt-dlp/yt-dlp
category: cli-tool
summary: Feature-rich command-line audio/video downloader supporting thousands of sites — a community-maintained fork of youtube-dl with faster multi-threaded downloads, advanced format selection, subtitle embedding, and a plugin system for custom extractors/postprocessors; ~200k GitHub stars, releases roughly every 2 weeks; Unlicense (public domain); flagged by the music-industry group IFPI for EU piracy watchlist consideration, though IFPI itself notes its open-source/public-domain nature makes it hard to remove.
tags:
  - video-download
  - audio-download
  - cli
  - media-ingestion
  - youtube
  - ffmpeg
  - extractor-plugins
  - public-domain
reviewed: 2026-10-29
acquired: 2026-10-29
license: Unlicense
security_flags:
  - copyright-dual-use
overlaps: []
source_url: https://github.com/yt-dlp/yt-dlp
source: web
---

## What it does

yt-dlp downloads audio/video from thousands of sites via a per-site extractor system, not just YouTube. It builds on the now largely dormant youtube-dl with faster multi-threaded fragment downloads, finer-grained format selection (resolution/codec/container filters, merge-format control), subtitle embedding/conversion, SponsorBlock integration, and metadata/thumbnail embedding via ffmpeg postprocessors. A plugin system auto-discovers Python modules placed in `~/.yt-dlp/plugins/` (or a few other search paths) and loads them as additional extractors or postprocessors without modifying core code. Distributed as a single executable (Python, PyInstaller builds for Windows/macOS/Linux) and as a pip package; CLI-first, with Python API usage also supported by importing `yt_dlp`.

## Security

Unlicensed (public domain) — no license obligations for use or redistribution. Actively maintained with continuous commits and releases roughly every two weeks (latest observed: 2026.08.19), unlike youtube-dl which stopped shipping releases after 2021. The project's ability to download from paywalled or DRM-restricted platforms it supports extractors for makes it dual-use: the same mechanism that pulls a user's own public uploads also pulls copyrighted material without rights clearance, which is why the music-industry group IFPI pushed to add it to the EU's piracy watchlist in 2026 — IFPI's own filing acknowledged the open-source, public-domain, globally-distributed nature of the project makes it difficult to contain or remove. The plugin system executes arbitrary Python code dropped into a user-writable directory; this is an intentional extension point, not a flaw, but it means any plugin sourced from an untrusted third party runs with full local privileges.
