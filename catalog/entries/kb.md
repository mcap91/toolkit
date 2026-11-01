---
name: kb
title: kb (Repo-Local Wiki + Agent Dispatch + Graph)
url: "https://github.com/mcap91/kb"
category: framework
summary: "Agent-facing toolkit providing a structured repo-local wiki (MCP + CLI), reviewed multi-agent dispatch with sandboxed launches and write-scope enforcement, and deterministic code-first graph extraction; runs from its own checkout and targets consuming repos via --dir; MCP servers for wiki (10 tools) and dispatch (9 tools); MIT"
tags: [wiki, dispatch, multi-agent, mcp-server, graph, knowledge-management, claude-code, codex, agent-infrastructure]
reviewed: 2026-07-15
acquired: 2026-07-15
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it says

An agent-facing toolkit with three subsystems, all operating from a single kb checkout targeting any number of consuming repos via `--dir`:

**Wiki** (MCP + CLI): Structured repo-local wiki with typed records (work items, decisions, issues, initiatives, areas, sources), ID allocation with prefix validation, managed CLAUDE.md/AGENTS.md blocks, generated views (catalog, now, inbox, backlog, archive), full-text search index, linting, and contract sync for template updates. Enforces wiki-first retrieval: agents must search the wiki before inspecting implementation files.

**Dispatch** (MCP + CLI): Reviewed multi-agent handoff system. Operator creates durable handoff documents specifying title, subject, allowed agents, mode, work item, write scope, and required reading. Review snapshots inputs into an agent-visible bundle. Launch runs the agent from the reviewed bundle, not the live repo root. Claude non-redteam launches honor reviewed write scope by deriving directory-granularity `--add-dir` access. Host capability probing via `check-environment` ensures sandbox requirements are met before launch.

**Graph** (CLI only): Deterministic code-first graph extraction producing `.graph.json` and `graph-summary.md` in the consuming repo's wiki directory.

### Architecture

- kb is the tooling repo; consuming repos are separate
- MCP servers (wiki + dispatch) run from the kb checkout as stdio processes
- Every tool call includes `dir` pointing at the target consuming repo
- Bootstrap writes `.mcp.json` (Claude) or emits `codex mcp add` commands (Codex) with resolved absolute paths
- `sync-contract` maintains managed blocks between markers in consuming repos' CLAUDE.md/AGENTS.md without touching user content outside markers
- Self-hosting supported: kb can target its own checkout as the consuming repo
- Dual-commit model: code changes (public repo) and wiki changes (private repo) are committed separately

### Installation

Clone as a sibling repo, `npm install`, then bootstrap each consuming repo. MCP servers are not persistent daemons — they must be restarted after VM reboot or shell restart. Recommended: configure the agent client to launch MCP server commands on session start.

## Key takeaways

- Wiki-first retrieval is a design constraint, not a suggestion — agents must search the wiki before using grep/glob on implementation files
- Dispatch provides a review gate: handoffs are reviewed before launch, write scope is enforced per agent, and the agent runs from a snapshot rather than the live repo
- The `--dir` architecture means one kb installation serves any number of consuming repos
- Windows-compatible: forward-slash paths in JSON, `.cmd` shims for PowerShell execution policy issues
- HO-* handoff records are dispatch-owned and excluded from wiki scanning operations

## Security

MIT licensed. Dispatch enforces write-scope restrictions on launched agents. Review snapshots isolate agent-visible files from the live repo. Host capability probing prevents launching agents in environments that can't satisfy sandbox requirements. No network calls beyond git operations.