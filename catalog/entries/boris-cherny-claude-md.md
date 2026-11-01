---
name: boris-cherny-claude-md
title: "Boris Cherny's CLAUDE.md"
url: "https://gist.github.com/hqman/e29cb6386c539d795767e8c3fd2c959b"
category: agent-pattern
summary: "A widely-shared CLAUDE.md (attributed to Boris Cherny) codifying a Claude Code operating discipline: plan-mode-by-default, liberal subagent use, a self-improvement lessons loop, verification-before-done, demanding elegance, and autonomous bug fixing, plus a tasks/todo.md + tasks/lessons.md task-management convention."
tags: [claude-md, workflow, agent-configuration, plan-mode, subagents, verification, claude-code]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: [creating-claude-md]
security_flags: []
source: unknown
---

## What it is

This GitHub gist is a CLAUDE.md configuration, presented as "Boris Cherny's CLAUDE.md," that encodes a set of operating rules for driving Claude Code. It is a reusable technique/configuration artifact rather than a tool. Its content is organized in three parts:

**Workflow Orchestration**
1. *Plan Node Default* — enter plan mode for any non-trivial task (3+ steps / architectural decisions); stop and re-plan when something goes sideways; write detailed specs upfront.
2. *Subagent Strategy* — use subagents liberally to keep the main context clean; offload research/exploration/parallel analysis; one task per subagent.
3. *Self-Improvement Loop* — after any user correction, record the pattern in `tasks/lessons.md` and write rules to prevent repeats; review lessons at session start.
4. *Verification Before Done* — never mark a task complete without proving it works (run tests, check logs, diff behavior).
5. *Demand Elegance (Balanced)* — for non-trivial changes, pause and ask whether there's a more elegant approach; skip for simple fixes.
6. *Autonomous Bug Fixing* — given a bug report, just fix it from logs/errors/failing tests without hand-holding.

**Task Management** — plan into `tasks/todo.md` with checkable items, verify the plan before implementing, track progress, explain changes, document a review section, and capture lessons in `tasks/lessons.md`.

**Core Principles** — simplicity first, no laziness / find root causes, minimal-impact changes.

## Mechanical details

- **Use:** copy the rules into a project or global `CLAUDE.md` (or `~/.claude/CLAUDE.md`) to adopt the discipline; it references `tasks/todo.md` and `tasks/lessons.md` files the agent maintains
- Format: plain Markdown instructions, framework-agnostic within Claude Code
- Attribution to Boris Cherny is as presented on the gist and is not independently verified here

## Security

No license is stated on the gist. The content is prose instructions for an agent's workflow and contains no executable code. Adopting it changes how an agent plans, delegates to subagents, and self-modifies its own `lessons.md` rules — review those behaviors before enabling in an autonomous setup.
