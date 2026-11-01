---
name: agent-first-architecture
title: Agent-First Architecture (The LLM Calls the Code)
url: "https://example.com"
category: agent-pattern
summary: "Architecture pattern where a general coding agent (Claude Code, Codex, OpenCode) running on a VPS is the orchestrator, calling deterministic scripts and connectors from a repo, inverting the usual app-calls-LLM relationship"
tags: [agent-architecture, orchestration, vps, deterministic-code, general-agent, tool-calling]
reviewed: 2026-08-09
acquired: 2026-08-09
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---

## What it does

Describes an architectural inversion: "code no longer calls the LLM — the LLM calls the code." Instead of building a dedicated application that embeds an LLM API call inside its own control flow, the pattern uses a general-purpose coding agent (Codex, Claude Code, OpenCode) as the top-level orchestrator, typically running unattended on a VPS. The agent operates against a repository containing natural-language instructions, deterministic scripts, and connectors (API wrappers, data fetchers, notifiers). The agent reads instructions, decides what to do, and invokes the deterministic code only when a step genuinely needs to be deterministic — the agent itself is the system, not a component bolted onto one.

## Differentiators / Key takeaways

The source frames this as a decision heuristic rather than a universal recommendation, listing conditions under which the pattern fits and conditions under which it doesn't:

**Green flags (fits):**
- Input data changes shape frequently (schemas, formats, sources are not stable)
- The task requires judgment calls, not just deterministic transforms
- Upstream sources change often, so hardcoded parsers/integrations would need constant maintenance

**Red flags (doesn't fit):**
- Many concurrent users (agent-as-orchestrator doesn't scale like a stateless service)
- Shared mutable state (concurrent-access hazards an ad hoc agent loop won't manage safely)
- Strict reproducibility requirements (LLM-driven control flow is non-deterministic run to run)
- High-frequency / low-latency needs (agent reasoning cycles are too slow)

## Mechanical details / What to adopt

- Repo layout: instructions (natural language, agent-readable) + deterministic scripts + connectors, checked into version control alongside each other
- The deterministic scripts remain unit-testable and auditable independent of the agent; the agent's job is deciding *when* to call them
- Suited to unattended/background operation on a persistent host (VPS) rather than per-request invocation

## Security

Reference/pattern content — no code shipped. The main operational risk of adopting this pattern is running an agent unattended with tool/shell access on a persistent host; the entry itself does not specify sandboxing or credential-handling practices, so those would need to be sourced separately if adopting the pattern.