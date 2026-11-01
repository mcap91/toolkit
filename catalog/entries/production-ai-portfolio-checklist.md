---
name: production-ai-portfolio-checklist
title: Production AI Portfolio Checklist (What Senior Engineers Actually Look For)
category: reference
summary: "Community-sourced checklist from senior/lead AI engineers on what distinguishes a production-grade AI portfolio project from tutorial copies — eval sets built from real failures, p50/p95 latency and cost-per-successful-task metrics, idempotent tool calls, prompt versioning tied to eval runs, traces of failed runs, and a 'what went wrong' section; consensus recommendation: build one narrow-domain agent (#2 deterministic workflow) over a routing gateway (#1) or fine-tuning demo (#3)"
tags: [career, portfolio, production, evaluation, observability, agent-engineering, best-practices, hiring]
reviewed: 2026-09-25
acquired: 2026-09-25
license: N/A
security_flags: []
overlaps: []
source: unknown
---

## What it does

Synthesis of senior/lead AI engineer perspectives on what makes a portfolio project signal production competence (r/AI_Agents, Sep 2026).

**Green flags in a repo:**
- Eval set hand-built from real failures (not only synthetic), with before/after pass rates from actual changes
- Numbers: p50/p95 latency, cost per *successful* task (not per call), failure rate by step
- Timeouts, retries with backoff, idempotency on tool calls with side effects
- Prompts versioned and tied to eval runs (which change broke what)
- "What went wrong / what I'd change" README section
- Traces you can open — one screenshot of a failed run in Langfuse showing *why* it failed beats buzzwords

**Common gaps:**
- Evals that only test the happy path
- No story for partial failure (step 3 of 5 dies, now what?)
- Using an LLM for tasks a regex or SQL query handles (showing when *not* to call the model is a strong signal)
- Stacking 6 frameworks — one boring, well-understood stack reads as more senior

**Consensus recommendation:** Pick one narrow domain with messy inputs, build a deterministic agent workflow around it, bolt on cost/latency tracking, spend at least a third of time on evals and failure handling. Also suggested: build a quality MCP server with observability + security testing suite that runs in CI.

## Assessment

Directly applicable as a checklist when evaluating catalog entries for production-readiness signals, and as guidance for our own tooling quality bar.