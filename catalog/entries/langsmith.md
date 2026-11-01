---
name: langsmith
title: LangSmith
url: https://smith.langchain.com/
category: framework
summary: LangChain's commercial observability, evaluation, and deployment platform for LLM/agent applications — traces, evals, and monitoring that work against almost any stack via OpenTelemetry, not just LangChain/LangGraph. The client SDK (langsmith-sdk) is MIT-licensed, but the platform backend, UI, and storage layer are closed-source and unpublished; self-hosting requires an Enterprise plan and a sales-issued license key. In May 2026, LangChain replaced LangSmith's ClickHouse storage engine on its US Cloud with SmithDB, a proprietary Rust engine on Apache DataFusion and Vortex; self-hosted deployments still run ClickHouse+Postgres, with SmithDB there in a waitlisted public beta that LangChain does not recommend self-operating.
tags:
  - observability
  - evaluation
  - llm-tracing
  - agent-monitoring
  - opentelemetry
  - closed-source
  - enterprise
  - langchain
reviewed: 2026-10-28
acquired: 2026-10-28
license: Proprietary (platform); MIT (langsmith-sdk client only)
security_flags:
  - closed-source
  - self-hosting-gated-enterprise
overlaps:
  - langchain
  - langgraph
source: text
---

## What it does

The tracing/evaluation/monitoring layer for the LangChain ecosystem, built to answer "what actually happened when the agent misbehaved." Captures traces and evals, and — because it ingests via OpenTelemetry — can point at almost any LLM/agent stack, not only LangChain or LangGraph. Adopting LangSmith does not require adopting the other two layers.

**Licensing split:** the `langsmith-sdk` client is MIT and open source (github.com/langchain-ai/langsmith-sdk); the platform itself — backend, UI, storage layer — is closed-source and not published. Self-hosting is gated behind an Enterprise plan; LangChain's docs describe self-hosted LangSmith as an Enterprise add-on for "largest, most security-conscious customers," requiring a sales-issued license key to trial.

**Storage architecture:** through early 2026, LangSmith ran on ClickHouse. In May 2026, LangChain's US Cloud moved to SmithDB, a proprietary Rust engine built on Apache DataFusion and Vortex. Self-hosted deployments still run ClickHouse+Postgres; SmithDB is available there only as a waitlisted public beta, which LangChain does not recommend operating yourself.

## Sources

- [LangSmith Alternative: Langfuse vs. LangSmith — Langfuse](https://langfuse.com/compare/langsmith) — self-hosting/licensing details, SmithDB migration.
- [Langfuse vs LangSmith: Pricing, OSS and Tracing 2026 — TrueFoundry](https://www.truefoundry.com/blog/langfuse-vs-langsmith)

## Security

Platform is closed-source; self-hosting requires an Enterprise license and sales engagement, limiting independent security review of the backend. Client SDK (langsmith-sdk) is MIT and auditable. Hosted (SaaS) use means trusting LangChain's cloud infrastructure for trace/eval data, which can include application prompts and outputs.
