---
name: caire
title: caire
url: https://github.com/esimov/caire
category: cli-tool
summary: Go content-aware image resizing library and CLI implementing seam carving — computes an edge-energy map, repeatedly finds and removes (or duplicates) the lowest-cumulative-energy one-pixel-per-row seam to shrink or grow an image without uniform squeezing; optional face-detection and protective/removal masks to guide which regions survive; ~11k GitHub stars, MIT
tags:
  - seam-carving
  - content-aware-resize
  - image-processing
  - go
  - cli
  - computer-vision
  - face-detection
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags: []
source: instagram
source_url: https://www.instagram.com/reel/Deb3bVkHBLV/
---

## What it does

caire resizes images by removing or duplicating "seams" — connected paths of one pixel per row (or column) — instead of uniformly scaling, so it can narrow or widen an image while preserving regions with high visual detail.

It builds an energy map from edge detection (Sobel by default), then uses dynamic programming to find the seam with the lowest cumulative energy across the image, removes it, and recomputes the energy map before repeating. This process does not understand object semantics — it only tracks edge energy, so which regions survive depends on the image's edge content, not what a viewer would consider important.

Implemented in Go as both a library and CLI (`-in`/`-out` support file paths, stdin/stdout, and directory batch processing). CLI flags include `-width`/`-height`/`-perc` for target size, `-square`, `-face` to run embedded face detection (via the Pigo library) so faces aren't deformed, `-mask`/`-rmask` binary masks to protect or force-remove regions, `-blur`/`-sobel` to tune edge detection, and `-debug` for a GUI visualization of seam removal (via Gio).

## Security

MIT licensed. Processes local files by default; no network calls unless a URL is passed to `-in`. No identified malicious dependencies. ~11k GitHub stars, active releases (v1.5.0+).
