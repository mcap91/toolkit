---
name: openrouter
title: OpenRouter
url: "https://openrouter.ai/"
category: framework
summary: "Unified LLM API gateway supporting 200+ models — useful as infrastructure reference, not directly needed when using Claude natively."
tags: [llm, api-gateway, model-routing, openai-compatible, infrastructure]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-proprietary
security_flags: [proprietary-saas, credentials-required, data-leaves-to-third-party]
overlaps: []
source: unknown
---

## What it does

OpenRouter is a unified API gateway that routes LLM requests to multiple providers (OpenAI, Anthropic, Google, Meta, Mistral, and others) through a single OpenAI-compatible endpoint. It supports 200+ models with automatic fallback between providers, cost optimization by comparing prices across providers, model routing based on price/speed/quality preferences, and usage tracking with rate limiting. The API is OpenAI SDK-compatible, so existing code can be pointed at OpenRouter with minimal changes. It is widely used in the open-source AI community and commonly integrated into frontends like SillyTavern and Open WebUI.

## Assessment

**Note.** Useful to know about as LLM infrastructure — particularly relevant if building multi-model agent workflows or needing provider redundancy. However, this toolkit primarily uses Claude directly via Claude Code and the Anthropic API, so OpenRouter adds a layer of indirection without clear benefit for the current setup. Worth revisiting if a workflow needs non-Anthropic models (e.g., for comparison benchmarks, specialized open-source models, or cost-sensitive batch inference). The existing Open WebUI catalog entry already references OpenRouter as a common integration.

## Mechanical details

- **API:** Single endpoint, OpenAI SDK-compatible. Drop-in replacement by changing the base URL.
- **Models:** 200+ from dozens of providers. Model selection via model ID or routing preferences.
- **Routing:** Configurable by price, speed, or quality. Automatic fallback if a provider is down.
- **Pricing:** Pass-through provider pricing plus OpenRouter margin. Free tier available for some models.
- **Auth:** API key required (generated at openrouter.ai/keys).
- **What to note:** If multi-model comparison or provider redundancy is ever needed, OpenRouter is the standard aggregator. The OpenAI-compatible API means any OpenAI SDK client works with a base URL change.

## Security

- **License:** Proprietary SaaS — no open-source server code.
- **Dependency health:** N/A (closed source).
- **Code quality / CI:** Not assessable; no public repository for the server.
- **Supply chain:** Single vendor. Well-established in the LLM ecosystem with significant community adoption.
- **Dangerous patterns:** None at the API level. Standard REST API with key-based auth.
- **Credential handling:** API key stored by user. All requests carry the key in headers. Keys can be scoped and rotated via the dashboard.
- **Data privacy:** All prompts and completions transit through OpenRouter servers before reaching the downstream provider. Users should review OpenRouter's data retention policy (they state they do not train on user data). Sensitive prompts are exposed to both OpenRouter and the downstream provider.
- **Maintenance:** Actively maintained commercial service with regular model additions.
- **security_flags rationale:** `proprietary-saas` (closed source), `credentials-required` (API key needed), `data-leaves-to-third-party` (prompts transit through OpenRouter before reaching the provider).

## Usage notes

- Use the OpenRouter model rankings (openrouter.ai/rankings) to scout and compare models when testing local/open LLMs.
