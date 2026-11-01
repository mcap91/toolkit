---
name: demucs
title: Demucs
url: https://github.com/adefossez/demucs
category: cli-tool
summary: Hybrid Transformer music source separation model from Alexandre Défossez — splits a song into drums, bass, vocals, and other stems via dual waveform/spectrogram branches joined by a cross-domain transformer; MIT licensed, pip/uvx installable, 9.0 dB SDR on MUSDB HQ
tags:
  - audio
  - music-source-separation
  - stem-separation
  - transformer
  - pytorch
  - vocal-removal
  - signal-processing
reviewed: 2026-10-29
acquired: 2026-10-29
license: MIT
security_flags: []
overlaps: []
source: instagram
source_url: https://www.instagram.com/reel/DeecMf9nBBn/
---

## What it does

Demucs (Deep Extractor for Music Sources) is a music source separation model that splits a song into four stems: drums, bass, vocals, and everything else (accompaniment). Originally released by Alexandre Défossez at Meta's FAIR group as `facebookresearch/demucs`; now maintained independently at `adefossez/demucs` after Défossez left Meta to join Kyutai. Based on a U-Net convolutional architecture inspired by Wave-U-Net.

The current v4 release, Hybrid Transformer Demucs, reads the input mixture as both a raw waveform and a spectrogram in parallel branches. Each branch compresses the input through convolutional downsampling, a cross-domain transformer encoder in the middle exchanges information between the two branches (self-attention within each domain, cross-attention across domains), then both branches expand back out into four output tracks whose estimates are summed. It was trained on the MUSDB HQ dataset plus an extra 800-song training set, and reports 9.00 dB SDR on the MUSDB HQ test set (9.20 dB with sparse attention and per-source fine-tuning).

## Differentiators

- **Dual-domain hybrid architecture**: combines waveform and spectrogram processing branches joined by a transformer, rather than operating in a single domain
- **Multiple pretrained model variants** selectable via `-n`: `htdemucs` (default), `htdemucs_ft` (fine-tuned, ~4x slower), `htdemucs_6s` (experimental 6-source with guitar/piano, piano quality is weak), `hdemucs_mmi` (retrained v3 baseline), `mdx`/`mdx_extra` (MDX challenge-trained), quantized variants (`mdx_q`, `mdx_extra_q`)
- **Karaoke/two-stem mode**: `--two-stems=vocals` isolates one source against the rest of the mix
- **Won the Sony MDX (Music Demixing) challenge** with the v3 hybrid-domain release

## Mechanical details

Install via `uvx demucs PATH_TO_AUDIO_FILE` (no install step) or `pip install demucs` / `uv tool install demucs`. Requires Python 3.10+; ffmpeg recommended for flac output and broader format decoding. Quantized models need the `quantized` extra: `uvx "demucs[quantized]" -n mdx_q file.mp3`.

CLI flags: `--mp3` / `--mp3-bitrate` / `--mp3-preset` for MP3 output, `--flac` for FLAC, `--float32`/`--int24` for wav bit depth, `--segment SECONDS` to reduce memory on GPU (Hybrid Transformer models cap at 7.8s segments), `--shifts=N` for shift-trick averaging (GPU only, N× slower), `--overlap` to tune prediction-window overlap (default 0.25), `-j N` for parallel jobs (multiplies RAM use), `-d cpu` to force CPU. Also usable as a Python API via `demucs.separate.main([...])`. GPU separation needs ~3–7GB VRAM depending on arguments; CPU separation runs at roughly 1.5× track duration.

## Security

MIT licensed for the code; pretrained model weights carry unclear licensing since MUSDB HQ includes research-only data, and the 6-source model was trained on an internal Meta dataset likely under CC-NC-BY terms. No credential handling or network access required for local inference — pure local audio processing once models are downloaded.
