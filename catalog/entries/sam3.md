---
name: sam3
title: SAM 3 (Segment Anything Model 3)
url: "https://github.com/facebookresearch/sam3"
category: framework
summary: "Meta's 848M-param unified foundation model for promptable segmentation in images and video; adds open-vocabulary detection/segmentation of all instances of a concept from a short text phrase or visual exemplars, on top of SAM 2's point/box/mask tracking. Checkpoints are gated (access request + HF auth)."
tags: [segmentation, computer-vision, foundation-model, open-vocabulary, video, image, pytorch, meta]
reviewed: 2026-08-17
acquired: 2026-08-17
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---
## What it does

SAM 3 is a unified foundation model for promptable segmentation across images and videos. It detects, segments, and tracks objects from either text prompts (a short noun phrase) or visual prompts (points, boxes, masks, image exemplars). Its distinguishing capability over SAM 2 is exhaustive open-vocabulary segmentation: given a text phrase, it finds and masks *every* instance of that concept in the scene. It reports 75–80% of human performance on the new SA-Co benchmark (270K unique concepts, ~50× larger than prior open-vocabulary segmentation benchmarks).

## Mechanical details

- **Architecture:** 848M parameters. A DETR-based detector conditioned on text, geometry, and image exemplars, plus a SAM 2-style transformer encoder-decoder tracker; detector and tracker share a vision encoder. A "presence token" improves discrimination between closely related prompts (e.g. "player in white" vs "player in red"); the detector/tracker are decoupled to reduce task interference.
- **API:** Python. `build_sam3_image_model()` + `Sam3Processor` for images (`set_image`, `set_text_prompt`, returns masks/boxes/scores); `build_sam3_video_predictor()` with a session/request API for video (JPEG folder or MP4).
- **Install:** Python 3.12+, PyTorch 2.7+ (2.10 shown), CUDA 12.6+ GPU; `pip install -e .`. Optional flash-attn-3 and cc_torch for faster inference.
- **Checkpoints are gated:** request access on the SAM 3 Hugging Face repo, then authenticate (`hf auth login`) to download.
- **SAM 3.1 update (2026-03-27):** improved checkpoints plus "Object Multiplex," a shared-memory approach for faster joint multi-object tracking; requires latest repo code.
- **Datasets:** releases SA-Co/Gold and SA-Co/Silver image benchmarks and SA-Co/VEval video benchmark (images/videos annotated with noun phrases → instance masks, including negative prompts with no matches).
- **Examples:** notebooks for image/video prediction, batched inference, an SAM 3 "agent" for complex text prompts, and use as a tool for an MLLM.

## Security

- **License:** SAM License (custom Meta license; reported as NOASSERTION by SPDX detectors) — review terms before commercial or redistribution use; it is not an OSI-approved open-source license.
- **Model access is gated:** checkpoints require an approved access request and authenticated Hugging Face download.
- **Runtime:** standard PyTorch/CUDA stack; requires loading model weights (pickle-based checkpoints — load only trusted checkpoints). No network services exposed by the library itself.
- Paper: arXiv:2511.16719 ("SAM 3: Segment Anything with Concepts").
