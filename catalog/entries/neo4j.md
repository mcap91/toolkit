---
name: neo4j
title: Neo4j
url: https://github.com/neo4j/neo4j
source_url: https://github.com/neo4j
source: web
category: framework
summary: "Native property-graph database storing data as labeled nodes and typed relationships with key-value properties, queried via Cypher (now standardized as ISO GQL); open-core licensing — Community Edition (GPLv3) covers ACID transactions, native graph storage/indexing, vector and full-text indexes, and APOC's 450+ procedures, while Enterprise Edition (commercial license) adds role-based auth, LDAP/Kerberos, Causal Clustering, tens-of-billions-scale graphs, rolling upgrades, and hot backup; also offered as AuraDB managed cloud and a newer Infinigraph Edition with unlimited horizontal sharding; Graph Data Science library ships as a separate open-core component (Community: all algorithms, 4-CPU cap, 3-model catalog limit; Enterprise: unlimited cores, cluster write support)."
tags:
  - graph-database
  - cypher
  - gql
  - property-graph
  - open-core
  - graph-data-science
  - aura
  - acid
reviewed: 2026-10-28
acquired: 2026-10-28
license: GPLv3 (Community Edition); commercial (Enterprise Edition, Graph Data Science Enterprise)
security_flags: []
overlaps:
  - knowledge-graph-construction-anthropic
  - three-store-hybrid-memory-architecture
---

## What it does

A native property-graph database: data is stored as nodes and relationships, each carrying labels/types and key-value properties, with index-free adjacency (relationships are traversed as direct pointers rather than via index lookups) as the core storage/query performance mechanism. Queried with Cypher, Neo4j's graph query language, which has since been standardized by ISO as GQL — external validation of the language design.

**Licensing is open-core, split at the edition boundary:**
- **Community Edition (GPLv3, free):** ACID transactions, native graph storage and indexing, Cypher, vector and full-text indexes, and APOC (450+ bundled procedures/functions). This is the bulk of Neo4j's own engineering investment.
- **Enterprise Edition (commercial license):** adds role-based authorization, segregation of duties, LDAP/Kerberos integration, property blacklisting, schema enforcement, Causal Clustering, support for tens-of-billions-scale ("XXL") graphs, rolling upgrades, and hot backup. Production-relevant essentials — clustering, online backup, RBAC, most constraint types — are Enterprise-only, and Community Edition is limited to a single writer per database.
- **AuraDB (managed cloud):** Neo4j's primary investment target; top tier (Business Critical) offers up to 512GB instances, 99.95% uptime SLA with HA clustering, and 24/7 support.
- **Infinigraph Edition (2026):** all Enterprise features plus unlimited horizontal scaling via automatic sharding, with Graph Data Science included in the license.

**Graph Data Science (GDS) library** is a separately open-cored component for running graph algorithms: Community Edition includes every algorithm but caps concurrency at 4 CPU cores and the model catalog at 3 models; Enterprise Edition removes the core cap and supports GDS write workloads inside a clustered deployment (requires a separate Enterprise license file).

Open components beyond Community Edition itself: openCypher (Apache-2.0) and native drivers for Java, JavaScript, Python, .NET, and Go (Apache-2.0).

**Adoption:** Neo4j reports 84% of Fortune 100 companies as users and 1,000+ enterprise customers, including NASA, UBS, and Volvo.

## Sources

- [FAQ: Neo4j Enterprise Edition is moving to an open core licensing model](https://neo4j.com/open-core-and-neo4j/) — licensing split, what's in each edition.
- [Neo4j Graph Data Science — Introduction](https://neo4j.com/docs/graph-data-science/current/introduction/) — GDS Community/Enterprise feature split.
- [Neo4j Review (2026): Graph Data at Scale](https://www.modern-datatools.com/tools/neo4j) — production-essentials-are-Enterprise-only characterization, single-writer limitation.

## Security

Open-core model: Community Edition's source (GPLv3) is auditable; Enterprise Edition components are closed-source, commercially licensed, and not independently reviewable without a license. Role-based access control, LDAP/Kerberos integration, and most constraint enforcement are Enterprise-only — Community Edition deployments lack these controls by default.
