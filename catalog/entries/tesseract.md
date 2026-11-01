---
name: tesseract
title: Tesseract OCR
url: https://github.com/tesseract-ocr/tesseract
source_url: https://www.instagram.com/reel/DfAVR6MtdFR/
source: instagram
category: cli-tool
license: Apache-2.0
summary: Open-source OCR engine (`libtesseract`) and CLI (`tesseract`), originally developed at HP and later Google, now maintained by Stefan Weil and Zdenko Podobny — LSTM-based neural line recognition in v4+ with the legacy v3 pattern-matching engine retained for compatibility, 100+ languages with UTF-8 output in plain text/hOCR/PDF/TSV/ALTO/PAGE formats; ~77.2k stars.
tags:
  - ocr
  - text-recognition
  - image-to-text
  - cli
  - open-source
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
security_flags: []
---

## What it does

Tesseract is an open-source OCR (optical character recognition) engine, distributed as a C/C++ library (`libtesseract`) and a command-line program (`tesseract`). Originally developed at HP Labs, open-sourced in 2005, and led by Ray Smith at Google until 2017; now maintained by Stefan Weil (lead) and Zdenko Podobny. Version 4+ added an LSTM (long short-term memory) neural-network line-recognition engine; the legacy pattern-matching engine from v3 is retained and selectable via `--oem` for compatibility. Recognizes 100+ languages with full UTF-8 Unicode output.

## Mechanical details

- CLI: `tesseract imagename outputbase [-l lang] [--oem ocrenginemode]`.
- Input formats: PNG, JPEG, TIFF, and other common image formats.
- Output formats: plain text, hOCR, PDF, TSV, ALTO, PAGE.
- APIs: native C and C++; third-party wrapper libraries exist for Python (pytesseract), Node.js, and other languages, documented separately from the core repo.
- Current stable release line: 5.x (5.0.0 shipped 2021-11-30).
- ~77.2k stars / 10.9k forks at review.

## Usage notes

- Used as the baseline "small model" for comparison against a larger model (e.g. Qwen) when training regression models that predict per-page accuracy gain and added latency for OCR-router escalation decisions. (source: https://www.instagram.com/reel/DfAVR6MtdFR/)

## Security

- Apache-2.0.
- Processes untrusted image/document input through a native C/C++ decoder — standard memory-safety surface for any native image-format parser.
- No disclosed CVEs reviewed in this pass.