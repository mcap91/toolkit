---
name: software-factory-orchestration
title: Software Factory Orchestration (DAG-Based Dev Lifecycle Automation)
category: agent-pattern
summary: "Pattern for automating the full software development lifecycle with a deterministic workflow DAG — spec writing → ticket generation → per-ticket plan/execute/review → final code review — using coding agents as nodes and a workflow engine (n8n, Airflow, or custom bash/TS script) as the orchestrator; addresses opacity and steering problems of pure multi-agent approaches"
tags: [orchestration, workflow, dag, software-factory, dev-lifecycle, automation, pi, coding-agent, deterministic]
reviewed: 2026-09-25
acquired: 2026-09-25
license: N/A
security_flags: []
overlaps: [jive]
source: unknown
---

## What it does

Pattern for end-to-end software development automation where a deterministic orchestrator (workflow DAG, bash script, or TS script with Pi SDK) drives coding agents through the full lifecycle:

1. `pi -p /write-spec "$GOAL"` → human review/edit
2. `pi -p /write-tickets-for-spec @spec.md` → human review/edit
3. Per ticket: plan → execute → quick review/fix
4. Final `pi -p /code-review`

Key design choice: use a programmatic orchestrator (n8n, Airflow, custom code) rather than multi-agent conversation for steering. Addresses the "too loose, opaque and difficult to steer" problem of pure subagent delegation.

Discussion source: r/PiCodingAgent (Sep 2026). Practitioners evaluating both GUI workflow builders (n8n-like DAG editors with CLI/REST API) and code-first approaches (bash scripts, TS SDK).

## Assessment

The pattern maps cleanly to existing CI/CD infrastructure. The human-review gates between spec/ticket/code stages are the key differentiator from fully autonomous approaches — they're where steering actually happens.