---
name: socratic
title: Socratic
url: "https://github.com/m4vic/socratic"
category: skill
summary: "Self-interrogation skill packaging 697 engineering questions across 15 domains — agent silently works through relevant questions, reads codebase, applies defaults, and only escalates genuine authority decisions to user; Core (90 questions) and Full (697) modes; knowledge-backed packs for specialist depth; MIT"
tags: [self-interrogation, engineering-review, requirements, pre-implementation, questions, planning, verification, multi-domain]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [superpowers-brainstorming, advise-project-approach]
license: MIT
security_flags: []
source: unknown
---

## What it does

Socratic is a self-interrogation skill for AI coding agents. It packages 697 questions across 15 engineering domains (requirements, frontend, backend, data, API design, security, infrastructure, testing, observability, AI/LLM, mobile, product/UX, cost/performance, compliance, team/maintenance) into a reasoning loop the agent runs silently before writing code.

The agent classifies the task, detects relevant domains via signal words (e.g., "auth" → Security, "database" → Data), loads the smallest useful question set, self-answers by reading the codebase and applying engineering defaults, then surfaces only assumptions, risks, and the few genuinely open questions (ideally 0-3) that require human authority (budget, vendor, legal risk, irreversible calls).

Two depth modes:

- **Core** (default): Top ~90 highest-signal questions. For prototypes, internal tools, one-off builds, day-to-day tasks.
- **Full**: Complete 697-question bank. For production systems, public APIs, auth, payments, PII, regulated data, deep audits.

**Knowledge-backed packs** add specialist depth after domain selection: software design (complexity, interfaces), data systems (distributed data, reliability), threat modeling (trust boundaries, abuse paths), AI engineering (LLM eval, retrieval, cost). Packs are compressed decision patterns from engineering books — what to ask, default answers, tradeoffs, common mistakes, escalation conditions, verification steps.

Domain selection is dynamic — can grow mid-build as the agent discovers new requirements (e.g., finding an unexpected persistent store adds the Data domain). Testing and Requirements domains are always included.

## Mechanical details

Install as Claude Code skill (`~/.claude/skills/socratic/`), Codex skill (`~/.codex/skills/`), or paste `PROMPT.md` into any LLM system prompt. `PROMPT_LITE.md` for minimal always-on overhead. MIT licensed. Extend by adding `questions/15-yourdomain.md` files and signal-table rows.

Interactive mode (one question at a time) is opt-in — user says "interview me" to switch from silent self-interrogation.

## Security

MIT licensed. No security flags. The skill is a prompt file — no code execution, no network calls, no credential handling. The question bank runs entirely within the agent's existing context.

## How to use it

cp -r socratic ~/.claude/skills/
