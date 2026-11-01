---
name: weaviate
title: Weaviate
url: "https://github.com/weaviate/weaviate"
category: framework
summary: "Go-based AI-native vector database — stores objects with vectors, integrated vectorization via OpenAI/Cohere/HuggingFace modules, semantic + BM25 keyword + hybrid search, built-in RAG and reranking, ACORN filtered search, multi-tenancy with RBAC, object TTL, gRPC/REST/GraphQL APIs; BSD-3-Clause"
tags: [vector-database, semantic-search, hybrid-search, rag, go, embeddings, multi-tenancy, reranking]
reviewed: 2026-09-29
acquired: 2026-09-29
license: BSD-3-Clause
security_flags: []
overlaps: [qdrant, milvus, pgvector, chroma, lancedb]
source: unknown
---

## What it does

Weaviate is an open-source, cloud-native vector database that stores data objects alongside their vector embeddings. Written in Go. Supports automatic vectorization at import time through integrated model modules, or direct import of pre-computed embeddings.

Core capabilities:

- **Semantic search**: Vector similarity search across text, images, and audio
- **Hybrid search**: Combines vector similarity with BM25 keyword search, adjustable alpha parameter for balance
- **Built-in RAG and reranking**: Generative search and reranking as query-time operations, no external tooling needed
- **Integrated vectorization**: Modules for OpenAI, Cohere, HuggingFace, Google, and lightweight Model2Vec; model swapping supported
- **ACORN filtered search**: Fast filtered vector search algorithm
- **Multi-tenancy**: Native tenant isolation with RBAC authorization
- **Object TTL**: Configurable time-to-live per collection for automatic data expiry
- **Weaviate Agents**: Autonomous data workflow capabilities (2026)

Client libraries: Python, JavaScript/TypeScript, Java, Go, C#/.NET. APIs: REST, gRPC, GraphQL.

## Mechanical details

Install via Docker, Kubernetes, or Weaviate Cloud (managed). Version 1.39 stable as of August 2026, v1.40 RC available with MUVERA indexing and RQ-4 quantization. Agent Skills package for AI coding assistants. Weaviate Embeddings provides managed embedding inference inside Weaviate Cloud. Modular architecture — vectorizer, reranker, and generative modules are pluggable.

## Security

BSD-3-Clause licensed. RBAC authorization with fine-grained permissions. TLS encryption. Multi-tenancy isolation. Weaviate Cloud offers enterprise-grade security. No telemetry concerns noted in open-source deployment.

## Usage notes

- Weaviate Cloud bills on stored dimensions plus an SLA tier, with a free sandbox then usage-based pricing; dimension-based billing rewards smaller embedding sizes (source: https://mixpeek.com/guides/vector-database-cost-comparison)
