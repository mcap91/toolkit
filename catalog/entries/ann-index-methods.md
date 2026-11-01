---
name: ann-index-methods
title: Approximate Nearest Neighbor (ANN) Index Methods Cheat Sheet
category: reference
summary: "Practitioner cheat sheet comparing 5 ANN vector-index methods by mechanism, complexity, and scale: Flat (exact brute-force, O(N) scan, <100K vectors or ground truth), IVF (k-means partitioning, O(nlist+nprobe*cluster_size), 100K-10M), HNSW (multi-layer proximity graph, O(log N) search, best recall/latency when the graph fits in RAM), IVF-PQ (IVF + Product Quantization residual compression, ~m bytes/vector, 100M-billion scale), and ScaNN (Google's anisotropic vector quantization + rerank, ~2x the QPS of the next-fastest of 11 tuned libraries at matched accuracy on ann-benchmarks.com); includes FAISS's own memory formulas and scale-bracket recommendations"
tags: [ann-search, vector-search, hnsw, ivf, ivf-pq, product-quantization, scann, faiss]
reviewed: 2026-10-13
acquired: 2026-10-13
overlaps: [vector-distance-metrics-cheatsheet, vector-database-basics-hnsw, faiss]
license: N/A
security_flags: []
source: unknown
---

## What it does

Decision reference for picking a vector-search index at a given data scale. Five methods compared, roughly in order of increasing scale/decreasing exactness:

1. **Flat (brute-force exact search)**: Compares the query to every stored vector — no index structure, no training. Guarantees exact top-k (100% recall) at O(N·d) query cost and no memory overhead beyond the raw vectors (d·4 bytes/vector, float32). Best under ~10K-100K vectors, for low query volume, or as the ground truth used to measure recall when tuning the other four methods.

2. **IVF (Inverted File Index)**: K-means partitions the dataset into `nlist` cells (Voronoi regions); each vector is filed under its nearest centroid. A query probes only the `nprobe` nearest cells instead of the whole set, cutting query cost to roughly O(nlist + nprobe·cluster_size) instead of O(N). Requires a training pass before vectors can be added — FAISS recommends a training sample of 30-256x `nlist` — and periodic re-training as data drifts. Sizing rule of thumb: `nlist` ≈ 4·sqrt(N) (FAISS's own guidance widens this to 4·sqrt(N)-16·sqrt(N) under 1M vectors); `nprobe` set to roughly 1-10% of `nlist`, trading recall (typically ~0.85-0.95) for speed. Good fit for 100K-10M vectors when some tuning effort is acceptable.

3. **HNSW (Hierarchical Navigable Small World)**: Builds a multi-layer proximity graph — sparse, long-range links in upper layers acting as skip-list-style highways, dense short-range links at the bottom — and greedily descends layer by layer toward the query. No training step; average search and insert cost is O(log N), full-index construction is O(N log N). Memory runs ≈ (d·4 + M·2·4) bytes/vector (FAISS's formula), where `M` (links per node, typically 4-64) is the main recall/memory dial, alongside `efConstruction` (build-time, ~100-500) and `efSearch` (query-time, ~64-512) candidate-list sizes. Typically the best recall (0.95-0.99+) at a given latency when the whole graph fits in RAM, but construction is slow at 100M+ vectors and deletion is awkward (no native remove in FAISS's base implementation).

4. **IVF-PQ (IVF + Product Quantization)**: Layers Product Quantization on top of IVF — each vector's residual from its cell centroid is split into `m` sub-vectors, and each sub-vector is encoded as a 1-byte codeword from its own trained codebook, shrinking storage from d·4 bytes to roughly `m` bytes per vector. Worked example: a 128-dim float32 vector (512 bytes) encoded as 8 sub-vectors of 1 byte each becomes 8 bytes — a 64x reduction. Query-time distances are estimated from precomputed lookup tables (asymmetric distance computation) rather than by decompressing vectors. The compression is lossy — recall typically lands around 0.90-0.97, below IVF-Flat or HNSW at equal `nprobe` — and is only partially recoverable by reranking top candidates against raw vectors or loosening the compression ratio (fewer, larger sub-vectors). Two independent tuning dials: `nprobe` buys recall with scan time (as in plain IVF), `m` buys recall with memory. This is the index that makes billion-scale search fit in RAM: 1B vectors at 768 dimensions in float32 is ~3TB uncompressed, infeasible on one machine without this kind of compression.

5. **ScaNN (Scalable Nearest Neighbors, Google)**: Google Research's library (ICML 2020, "Accelerating Large-Scale Inference with Anisotropic Vector Quantization"), built around a 3-stage pipeline — partition (IVF-like clustering), anisotropic vector quantization, and rerank. Core idea: standard quantization minimizes average reconstruction error, but for maximum inner-product search (MIPS) and cosine similarity, a quantization error *parallel* to a vector's direction distorts its inner product with queries more than an *orthogonal* error of the same magnitude — so ScaNN's loss function penalizes parallel error more heavily (tunable via a threshold t∈[0,1)), then reranks top candidates with exact distances. Google's own benchmark on glove-100-angular (ann-benchmarks.com) reports ScaNN handling roughly twice the queries-per-second of the next-fastest of 11 other carefully tuned vector-search libraries at matched accuracy. Open source (`pip install scann`, TensorFlow/NumPy interfaces); powers Google Cloud's Vertex AI Vector Search. Best fit when the workload is MIPS/cosine-shaped and the goal is maximum QPS at a fixed accuracy/memory budget.

### Comparison table

| Method | Mechanism | Query cost | Memory/vector | Typical recall | Training/build | Best scale |
|---|---|---|---|---|---|---|
| Flat | Linear scan vs. every vector | O(N·d) | d·4 B (uncompressed) | 100% (exact) | None | <10K-100K, or ground truth |
| IVF | k-means into `nlist` cells; probe `nprobe` nearest | O(nlist + nprobe·cluster_size) | ≈ d·4 B + small list overhead | ~0.85-0.95 | k-means (needs 30-256x `nlist` training vectors) | 100K-10M |
| HNSW | Multi-layer proximity graph, greedy descent | O(log N) search; O(N log N) build | d·4 + M·2·4 B | ~0.95-0.99+ | None (incremental insert, O(log N) each) | Up to ~10M-100M, RAM-permitting |
| IVF-PQ | IVF + per-sub-vector quantization of residuals | Same shape as IVF; cheap table-lookup (ADC) distances | ≈ `m` B (e.g., 64x smaller than Flat at d=128, m=8) | ~0.90-0.97 | k-means (coarse) + PQ codebook training | 100M-billion+, memory-bound |
| ScaNN | Partition + anisotropic quantization + exact rerank | Same shape as IVF-PQ, plus a rerank pass | Comparable to IVF-PQ's class; tunable | Matched-accuracy comparisons show ~2x QPS vs. the next-best of 11 libraries (Google, glove-100-angular) | Partition + anisotropic codebook training | Million-billion, MIPS/cosine workloads |

### Scale thresholds (FAISS's own guidance)

- **<10K-100K vectors**, or few queries: Flat — direct computation is already fast enough and exact.
- **100K-1M**: `IVF{nlist}` with `nlist` ≈ 4·sqrt(N) to 16·sqrt(N).
- **1M-10M**: FAISS recommends an HNSW coarse quantizer inside IVF (`IVF65536_HNSW32`).
- **10M-100M**: `IVF262144_HNSW32`.
- **100M-1B**: `IVF1048576_HNSW32`, generally paired with PQ/OPQ compression (i.e., IVF-PQ) once vectors no longer fit RAM uncompressed.
- **MIPS/cosine workloads at any of the above scales** where maximum QPS-per-accuracy-per-dollar matters: ScaNN, or its managed form (Vertex AI Vector Search).

## Sources

- [Guidelines to choose an index — FAISS wiki (facebookresearch/faiss)](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index) — memory formulas, scale brackets, nlist/training-sample guidance (fetched directly).
- [Announcing ScaNN: Efficient Vector Similarity Search — Google Research blog](https://research.google/blog/announcing-scann-efficient-vector-similarity-search/) — anisotropic quantization rationale, glove-100-angular QPS claim (fetched directly).
- [What is ScaNN (Scalable Nearest Neighbors)? — Zilliz Learn](https://zilliz.com/learn/what-is-scann-scalable-nearest-neighbors-google) — ScaNN's 3-stage partition/quantize/rerank pipeline.
- [HNSW vs IVF-PQ vs LSH: Approximate Nearest Neighbor Algorithms Compared](https://www.abhik.ai/concepts/embeddings/ann-comparison) — recall/latency/memory/build/update summary table (fetched directly).
- [IVF-PQ: Inverted File with Product Quantization](https://www.abhik.ai/concepts/embeddings/ivf-pq) — residual quantization and asymmetric distance computation mechanics.

## Security

N/A — reference content, not software. Methods are implemented by open-source libraries (e.g., FAISS, MIT; ScaNN, Apache-2.0 — confirmed via PyPI/GitHub license headers) that practitioners install separately; this entry does not itself ship code.
