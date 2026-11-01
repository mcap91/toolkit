---
name: pgvector
title: pgvector
url: "https://github.com/pgvector/pgvector"
category: framework
summary: "PostgreSQL extension for vector similarity search — HNSW and IVFFlat indexes, exact and approximate nearest neighbor, vector/halfvec/bit/sparsevec types, 6 distance functions (L2/IP/cosine/L1/Hamming/Jaccard), iterative index scans, binary quantization, multitenancy via partitioning, hybrid search with pg full-text; all Postgres guarantees (ACID, JOINs, WAL replication); PostgreSQL License"
tags: [vector-database, postgresql, extension, hnsw, ivfflat, embeddings, sql, similarity-search]
reviewed: 2026-09-29
acquired: 2026-09-29
license: PostgreSQL
security_flags: []
overlaps: [qdrant, weaviate, milvus, chroma, lancedb]
source: unknown
---

## What it does

pgvector adds vector similarity search to PostgreSQL as a native extension. Vectors live alongside relational data in the same database, with full access to ACID transactions, JOINs, WAL replication, and point-in-time recovery.

Core capabilities:

- **Vector types**: `vector` (float32, up to 16k dims), `halfvec` (float16, up to 16k dims), `bit` (binary, up to 64k dims), `sparsevec` (sparse, up to 16k non-zero elements)
- **Index types**: HNSW (better speed-recall tradeoff, no training) and IVFFlat (faster builds, less memory)
- **Distance functions**: L2, inner product, cosine, L1, Hamming, Jaccard
- **Iterative index scans** (v0.8): Automatically scans more of the index when metadata filters reduce results, with strict or relaxed ordering
- **Binary quantization**: Expression indexing for compressed binary indexes with re-ranking
- **Hybrid search**: Combine with PostgreSQL full-text search using RRF or cross-encoder fusion
- **Multitenancy**: List partitioning or separate tables for tenant isolation
- **Subvector indexing**: Index and search on vector subsets with re-ranking

Works with any language that has a PostgreSQL client. Dedicated client libraries for 30+ languages.

## Mechanical details

Install from source (C, `make && make install`), Docker, Homebrew, PGXN, apt, yum, conda-forge. Requires Postgres 13+. Version 0.8.6 current. Available on all major managed Postgres providers (AWS RDS/Aurora, GCP Cloud SQL, Azure, Supabase, Neon, Heroku). Parallel index builds supported. Each vector takes `4 * dimensions + 8` bytes (float32).

## Security

PostgreSQL License (liberal open-source). Inherits all PostgreSQL security — authentication, TLS, row-level security, audit logging. No additional attack surface beyond the extension's C code. No telemetry. Widely deployed on managed platforms with SOC 2/HIPAA compliance inherited from the provider.

## Usage notes

- Self-hosted pgvector trades vendor fees for infrastructure cost and ops time; a realistic self-hosted floor is cited at ~$50+/month in instance cost alone, with operational time as "the real bill" (source: https://mixpeek.com/guides/vector-database-cost-comparison)
