---
name: jax
title: JAX
url: "https://github.com/jax-ml/jax"
category: framework
summary: "Python library for accelerator-oriented array computing and composable function transformations: jax.grad (autodiff to any order, forward/reverse), jax.jit (XLA compilation to CPU/GPU/TPU), and jax.vmap (auto-vectorization), plus sharding APIs to scale across thousands of devices. Apache-2.0; a research project, not an official Google product."
license: Apache-2.0
tags: [machine-learning, autodiff, jit, xla, gpu, tpu, numpy, numerical-computing]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

JAX is a Python library for accelerator-oriented array computation and program transformation. It can automatically differentiate native Python and NumPy functions — through loops, branches, recursion, and closures — via `jax.grad`, supporting forward- and reverse-mode differentiation composed to arbitrary order. It uses XLA to compile and run NumPy-style programs on CPUs, GPUs, and TPUs (`jax.jit`), and auto-vectorizes functions across array axes with `jax.vmap`. These transformations compose arbitrarily. For scaling, JAX offers compiler-based automatic parallelization, explicit sharding with automatic partitioning, and manual per-device programming with explicit collectives, addressable through a mesh/`PartitionSpec` sharding API.

The README notes JAX is a research project, not an official Google product, and to "expect sharp edges."

## Mechanical details

- **Install:** `pip install -U jax` (CPU); `pip install -U "jax[cuda13]"` (NVIDIA GPU); `pip install -U "jax[tpu]"` (Google TPU); ROCm and Intel GPU variants documented
- **Core transforms:** `jax.grad`, `jax.jit`, `jax.vmap`, composable (e.g. `jax.jit(jax.vmap(jax.grad(loss)))`)
- Supported platforms: Linux x86_64/aarch64, macOS aarch64, Windows x86_64/WSL2 (GPU support varies by platform; see the compatibility table)

## Security

Apache-2.0 licensed. JAX is a numerical-computing library with no network service of its own; JIT compilation invokes XLA locally. No security flags recorded from the observed material.

## How to use it

pip install jax
