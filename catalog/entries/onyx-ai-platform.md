---
name: onyx-ai-platform
title: Onyx AI Platform
url: "https://github.com/onyx-dot-app/onyx"
category: framework
summary: "Full self-hostable AI platform with agentic RAG and MCP — notable architecture reference, but too deployment-heavy to adopt as a composable toolkit component"
tags: [rag, agentic-rag, self-hosted, llm, mcp, knowledge-retrieval, enterprise, connectors]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [curl-pipe-install, large-attack-surface, code-execution-sandbox]
overlaps: []
source: unknown
---

## What it does

Onyx is a self-hostable, open-source AI application platform built on top of LLMs. It provides a full-featured chat UI combined with a hybrid vector+keyword index for agentic RAG, deep research flows, web search (Serper, Brave, SearXNG, Firecrawl/Exa), sandboxed code execution, artifact generation, voice mode, image generation, and MCP-based action integrations. It ships with 50+ pre-built data connectors (document stores, wikis, ticketing systems, etc.) for knowledge ingestion. Deployment is Docker, Kubernetes, or Helm/Terraform. The "Lite" mode requires under 1 GB RAM and runs a stripped-down stack; the full "Standard" mode adds Redis, MinIO, background job workers, and dedicated ML inference servers. Enterprise Edition adds SSO (OIDC/SAML/Google OAuth), SCIM provisioning, RBAC, analytics, query audit logs, PII scrubbing hooks, and whitelabeling.

## Assessment

Onyx is a well-resourced, actively maintained project with broad feature coverage and a clean MIT license for the community edition. However, it is a full product platform rather than a composable component: adopting it means deploying and operating a multi-container stack. The catalog here is oriented toward skills, agent patterns, MCP servers, and lightweight CLI tools that integrate directly into Claude Code workflows. Onyx is worth watching as a reference architecture for (a) how agentic RAG pipelines are structured with hybrid retrieval, (b) how MCP can be used as the action/integration layer in a deployed AI product, and (c) how multi-connector knowledge ingestion is engineered at scale. If the project ever extracts its RAG pipeline or connector framework as a standalone library, that would be catalog-adopt territory.

## Mechanical details

- **Deployment:** `curl -fsSL https://onyx.app/install_onyx.sh | bash` (Lite) or full Docker Compose / Helm charts.
- **LLM backends:** Anthropic, OpenAI, Gemini, Ollama, LiteLLM, vLLM — any OpenAI-compatible endpoint.
- **RAG architecture:** Hybrid index (vector + BM25 keyword), AI agents for retrieval orchestration, configurable chunk sizes and reranking.
- **Deep Research:** Multi-step research flow claimed top of leaderboard as of Feb 2026.
- **MCP integration:** Agents can call external services via MCP with flexible auth options.
- **Code execution:** Sandboxed execution for data analysis, graph rendering, file manipulation.
- **Connectors:** 50+ indexing connectors out of the box (Confluence, Notion, Jira, Slack, GDrive, etc.).
- **What to adopt from it:** The connector-normalization pattern (chunked ingest → hybrid index → rerank → agent synthesis) is a good reference for building document-grounded agent workflows. The MCP action layer design is worth studying for how auth and tool registration are handled in a multi-tenant context.

## Security

- **License:** MIT for Community Edition; Enterprise Edition is proprietary. Dual-licensing is clearly documented and cleanly separated.
- **Install vector:** The recommended quick-start uses `curl ... | bash` with no checksum verification — a supply chain risk if the install server or DNS is compromised. Production deployments should pull versioned Docker images directly rather than using the script.
- **Code execution:** Built-in sandboxed code execution is a high-value attack surface. Sandbox escape risk depends on implementation details not visible in the README; treat with caution in multi-tenant or untrusted-input scenarios.
- **Attack surface:** Large stack (web server, vector DB, job queue, blob store, ML inference, SSO/SCIM) — each component expands the security perimeter. Credential and token handling across this surface requires careful configuration.
- **Credential handling:** SSO/SAML/SCIM integration handles identity tokens; RBAC controls access to agents and actions. No observed eval() or shell injection patterns in the README, but the custom-code PII-scrubbing hook feature (EE) allows arbitrary code execution by design.
- **Maintenance:** Active development; top-of-leaderboard claim dated Feb 2026 suggests recent active work. GitHub repo public with community Discord.
- **security_flags rationale:** `curl-pipe-install` (no-hash remote script), `large-attack-surface` (multi-component stack with ML inference + blob store + auth), `code-execution-sandbox` (sandboxed exec present, escape risk not independently verified).
