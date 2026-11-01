---
name: zdr-router-trust
title: ZDR Router Trust — DeepSeek/Kimi/Xiaomi Data Leak Investigation (Sep 2026)
category: reference
summary: "Chinese authorities investigating DeepSeek, Moonshot (Kimi), and Xiaomi for routing third-party router users' requests to Anthropic models, injecting hidden prompts to harvest CoT traces, modifying returned text, and training on the interactions — raising questions about ZDR (zero data retention) credibility of third-party model routers like OpenRouter and OpenCode"
tags: [security, privacy, zdr, model-routing, openrouter, deepseek, kimi, anthropic, data-leak, trust]
reviewed: 2026-09-25
acquired: 2026-09-25
license: N/A
security_flags: [data-exfiltration, privacy-violation]
overlaps: []
source: unknown
---

## What it does

Reference documenting a September 2026 investigation by China's Cyberspace Administration into DeepSeek, Moonshot (Kimi), and Xiaomi Mimo model providers. Key findings:

- These providers routed user requests from third-party routers (likely OpenRouter, OpenCode) to Anthropic models
- Injected hidden prompts to harvest chain-of-thought traces
- Modified returned text before passing to users
- Used captured data to train their own models
- Leaked sessions contained names, email addresses, company data, and sensitive information in 12+ languages

Anthropic published a 146-page investigation report documenting the detection and evidence.

Source: The Standard (HK), Sep 2026; Anthropic investigation report (anthropic.com).

## Assessment

Directly relevant to any workflow routing through third-party model providers. The core risk: ZDR policies are contractual, not cryptographic. A router can claim zero retention while a downstream provider silently captures everything. Implications for self-hosted vs. routed inference decisions.