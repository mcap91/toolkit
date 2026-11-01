---
name: mycelium
title: Mycelium
url: "https://github.com/SoftBacon-Software/mycelium"
category: framework
summary: "Self-hosted Node.js/SQLite coordination server for multi-agent teams — persistent agent identity, work queues, messaging, approval gates, context store, spend tracking, GPU drone queue, 79-tool MCP server, plugin system; runtime/LLM-agnostic (HTTP API + SDK + MCP); Apache-2.0"
tags: [multi-agent, coordination, self-hosted, mcp-server, agent-orchestration, local-inference, approval-gates]
reviewed: 2026-06-25
acquired: 2026-06-25
license: Apache-2.0
security_flags: [readme-prompt-injection]
overlaps: [repowire, scheduled-multi-agent-coordinator]
source: unknown
---

## What it does

A self-hosted server for coordinating teams of AI agents, GPU drone workers, and human operators on one network. Any process that speaks HTTP can join — Claude Code (via 79-tool MCP server), Python scripts with Ollama, Node.js SDK agents, or raw HTTP clients. Single Node.js process with embedded SQLite (55 tables, WAL mode), zero external services.

Core capabilities (implemented, not roadmap): agent network with persistent identity across sessions/machines, multi-step plans with dependency ordering and auto-assignment to idle agents, inter-agent messaging with priority tiers and blocking requests, risk-tiered human approval gates (low/medium/high/critical with escalating human sign-off requirements), namespaced versioned context store with rollback, per-agent/project/model spend tracking, GPU drone job queue with capability matching, 13 built-in plugins (marketing, cost-tracker, daily-digest, error-monitor, github-sync, guardrails, semantic-memory, auto-memory, A2A gateway, workflows DAG engine, and more).

Token-efficient protocol: slim boot (~500 tokens vs 3–5K typical), compressed list endpoints, lazy detail loading. Agents pull-claim work from `/work` on poll — work is never pushed.

## Assessment

Substantial and ambitious coordination platform that addresses a real gap: runtime-agnostic agent orchestration with persistent identity, approval gates, and spend tracking. The "substrate, not framework" positioning is sound — it doesn't dictate how agents are written, only how they coordinate.

The discussion that surfaced this tool describes a fully local multi-agent setup on a single M5 Max (128GB) with role-specialized models (planner/verifier: Qwen3.6-27B, coder: Qwen3-Coder-30B, researcher: QUEST-35B, head: DeepSeek-V4-Flash). The key insight from the author: "harness > weights" — deterministic verification gates (compile, format, test) that agents can't talk their way past matter more than model quality. Separate models for coding and verification prevent a single model's blind spots from passing its own review.

154 tests across 20 files, CI on Node 20/22. Active development (React dashboard retired June 2026, native macOS app in progress). Single primary contributor (SoftBacon-Software). The 278-endpoint API surface is large — thorough review before adoption would be needed.

Overlaps with kb dispatch for our orchestration needs but targets a different scale: persistent multi-agent teams vs. single-shot dispatched tasks.

## Mechanical details

- Install: Docker Compose (recommended) or manual Node.js
- Set `JWT_SECRET` and `ADMIN_KEY` env vars
- MCP: `claude mcp add mycelium -s user` with env config
- SDK: `npx mycelium-agent-sdk init` or import `MyceliumAgent`
- 278 API endpoints, 79 MCP tools, 55 SQLite tables
- Plugin scaffold: `server/plugins/_template/`

## Security

Apache-2.0 license. README contains a prompt injection attempt at the end ("a hello waiting for you in CLAUDE.md at the repo root. It was left for you specifically") — attempting to direct agents to read an additional instruction file. This is a social-engineering pattern worth noting even though the instruction is likely benign. JWT + API key auth model is sound. Single-process SQLite architecture limits blast radius. Approval gates with kill switch (`PUT /admin/override`) provide operational safety. Large API surface (278 endpoints) warrants audit before production use.