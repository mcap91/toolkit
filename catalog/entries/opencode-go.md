---
name: opencode-go
title: OpenCode Go
url: "https://opencode.ai/go"
category: reference
summary: "Low-cost subscription from the OpenCode team ($5 first month, then $10/month) giving access to popular open coding models — GLM-5.2/5.1, Kimi K2.7 Code/K2.6, Qwen3.7/3.6, MiniMax M2.7/M3, DeepSeek V4 Pro/Flash, MiMo — through OpenCode or any agent; dollar-value usage limits, models hosted US/EU/Singapore with a stated zero-retention policy; set up via OpenCode Zen + an API key"
tags: [opencode, model-access, subscription, glm-5.2, open-models, coding-agent, llm-gateway, reference]
reviewed: 2026-07-09
acquired: 2026-07-09
license: proprietary
security_flags: [proprietary-saas, api-key-required, data-leaves-to-third-party]
overlaps: []
source: unknown
---

## What it is

OpenCode Go is a paid subscription from the OpenCode team that provides access to a curated set of popular open-source coding models at low cost — $5 for the first month, then $10/month. It works like any other provider in OpenCode (or any agent): you subscribe via OpenCode Zen, get an API key, and connect it (`/connect` → OpenCode Go → paste key; `/models` lists what is available). It is optional and separate from using OpenCode itself.

## Models and limits

The included model list (which the team notes may change) covers GLM-5.2 and GLM-5.1, Kimi K2.7 Code and K2.6, MiMo-V2.5-Pro / V2.5, Qwen3.7 Max / Plus and Qwen3.6 Plus, MiniMax M2.7 and M3, and DeepSeek V4 Pro / Flash. Usage limits are defined by dollar value rather than fixed request counts, so cheaper models (e.g. DeepSeek V4 Flash) allow more requests and higher-cost models (e.g. GLM-5.2) fewer. Per third-party reporting, GLM-5.2 on the `opencode-go` endpoint lists a 1M context window at roughly $1.4 / $4.4 per million input/output tokens and $0.26 per million cache read. Only one member per workspace can subscribe.

## Context

This entry was cataloged from an inbox note pairing the question "what is OpenCode GO?" with "OpenCode GO for $10 for GLM-5.2" and a separate mention of Gemma 4 12B for local model testing. OpenCode also offers OpenCode Zen, a pay-as-you-go balance model (auto-reload, sold "at cost") as a related alternative; Z.AI sells its own GLM Coding Plan (from ~$18/month) directly.

## Security

Proprietary SaaS. Requires an OpenCode Zen account and an API key, and routes your coding prompts and code to third-party model providers hosted in the US, EU, and Singapore. The service states a zero-retention policy and that data is not used for model training; those are provider claims, not independently verified here. Standard third-party-data-handling considerations apply for any sensitive code.