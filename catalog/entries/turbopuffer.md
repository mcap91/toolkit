---
name: turbopuffer
title: turbopuffer
url: https://turbopuffer.com/
category: framework
summary: Serverless vector and full-text search database built object-storage-first (S3/GCS/Azure Blob as source of truth, ~$0.02/GB) with an NVMe SSD and RAM caching hierarchy layered on top — cold namespaces cost near-zero, hot namespaces get sub-10ms p50 cached-query latency; write-ahead log on object storage for durability (~10K+ vectors/sec writes), strong consistency by default; no free tier, $64/month minimum; proprietary, no self-hosted version; production users include Cursor (95% cost reduction after migrating from Pinecone), Anthropic, Notion, Linear.
tags:
  - vector-database
  - object-storage
  - serverless
  - full-text-search
  - hybrid-search
  - closed-source
  - cost-optimization
reviewed: 2026-10-28
acquired: 2026-10-28
license: Proprietary
security_flags:
  - closed-source
  - no-self-hosting
  - no-free-tier
overlaps:
  - qdrant
  - weaviate
  - milvus
  - lancedb
  - chroma
  - pgvector
source: text
---

## What it does

A vector + full-text search database that inverts the usual vector-database storage hierarchy: object storage (S3/GCS/Azure Blob, ~$0.02/GB) is the source of truth rather than RAM or SSD, with an NVMe SSD cache (tens-of-ms queries) and RAM cache (<10ms queries) layered on top — nicknamed the "pufferfish" model. Data migrates up the cache tiers automatically the more a namespace is queried, so a dormant namespace (e.g., an unopened codebase or workspace) costs near-zero while sitting cold in object storage.

**Durability:** writes go through a write-ahead log on object storage, supporting roughly 10,000+ vectors/second; strong consistency by default, with an eventually-consistent option for lower latency.

**Scale:** reported handling 2.5T+ documents with sub-10ms p50 latency on cached queries, at roughly 10x lower cost than RAM/SSD-backed alternatives (turbopuffer's ~$0.02/GB versus Pinecone Serverless's ~$0.33/GB).

**Pricing:** usage-based with no free tier — Launch ($64/month minimum, all features included), Scale ($256/month, adds HIPAA BAA/SSO/priority support), Enterprise ($4,096+/month, single-tenant/BYOC/CMEK/99.95% SLA). Storage/query/write usage bills on top of the platform minimum.

**Fit:** poor match for always-hot, ultra-low-latency workloads needing single-digit-ms tail latency on every request regardless of access pattern — the cost advantage depends on having a meaningfully cold-data pattern.

**Production users:** Cursor (reported 95% cost reduction migrating code-search embeddings off Pinecone), Anthropic, Notion (migrated from Pinecone), Linear, Atlassian, Ramp, Grammarly, Superhuman.

## Sources

- [TurboPuffer: Object Storage-First Vector Database Architecture — Jason Liu](https://jxnl.co/writing/2025/09/11/turbopuffer-object-storage-first-vector-database-architecture/)
- [turbopuffer.com](https://turbopuffer.com/) — pricing, features.

## Security

Closed-source, proprietary, no self-hosted option — adoption means trusting turbopuffer's cloud infrastructure entirely for both data-plane operation and the write-ahead durability log. No independent code audit possible; no CVEs or dangerous-pattern findings surfaced (no public source to inspect).
