---
name: weft-language
title: Weft
url: "https://github.com/WeaveMindAI/weft"
category: framework
summary: "Novel AI orchestration language with typed nodes, durable execution, and human-in-the-loop primitives — early-stage but architecturally interesting"
tags: [programming-language, ai-orchestration, durable-execution, visual-programming, human-in-the-loop, rust, orchestration]
reviewed: 2026-06-10
acquired: 2026-06-10
license: O-Saasy-1.0
security_flags: [saas-restriction]
overlaps: []
source: unknown
---

## What it does

A programming language where LLMs, humans, APIs, and infrastructure are first-class primitives. Programs are typed node graphs: LLM inference, human approval forms, database queries, and messaging (Discord/Slack/Telegram/etc.) are all single-node operations wired together with a compiler that checks types and connections before anything runs. Programs survive crashes via Restate durable execution — a human approval that takes three days uses the same code as one that takes three seconds. Two native views: dense text code for AI builders and a visual graph for humans, kept in sync. Rust backend, SvelteKit dashboard, ~30 built-in nodes across AI, code, communication, data, flow, storage, and triggers.

## Assessment

Early-stage ("two months in, breaking changes expected") but the architecture is genuinely interesting: typed end-to-end node graphs with durable execution and first-class human-in-the-loop. The recursive folding (any group of nodes collapses into a single node with a described interface) is a clean abstraction. Worth watching for patterns to borrow — particularly the durable execution model and human query primitives — but too young and too different from the Claude Code skill model to adopt or pilot now.

## Mechanical details

- Rust crates: weft-core (compiler/type system), weft-nodes (registry), weft-api (REST), weft-orchestrator (Restate services)
- Node catalog: ~30 nodes in `catalog/` — each is a `backend.rs` + `frontend.ts` pair
- Requires Docker (PostgreSQL), Node.js; auto-installs Rust, Restate, pnpm
- O'Saasy License: MIT with SaaS restriction — free to use/modify/self-host, cannot offer as competing hosted service

## Security

O'Saasy License (MIT + SaaS restriction) — not pure open source; the SaaS clause may matter for hosted deployments. Requires API keys for external services (OpenRouter, Tavily, etc.) stored in `.env`. PostgreSQL auto-provisioned via Docker. Infrastructure nodes can provision Kubernetes resources. The `.sqlx` directory is committed for offline builds. Early-stage project with a single maintainer — expect rapid churn. No obvious dangerous patterns in the language design itself.