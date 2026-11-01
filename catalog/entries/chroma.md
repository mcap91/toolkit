---
name: chroma
title: Chroma
url: "https://github.com/chroma-core/chroma"
category: framework
summary: "AI-native open-source embedding database — 4-function core API, automatic tokenization/embedding/indexing, metadata filtering, in-memory or persistent modes, SIMD-accelerated maxscore, sharding, group-by aggregation, Python/JS/Go clients; Chroma Cloud for managed serverless; Apache-2.0"
tags: [vector-database, embeddings, rag, python, javascript, similarity-search, developer-experience]
reviewed: 2026-09-29
acquired: 2026-09-29
license: Apache-2.0
security_flags: []
overlaps: [qdrant, weaviate, milvus, pgvector, lancedb]
source: unknown
---

## What it does

Chroma is an open-source embedding database designed for simplicity in AI application development. Written in Rust, Python, TypeScript, and Go. Optimized for developer experience with a minimal API surface.

Core capabilities:

- **4-function API**: `create_collection`, `add`, `query`, `get` — automatic tokenization, embedding, and indexing
- **Automatic vectorization**: Handles embedding generation at insert time, or accepts pre-computed vectors
- **Metadata filtering**: Filter results by metadata fields and document content during search
- **Multiple modes**: In-memory for prototyping, persistent for production, client-server for distributed use
- **Sharding**: Per-shard retry logic, seal operator, merge/sort/truncate in frontend (v1.5.x)
- **SIMD maxscore**: Hardware-accelerated scoring for fast retrieval
- **Group-by**: Aggregate search results by metadata values (v1.5.9)
- **Advanced Search API**: Full-text search, quantization options

Client libraries: Python (`pip install chromadb`), JavaScript/TypeScript (`npm install chromadb`), Go.

## Mechanical details

Install via pip or npm. Version 1.5.9 stable (May 2026). Runs in-process (`chromadb.Client()`) or as server (`chroma run`). Chroma Cloud offers managed serverless with EU region support, S3/GitHub/Web sync, metadata arrays, private networking. $18M seed funding (2023). Weekly release cadence (Mondays). Integrates with LangChain, LlamaIndex, and major embedding providers.

## Security

Apache-2.0 licensed. Chroma Cloud provides private networking and access controls. Self-hosted mode runs entirely locally with no external calls unless embedding modules are configured. No telemetry concerns noted.