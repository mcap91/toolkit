---
name: nemo-switchyard
title: NVIDIA NeMo Switchyard
url: "https://github.com/NVIDIA-NeMo/Switchyard"
category: framework
summary: "Model-routing layer that selects which LLM serves each request (efficient vs. capable) per call, embeddable as a library, run through a standalone OpenAI/Anthropic-compatible proxy, or loaded as a NeMo Relay / LiteLLM plugin"
tags: [model-routing, llm-gateway, cost-optimization, proxy, nvidia, nemo, litellm, openai-api, anthropic-api, rust, python]
reviewed: 2026-09-16
acquired: 2026-09-16
license: Apache-2.0
security_flags: []
overlaps: [litellm, headroom]
source: unknown
---

## What it does

Switchyard is NVIDIA's open-source model-routing layer for LLM applications and agent harnesses. It decides which model (an "efficient" or "capable" target, or more categories in custom setups) should serve each individual LLM call, then hands the actual request off to the caller's own HTTP client, credentials, and retry logic — it does not make model calls itself in library mode. It preserves native OpenAI Chat Completions, Anthropic Messages, and OpenAI Responses API compatibility, so existing clients (Claude Code, Codex CLI, or any OpenAI/Anthropic SDK client) can point at it without code changes.

Three integration paths, per the README:
- **Path 1 — NeMo Relay plugin**: loads into an existing NeMo Relay (>=0.8.0, <1.0.0) deployment via a `routes.toml` file.
- **Path 2 — Embed the library** (`switchyard-libsy` for Rust, `nemo-switchyard`/`switchyard.libsy` for Python via `pip install`): the caller constructs a routing algorithm, drives its async step stream (`Step.CallModel`, `Step.Done`), and supplies the model call itself.
- **Path 3 — Standalone proxy** (`switchyard-server`, `cargo install --locked switchyard-server`): a Rust server on `localhost:4000` answering `/v1/chat/completions`, `/v1/messages`, and `/v1/responses`, configured entirely via `routes.toml` (LLM client backends, targets/model IDs, and one or more named routes).

## Differentiators

Ships several distinct routing algorithms rather than a single strategy: **Capability** (LLM-judge on the first request only, route type `llm_classifier`), **Stage** (per-tool-response judging by pattern match or LLM, route type `stage_router`), **Capability + Stage** composite, **Escalation** (starts on the efficient model, an LLM judge reviews responses for issues and escalates mid-task), **Advisor Gate** (a stronger "advisor" model approves or rejects a weaker executor's plans and completion claims), **Sub-Agent-Aware** (routes delegated sub-agent traffic separately from parent-agent traffic), **Custom** (LLM classifies against caller-defined criteria across 2+ models), and **Random** (baseline). The README publishes Terminal-Bench 2.1 benchmark numbers (against a $98.06 Opus 4.8 baseline at 76.0% accuracy) for four of these: Escalation 75.7% at $85.00 (13.3% cheaper), Stage 72.7% at $68.19 (30.5% cheaper), Capability 71.2% at $79.32 (19.1% cheaper); Composite, Sub-Agent-Aware, and Custom are listed as "not yet benchmarked." The escalation routing profile used for the benchmark is checked into the repo (`benchmark/routing-profiles/tb21-escalation-opus-glm-deepseek.toml`) with OpenRouter targets substituted for NVIDIA-internal endpoints so it is publicly runnable, and the README notes those internal-endpoint benchmark runs may not reproduce on other serving stacks. It exposes `/v1/stats` (which target served which request) and Prometheus `/metrics` for latency, error, and token counters — routing-overhead observability the README frames as necessary given Switchyard's own added latency.

## Mechanical details

Components carry individual stability labels: `switchyard-libsy` (Beta), `switchyard-llm-client` (Alpha, HTTP calls + protocol translation alongside libsy), `switchyard-runner` (Alpha, runs configured routes inside another runtime such as NeMo Relay), `switchyard-server` (Demo — README states "Demos and evaluation only. Not for production."). The whole project is labeled pre-1.0 with the warning that "APIs, configuration, and routing behavior can change between releases — pin the version you integrate," including by commit SHA for both pip (`@<sha>`) and Cargo (`rev = "<sha>"`) since the newest library API postdates the `nemo-switchyard` 0.2.0 PyPI release. `routes.toml` schema: `[llm_clients.<name>]` (format, base_url, api_key_env), `[targets.<name>]` (model id, llm_client), `[routes.<name>]` (id, type, and per-algorithm fields such as `picker`/`confidence_threshold` for `stage_router`). `switchyard-server --config routes.toml --dry-run` validates config and prints exposed model IDs without starting the server. A "passthrough" route type registers one target under one model ID with no routing decision. Also has a Rust crate `switchyard-protocol` (provider-neutral request/response/streaming types) and `switchyard-translation` (request/response/stream translation between provider formats).

## Security

Apache-2.0 licensed, copyright NVIDIA Corporation (per the repository's own License section — note that some press coverage of the same NVIDIA launch describes an "OpenMDW-1.1" license, which this repo's README does not corroborate). No security-relevant red flags identified from the README: the library mode explicitly keeps model calls, credentials, and retries in the caller's own harness rather than Switchyard's; the standalone proxy mode does sit in the request path for all LLM traffic routed through it and is explicitly labeled "Demo" / "Not for production" by the maintainers themselves. Routing in most algorithms depends on an LLM-as-judge call, which is an added inference cost and an additional trust dependency (the judge's classification determines where user/agent traffic is sent). No independent security audit or supply-chain review found via the fetched README or web search at review time.
