---
name: claude-code-dynamic-workflows
title: Claude Code Dynamic Workflows
url: "https://code.claude.com/docs/en/workflows"
category: reference
summary: "Anthropic docs page describing Claude Code's dynamic workflows feature, a JavaScript orchestration script that fans work out to many subagents in the background"
tags: [claude-code, workflows, orchestration, subagents, documentation]
reviewed: 2026-09-16
acquired: 2026-09-16
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it says

A dynamic workflow is a JavaScript script that orchestrates many subagents at once. Claude writes the script for a described task, and a runtime executes it in the background while the interactive session stays responsive. The doc contrasts four primitives by "who holds the plan": subagents and skills keep the plan in Claude's turn-by-turn context, agent teams keep it with a lead agent supervising peer sessions, and workflows move the plan into a script whose variables hold intermediate state. Workflows scale to dozens-to-hundreds of agents per run versus a handful for agent teams or a few delegated tasks per turn for subagents.

The bundled `/deep-research` workflow fans out web searches across several angles, cross-checks sources, votes on claims, and returns one cited report. Workflows can be requested explicitly (the `ultracode` keyword in a prompt, or in the user's own words) or triggered automatically for every substantive task by setting `/effort ultracode` (Claude Code v2.1.203+, xhigh reasoning effort). A run's phases, agent counts, tokens, and elapsed time are viewable and controllable (pause/resume/stop/restart) via `/workflows`. Approval prompts before a run depend on permission mode (Auto, Manual/accept-edits, Bypass); `claude -p` and the Agent SDK never show the prompt and instead route the launch through the same permission evaluation as other tool calls.

Scripts hold `agent()`, `pipeline()`, and `parallel()` calls plus `phase()` and `log()`; a `meta` block (name, description) must stay a plain object literal or the workflow drops from `/` autocomplete. Agents in the same run can share prompt cache when they match on model, effort, agent type, tools, output schema, and working directory; workflow-agent cache TTL defaults to 5 minutes (extendable to 1 hour via `subagentPromptCacheTtl`). Documented limits: up to 16 concurrent agents (fewer under CPU constraints), up to 4,096 items per `parallel()`/`pipeline()` call, and 1,000 agents total per run. Runs are resumable within a session; completed agents replay from saved results, failed or still-running agents rerun, and a failure mid-fan-out reruns every agent that started after it. When an agent hits a claude.ai usage limit, the run pauses and resumes after reset (up to twice) rather than failing, under specific conditions (interactive session, `autoContinueAtUsageLimit` on, reset within 24h). Saved workflows live in `.claude/workflows/` (project, shared) or `~/.claude/workflows/` (personal) and can be distributed via plugins, namespaced as `/<plugin-name>:<workflow-name>`. A size guideline setting (`unrestricted`/`small`/`medium`/`large`) advises Claude on target agent count; a "Large workflow" warning shows above 25 agents or 1.5M projected tokens. Workflows can be disabled per-user (`/config`, `disableWorkflows` setting, `CLAUDE_CODE_DISABLE_WORKFLOWS=1`) or org-wide via managed settings.

## Key takeaways

- Workflows are a distinct orchestration primitive from subagents, skills, and agent teams: the runtime, not Claude's turn-by-turn context, holds the plan and intermediate results, enabling much larger fan-out (up to 1,000 agents/run, 16 concurrent).
- `/deep-research` is the only bundled workflow; custom workflows are authored by asking Claude to write one (optionally via the `ultracode` keyword or `/effort ultracode`), then saved as a reusable `/<name>` command.
- Approval and permission handling differs by surface: interactive CLI shows an approval prompt (mode-dependent), while `claude -p` and the Agent SDK evaluate the `Workflow` tool call under normal permission rules (allow rules, auto-classifier, bypass mode, or a `PreToolUse` hook) with no prompt shown.
- Concrete numeric limits are documented: 16 concurrent agents, 4,096 items per `parallel()`/`pipeline()` call, 1,000 agents total per run, 25-agent/1.5M-token thresholds for the "Large workflow" warning.
- Cost is a first-class concern in the docs: runs count toward plan usage/rate limits, token usage is visible per agent in `/workflows`, and a size guideline (`small`/`medium`/`large`/`unrestricted`) can bound how many agents Claude aims to spawn.

## What to adopt

Not applicable — this is a documentation/reference entry describing a first-party Claude Code feature, not a third-party tool being evaluated for adoption.

## Security

The doc documents the permission model rather than raw scanner findings. Key points as stated in the source: the workflow's script body itself has "no direct filesystem or shell access" — only the agents it spawns read, write, and run commands, and those agents use the invoking session's existing permission rules. In `claude -p`/Agent SDK contexts, a `Workflow` tool call is evaluated like any other tool call (deny/ask rules, auto-classifier, bypass mode, `PreToolUse` hook, or a host's `--permission-prompt-tool`/`canUseTool` callback), so a misconfigured allow rule (e.g., a blanket `Workflow` allow) approves every workflow without further prompting. The doc also notes that in auto permission mode a classifier can block an individual `agent()` call before the subagent starts (surfaced in the run's progress view), and that saving a workflow performs a symlink check on the target location before writing, refusing to write through a symlinked `.claude`, `.claude/workflows`, or target file in the project location (checked only on the target file itself in the personal `~/.claude/workflows/` location, to remain compatible with dotfiles-managed home directories); versions before v2.1.216 followed the link, which could place the saved file outside the intended directory. No security_flags are set because the doc reports these as documented platform behaviors, not vulnerabilities found through independent testing.
