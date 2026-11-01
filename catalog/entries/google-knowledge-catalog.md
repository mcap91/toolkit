---
name: google-knowledge-catalog
title: Google Cloud Knowledge Catalog
url: "https://github.com/GoogleCloudPlatform/knowledge-catalog"
category: framework
summary: "Google Cloud's Gemini-powered data catalog and metadata management platform (formerly Dataplex); builds a dynamic context graph of structured/unstructured data assets for AI agent grounding, with MCP server integration for context retrieval"
tags: [data-catalog, metadata, google-cloud, gemini, mcp, knowledge-graph, data-governance, ai-agents]
reviewed: 2026-07-12
acquired: 2026-07-12
license: Apache-2.0
security_flags: [cloud-hosted, requires-gcp-auth]
overlaps: []
source: unknown
---

## What it is

Google Cloud Knowledge Catalog (rebranded from Dataplex Universal Catalog in April 2026) is a fully managed data cataloging and metadata management platform. It automatically harvests technical metadata from BigQuery, AlloyDB, Spanner, Cloud SQL, Firestore, Looker, and third-party systems, then uses Gemini to infer business semantics — generating natural language descriptions, discovering relationships, and proposing verified SQL patterns ("golden queries").

The GitHub repository (`GoogleCloudPlatform/knowledge-catalog`) contains tools, agents, and samples demonstrating how to build context management, enrichment, and retrieval solutions on top of the platform.

## Core capabilities

1. **Governance foundation.** Centralized business glossary, data quality checks, anomaly detection, and policy-based governance across the data estate.

2. **Context curation.** Gemini analyzes schemas, query logs, and semantic models to generate descriptions, discover relationships, and surface example queries capturing complex business logic.

3. **Context retrieval.** AI agents retrieve enriched context via semantic search and Model Context Protocol (MCP). Two MCP implementations: a remote MCP server for cloud-native/serverless, and a local MCP Toolbox for prototyping.

**Official launch framing (2026 announcement).** Google's launch post frames the Knowledge Catalog around three pillars: (1) *Aggregation* — unify context across BigQuery, AlloyDB, Spanner, Cloud SQL, Firestore (Preview), and Looker (Preview), plus partner catalogs (Atlan, Collibra, Datahub, Ab Initio, Anomalo) and enterprise-connectivity federation to SAP, Salesforce Data360, ServiceNow, Workday, and Palantir (Preview); packaged as GA "data products" with built-in intent/SLAs/governance. (2) *Enrichment* — Smart Storage / Object Context API auto-tags and embeds files landing in GCS (Preview), deep multimodal metadata extraction via Gemini, automated context curation (descriptions, glossaries, relationships), and verified SQL patterns with semantic guardrails to curb hallucinated joins. (3) *Search* — GA high-precision hybrid semantic search with sub-second latency, access-control-aware retrieval respecting source permissions, and a context-evaluation framework. The Deep Research Agent in Gemini Enterprise is now natively powered by the Knowledge Catalog (Preview). (Sourced from the Google Cloud launch blog and the `GoogleCloudPlatform/knowledge-catalog` repo — both previously queued items, folded into this entry.)

## MCP integration

Knowledge Catalog exposes its context graph through MCP, allowing AI agents to discover data assets and retrieve business context without custom integration code. This grounds agent reasoning in enterprise metadata, reducing hallucinations.

## Security

Requires GCP authentication and IAM configuration. The platform is fully managed (no self-hosted option). The GitHub samples repo is Apache-2.0 licensed. Third-party integrations (Ab Initio, Anomalo, Atlan, Collibra, Datahub) may have separate licensing. Data Catalog (the predecessor service) began phased shutdown June 1, 2026.