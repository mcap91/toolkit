---
name: redis-iris
title: Redis Iris
url: "https://redis.io/iris/"
category: framework
summary: "Redis's context-and-memory platform for AI agents (announced May 18, 2026) — bundles real-time structured/unstructured data retrieval (Context Retriever), short- and long-term agent memory (Agent Memory: interaction history, user preferences, persistent attributes), and continuous data sync from source-of-record systems (Redis Data Integration) into one product, layered on existing Redis Search and LangCache semantic caching"
tags: [redis, agent-memory, rag, context-engineering, semantic-cache, data-integration, ai-agents, context-retrieval]
reviewed: 2026-08-25
acquired: 2026-08-25
license: proprietary
security_flags: ["Commercial Redis product; the fetched redis.io/iris/ marketing page itself renders mostly as navigation chrome with minimal on-page prose — most factual detail in this entry comes from third-party reporting and Redis's own docs.redis.io context-engine page rather than the linked landing page directly", No independent security/privacy audit of the Agent Memory data-retention or multi-tenant isolation model found during this review]
overlaps: []
source: unknown
---

## What it says

Redis announced Iris on May 18, 2026 as a context-and-memory platform purpose-built for AI agents, addressing the stateless nature of LLMs (every interaction starts from scratch unless something external provides continuity) and the observation that agentic workloads generate orders-of-magnitude more data requests than human-scale usage patterns that most retrieval pipelines were designed for.

Iris consolidates three previously separate capabilities into one system:

- **Redis Context Retriever** — real-time retrieval of structured and unstructured data so an agent can ground responses in current facts.
- **Redis Agent Memory** — preserves short-term conversational state and longer-term memory (recent interaction history, user preferences, persistent attributes) so systems can carry context across turns and sessions; available via Python and TypeScript SDKs and a REST API.
- **Redis Data Integration (RDI)** — synchronizes data from source systems (relational databases, data warehouses, document stores) into Redis in agent-optimized formats, forming a continuously updated operational data layer separate from systems of record.

These are built on existing Redis technology: LangCache provides semantic caching to cut latency and token use, and Redis Search handles retrieval across vector, structured, unstructured, and real-time data.

Alongside Iris, Redis introduced a Flex SSD storage tier — a rewritten storage engine that keeps ~99% of data on flash, claimed by Redis to cost a tenth of pure in-memory storage — aimed at making larger context windows and longer agent memories affordable at scale.

Redis states that 43% of enterprise AI agent stacks already use Redis somewhere in the runtime layer, and frames Iris as expanding Redis's role from a performance/data-access layer into context infrastructure for agentic AI.

## Key takeaways

- Packages three previously separate Redis capabilities (real-time retrieval, agent memory, data integration/RDI) as one named product/platform rather than components a team assembles individually.
- Distinguishes "systems of record" (source databases/warehouses) from a continuously synced "retrieval layer" that agents query directly, via RDI.
- New Flex SSD tier is a cost lever specifically for agent-memory-at-scale use cases (mostly-flash storage vs. pure in-memory).
- Agent Memory ships with Python/TypeScript SDKs and a REST API; Redis Cloud manages the sync pipeline.

## Mechanical details

- Availability: Agent Memory — Python SDK, TypeScript SDK, REST API.
- Underlying components referenced: LangCache (semantic caching), Redis Search (vector/structured/unstructured/real-time retrieval), Redis Data Integration (RDI), Redis Flex (SSD-backed storage engine).
- Related docs surface: `redis.io/docs/latest/develop/ai/context-engine/`.
- Announcement date: May 18, 2026.

## Security

- **License**: Proprietary Redis product (Redis Cloud / Redis Enterprise commercial offering); not open-source.
- **Data handling**: Agent Memory stores interaction history, user preferences, and persistent attributes in Redis — a data-retention and multi-tenant-isolation surface that was not detailed in the sources reviewed; evaluate data-residency and retention controls before storing sensitive data.
- **Supply chain**: Published by Redis Inc., an established commercial vendor; no third-party or community package involved.
- **Source caveat**: This entry is based on third-party reporting (Let's Data Science, Blocks & Files) and the Redis docs context-engine page, since the linked `redis.io/iris/` marketing page returned mostly navigation/menu content with little substantive body text when fetched.
