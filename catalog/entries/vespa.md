---
name: vespa
title: Vespa
url: https://github.com/vespa-engine/vespa
category: framework
summary: Open-source (Apache-2.0) big-data serving engine from Yahoo (open-sourced 2017, spun out as Vespa.ai in 2023) combining hybrid search (BM25 keyword + vector + tensor operations), real-time indexing, and machine-learned multi-phase ranking at billions-of-documents scale with sub-100ms latency; stateless container clusters handle query/indexing logic separately from stateful content clusters holding the data; available self-hosted or as Vespa Cloud; used in production by Spotify, Perplexity, Etsy, and others.
tags:
  - vector-database
  - hybrid-search
  - bm25
  - tensor
  - real-time-indexing
  - open-source
  - yahoo
  - self-hosted
reviewed: 2026-10-28
acquired: 2026-10-28
license: Apache-2.0
security_flags: []
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

A search and big-data serving engine, not a vector-only database: it combines structured, text, and vector search with real-time recommendation/personalization/targeting in one system. Handles hybrid search (BM25 keyword search fused with vector similarity), general tensor operations, and multi-phase machine-learned ranking across billions of documents, reported at up to 90,000 requests/second with tens-of-milliseconds latency.

**Origins:** traces to search technology at Overture and AltaVista, used inside Yahoo (via the 2003 Overture acquisition and 2003 AlltheWeb acquisition) for search, shopping, recommendations, and ad serving since the mid-2000s. Yahoo open-sourced it in 2017 under Apache-2.0. Vespa.ai spun out of Yahoo as an independent company in 2023, offering both the open-source engine and a managed Vespa Cloud.

**Architecture:** stateless container clusters handle query execution and indexing-transformation logic (middleware), passing operations to stateful content clusters that hold the actual data; a single container cluster can be configured, or separate clusters per task.

**Deployment:** fully self-hostable (entire product buildable from the public GitHub repo, no license-gated enterprise tier) or consumable as Vespa Cloud.

**Production users:** Yahoo, Perplexity, Spotify, Etsy, Taboola, AlphaSense, Otto, Kleinanzeigen.

## Sources

- [Vespa GitHub](https://github.com/vespa-engine/vespa) — Apache-2.0 license, full source.
- [Why Vespa — Vespa.ai](https://vespa.ai/why-vespa/)
- [Yahoo open-sources Vespa — SiliconANGLE (2017)](https://siliconangle.com/2017/09/26/yahoo-open-sources-vespa-important-software-release-since-hadoop/) — open-sourcing history.

## Security

Apache-2.0, fully open source — entire product buildable from the public repository, no enterprise-only gated build. Self-hosted deployments carry standard operational responsibility for a distributed serving system (cluster security, network exposure); no specific CVEs or dangerous-pattern findings surfaced during review.
