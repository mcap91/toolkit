---
name: amazon-s3-vectors
title: Amazon S3 Vectors
url: https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-s3-vectors-preview-native-support-storing-querying-vectors/
category: framework
summary: AWS cloud object storage with native vector support — 'vector buckets' hold vector indexes (up to 10,000 per bucket, up to 2 billion vectors per index at GA) queryable via dedicated APIs with no infrastructure to provision, up to 90% lower cost than purpose-built vector databases per AWS; metadata key-value filtering per vector; SSE-S3 or SSE-KMS encryption with per-index customer-managed keys; natively integrated with Amazon Bedrock Knowledge Bases and Amazon OpenSearch Service; announced in preview July 2025, reached general availability December 2, 2025 with a 40x per-index scale increase over preview.
tags:
  - vector-database
  - aws
  - object-storage
  - s3
  - rag
  - bedrock
  - managed-service
  - cloud
reviewed: 2026-10-28
acquired: 2026-10-28
license: Proprietary (AWS managed service)
security_flags:
  - closed-source
  - no-self-hosting
overlaps:
  - qdrant
  - weaviate
  - milvus
  - lancedb
  - chroma
  - pgvector
  - turbopuffer
source: text
---

## What it does

A new S3 bucket type ("vector bucket") with dedicated APIs for storing, filtering, and similarity-querying vector data at object-storage cost, without provisioning servers or clusters. Announced in preview at AWS Summit New York, July 2025, as "the first cloud object store with native support to store large vector datasets," reducing the cost of uploading, storing, and querying vectors by up to 90% versus purpose-built vector databases, per AWS.

**Capacity:** at preview, up to 10,000 vector indexes per bucket, tens of millions of vectors per index. At general availability (December 2, 2025), per-index capacity jumped 40x to up to 2 billion vectors per index, with the 10,000-index-per-bucket limit retained. Query performance at GA: frequent queries return in ~100ms; infrequent queries complete in under a second.

**Metadata:** key-value pairs can be attached to each vector for filtering (e.g., by date, category, user preference).

**Security:** encrypts all vector data by default with SSE-S3 (S3-managed keys), with an SSE-KMS option for a bucket-default customer-managed key or a dedicated customer-managed key per vector index; supports tagging for attribute-based access control (ABAC) and cost tracking.

**Integrations:** native integration with Amazon Bedrock Knowledge Bases (for RAG) and Amazon OpenSearch Service (to tier infrequently-queried vectors to cheap storage, then move them to OpenSearch as query demand increases).

**Adoption:** in the roughly four months between preview and the November 28, 2025 measurement, AWS reports customers created over 250,000 vector indexes, ingested more than 40 billion vectors, and ran over 1 billion queries.

## Sources

- [Announcing Amazon S3 Vectors (Preview) — AWS](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-s3-vectors-preview-native-support-storing-querying-vectors/)
- [Amazon S3 Vectors Now Generally Available with Increased Scale and Performance — BigDATAwire](https://www.hpcwire.com/bigdatawire/this-just-in/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance/) — GA capacity/performance figures.

## Security

Proprietary AWS managed service, no self-hosting. Default encryption at rest (SSE-S3) with optional per-index customer-managed KMS keys; ABAC via tagging. Security posture otherwise inherits standard AWS IAM/account-boundary considerations; no independent code audit possible (closed-source service).
