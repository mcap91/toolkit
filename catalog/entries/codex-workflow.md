---
name: codex-workflow
title: Codex Workflow (viettran-edgeAI)
url: "https://github.com/viettran-edgeAI/codex_workflow"
category: agent-pattern
summary: "Multi-agent orchestration architecture for Codex/Claude Code optimizing token usage within plan limits — 7 specialized roles (Main Agent, Companion/Luna, Investigator, Default Executor/Luna max, Senior Executor/Sol, Tester, Archivist) with fine-tuned batching, knowledge distribution via task-completion guides, and built-in per-agent token reporting; Sol xhigh ran 4h22m at 90% of 5h limit vs Astra at 260%; MIT"
tags: [orchestration, multi-agent, codex, token-optimization, roles, subagents, sol, astra]
reviewed: 2026-09-14
acquired: 2026-09-14
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

A multi-agent orchestration architecture for Codex (and adaptable to Claude Code) that optimizes token usage to run complex tasks within plan time/token limits. Developed through hundreds of trials over months of iteration.

**7 specialized roles**:

| Role | Model | Responsibility | Qty |
|---|---|---|---|
| Main Agent | session-selected | Primary orchestrator, high-level decisions, knowledge distribution | 1 |
| Companion | Luna xhigh | Persistent secretary — reduces context pressure by handling supporting context, organizing info, consolidating reports | 1 |
| Investigator | Luna xhigh | Research specialist — searches for evidence, documentation, prior art, including web | As needed |
| Default Executor | Luna max | Implementation worker — coding, modifications, integration | As needed |
| Senior Executor | Sol medium | High-capability specialist for complex/high-impact work (algorithms, architecture) | 1 max |
| Tester | Luna max | Independent verification — designs/runs tests, validates requirements | As needed |
| Archivist | Luna xhigh | Documentation, Git handoff, end-of-deployment token report | 1 per deployment |

**Key design principles**:
- Flexibility: provides resources and guidance without forcing rigid process
- Knowledge distribution: each task package includes a task-completion guide
- Batching guidelines prevent excessive main agent rollout
- Addresses the problem of main agent waking workers too often
- Built-in end-of-session token statistics per agent

**Benchmark** (comprehensive OCR + AI chatbot upgrade on Jetson Orin Nano):
- Sol xhigh: 4h22m runtime, 90% of 5h limit, 15% weekly limit, 6.2% uncached tokens, 60% cost share
- Astra: 2h30m runtime, 260% of 5h limit, 43% weekly limit, 14.2% uncached tokens, 88% cost share
- Conclusion: Sol is more comprehensive with better verification; Astra finds core problems better but costs 4–7x more

## Security

No security concerns — this is an orchestration pattern and AGENTS.md configuration, not executable infrastructure.