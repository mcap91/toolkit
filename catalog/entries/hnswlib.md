---
name: hnswlib
title: HNSWlib
url: "https://github.com/nmslib/hnswlib"
category: framework
summary: "Header-only C++ library (with Python bindings) implementing HNSW (Hierarchical Navigable Small World) graph search — the standalone reference implementation of the HNSW algorithm by Yury Malkov and Dmitry Yashunin; incremental index construction, element deletion/update, custom C++ distances, L2/inner-product/cosine spaces; Apache-2.0"
tags: [similarity-search, nearest-neighbor, hnsw, embeddings, cpp, ann-search, header-only]
reviewed: 2026-10-13
acquired: 2026-10-13
license: Apache-2.0
security_flags: []
overlaps: [faiss, scann]
source: unknown
---

## What it does

HNSWlib is a header-only C++ library implementing Hierarchical Navigable Small World (HNSW) graphs for approximate nearest neighbor search, with full Python bindings. Written by Yury Malkov — co-inventor of the HNSW algorithm (with Dmitry Yashunin) — and maintained under the nmslib GitHub organization as the standalone extraction of NMSLIB's fastest method. ~5,350 GitHub stars.

Unlike multi-index libraries (FAISS, Milvus), HNSWlib implements a single algorithm: the HNSW graph. There is no flat, IVF, or PQ index — HNSW is the only option.

Core capabilities:

- **Distances/spaces**: L2 (squared Euclidean), inner product (`ip`), and cosine, selected at index creation (`hnswlib.Index(space, dim)`); custom user-defined distances supported in C++
- **Incremental construction**: elements can be added after index creation (`add_items`), and the index capacity can be resized; most ANN graph structures are build-once
- **Element deletion/update**: `mark_deleted`/`unmark_deleted` flag elements out of search results without freeing memory; `allow_replace_deleted` lets new inserts reuse that freed capacity; re-adding an existing label updates it in place (slower than a fresh insert, but more memory/query-efficient)
- **Filtering**: boolean filter callback in `knn_query`, though the Python filter path is GIL-limited — the README recommends `num_threads=1` when filtering
- **Multi-vector document search and epsilon search** (v0.8+, C++ only so far)
- **Picklable Python index**: full serialization round-trip via `pickle` or `save_index`/`load_index` to a binary file
- **No-exceptions C++ API** (`v0.10.0` release candidate, Sept 2026): `*NoExceptions` method variants return `Status`/`StatusOr` instead of throwing, for builds compiled with `-fno-exceptions`

Third-party bindings (not in the core repo) exist for Java, R, Rust, Go, .NET, and a CUDA port.

## Mechanical details

Install via `pip install hnswlib`, or from source (`git clone` + `pip install .`) for the C++ header. No dependencies beyond a C++11 compiler for the core header. Build/query trade-off parameters: `M` (max graph connections per node per layer) and `ef_construction` (build-time accuracy/speed) set at `init_index`; `ef` (query-time accuracy/speed) set via `set_ef()`. Thread-safety: concurrent `add_items` calls are safe with each other, and concurrent `knn_query` calls are safe with each other, but the two are not safe concurrently with each other.

The PyPI package (`hnswlib` 0.8.0, uploaded December 2023) trails the GitHub repo, whose latest tagged stable release is `v0.9.0` (March 2026) — installing from source gets newer fixes than `pip install hnswlib`. Repo pushed as recently as September 2026 (855 forks), so development is active even though PyPI releases lag.

## Security

Apache-2.0 licensed. Pure C++/Python computation library — no network access or credential handling. Reads/writes local binary index files via `save_index`/`load_index`; no documented validation of untrusted index files beyond the exception/`Status` handling added in the v0.10.0 release candidate, so loading an index from an untrusted source carries the same risk as deserializing any unvalidated binary blob. No telemetry.
