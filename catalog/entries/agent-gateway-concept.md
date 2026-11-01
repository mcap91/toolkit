---
name: agent-gateway-concept
title: Agent Gateway (Concept)
category: reference
summary: "Explainer on agent gateways — a specialized gateway layer between AI agents and their backends (LLMs, MCP servers, other agents) that understands agentic protocols (MCP, A2A) and provides unified identity, per-tool policy, prompt-injection screening, PII redaction, provider-agnostic model routing, and full-hop observability; distinguishes from traditional API gateways and LLM-only gateways"
tags: [agent-gateway, mcp, a2a, infrastructure, security, observability, routing, policy]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: ""
security_flags: []
source: unknown
---

## What it is

An agent gateway is a single front door between AI agents and everything they talk to — LLM providers, MCP tool servers, and other agents. Every call passes through it, providing one place to connect, secure, and observe all agent traffic.

Traditional API gateways see HTTP verbs and URL paths. Agent traffic is different: MCP calls are always `POST /mcp` with the real action (which tool, which arguments) inside the JSON body, over sessions that stay open and stream back. An agent gateway reads the message content, not just the HTTP envelope.

## What it adds

- **Protocol awareness**: understands MCP, A2A, and LLM traffic natively.
- **Tool aggregation**: many MCP servers behind one endpoint; each agent sees only its authorized tools; REST APIs can be exposed as MCP tools.
- **Security**: signed agent identity, per-tool policy enforcement, prompt-injection screening, PII redaction.
- **Model routing**: one OpenAI-compatible API, swap providers without code changes, token budgets and rate limits.
- **Observability**: every hop (model call, tool call, agent-to-agent message) in one trace.

## Implementations

Open source: LiteLLM (Python, broad provider catalog + MCP/A2A support), agentgateway (Rust, AAIF-hosted, 300x less memory than Python alternatives, #1 trending GitHub August 2026). Platforms: Kong AI Gateway, Portkey, Cloudflare AI Gateway. Cloud-native: Google Agent Gateway, AWS AgentCore Gateway, Azure API Management.

## Taxonomy

An **AI gateway** handles agent-to-LLM-provider traffic (routing, fallbacks, budgets). An **MCP gateway** manages agent-to-tool-server traffic (tool allow-lists, guardrails). An **agent gateway** unifies both plus A2A with unified identity, policy, and audit across all paths.

## Security

Reference entry — no installable artifact. Security considerations for agent gateways themselves: they become a single point of trust and failure; the gateway's own credential store, policy engine, and PII redaction pipeline are high-value targets; Rust-based implementations (agentgateway) reduce memory-safety risk versus Python alternatives.