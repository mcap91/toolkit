---
name: litellm
title: LiteLLM
url: "https://github.com/BerriAI/litellm"
category: framework
summary: "Open-source Python SDK and self-hosted AI gateway (proxy server) providing a unified OpenAI-compatible interface to 100+ LLM providers — model routing, automatic fallbacks, cost tracking, per-team budgets, Redis caching, guardrails, MCP/A2A support; ~40K stars, 1300+ contributors, YC-backed; MIT"
tags: [llm-gateway, api-proxy, model-routing, cost-tracking, openai-compatible, multi-provider]
reviewed: 2026-06-26
acquired: 2026-06-26
license: MIT
security_flags: []
overlaps: [openrouter, hugging-face-inference-providers]
source: unknown
---

## What it does

LiteLLM is an open-source Python SDK and self-hosted proxy server (AI Gateway) from BerriAI that provides a single OpenAI-compatible interface to call 100+ LLM providers — OpenAI, Anthropic, Gemini, AWS Bedrock, Azure, Cohere, HuggingFace, vLLM, NVIDIA NIM, and more. Any client that works with the OpenAI API works with the LiteLLM proxy without code changes.

Two modes of operation:
- **Python SDK:** Direct library import for prototyping and scripts. Zero infrastructure.
- **Proxy Server:** Self-hosted OpenAI-compatible gateway with key management, budgets, observability, and multi-tenant governance. Containerized, PostgreSQL-backed, optional Redis.

## Key takeaways

- Unified interface: same request/response format regardless of backing provider. Routes by model name, cost, or task complexity.
- Reliability engine: automatic fallbacks between providers, retries, usage-based routing, failure budgets.
- Cost controls: per-key/team/user spend tracking, automatic cutoff or reroute when budgets hit.
- Multi-tenancy: organizations, teams, virtual API keys, RBAC, SSO (Okta/Azure AD — enterprise).
- Observability: callbacks for LangSmith, Helicone, Lunary, MLflow; native Prometheus metrics; OpenTelemetry with W3C baggage propagation.
- Agent support (2026): unified gateway for LLMs, A2A agents, and MCP tools; central MCP endpoint with per-key access control.
- Redis caching can cut costs 20-40% on repeat-query workloads.
- models.litellm.ai provides a browsable catalog of 2600+ models across 140+ providers with pricing and context window data.

## Mechanical details

- **Architecture:** Containerized proxy behind load balancer → PostgreSQL + optional Redis → routes to LLM providers. Single instance handles hundreds req/s, horizontally scalable.
- **Latency overhead:** 5-15ms for proxy routing layer.
- **SDK usage:** `from litellm import completion; completion(model="anthropic/claude-sonnet-4-20250514", messages=[...])`.
- **Proxy config:** YAML-based model definitions with aliases, fallback chains, per-model rate limits.
- **Scale:** ~40K GitHub stars, 1300+ contributors, rapid model additions (GPT-5.4, Gemini 3.x in v1.82.3).

## Security

MIT license. Large contributor base (1300+). Active maintenance with frequent releases. The proxy becomes a critical infrastructure dependency — routes all LLM traffic and manages API keys. Self-hosted deployment keeps keys within your infrastructure. Enterprise features (SSO, audit logs, RBAC) are paid.