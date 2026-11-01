---
name: adeptly
title: Adeptly
url: "https://github.com/ShopDevX/adeptlydev"
category: cli-tool
summary: "Plan-first companion GUI for Claude Code — drafts structured plans with inline Claude Code feature recommendations (subagents, skills, hooks, MCP, plan mode), scores feature coverage and token hygiene, then optionally executes plans as a role pipeline (Architect→Builder→Medic→Reviewer→Security→Pilot) via headless claude CLI; local-first Next.js app, MIT"
tags: [claude-code, planning, orchestration, crew, subagents, skills, hooks, feature-discovery, local-first, next-js]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

Adeptly is a local web UI (Next.js on localhost:3000) that sits upstream of Claude Code implementation. Given a natural-language task description, it uses the local `claude --print` CLI to draft a structured plan (problem, approach, files to change, Mermaid diagrams, risks, approval status) with specific Claude Code features named inline — subagents, skills, hooks, MCP servers, plan mode, /security-review, auto-memory — annotated with hover tooltips explaining when and why to use each.

Key capabilities as of v0.7:

- **Feature Coverage scoring**: measures how many of Claude Code's 30+ features a plan uses, surfaces missing high-value ones with one-click additions.
- **Token Hygiene scoring**: rates plan efficiency against cost-saving habits (Plan Mode first, Explore subagent for search, /clear between tasks, cache-friendly ordering, Haiku for mechanical work).
- **Recipe generation**: structured workflow output — subagent allocation, skills with when-to-invoke, hooks to wire, expected turns and cost estimate.
- **Crew runner**: executes the approved plan as a role pipeline — Architect (read-only code mapping) → Approval Gate → Builder (branch + implement) → Medic (build/test + self-heal) → Reviewer + Security (diff review) → Pilot (commit, push, PR). Dry-run by default; live runs require plan approval + `ADEPTLY_LIVE=1`.
- **Usage ledger**: records token/cost receipts to `.adeptly/usage.jsonl` with cache-hit % and cost-by-model breakdowns.
- **Multi-developer workflow**: plans are markdown files in `docs/plans/` tracked in git. Approvals in JSON alongside. No backend, no accounts.
- **CLI feature refresh**: asks the local `claude` CLI what features exist, avoiding stale built-in catalogues.

## Mechanical details

Requires Node 18.17+ and Claude Code CLI on PATH. Plans stored as `docs/plans/<slug>.md`, recipes in `docs/plans/recipes/`, crew run logs in `docs/plans/runs/<slug>/` as JSON + append-only `audit.jsonl`. The `.adeptly/` directory is gitignored. Supports voice input (Web Speech API push-to-talk), image/file upload via paste, dark/light themes, command palette (Cmd+K), and focus mode.

No code leaves the machine except through the user's own `claude` CLI subprocess, which sends prompts to Anthropic exactly as a normal Claude Code session would. Adeptly holds no API keys and opens no outbound connections of its own.

## Security

MIT licensed. No security flags — the tool is a thin local GUI over the user's existing `claude` CLI. No new trust surface beyond what Claude Code already requires. No telemetry, analytics, or accounts. Crew live-runs are double-gated (plan approval + env var). All execution is auditable via the run log files.

## How to use it

npx adeptly
