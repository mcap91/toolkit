---
name: agent-software-engineering-fundamentals
title: Software Engineering Fundamentals for AI Agents (schema-first memory, deterministic guardrails)
url: https://www.reddit.com/r/AI_Agents/comments/1x6bwg9/is_anyone_else_noticing_that_people_building_ai/
category: agent-pattern
summary: Practitioner discussion arguing most agent memory, prompt-injection, and goal-hijacking problems are solved by pre-LLM software-engineering basics — design the memory data model first (what is stored, how it changes behavior, TTL and scope) instead of free-text dumps; treat LLM output as untrusted input validated against schemas; model the agent as a workflow (defined state + allowed transitions, model proposes moves that code checks); least-privilege scoped credentials, tool allowlists, process/data isolation, audit logs; reserve human approval for irreversible or boundary-crossing actions and show the exact payload to avoid approval fatigue
tags:
  - agent-architecture
  - agent-memory
  - guardrails
  - prompt-injection
  - schema-validation
  - least-privilege
  - human-in-the-loop
  - workflow-state-machine
  - software-engineering
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - agent-first-architecture
  - harness-engineering
  - agent-identity-borrowed-credentials
  - governance-first-multi-agent-architecture
license: N/A
security_flags: []
source: unknown
---

## What it does

Captures a recurring argument from an r/AI_Agents thread (Oct 2026): agent builders are re-encountering problems that conventional software engineering already solved, and the fixes transfer directly.

Techniques raised in the post and replies:

- **Schema-first memory.** Before storing anything, answer: what should change in the agent's behavior because of this memory, and how long is it valid? Without a data model, everything becomes free text, which invites injection and stale facts. TTL and scope matter as much as content. "Memory without a retrieval strategy is just noise."
- **Inherited notes are claims, not facts.** An AI-agent commenter describes five consecutive sessions repeating one wrong diagnosis because each read the previous session's note; their fix is a gate that marks an inherited claim unverified unless the current session ran a command against the thing the claim is about. Memory doesn't expire; permission to act on it without re-checking does.
- **Agent as workflow.** Define state and allowed transitions; let the model propose moves that code validates. Where an agent is one step in an existing workflow, use structured JSON in/out like any service API rather than a free-form user-facing agent doing parsing, decisions, business logic, and response writing.
- **Untrusted input.** Treat LLM output and tool content as untrusted channels with strict schema validation and backend permission checks before relying on prompt guardrails.
- **Least privilege and isolation.** Scoped per-agent credentials, short-lived tokens, tool allowlists, isolation so one agent cannot touch another's data, and logs an auditor could read.
- **Human-in-the-loop placement.** Require approval for actions the system can't undo or that cross a boundary (external messages, payments, deletes/overwrites, permission changes, production). Let reads, drafts, searches and internal updates auto-run once deterministic checks pass. Show the exact payload or diff in the approval prompt and batch low-risk actions; approval prompts with no payload produce fatigue and rubber-stamping. Blast radius, not tool name, is the criterion.
- **Business rules in code, not prompts.** Rules duplicated across prompts/skills "hoping the LLM will listen" expand blast radius; keep probabilistic behavior only where it is needed.

## Usage notes

- One replier (co-founder of an agent-guardrails vendor, disclosed) lists the shippable minimum as scoped credentials per agent, a tool allowlist, inter-agent data isolation, and auditor-grade logs.

## Security

Discussion content, no code. The patterns are defensive (injection resistance, least privilege, approval design).
