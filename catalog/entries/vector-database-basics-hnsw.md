---
name: vector-database-basics-hnsw
title: "Vector Database Basics: HNSW (Tiger Data / Timescale)"
url: "https://www.tigerdata.com/blog/vector-database-basics-hnsw"
category: reference
summary: "Tiger Data (Timescale) blog explainer on HNSW (Hierarchical Navigable Small World) vector indexing: describes HNSW's skip-list-inspired multi-layer graph (sparse long-edge upper layers for coarse navigation, dense lower layers for fine-grained search), and its use with pgvector/Timescale Vector on Postgres via the m (max connections per layer) and ef_construction (build-time candidate list size) parameters that trade index size/build time for search accuracy."
tags: [hnsw, vector-database, pgvector, timescale, ann-search, postgres, indexing]
reviewed: 2026-08-25
acquired: 2026-08-25
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---

## What it says

A Tiger Data (the company behind TimescaleDB) blog post explaining HNSW (Hierarchical Navigable Small World), an approximate-nearest-neighbor (ANN) graph index used for vector similarity search, framed as an entry in a "Vector Database Basics" series. Stated goal: explain why HNSW indexes are useful and how to use them with pgvector.

**Sourcing caveat**: automated content extraction of the live page returned only site navigation text ("Product / Tiger Cloud / TimescaleDB Enterprise / Open source / TimescaleDB / Search") rather than the article body — the raw HTML document is 400K+ characters, consistent with content that the static extractor could not resolve. A Medium mirror of the same article (`medium.com/timescale/vector-database-basics-hnsw-ae751f461b04`) returned HTTP 403 on fetch. The description below is reconstructed from search-engine-indexed excerpts of the article plus Tiger Data's companion pgvector/HNSW documentation on the same domain, corroborated against independent HNSW literature — treat it as lower-confidence than a direct full-text fetch.

## Mechanical details reported

- **Skip-list-inspired structure**: HNSW builds multiple graph layers; upper layers have fewer nodes connected by "long" edges spanning large distances in the vector space, acting as highways for coarse navigation toward the target; lower layers are denser for fine-grained search. As a query descends from the top layer to the bottom, edge length shrinks and the search area localizes around the nearest neighbors.
- **Build-time parameters**, per Tiger Data's pgvector/Timescale Vector SQL interface docs:
  - `m` — max number of connections (edges) per node per layer; a higher `m` increases recall/accuracy but increases index build time and size.
  - `ef_construction` — size of the dynamic candidate list used while building the graph; higher values improve index quality/search accuracy at the cost of longer build time.
  - Example DDL cited in Tiger Data's docs: `CREATE INDEX document_embedding_idx ON document_embedding USING hnsw(embedding vector_cosine_ops) WITH (m = 20);`
- Companion Tiger Data pages on the same topic: `hnsw-vs-diskann` (index tradeoffs) and `postgresql-extensions-pgvector` (pgvector guide).

## Notes

- Publisher: Tiger Data (formerly Timescale) — vendor of TimescaleDB and pgvector-adjacent Postgres products; this is vendor-published educational content.
- A near-identical version was also published on Timescale's Medium publication, dated August 13, 2024 per search results.

## Security

- Article/documentation content — no executable code ships in the post itself. The referenced technology (pgvector) is a separately-licensed open-source Postgres extension. License of the article text: N/A (recorded as NOASSERTION).