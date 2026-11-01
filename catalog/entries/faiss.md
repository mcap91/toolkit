---
name: faiss
title: FAISS
url: "https://github.com/facebookresearch/faiss"
category: framework
summary: "Meta's C++/Python library for efficient similarity search and clustering of dense vectors — billion-scale datasets, GPU acceleration (CUDA/ROCm), multiple index types (HNSW, NSG, IVF, PQ), L2/dot-product/cosine similarity; 40K+ stars, MIT"
tags: [similarity-search, vector-search, clustering, gpu, embeddings, nearest-neighbor]
reviewed: 2026-10-13
acquired: 2026-07-01
license: MIT
security_flags: []
overlaps: [chromadb, hnswlib, scann]
source: unknown
---

## What it does

FAISS (Facebook AI Similarity Search) is a library for efficient similarity search and clustering of dense vectors, searching sets of vectors of any size including those that do not fit in RAM. Written in C++ with complete Python/NumPy wrappers. Developed at Meta's Fundamental AI Research group. ~40K GitHub stars.

Supports three distance metrics: L2 (Euclidean), dot product, and cosine similarity. Index types range from exact brute-force search to approximate methods trading accuracy for speed and memory. Reported to index 1.5 trillion 144-dimensional vectors for internal Meta applications. Used as a core component in vector databases like OpenSearch, Milvus, and Vearch.

## Differentiators

- **Scale**: Handles billion-scale vector sets on a single server via compressed representations (binary vectors, compact quantization codes)
- **GPU acceleration**: Drop-in GPU index replacements (e.g., `GpuIndexFlatL2`) for NVIDIA CUDA and AMD ROCm, with automatic CPU/GPU memory management; optional cuVS backend for NVIDIA GPU implementations; experimental Metal backend for Apple GPUs (`MetalIndexIVFPQ`, added v1.15.0)
- **Index variety**: Multiple index structures — flat (exact), IVF (inverted file), PQ (product quantization), HNSW, NSG, RaBitQ — each with different search-time/quality/memory tradeoffs
- **Mature**: Published research backing (IEEE TBD 2019, arXiv 2024), extensive wiki documentation, active community via GitHub Discussions, latest release v1.15.1 (Sept 2026)

## Mechanical details

Install via conda (`faiss-cpu`, `faiss-gpu`, `faiss-gpu-cuvs`) or build from source with cmake. Only dependency is a BLAS implementation. GPU support requires CUDA or ROCm. Python interface wraps the C++ core.

Core API: create an index, `add()` vectors, `search()` for k-nearest neighbors. Training step required for quantization-based indexes. Supports single and multi-GPU configurations.

## Security

MIT licensed. Maintained by Meta with 7 named core contributors, ~4.4K forks. No credential handling or network access — pure computation library. Dependencies minimal (BLAS + optional CUDA).