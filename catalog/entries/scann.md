---
name: scann
title: ScaNN
url: "https://github.com/google-research/google-research/tree/master/scann"
category: framework
summary: "Google Research library for efficient large-scale vector similarity search — anisotropic vector quantization (AVQ) for Maximum Inner Product Search plus SOAR indexing, partition/score/rescore search pipeline, native Python and optional TensorFlow APIs, AVX/NEON-optimized x86/ARM wheels; powers Vertex AI Vector Search; Apache-2.0"
tags: [similarity-search, nearest-neighbor, quantization, embeddings, ann-search, python, tensorflow]
reviewed: 2026-10-13
acquired: 2026-10-13
license: Apache-2.0
security_flags: []
overlaps: [faiss, hnswlib]
source: unknown
---

## What it does

ScaNN (Scalable Nearest Neighbors) is a Google Research library for efficient similarity search over large vector datasets. It ships as a subdirectory of the `google-research/google-research` monorepo rather than a standalone repository. Core algorithm is anisotropic vector quantization (AVQ) — from "Accelerating Large-Scale Inference with Anisotropic Vector Quantization" (Guo et al., ICML 2020) — built for Maximum Inner Product Search (MIPS), plus Euclidean distance support. SOAR ("SOAR: Improved Indexing for Approximate Nearest Neighbor Search", Sun et al., NeurIPS 2023) adds a redundant backup routing path so a second index can recover neighbors AVQ's primary clustering route misses. Optimized for x86 (AVX/FMA) and ARM (NEON) processors; no GPU backend.

## Differentiators

- **Three-stage search pipeline**: partitioning (optional tree-based space partitioning to shortlist candidate clusters), scoring (fast approximate distance via the AVQ quantizer, or brute force), and rescoring (exact distance recomputation over the shortlist to recover accuracy lost to quantization)
- **Benchmark positioning**: historically state-of-the-art throughput-at-recall on ann-benchmarks.com's glove-100-angular dataset versus other ANN libraries on angular/cosine workloads, per its README and independent third-party benchmarking at release
- **Dual API**: native Python bindings (`scann.scann_ops_pybind`, the recommended path) and optional TensorFlow ops (`scann.scann_ops`) that embed ANN search directly into a TF SavedModel, including custom TF Serving Docker images
- **Production lineage**: the underlying ANN engine behind Google Cloud's Vertex AI Vector Search managed service

## Mechanical details

Install via `pip install scann` — `manylinux_2_27` wheels on PyPI, current release 1.4.2 (Aug 2025). Linux only (no official macOS/Windows wheels); Python 3.9–3.13. x86 wheels require AVX+FMA; ARM wheels require NEON. As of ScaNN 1.4.0, TensorFlow integration is opt-in (`pip install scann[tf]`) rather than bundled by default. Building from source needs Bazel 7.x, Clang 19, libstdc++ for C++17 (via GCC 9+), and TensorFlow 2.20 — a heavier toolchain than FAISS or HNSWlib. The parent monorepo has ~38.9K GitHub stars; the README describes the code as "released for research purposes" rather than as a general-purpose maintained dependency.

## Security

Apache-2.0 licensed (inherited from the `google-research` monorepo). Pure computation library — no network access or credential handling, no telemetry. No security advisories found specific to the `scann` subdirectory; it inherits whatever scrutiny applies to the broader monorepo rather than having independent review.
