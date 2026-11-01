---
name: vidnote
title: Vidnote
url: "https://github.com/amingilani/vidnote"
category: cli-tool
summary: "Self-hosted video-lecture-to-markdown converter with slide screenshots (Whisper + PySceneDetect); 'heavily vibe-coded' single-purpose tool — useful concept for certification-course capture but low polish and bus-factor 1"
tags: [video, transcription, slides, markdown, whisper, lecture-capture]
reviewed: 2026-06-19
acquired: 2026-06-19
license: UNLICENSED
security_flags: [single-contributor, no-tests, no-license, vibe-coded]
overlaps: [faster-whisper, whisperx]
source: unknown
---

## What it does

Containerized pipeline that converts a video lecture into a Markdown document with correlated slide screenshots:

1. Extracts audio → transcribes with OpenAI Whisper
2. Detects scene changes with PySceneDetect (ContentDetector, configurable threshold)
3. Inserts slide screenshots at corresponding timestamps in the transcript
4. Outputs `transcript.md` + `images/` directory

Runs via Podman container. Batch processing supported via `batch_process.sh` (idempotent — skips already-processed videos).

## Assessment

The concept is directly relevant for converting certification course videos into agent-readable markdown with visual context. However, the author explicitly calls it "heavily vibe coded" for a single personal use case (converting lectures at clares.ca). No tests, no stated license, single contributor, minimal error handling.

The pipeline is straightforward enough to reimplement with faster-whisper/whisperX + PySceneDetect if the concept proves valuable. More useful as a reference architecture than as an adoptable dependency.

## Mechanical details

- **Runtime**: Podman container (Python 3.11, FFmpeg, OpenCV)
- **Usage**: `./run_processor.sh <video> <output_folder>`
- **Batch**: `./batch_process.sh` over `vids/` directory
- **Scene threshold**: `--threshold` (default 15.0; lower = more sensitive)
- **Output**: `transcript.md` with inline image references + `images/` directory

## Security

- **License**: none stated — no SPDX identifier, no LICENSE file observed
- **Dependencies**: Whisper, PySceneDetect, OpenCV, FFmpeg — all well-known, but unpinned
- **Code quality**: no tests, no CI, self-described "heavily vibe coded"
- **Supply chain**: single contributor, personal project
- **Dangerous patterns**: none observed — container isolation is a positive
- **Maintenance**: appears to be a one-off personal tool