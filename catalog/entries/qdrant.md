---
name: qdrant
title: Qdrant
url: "https://github.com/qdrant/qdrant"
category: framework
summary: "Rust-based vector similarity search engine and database — HNSW with inline payload filtering, dense/sparse/multi-vector search, hybrid search with RRF/DBSF fusion, TurboQuant 4-bit/8-bit compression, GPU-accelerated indexing, distributed sharding and replication, gRPC and REST APIs, Edge variant for in-process use; Apache-2.0"
tags: [vector-database, similarity-search, rust, hnsw, embeddings, rag, hybrid-search, quantization, gpu]
reviewed: 2026-09-29
acquired: 2026-09-29
license: Apache-2.0
security_flags: []
overlaps: [weaviate, milvus, pgvector, chroma, lancedb]
source: unknown
---

## What it does

Qdrant is a vector similarity search engine and database for storing, searching, and managing vectors with JSON payload metadata. Written in Rust with SIMD optimizations and a custom storage engine (Gridstore).

Core capabilities:

- **Dense, sparse, and multi-vector search**: Supports named vectors per point, enabling ColBERT-style late interaction and multi-modal workflows
- **Inline payload filtering**: Metadata filters applied during HNSW graph traversal (not pre/post-processing), maintaining recall under selective filters
- **Hybrid search**: Combines multiple vector types in a single query with configurable fusion (RRF, DBSF)
- **Quantization**: Scalar, product, and TurboQuant (4-bit/8-bit) compression — up to 32x memory reduction with under 1% recall loss
- **Distributed mode**: Sharding and replication across nodes with zero-downtime resharding
- **GPU indexing**: NVIDIA and AMD GPU support for accelerated index builds
- **Qdrant Edge**: Lightweight in-process variant for edge devices with server sync

Client libraries: Python, Rust, Go, JavaScript/TypeScript, .NET/C#, Java. Community: Kotlin, PHP.

## Mechanical details

Install via Docker (`qdrant/qdrant`), binary download, or Rust crate. REST API on port 6333, gRPC on 6334. Built-in Web UI for collection management and data exploration. Version 1.17 as of March 2026, ~34k GitHub stars. Qdrant Cloud available as managed service with SOC 2 and HIPAA compliance. Agent skills package available for AI coding assistants.

## Security

Apache-2.0 licensed. API key authentication, TLS encryption. Qdrant Cloud offers SOC 2 Type II and HIPAA compliance. Built-in audit logging (cloud). No telemetry in self-hosted by default. Standard Docker deployment trust model.

## Usage notes

- Qdrant Cloud bills on provisioned cluster size (RAM/CPU/disk) rather than usage, with a free 1GB cluster tier — capacity is provisioned up front, not metered per query (source: https://mixpeek.com/guides/vector-database-cost-comparison)
