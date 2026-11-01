---
name: builderio-skills
title: Builder Skills (BuilderIO/skills)
url: "https://github.com/BuilderIO/skills"
category: plugin
summary: "Builder.io's pack of 15 composable agent skills (visual-plan, visual-recap, webmcp, agent-watchdog, plan-arbiter, efficient-fable, rewind, quick-recap, etc.) installable via npx @agent-native/skills across Claude Code, Codex, Cursor, Pi, OpenCode, and Copilot; doubles as a Claude Code / Cowork plugin marketplace; MIT, ~4.2k stars"
tags: [skills, claude-code, codex, cursor, plugin-marketplace, visual-plans, orchestration, mcp, agent-native, builder-io]
reviewed: 2026-09-10
acquired: 2026-09-10
license: MIT
security_flags: [hosted-service-default, screen-capture-integration]
overlaps: [agent-skills-osmani, awesome-claude-code]
source: unknown
---

## What it does

A collection of 15 small, composable skills for coding agents from Builder.io, published under the "Agent-Native" brand (agent-native.com). Installs via `npx @agent-native/skills@latest add` (interactive picker) into the shared `.agents` path used by Codex, Pi, Cursor, OpenCode, GitHub Copilot/VS Code, plus Claude Code's native skills path. The repo is also a Claude Code and Cowork plugin marketplace (`/plugin marketplace add BuilderIO/skills`).

The skills:

- `/an` — open and operate Agent-Native apps (e.g. Slides) beside the conversation via a Dispatch MCP server (`https://dispatch.agent-native.com/mcp`)
- `/webmcp` — open web apps in the host's built-in browser and prefer the page's MCP/WebMCP tools (`window.__agentNativeWebMcp`) over UI automation; one screen read, one smallest mutation, one readback
- `/visual-plan` — turn text plans into interactive MDX visual plans (diagrams, file maps, annotated code, open questions) viewed with the Agent-Native plans app; hosted links or local-files mode via a localhost bridge
- `/visual-recap` — turn a branch/commit/PR diff into an interactive visual recap (annotated diffs, diagrams, API/schema summaries, file maps); optional GitHub Action generates one per PR
- `/visual-edit` — open a running local app as URL-backed iframe screens for visual inspection and source-backed editing
- `/rewind` — recover recent local screen context (transcripts, OCR, frames) through the Clips Desktop app's `clips-screen-memory` MCP connection; macOS only, capture opt-in
- `/agent-watchdog` — audit another agent's work from a session transcript, PR, branch, or run summary
- `/plan-arbiter` — compare competing agent plans and output a decision memo (winning/hybrid plan, rejected alternatives, verification gates)
- `/plow-ahead` — proceed through ordinary ambiguity with conservative assumptions and a decision recap
- `/efficient-fable` / `/efficient-frontier` — reserve the expensive model (Claude Fable or any frontier model) for orchestration and judgment; delegate token-heavy research, coding, testing, and log reduction to cheaper agents
- `/stay-within-limits` — track 5-hour/weekly usage limits and pause at 95%
- `/quick-recap` — end every response with a green/yellow/red status block
- `/read-the-damn-docs` — web-search authoritative docs before guessing from stale model memory
- `/turn-into-app` — convert the current thread or a skill into a runnable Agent-Native app

## Differentiators

- Multi-host by design: one installer targets Claude Code, Codex, Cursor, Pi, OpenCode, and Copilot through the shared `.agents` path, with managed AGENTS.md/CLAUDE.md instruction blocks.
- Visual artifacts (plans/recaps) are MDX with custom components, viewable hosted or fully local — an unusual local-files escape hatch for a hosted-first product.
- Several skills wire into Builder.io hosted services (Dispatch MCP, plans app, Clips Desktop) rather than being self-contained prompt files.
- Explicit safety posture around `/rewind`: the plugin never installs capture software silently and treats Rewind as unavailable until `screen_memory_status` succeeds.

## Mechanical details

- Install: `npx @agent-native/skills@latest add` (picker), `--skill <name>` to skip, `--with-github-action` for PR recaps; plain copies via Vercel's `npx skills@latest add BuilderIO/skills --skill <name>` (but that path skips managed instruction blocks and the GitHub Action).
- Claude Code: `/plugin marketplace add BuilderIO/skills` then `/plugin install builder-skills@builder-skills`; skills namespaced as `/builder-skills:<name>`.
- Cowork: Customize > Plugins > Add marketplace > `BuilderIO/skills`.
- JavaScript, MIT, ~4.2k stars, 206 forks, created 2026-06, actively pushed (same-day commits at review time). Homepage: agent-native.com.

## Security

- **License:** MIT.
- `hosted-service-default` — `/an`, `/visual-plan`, and `/visual-recap` default to Builder's hosted services (Dispatch MCP at dispatch.agent-native.com, hosted plans database); plan/recap content leaves the machine unless local-files mode is chosen at install.
- `screen-capture-integration` — `/rewind` integrates with Clips Desktop screen recording; capture is opt-in, local-first, and the installer refuses to install it silently, but the skill's purpose is reading recorded screen memory.
- Backed by a known vendor (Builder.io) with an active org; installer modifies AGENTS.md/CLAUDE.md when the user opts in.