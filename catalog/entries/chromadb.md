---
name: chromadb
title: ChromaDB
url: "https://www.trychroma.com/products/chromadb"
category: framework
summary: "Open-source AI search infrastructure with vector, full-text, regex, and hybrid search — embedding-agnostic with Python/JS SDKs, serverless cloud option, and multi-modal retrieval; strong fit for literature/sequence RAG pipelines"
tags: [vector-database, embeddings, search, RAG, AI-infrastructure, multi-modal]
reviewed: 2026-06-18
acquired: 2026-06-18
license: Apache-2.0
security_flags: []
overlaps: [claude-mem]
source: unknown
---

## What it does

ChromaDB is open-source search infrastructure for AI applications. It unifies dense vector search, sparse vector search (BM25, SPLADE), full-text search (trigram/regex), and metadata filtering in a single query interface with hybrid search combining multiple methods. Supports multi-modal retrieval across text, images, and audio.

Core API is 4 functions — create collection, add documents, query, get. Embedding-model agnostic: works with OpenAI, Cohere, HuggingFace, sentence-transformers, or bring your own. Handles tokenization, embedding, and indexing automatically or accepts pre-computed embeddings.

Deployment options: single-node via `pip install chromadb` / `npm install chromadb` / Docker (in-memory or persistent storage), Chroma Cloud (managed serverless with auto-scaling), or bring-your-own-cloud with VPC, multi-region replication, and point-in-time recovery.

Performance at 100k vectors (384 dim): p50 warm 20ms, p99 warm 57ms. Write throughput 30 MB/s (2000+ QPS). Up to 1M collections, 5M records per collection, 90-100% recall. Object-storage-optimized indexes with query-aware data tiering and caching.

Additional features: dataset versioning/forking for A/B testing, CLI tools, example projects for agentic search and AST-aware code search.

Docs: https://docs.trychroma.com/docs/overview/introduction

## Assessment

Strong fit for bioinformatics RAG pipelines — embedding literature abstracts, gene ontology terms, protein descriptions, or sequence similarity results into a searchable vector store. The hybrid search (combining semantic + keyword + metadata filtering) is particularly useful for scientific text where exact terms (gene names, accession numbers) matter alongside semantic similarity.

The 4-function API keeps integration simple. Python and JS SDKs mean it works in both analysis scripts and web-facing tools. Local mode (`pip install chromadb`) lets you prototype without infrastructure, then scale to cloud.

The existing catalog entry "Claude Mem" uses Chroma as a component but wraps it in unnecessary complexity. ChromaDB standalone is the cleaner building block.

## Mechanical details

- **Install**: `pip install chromadb` (Python) or `npm install chromadb` (JS/TS)
- **Local persistent**: `chroma run --path /chroma_db_path` for client-server mode
- **Docker**: official image available
- **Cloud**: Chroma Cloud with $5 free credits, serverless pricing based on object storage ($0.02/GB/mo vs $5/GB/mo for memory)
- **SDKs**: Python, JavaScript/TypeScript
- **Min API surface**: `Client()`, `create_collection()`, `collection.add()`, `collection.query()`

## Security

- **License**: Apache-2.0, no commercial restrictions
- **Maintenance**: Weekly release cadence (Mondays), hotfixes any day; active development
- **Community**: Large GitHub community, Discord, contributing guide, good-first-issue tags
- **Supply chain**: Major open-source project trusted by production teams; same codebase powers open-source and cloud offerings
- **No dangerous patterns observed** in the public API surface