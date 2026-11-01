---
name: claude-code-setup-plugin
title: Claude Code Setup Plugin
url: "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup"
category: plugin
summary: "Official Anthropic plugin that scans a codebase and recommends tailored Claude Code automations — top 1-2 recommendations per category (MCP servers, skills, hooks, subagents, slash commands); read-only analysis, no file modifications"
tags: [claude-code-plugin, setup, automation, anthropic-official]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [dotclaude]
source: unknown
---

## What it does

Official Anthropic Claude Code plugin that analyzes a codebase and recommends the top 1–2 automations in each of five categories:

1. **MCP Servers** — external integrations (e.g., context7 for docs, Playwright for frontend)
2. **Skills** — packaged expertise (e.g., Plan agent, frontend-design)
3. **Hooks** — automatic actions (e.g., auto-format, auto-lint, block sensitive files)
4. **Subagents** — specialized reviewers (e.g., security, performance, accessibility)
5. **Slash Commands** — quick workflows (e.g., /test, /pr-review, /explain)

Read-only — analyzes but does not modify files.

## Differentiators

- **Official Anthropic authorship** (Isabella He, isabella@anthropic.com)
- Part of the `anthropics/claude-plugins-official` repository
- Codebase-aware recommendations rather than generic setup templates

## Mechanical details / What to adopt

Invoked via natural language: "recommend automations for this project", "help me set up Claude Code", "what hooks should I use?"

## Security

Part of Anthropic's official plugin repository. Read-only — no file modifications. License not explicitly stated in the plugin directory (inherits from parent repo).