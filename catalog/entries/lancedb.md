---
name: lancedb
title: LanceDB
url: "https://github.com/lancedb/lancedb"
category: framework
summary: "Embedded serverless vector database built on Lance columnar format — runs in-process with no server, IVF/HNSW/PQ/RQ vector indexes + BM25 full-text, multimodal columns (text/image/video/audio), Git-style versioning, zero-copy reads, object storage backend (S3/GCS/AZ), DuckDB SQL integration, Python/TypeScript/Rust/REST SDKs; Apache-2.0"
tags: [vector-database, embedded, serverless, lance, multimodal, versioning, similarity-search, duckdb, arrow]
reviewed: 2026-09-29
acquired: 2026-09-29
license: Apache-2.0
security_flags: []
overlaps: [qdrant, weaviate, milvus, pgvector, chroma]
source: unknown
---

## What it does

LanceDB is an embedded, serverless vector database that runs directly inside the application process — no separate server to manage. Built on the Lance columnar format, an Apache Arrow-native storage format designed for ML and multimodal data.

Core capabilities:

- **Serverless/embedded**: Runs in-process in Python, TypeScript, or Rust — no server deployment
- **Multimodal storage**: Text, vectors, images, audio, video stored as columns in the same table
- **Vector indexes**: IVF, HNSW, PQ (product quantization), RQ (RabitQ quantization)
- **Full-text search**: BM25 keyword search alongside vector similarity
- **Hybrid search**: Combine vector and keyword retrieval with configurable re-rankers
- **Git-style versioning**: Every write creates a new version — checkout, restore, tag any past state
- **Object storage**: Same API works against local disk, S3, GCS, or Azure Blob
- **Schema evolution**: Add, rename, retype, or drop columns without full rewrite
- **DuckDB integration**: Lance extension for DuckDB exposes vector/FTS/hybrid retrieval as SQL table functions
- **Geospatial**: Arrow-native geospatial with R-Tree indexing

SDKs: Python, TypeScript/JavaScript, Rust, REST API. Integrates with LangChain, LlamaIndex, Apache Arrow, Pandas, Polars, DuckDB.

## Mechanical details

Install via `pip install lancedb` or `npm install @lancedb/lancedb`. Python SDK v0.34.0, JS SDK v0.38.0 as of mid-2026. Petabyte-scale claimed (100B+ rows per table). GPU support for index builds. KMeans ~30x speedup in recent releases. Page cache prewarm API for enterprise benchmarking. LanceDB Cloud available for managed deployment.

## Security

Apache-2.0 licensed. Embedded mode runs entirely in-process — no network surface. Object storage authentication delegated to cloud provider IAM. No telemetry mentioned. Data sovereignty via self-hosted or BYOC deployment.