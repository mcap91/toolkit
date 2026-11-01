---
name: atomic-claude
title: Atomic Claude
url: https://github.com/damusix/atomic-claude
source_url: https://www.instagram.com/reel/DeNJmVuDpx_/
source: instagram
category: plugin
summary: "Opinionated Claude Code configuration bundle that replaces per-session repo re-discovery with a standing local code graph and wiki: a tree-sitter symbol graph (31 languages, 23 web frameworks, no compiler) indexes functions/types/imports/calls plus SQL lineage (Postgres/MySQL/T-SQL/Snowflake, dbt models) into a local SQLite file, answering callers/call-sites/blast-radius as file:line instead of grep text matches; layers an /autopilot plan→implement→review→ship loop (fresh-context implementer/reviewer split, tests-first, blast-radius check before edits), a self-maintaining repo/realm wiki, a self-sharpening config (/retrospective-learning), and an inter-session message bus. Free, fully local — no server, no account, nothing uploaded; ships as one static binary. MIT."
tags:
  - claude-code
  - code-graph
  - tree-sitter
  - symbol-graph
  - sql-lineage
  - agent-workflow
  - wiki
  - mcp
  - static-binary
  - open-source
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags: []
overlaps: []
---

## What it does

A standing local index that replaces the repeated per-session cost of an AI coding agent re-discovering a codebase from scratch (grepping for a symbol's name, opening files to find callers, guessing the build command). Running `atomic code index` parses every file with tree-sitter compiled to WebAssembly (one static binary, no system dependencies) and writes a symbol graph — every function, type, import, and call between them, across 31 languages and 23 web frameworks — into a SQLite file inside the repo. Re-running the index only reparses changed files. Three graph queries (callers, callees, impact) then answer with a file:line from the parse itself rather than a list of text matches sharing a name.

**SQL as code:** indexes `.sql` files statically (never connects to a live database) — stored-procedure lineage down to the column (including temp tables), dbt models/macros, and Snowflake tasks — and also extracts SQL written as strings inside application code across 20 languages, placing it in the same graph. Supports Postgres, MySQL, T-SQL, and Snowflake dialects.

**Workflow layer on top of the graph:** `/autopilot` takes an issue to a merged PR unattended (plan → implement with tests-first → fresh-context review that cannot inherit the implementer's reasoning → ship), checking the graph for blast radius before each edit. `/setup-wiki` and `/refresh-wiki` maintain a standing repo wiki (build command, layout, domain map) and an optional cross-repo "realm" wiki, loaded automatically at session start so Claude doesn't re-learn the repo every session. Other components: `/retrospective-learning` (mines corrections to edit the config's own skills/rules, only with operator approval), an inter-session message bus for concurrent Claude Code sessions to coordinate over named rooms, and persistent named Python/Node REPL sessions that hold state across separate Bash calls.

**Distribution:** one install, fully local — no server, no account, nothing uploaded. MIT license.

## Sources

- [atomic-claude — GitHub README](https://github.com/damusix/atomic-claude) — feature table, workflow commands, wiki architecture, license (fetched directly).

## Security

MIT, open source. README states the code graph and SQL indexing are purely static/local with no network calls, no server, and no account — reducing the usual self-hosted-tool data-exfiltration surface to what the bundled commands/scripts themselves do inside the agent's existing filesystem/shell access. Single-maintainer repo (damusix); no independent CVE or supply-chain audit found at review time.
