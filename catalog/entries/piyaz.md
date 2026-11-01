---
name: piyaz
title: Piyaz
url: "https://github.com/FrkAk/piyaz/"
category: framework
summary: "Agentic workspace where people and AI coding agents collaborate on projects — context network with dependency-graph task management, 6 MCP tools, end-to-end composer orchestration (Claude Code), plugins for Codex/Cursor/Antigravity; hosted + self-hostable, AGPL-3.0"
tags: [project-management, agent-workspace, context-network, task-graph, mcp, multi-agent, claude-code]
reviewed: 2026-06-23
acquired: 2026-06-23
license: AGPL-3.0-only
security_flags: [copyleft-license, cloud-hosted-default, oauth-required]
overlaps: [openclaw]
source: unknown
---

## What it does

Piyaz is a project management + context delivery system designed for AI coding agents. Instead of briefing agents with manual context, Piyaz maintains a live knowledge graph of tasks, dependencies, decisions, and execution records, then delivers the right context shape for each task's current stage.

**Core components:**
- **6 MCP tools**: `piyaz_project`, `piyaz_task`, `piyaz_edge`, `piyaz_query`, `piyaz_context`, `piyaz_analyze`
- **Context retrieval interface**: Four shapes optimized for U-shaped LLM attention — `summary` (quick lookup), `working` (refining/reviewing), `planning` (writing impl plans), `agent` (coding the task)
- **4 workflow skills**: Brainstorm (shape ideas), Onboarding (reverse-engineer existing codebase into task graph), Decompose (break brief into dependency graph), Manage (CTO-mode review/rebalancing)

**Claude Code extras:**
- **/piyaz:composer**: End-to-end task orchestrator — picks highest-value ready task, drives through research → plan → implement → review via per-phase subagents, merges PR when authorized, loops until queue empty
- **Composer subagents**: Researcher, planner, implementer, reviewer — each in clean per-phase context
- **Decompose-task / decompose-feature agents**: Split oversize tasks or add feature clusters

**Multi-platform**: Plugins for Claude Code, Codex, Cursor, and Antigravity (Gemini CLI successor). All share 6 MCP tools + 4 workflows + /piyaz skill.

**Hosting**: Hosted at app.piyaz.ai (OAuth sign-in) or self-hostable (Bun + PostgreSQL, AGPL-3.0).

## Assessment

The most ambitious agent workspace in this catalog. The context-shape concept (summary/working/planning/agent) is well-designed — delivering different context bundles based on task stage solves the "agent needs briefing" problem. The U-shaped attention optimization (highest-recall content at start and end of context) reflects real LLM attention patterns.

The composer orchestration (Claude Code only) is genuinely end-to-end: pick task → research → plan → implement → PR → review loop → merge → next task. This is the closest thing to autonomous project completion available as open source.

Tradeoffs: AGPL-3.0 copyleft, hosted version requires OAuth, Claude Code composer depends on subagent dispatch (not available on other platforms yet). The task graph approach adds overhead for small projects but becomes valuable for anything with >10 tasks and dependency chains. Overlaps with our kb wiki + dispatch system but takes a different architectural approach (centralized graph server vs file-based wiki).

## Mechanical details

```bash
# Claude Code (hosted)
claude plugin marketplace add FrkAk/piyaz
claude plugin install piyaz@piyaz
# then /mcp → select piyaz → browser sign-in

# Self-hosted
git clone git@github.com:FrkAk/piyaz.git && cd piyaz
bun install --production
cp .env.local.example .env.local  # fill in config
bun run db:setup && bun run build && bun run start
# Use piyaz-local MCP server pointing at localhost:3000
```

Stack: Next.js 16, TypeScript 6, React 19, PostgreSQL, Drizzle ORM, Tailwind CSS v4, Motion.

## Security

- **License**: AGPL-3.0 — copyleft; commercial license also available
- **Auth**: OAuth for hosted version; self-hosted controls its own auth
- **Data**: Hosted version stores project data on Piyaz servers; self-hosted keeps everything local
- **Supply chain**: Single primary contributor, growing community, CI-enforced plugin sync
- **MCP surface**: 6 tools with structured inputs — no arbitrary code execution
- **Composer**: Dispatches subagents with per-phase tool restrictions (Claude Code only)