---
name: deep-live-cam
title: Deep-Live-Cam
url: "https://github.com/hacksider/Deep-Live-Cam"
category: framework
summary: "Real-time face swap and video deepfake from a single image — webcam live mode, multi-face mapping, mouth mask, GPU acceleration (CUDA/CoreML/DirectML/OpenVINO); built on InsightFace/GFPGAN; viral 50K+ stars but no stated SPDX license and uses non-commercial research models"
tags: [deepfake, face-swap, computer-vision, real-time, video]
reviewed: 2026-06-22
acquired: 2026-06-22
license: AGPL-3.0-only
security_flags: [non-commercial-models, ethical-risk]
overlaps: []
source: unknown
---

## What it does

Real-time face swapping application that takes a single source face image and applies it to a webcam feed or video. Core capabilities:

- **Live webcam mode**: select a face image, click "Live," stream via OBS
- **Image/video mode**: swap faces in pre-recorded content
- **Multi-face mapping**: different source faces on multiple subjects simultaneously
- **Mouth mask**: retain original mouth movement for accurate lip sync
- **GPU acceleration**: CUDA (NVIDIA), CoreML (Apple Silicon), DirectML (Windows), OpenVINO (Intel)
- **Face enhancement**: GFPGAN post-processing for quality

Built on InsightFace (inswapper_128_fp16.onnx) for face swapping and GFPGANv1.4 for face enhancement. Python 3.11, requires ffmpeg.

## Assessment

Extremely popular (50K+ stars) real-time deepfake tool. Not relevant to bioinformatics workflows but cataloged as a notable AI/CV tool. The ethical considerations are significant — while the tool includes NSFW content filtering, it's fundamentally a deepfake generator. The InsightFace model is explicitly non-commercial research only, creating a license conflict for any commercial use.

Worth knowing about for computer vision capability awareness, not for adoption.

## Mechanical details

- Install: `git clone`, download models (inswapper_128, GFPGANv1.4) to `models/`, `pip install -r requirements.txt`
- Run: `python run.py` (GUI) or `python run.py -s source.jpg -t target.mp4` (CLI)
- GPU: `--execution-provider cuda|coreml|directml|openvino`
- Python 3.11 required (especially on macOS)
- Pre-built binaries available for Windows/Mac (paid, v2.7 RC2)

## Security

- **License**: AGPL-3.0-only (repo), but InsightFace models are **non-commercial research only** — creates usage restriction
- **Ethical risk**: real-time face impersonation capability; built-in NSFW filter but no identity verification
- **Models**: downloaded from HuggingFace (~300MB); inswapper_128_fp16.onnx and GFPGANv1.4
- **Dependencies**: heavy — ONNX Runtime, PyTorch, OpenCV, InsightFace, GFPGAN
- **Maintenance**: active, many contributors, viral community