---
name: milvus
title: Milvus
url: "https://github.com/milvus-io/milvus"
category: framework
summary: "Go/C++ cloud-native vector database — fully distributed K8s-native architecture, HNSW/IVF/DiskANN/CAGRA GPU indexes, dense + sparse + BM25 full-text + hybrid search, lake-native data access (v3.0) with Apache Iceberg/Parquet/Lance, multi-tenancy with hot/cold storage, Milvus Lite for embedded use; LF AI and Data Foundation; Apache-2.0"
tags: [vector-database, distributed, kubernetes, hybrid-search, gpu, embeddings, rag, data-lake, go, cpp]
reviewed: 2026-09-29
acquired: 2026-09-29
license: Apache-2.0
security_flags: []
overlaps: [qdrant, weaviate, pgvector, chroma, lancedb]
source: unknown
---

## What it does

Milvus is a high-performance, cloud-native vector database designed for billion-scale similarity search. Written in Go and C++ with hardware acceleration. Under the Linux Foundation AI and Data, with Zilliz as primary contributor.

Core capabilities:

- **Distributed architecture**: Separates compute and storage, horizontally scalable on Kubernetes with independent query and data nodes
- **Index types**: HNSW, IVF, FLAT, SCANN, DiskANN, GPU-accelerated CAGRA (NVIDIA cuVS)
- **Hybrid search**: Dense vectors + sparse vectors (SPLADE, BGE-M3) + native BM25 full-text search, fused via configurable reranking
- **Lake-native access (v3.0)**: Index vectors directly in S3/GCS/ADLS using Apache Iceberg, Parquet, Lance, or Vortex — no ETL required
- **External collections**: Define searchable indexes over data in object storage
- **Snapshots**: Point-in-time read-only views for evaluation and validation
- **Multi-tenancy**: Isolation at database, collection, partition, or partition-key level
- **Hot/cold storage**: Frequently accessed data in memory/SSD, cold data on cheaper storage
- **Milvus Lite**: Embedded variant via `pip install pymilvus`, stores to local file

Client libraries: Python, Java, Go, Node.js, C#, RESTful API. 44k+ GitHub stars.

## Mechanical details

Deploy via Docker, Kubernetes (Helm), or Milvus Lite (pip). Version 3.0 GA as of July 2026. Spark integration for batch processing. Attu GUI for administration, Birdwatcher for debugging, Prometheus/Grafana for monitoring. Milvus CDC for data synchronization. Zilliz Cloud offers managed service with Serverless, Dedicated, and BYOC options.

## Security

Apache-2.0 licensed, LF AI and Data Foundation governance. Mandatory user authentication, TLS encryption, RBAC with fine-grained permissions. SOC 2 compliance available on Zilliz Cloud. Published SIGMOD/VLDB papers on architecture.

## Usage notes

- Zilliz Cloud (the managed Milvus offering) bills on compute units plus storage, with a free tier then dedicated-capacity pricing; compute-unit sizing requires tuning (source: https://mixpeek.com/guides/vector-database-cost-comparison)
