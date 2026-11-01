---
name: cupy
title: CuPy
url: "https://github.com/cupy/cupy"
category: framework
summary: "NumPy/SciPy-compatible Python array library for GPU-accelerated computing — drop-in replacement on NVIDIA CUDA (12.x/13.x) and AMD ROCm 7.0 with low-level CUDA access (RawKernels, Streams, Runtime APIs); includes cuSignal; 11K stars, 127 contributors, MIT, Preferred Networks"
tags: [gpu, numpy, scipy, cuda, rocm, array-computing, python, signal-processing]
reviewed: 2026-07-01
acquired: 2026-07-01
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

CuPy is a NumPy/SciPy-compatible array library that runs existing NumPy/SciPy code on GPUs without code changes. Import `cupy` instead of `numpy` and operations execute on NVIDIA CUDA or AMD ROCm hardware. Also provides direct access to low-level CUDA features: RawKernels for custom CUDA C/C++ code, Streams for concurrent execution, and CUDA Runtime API calls. 11K GitHub stars, 127 contributors.

Includes cuSignal (merged in v13.0.0) for GPU-accelerated signal processing. Utilizes CUDA Toolkit libraries including cuBLAS, cuRAND, cuSOLVER, cuSPARSE, cuFFT, cuDNN, and NCCL. Used by Microsoft DeepSpeed, vLLM, DALI, spaCy, cuDF, and cuML.

## Differentiators

- **Drop-in replacement**: Existing NumPy/SciPy code runs on GPU by changing the import — API-compatible, speeds up some operations more than 100x
- **Low-level access**: RawKernels allow custom CUDA C/C++ to operate directly on CuPy arrays, bridging high-level Python and custom GPU code
- **Broad platform support**: CUDA 12.x, CUDA 13.x, and ROCm 7.0 (experimental) across x86_64 and aarch64; Python 3.10–3.14
- **Professional backing**: Maintained by Preferred Networks with community contributors; NeurIPS 2017 publication; latest release v14.1.1 (June 2026)

## Mechanical details

Install via pip (`cupy-cuda12x`, `cupy-cuda13x`, `cupy-rocm-7-0`), conda (`conda install -c conda-forge cupy`), or Docker (`cupy/cupy`). Slim install via `cupy-core`. Conda supports `cuda-version` metapackage for version pinning. Pre-release builds available via `pip.cupy.dev/pre`.

Core API mirrors NumPy: `cp.array`, `cp.arange`, `cp.sum`, etc. Memory transfers between CPU and GPU handled automatically.

## Security

MIT licensed. 127 contributors, ~1K forks, active conda-forge packaging with dedicated issue tracking (`cupy-feedstock`). No credential handling or network access — pure computation library. Dependencies are NumPy + CUDA/ROCm runtime.