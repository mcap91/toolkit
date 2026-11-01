---
name: orq-ai
title: Orq.ai (Agent Runtime / LLMOps Platform)
url: https://orq.ai/
category: framework
summary: Amsterdam-based (founded 2022, formerly Orquesta.cloud) proprietary enterprise control platform for the AI agent lifecycle — Agent Runtime sits in the request path to manage tools, memory, retries/handoffs, and multi-step orchestration; supports granular per-tool approval gates (an individual MCP tool can be flagged to pause and require human sign-off without gating the whole agent run), risk-based approval thresholds, a governed registry of approved agents/models/MCPs/skills/tools with pre-production approval and default-deny for anything outside it, plus guardrails, PII masking, RBAC, observability/tracing, and human-in-the-loop evaluation workflows; 300+ models across 17 providers via its AI Gateway; cloud/VPC/on-prem deployment with US/EU data residency, SOC 2 and GDPR compliance; closed-source SaaS, pricing not published
tags:
  - llmops
  - agent-runtime
  - human-in-the-loop
  - tool-approval
  - governance
  - guardrails
  - observability
  - enterprise
  - saas
  - mcp
reviewed: 2026-10-30
acquired: 2026-10-30
license: proprietary
security_flags:
  - closed-source
  - vendor-sits-in-request-path
overlaps:
  - production-agentic-platforms-2026
source_url: https://www.reddit.com/r/AI_Agents/comments/1xcqkgw/anthropics_own_data_suggests_were_becoming_middle/
source: reddit
---

## What it does

Orq.ai is a proprietary enterprise platform for running AI agents in production. Its Agent Runtime component sits directly in the request path between an application and the LLM/tools it calls, giving teams a control panel over tools, memory, context, guardrails, retries, and human handoffs for multi-step agent workflows. Approval gating is tool-level rather than run-level: an individual MCP tool can be flagged as requiring approval, so only that action pauses on an approval card for a human decision — the rest of the run continues ungated. Teams can also set risk-based thresholds (e.g. let reversible, low-risk work run further before anyone intervenes, while a destructive or hard-to-undo action always waits). On the governance side, Orq.ai maintains a centrally managed "compliance registry" of approved agents, models, prompts, and MCP servers; anything not on the approved list is blocked by default, and new additions go through an approval workflow before reaching production. Human-in-the-loop is also built into evaluation: logged responses can be sent to a dataset for human or rule-based grading, feeding retraining/optimization loops. The platform supports 300+ models across 17 providers through its AI Gateway, integrates with LangChain/LlamaIndex, and deploys to cloud, VPC, or on-premise with US/EU data residency.

## Security

Closed-source proprietary SaaS; no self-hosted/open-source release. SOC 2 certified, GDPR compliant, states alignment with EU AI Act requirements. Because Agent Runtime and the AI Gateway sit in the live request path, routing prompts/completions/tool calls through Orq.ai's infrastructure is itself a trust-boundary consideration for sensitive data, independent of the vendor's own compliance claims. Founded 2022 (as Orquesta.cloud), Amsterdam; raised ~€7.3M total across five rounds through a December 2025 seed round; pricing not published.
