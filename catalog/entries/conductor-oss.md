---
name: conductor-oss
title: Conductor OSS
url: "https://github.com/conductor-oss/conductor"
category: framework
summary: "Open-source durable execution platform (ex-Netflix) for microservices, AI agents, and adaptive workflow graphs — JSON-defined orchestration with durable state, native LLM tasks, MCP tool calling, human approval, dynamic fork/join, DO_WHILE loops, polyglot workers (Java/Python/Go/JS/C#/Ruby/Rust), 5 persistence backends, 6 message brokers; Claude Code plugin; Apache-2.0"
tags: [workflow-engine, durable-execution, orchestration, ai-agents, mcp, llm, microservices, java, polyglot, netflix, orkes]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

Conductor is a durable execution platform that separates orchestration (versioned JSON workflow graphs) from business logic (polyglot workers that poll, execute, and report). Originated at Netflix, maintained by Orkes and community. Every step is persisted — survives crashes, restarts, and network failures.

Key capabilities:

- **Durable adaptive graphs**: runtime-selected paths, bounded fan-out, tool calls, approvals, retries, cancellation, and recovery — all inspectable.
- **AI agent orchestration**: native `LLM_CHAT_COMPLETE` tasks, `LIST_MCP_TOOLS` / `CALL_MCP_TOOL` for MCP server integration, human approval gates, vector workflows for RAG, DO_WHILE loops for agent think-act cycles.
- **Dynamic at runtime**: dynamic forks, tasks, and sub-workflows resolved at runtime. LLMs can generate and modify workflow JSON — no compile/deploy cycle.
- **Execution recovery**: restart, rerun, retry, pause, resume, or terminate. Long-running workflows (days/weeks/months) with no in-memory state.
- **Polyglot workers**: Java, Python, Go, JavaScript, C#, Ruby (incubating), Rust (incubating). Workers are plain code — any language, library, or I/O.
- **Control flow**: SWITCH (branching), DO_WHILE (loops), FORK_JOIN (parallel), SUB_WORKFLOW (composition), DYNAMIC tasks.

## Mechanical details

Install via npm (`@conductor-oss/conductor-cli`), Docker, or build from source (Java 21+, Gradle). Server at localhost:8080, built-in ui-next UI. 5 persistence backends (Redis, Postgres, MySQL) × 6 message brokers. Workflow definitions versioned by number — running executions pinned to their version. Claude Code plugin available (`conductor-oss/conductor-skills`). Orkes offers enterprise SaaS with 100% API compatibility.

## Security

Apache-2.0 licensed. Self-hosted, no vendor lock-in. Workflow inputs validated against JSON Schema. Workers decoupled from orchestration — update graphs or swap implementations independently. No telemetry mentioned. Standard Java/Docker deployment trust model.