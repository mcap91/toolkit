---
name: audio2face-3d
title: NVIDIA Audio2Face-3D
url: https://github.com/NVIDIA/Audio2Face-3D
source_url: https://www.instagram.com/reel/De369jptIw-/
source: instagram
category: framework
summary: NVIDIA technology collection that generates 3D facial animation — synchronized jaw/tongue/eye articulation plus emotional expression inferred from speech tone — from pre-recorded or real-time audio, driving a character via mesh deformation, joint transforms, or blendshape weights; ships as a C++/Python inference SDK (MIT), a Python+Docker model-training framework (Apache-2.0), an Autodesk Maya plugin (MIT), an Unreal Engine 5.4/5.5/5.6 Blueprint-integrated plugin with a MetaHuman sample project (MIT), and a gRPC containerized NIM microservice for multi-user deployment (NVIDIA Software License Agreement); pre-trained regression (v2.3) and diffusion (v3.0) lip-sync models (Mark/Claire/James voices) and emotion-inference models are distributed separately on Hugging Face under an NVIDIA Open Model license (Audio2Emotion models under a custom license restricted to use with Audio2Face only); mixed licensing across code and model-weight components.
tags:
  - facial-animation
  - lip-sync
  - nvidia
  - audio-to-face
  - blendshapes
  - unreal-engine-plugin
  - maya-plugin
  - real-time
  - metahuman
reviewed: 2026-10-30
acquired: 2026-10-30
license: mixed (MIT SDK/Maya/UE5 plugins, Apache-2.0 training framework, NVIDIA Software License NIM, NVIDIA Open Model / custom license on model weights)
security_flags:
  - mixed-licensing
overlaps: []
---

## What it does

Audio2Face-3D generates high-fidelity 3D facial animation from an audio source, taking either a pre-recorded file or a real-time stream and synthesizing the synchronized motion of jaw, tongue, and eyes plus facial-skin deformation. It produces two combined outputs: phonetically accurate lip-sync, and emotional expression inferred from the tone of the speech. The resulting performance drives a target character through one of three output modes: direct mesh deformation, joint/bone transforms, or blend shape weights — letting it plug into whatever rigging approach a given character pipeline already uses.

The NVIDIA/Audio2Face-3D GitHub repo is a hub, not a single codebase — it links the actual components: the Audio2Face-3D SDK (a C++ library for embedding real-time inference directly in custom software, tools, or batch pipelines); the Audio2Face-3D Training Framework (the same toolset NVIDIA used to train its own Mark/Claire/James models, for training a custom model on a studio's own lip-synced data, including multi-language support); the Maya ACE (MACE) plugin (an artist-facing Maya UI for generating and previewing facial animation in-viewport, loading any compatible model via its JSON model card, exporting as Maya keyframes or FBX); the Unreal Engine 5 plugin (Blueprint-node integration for driving a character's facial rig at editor time, with a sample project demonstrating setup against Epic's MetaHuman rig); and the Audio2Face-3D NIM (NVIDIA Inference Microservice) — a containerized, gRPC-based service for serving concurrent inference requests to many clients at once, aimed at centralized studio deployments or web/cloud-hosted digital humans.

## Mechanical details

- **SDK**: C++/Python, cross-platform, GPU-accelerated via NVIDIA hardware with a CPU fallback; MIT license.
- **Training Framework**: Python, distributed as a Docker container; Apache-2.0 license; produces a trained model plus a JSON model card for use by the other components.
- **Maya ACE (MACE)**: v2.0, Autodesk Maya plugin module + C++/Python source; local or remote (microservice) inference; MIT license.
- **Unreal Engine 5 plugin**: v2.5, separate builds for UE 5.4/5.5/5.6, `.uplugin` + C++ source, Blueprint-only workflow for standard use, full source available for C++ extension; MIT license; requires installing both the core ACE Unreal plugin and a separate Audio2Face-3D Models plugin.
- **NIM**: Docker container, gRPC protocol, licensed under the NVIDIA Software License Agreement and Product-Specific Terms for AI Products (not MIT/Apache).
- **Models (Hugging Face, not this repo)**: Audio2Face-3D regression models (v2.3: Mark, Claire, James voices) and a newer diffusion model (v3.0), distributed as open weights (onnx-trt) under an "Nvidia Open Model" license; separate Audio2Emotion models (production v2.2, experimental v3.0) infer emotional state from audio under a custom license that restricts use to "with Audio2Face only"; a sample training dataset (Claire, audio + blendshape + geometry-cache data) is licensed "evaluation only."

## Security

Mixed licensing is the main thing to track before adopting: the SDK/plugin code is permissively licensed (MIT/Apache-2.0), but the NIM microservice carries NVIDIA's own commercial software-license terms, and the pre-trained model weights carry their own non-OSI "Open Model"/custom licenses with usage restrictions distinct from the code license. No code-execution or credential-handling risk pattern observed in the SDK/plugin components beyond standard GPU-accelerated inference; the NIM is a server component and should be evaluated under normal containerized-service security practice (network exposure, image provenance) before production deployment.

## Sources

- [GitHub: NVIDIA/Audio2Face-3D](https://github.com/NVIDIA/Audio2Face-3D) — repo-collection README: component list, licenses, target audiences, feature descriptions
- [Instagram reel](https://www.instagram.com/reel/De369jptIw-/) — named "Audio2Face-3D" as one of five repos that "turn Claude into an entire game studio," citing voice-line-to-lip-sync facial animation (catalog source; no link given in the reel itself)