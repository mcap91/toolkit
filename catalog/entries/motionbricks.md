---
name: motionbricks
title: MotionBricks (NVIDIA)
url: https://github.com/NVlabs/motionbricks
source_url: https://www.instagram.com/reel/DfHyJofDMqS/
source: instagram
category: framework
summary: NVIDIA's modular latent generative model (SIGGRAPH 2026 / ACM TOG) for real-time character and robot motion synthesis — given 4 recent poses and up to 4 target poses it generates the in-between motion at 30 Hz via a root-path module, a masked-token pose transformer, and a VQ-VAE decoder; chaining generations with application-supplied targets produces continuous locomotion, navigation, and object interaction ("Smart Primitives") with no retraining; ships pretrained ONNX checkpoints for the SOMA human body model and the Unitree G1 robot, a Python runtime (Warp/Newton/TensorRT) and demo/editor apps; requires an NVIDIA GPU (TensorRT); code Apache-2.0, models under the NVIDIA Open Model Agreement, bundled sample motions restricted to NVIDIA evaluation use only; ~561 stars, 55 forks.
tags:
  - nvidia
  - motion-generation
  - character-animation
  - robotics
  - real-time
  - generative-model
  - tensorrt
  - onnx
  - vq-vae
  - siggraph
reviewed: 2026-10-30
acquired: 2026-10-30
license: Apache-2.0 (code); NVIDIA Open Model Agreement (models); NVIDIA Sample Data Evaluation License (sample motions)
security_flags: []
overlaps: []
---

## What it does

MotionBricks is NVIDIA's real-time motion-generation model for animating characters (the SOMA parametric human body model) and robots (Unitree G1), introduced at SIGGRAPH 2026. Given the character's current motion (its 4 most recent poses, "context") and one or more target poses placed ahead ("target"), it generates every in-between frame, deciding transition duration itself (one generation produces 6–16 tokens of 4 poses, roughly 0.6–1.9 s of motion). Chaining generations — feeding the last 4 played poses back in as context and letting the calling application choose new targets — turns a single inbetweening model into continuous locomotion, keyframe animation, or scripted object interactions. "Smart Primitives" package target poses as reusable building blocks for behaviors like vaulting, ducking, and sitting that compose around obstacles without retraining the model.

## Mechanical details

Three learned modules do the work: a root module predicts the duration and path of the character's root; a pose module (a masked-token transformer) predicts motion tokens along that path; a decoder (a VQ-VAE with several codebook heads) turns tokens into continuous motion reaching the targets. One runtime and code path drives both the SOMA human skeleton and the Unitree G1 robot — only the pose layout differs. Pretrained checkpoints (MotionBricks-SOMA-RP-v1, MotionBricks-G1-RP-v1; both trained on the Bones RigPlay 1 motion-capture dataset at 30 FPS) are distributed as SafeTensors on Hugging Face and bundled as exported ONNX models in the repo. The Python runtime is built on NVIDIA Warp, Newton, and TensorRT (TensorRT requires an NVIDIA GPU; tested on RTX 4090, Windows/Linux x86-64; first launch builds a cached TensorRT plan, taking a few minutes). Ships two demos (Inbetweener: place poses, generate motion through them; Scene Preview: a character walks/runs/vaults/ducks/sits through a scene with 6 style modes) and two editors (Smart Primitive Editor, Scene Editor) for authoring new primitives and scenes. ~561 stars, 55 forks on GitHub as of 2026-10-30; not accepting external contributions. A separate community GGML/C++ port (localai-org/motion-bricks.cpp) exists with ~334 stars. Related NVIDIA humanoid-motion projects referenced in the repo: Kimodo, ARDY, SOMA Body Model, BONES-SEED Dataset, ProtoMotions, SOMA Retargeter, GEM, GEAR SONIC.

## Security

Code is Apache-2.0; pretrained model weights (SOMA/G1 checkpoints, ONNX exports) are licensed separately under the NVIDIA Open Model Agreement, which permits commercial use and redistribution of modified models. Bundled sample motion clips (BVH/CSV) are under a separate NVIDIA Sample Data Evaluation License restricted to internal evaluation/testing of NVIDIA technologies — not for redistribution or published output. Requires downloading and installing TensorRT runtime packages (tensorrt-cu12 and related) governed by the separate NVIDIA TensorRT Software License Agreement; review those terms before use. No code-execution or network-call security concerns beyond a standard local ML inference runtime requiring an NVIDIA GPU driver and CUDA/TensorRT stack.

## Sources

- [GitHub: NVlabs/motionbricks](https://github.com/NVlabs/motionbricks) — README, license, model cards
- [Instagram reel](https://www.instagram.com/reel/DfHyJofDMqS/) (@hyun2xyz) — demonstrates MotionBricks generating a zigzag walk from a T-pose with no input motion clips, driven by a continually-updated target pose
- [GitHub: localai-org/motion-bricks.cpp](https://github.com/localai-org/motion-bricks.cpp) — community GGML/C++ port, noted for context on ecosystem activity