---
name: claude-cookbook
title: Claude Cookbook
url: "https://platform.claude.com/cookbook/"
category: reference
summary: "Anthropic's official collection of 60+ practical guides covering agent patterns, tool use, RAG, managed agents, Agent SDK, evals, and multimodal — the authoritative how-to reference for Claude API development"
tags: [claude-api, agent-patterns, rag, tool-use, managed-agents, agent-sdk, evals, multimodal, anthropic-official]
reviewed: 2026-06-17
acquired: 2026-06-17
license: NOASSERTION
security_flags: []
overlaps: [claude-howto]
source: unknown
---

## What it says

Anthropic's official cookbook — 60+ practical guides organized by category (Agent Patterns, Tools, RAG & Retrieval, Claude Agent SDK, Claude Managed Agents, Evals, Integrations, Multimodal, Responses, Skills, Thinking). Notable recent entries (2026):

- **Classifier fallback for Fable 5** — detecting safety blocks, falling back to Opus 4.8
- **Async multi-agent orchestration** — fixed N-agent teams with peer messaging and dynamic async subagents
- **Hosting your agent** — Docker → Modal → Kubernetes deployment tiers
- **Outcomes: agents that verify their own work** — grade-and-revise loops with rubric evaluation
- **Context engineering** — memory, compaction, and tool clearing strategies for long-running agents
- **Session memory compaction** — background threading + prompt caching for long conversations
- **Programmatic tool calling (PTC)** — letting Claude write code that calls tools programmatically

Older foundational entries cover RAG, tool use, structured JSON extraction, batch processing, extended thinking, and prompt caching.

## Assessment

This is the single most authoritative reference for Claude API development patterns. Every cookbook entry includes runnable code (Jupyter notebooks), is authored by Anthropic engineers, and covers real production patterns. The agent-related entries (managed agents, Agent SDK, orchestration patterns) are directly relevant to our toolkit's architecture.

Key high-value entries for this project:
- Context engineering guide — directly informs how we manage long agent sessions
- Async multi-agent orchestration — patterns applicable to kb dispatch and workflow orchestration
- Outcomes (verify-your-work) — aligns with our verification-before-completion skill
- Knowledge graph construction — relevant to kb graph development

## What to adopt

- Bookmark as the primary reference when building or debugging Claude API features
- The agent pattern cookbooks are directly applicable design references
- Check for new entries when upgrading Claude API usage or exploring new features

## Security

Not applicable — first-party Anthropic documentation, no third-party code execution risk.