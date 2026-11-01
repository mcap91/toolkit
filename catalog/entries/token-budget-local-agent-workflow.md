---
name: token-budget-local-agent-workflow
title: Token-Budget Workflow for Small-Context Local Coding Agents
category: agent-pattern
summary: "Practitioner workflow for making a heavily quantized local LLM (32K-65K context) usable as a coding agent despite its narrow context window and higher error rate: (1) pick a harness with a small startup token footprint (author reports Pi needs ~1.5K tokens vs. an estimated 10-14K for Codex/Claude Code, leaving more of a 64K window for actual work) instead of a heavier, feature-rich harness; (2) split every task into a planning turn that writes plan.md, then clear the session (Pi's /new) and run a separate implementation turn that reads plan.md and records results in it, so neither turn needs the whole task history in context; (3) for plans too large for one implementation turn, delegate via a subtask-runner skill (subtask4llm) that executes up to 10 subtasks sequentially in fresh, isolated agent contexts, feeding results back to the coordinating instance; (4) compensate for the model's lower quality at low-bit quantization by enforcing hard constraints in AGENTS.md — a 300-500 line file-size ceiling, one responsibility per module, mandatory unit tests for every function/change, tests-and-build must pass before done, no commits without explicit user request — which the author attributes to a remark by Robert Martin (Uncle Bob, author of Clean Code) that he has stopped reading AI-generated code, substituting enforced constraints for manual review and spending free local-GPU iterations letting the model self-correct against those constraints."
tags:
  - agent-pattern
  - local-llm
  - context-management
  - plan-md
  - agents-md
  - token-budget
  - task-decomposition
  - pi-coding-agent
reviewed: 2026-10-30
acquired: 2026-10-30
license: ""
security_flags: []
overlaps:
  - local-model-harness-patterns
  - pi-coding-agent
  - subtask4llm
source_url: https://www.reddit.com/r/LocalLLM/comments/1xgqyz4/125_tokens_per_second_on_an_rtx_4070_ti_super_how/
source: reddit
---

## What it says

A practitioner running a heavily quantized (UD-Q2_K_XL) 35B MoE coding model on a single 16GB consumer GPU (RTX 4070 Ti SUPER) at a 65,536-token context window describes a four-part workflow to keep the agent usable despite that narrow window and the extra mistakes a 2-bit quant makes.

## Key takeaways

- **Harness choice drives usable context.** The author avoids "heavy" coding agents (named: Codex, Claude Code), reporting they consume 10-14K tokens on the system prompt and surrounding scaffolding alone — 15-20% of a 65K window before any work starts — and that large system instructions distract an already-fragile local model further. They use Pi Coding Agent instead, reporting it needs about 1.5K tokens to start, roughly 10x less.
- **Two-phase plan/implement split per task.** Rather than asking the agent to make a large change directly, the author starts a fresh session (`/new`) and has the agent write a `plan.md` describing the change. For tasks small enough to fit, they then clear context again and run a second session that implements from `plan.md` and records results in it when done — so each turn's context holds only one phase, not both.
- **Subtask delegation for large plans.** When a `plan.md` is too large for one implementation turn, the author uses their own skill, `subtask4llm`, which breaks the plan into up to 10 subtasks run sequentially, each in a separate agent instance that receives only what's relevant to that subtask; results flow back to the main Pi instance, which handles coordination, planning, and checking, without filling its own context.
- **AGENTS.md constraints as a substitute for manual code review.** To offset the lower quality of a 2-bit quantized model, the author enforces constraints via AGENTS.md: a 300-500 line ceiling per file (split if exceeded, but not at the cost of logical cohesion), one cohesive responsibility per module, mandatory unit tests for every function and for every change/bugfix, a requirement that tests and build pass without warnings before submission (with an explicit instruction not to weaken or delete tests to pass them), and a rule never to commit without a direct user request. They attribute the idea to a remark by Robert Martin (Uncle Bob, author of Clean Code) that he has stopped reading AI-generated code — tight constraints substitute for that reading, and since local-GPU inference is free, extra correction iterations are affordable.

## Security

n/a — community workflow description, no code artifact of its own. Depends on the harness (Pi Coding Agent), skill (subtask4llm), and local model/quantization choices the author names, each covered under their own catalog entries where applicable.
