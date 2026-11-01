---
name: scheduled-multi-agent-coordinator
title: Scheduled Multi-Agent Coordinator Pattern
url: "https://github.com/nanocoai/nanoclaw"
category: agent-pattern
summary: Useful architecture pattern for persistent scheduled agents with coordinator + messaging; NanoClaw and Hermes are mature implementations
tags: [multi-agent, scheduling, coordinator, persistent-agent, messaging-integration, codex, nanoclaw, hermes, orchestration]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: []
overlaps: [overcut, odysseus]
source: unknown
---

## What it says

A discussion post describing a desired architecture for running multiple Codex CLI agents on schedules or event triggers, with a coordinator agent that:

- Manages the other agents and ensures system stability
- Handles events, schedules, and connections to third-party services
- Provides remote communication via Slack, web app, or phone
- Uses a subscription ($200/mo Codex) rather than per-call API keys

The post names two existing open-source multi-agent loop systems as starting points:

**NanoClaw** (github.com/nanocoai/nanoclaw) — a lightweight, container-isolated alternative to OpenClaw. Agents run in Docker/Apple Containers with filesystem isolation. Supports multiple LLM providers (Claude via Agent SDK, Codex CLI via `/add-codex`, OpenCode, Ollama). Multi-channel messaging: WhatsApp, Telegram, Discord, Slack, Teams, iMessage, email, and more. Credentials stored in OneCLI vault, never inside containers.

**Hermes Agent** (hermes-agent.org by Nous Research) — a self-hosted multi-agent framework with a built-in learning loop (writes reusable skills after complex tasks). 32k+ GitHub stars, 200+ LLM backends, 40+ tools. The opencode-hermes-multiagent variant provides 17 specialized coding agents. MIT licensed, supports Linux/macOS/WSL2.

## Assessment

**Note.** The pattern itself — scheduled persistent agents with coordinator oversight and messaging integration — is architecturally relevant to how we might scale automated workflows. However:

- This is a concept/wish-list, not a deployable tool
- NanoClaw and Hermes are each substantial tools that would merit their own entries if pursued
- The Codex subscription constraint (avoiding API keys) limits provider flexibility
- Container-based agent isolation (NanoClaw) is a strong security model worth noting
- Hermes's self-improving skill loop is interesting but raises questions about skill drift and auditability

Upgrade to **watch** if we decide to pursue a persistent agent coordinator setup.

## Mechanical details

The architecture described has three tiers:

1. **Worker agents** — individual Codex/Claude/OpenCode agents that perform scheduled or event-triggered tasks (backups, monitoring, code reviews, etc.)
2. **Coordinator agent** — a meta-agent that manages the workers, monitors system health, handles escalation, and accepts commands from the user
3. **Communication layer** — Slack, web app, or messaging integration for remote control from phone/desktop

NanoClaw implements this most directly: long-lived poll loops per agent container, message routing between channels and agents, provider-agnostic (Claude, Codex, OpenCode, Ollama). Setup is `git clone` + `codex` + `/setup`.

Hermes takes a different approach: a single orchestrator with specialized sub-agents, persistent memory, and a skill-evolution loop. More autonomous but less explicitly schedulable.

## Security

- **NanoClaw:** Container isolation (Docker/Apple Container) is a strong security boundary. Credentials in OneCLI vault, not in containers. Bash commands run inside containers, not on host. MIT licensed. However, the "Claw" ecosystem has been flagged in academic research for potential memory pollution vectors in persistent agents (arxiv.org/pdf/2603.23064).
- **Hermes:** MIT licensed, self-hosted (data stays on machine). 32k+ stars suggests community review. The self-improving skill loop means agent behavior evolves over time — requires monitoring for drift.
- **General pattern risk:** Persistent scheduled agents with third-party service access create a large attack surface. Scoped tokens, audit logs, and coordinator oversight are essential controls.
- **security_flags:** Clean for the pattern itself; individual tool entries would need their own security review.