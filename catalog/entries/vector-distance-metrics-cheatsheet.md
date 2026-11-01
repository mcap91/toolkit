---
name: vector-distance-metrics-cheatsheet
title: Vector Embeddings Distance Metrics Cheat Sheet
category: reference
summary: "Practitioner cheat sheet on choosing vector distance metrics for RAG: cosine similarity (unnormalized text), dot product (fastest for normalized unit vectors), L2 Euclidean (clustering); plus Matryoshka trick — truncate embedding dimensions from 1536→512 to cut vector RAM by 80% with minimal accuracy loss"
tags: [vector-search, embeddings, rag, cosine-similarity, distance-metrics, matryoshka, optimization]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [vector-database-basics-hnsw, faiss, rag-retrieval-recipe]
license: N/A
security_flags: []
source: unknown
---

## What it does

Concise engineering reference for choosing the right distance metric in vector databases, framed as a common source of silent retrieval failures in production RAG systems.

Three metrics compared:

1. **Cosine Similarity**: Measures the angle between vectors. Best for unnormalized text embeddings where magnitude varies. Most common default in vector DBs.
2. **Dot Product**: Measures angle plus magnitude. Fastest when vectors are pre-normalized to unit length (cosine and dot product become equivalent on unit vectors).
3. **L2 Euclidean Distance**: Measures geometric distance in embedding space. Best suited for clustering tasks where absolute position matters.

**Matryoshka Representation Learning trick**: Many modern embedding models (OpenAI text-embedding-3, nomic-embed) support Matryoshka embeddings — the first N dimensions of the full vector preserve most of the semantic information. Truncating from 1536 to 512 dimensions cuts vector storage RAM by ~80% with reported zero or near-zero accuracy loss on standard benchmarks. This is a property of how the model was trained, not a general compression technique.

Choosing the wrong metric (e.g., L2 on unnormalized embeddings with high magnitude variance) causes retrieval to silently return semantically wrong results without any error signal.

## Security

N/A — reference content, not software.