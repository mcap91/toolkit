---
name: memoose
title: Memoose
url: "https://github.com/AndrewNgo-ini/memoose"
category: framework
summary: "Local, no-API-key dual-path memory system for coding agents — SQLite knowledge graph, CLI + 26 MCP tools + skills/hooks harness; procedures stored as self-evolving 'procedural graphs' (steps as nodes, edges carrying conditions/advice/pitfalls) after Google's Procedural Graphs paper (arXiv 2609.09153)"
tags: [memory, procedural-graph, knowledge-graph, mcp-server, cli-tool, sqlite, local-first, no-api-key, claude-code, hooks]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Apache-2.0
security_flags: [unverified-vendor-claims]
overlaps: [ai-memory-comparison, okf-agent-memory, mempalace, claude-mem]
source: unknown
---

## What it does

Memoose is a dual-path, local memory system for coding agents (author: AndrewNgo-ini), pairing a deterministic engine (SQLite-backed knowledge graph, a CLI, and 26 MCP tools) with a harness of skills, hooks, and a maintenance subagent. It stores two kinds of memory: factual/declarative memory (decisions, conventions, ownership facts, each carrying an evidence pointer to its source) and procedural memory, modeled explicitly as "procedural graphs" rather than a knowledge graph — following the framing in Google's paper "Procedural Graphs: Self-Evolving Execution Structures for LLM Agents" (arXiv 2609.09153, Lu/Chen/Wu/Arık; Google, Georgia Tech, Peking University). That paper argues knowledge graphs (entity-relation-entity triplets) suit "what is" questions but not "what to do" procedural knowledge, and proposes graphs of (procedure, relation, procedure) triplets instead: an online phase localizes the agent's active step and feeds its 2-hop neighborhood plus recent steps to a guidance model that injects step-level guidance, and an offline phase self-evolves the graph by having an LLM refiner contrast failed vs. successful trajectories and edit the graph's topology, validating edits against held-out performance.

In Memoose's implementation, a procedure is stored as a graph of step nodes; edges between steps carry a condition, advice, and a pitfall. At runtime the agent declares its current step, the engine surfaces the outgoing (2-hop) transitions, and the agent picks the next step. Each transition taken is tallied against its outcome, so repeated runs bias the graph toward what worked in practice — Memoose's stated mechanism for learning from real runs, which parallels but is simpler than the paper's offline LLM-refiner graph-editing step.

Separately from procedures, Memoose exposes two retrieval paths for memory generally: recall (explicit search, for a question the agent thought to ask) and recommendation (an automatic hint surfaced before each prompt, for what it didn't think to ask). `memoose maintain` periodically sweeps the store into a worklist that a small subagent judges (e.g., retiring stale facts) rather than doing so automatically.

## Differentiators

- No API key required and no persistent background service on the default CLI/skills install path — stated by the author as the reason for building it, in contrast to other memory libraries that require an embedding/extraction API key or run a service.
- Explicit split between factual memory (knowledge-graph style) and procedural memory (procedural-graph style, per the arXiv paper), rather than storing everything as flat text or vector blobs.
- The Procedural Graphs paper's authors published no accompanying code; Memoose is one of several independent implementations built from the paper text alone (others found during research: paulbruffett/agentic-procedural-graphs on LangGraph, preprint-labs/procedural-graphs with a FastMCP overlay, vikm2o/proceduralgraph).
- Reports Claude Haiku 4.5 at 90.4% accuracy on the LoCoMo benchmark (1,540 questions, 4,699 mean tokens/query) — a project-reported figure, not independently verified.

## Mechanical details

- Install: `pip install memoose` / `pipx install memoose` (Python 3.11+); Claude Code plugin via `/plugin marketplace add AndrewNgo-ini/memoose` then `/plugin install memoose@memoose`; skills+hooks via `memoose install claude` (also supports Codex, OpenCode, Cursor); optional MCP mode via `memoose install <host> --mcp` (requires `uv`, runs `uvx memoose serve`).
- For Claude Code, install registers hooks in `~/.claude/settings.json` and adds a maintenance agent under `~/.claude/agents/`; user-scoped by default, `--project` scopes it to one repository; uninstall reverses the changes.
- Storage: local SQLite at `~/.memoose/<dataset>.sqlite`, path configurable via `MEMOOSE_DATA_DIR`.
- CLI commands: `memoose remember` (store facts with evidence), `memoose recall` (search), `memoose guidance` (procedural next-step lookup), `memoose maintain` (upkeep worklist), `memoose view` (browser-based graph visualization), `memoose session` (working-session tracking).
- Optional extras: `fastembed` for local embeddings, `ontology` for full RDF/OWL parsing.
- 26 MCP tools exposed when running in MCP mode.
- ~49 GitHub stars, 6 forks, 38 commits at time of review (2026-09-25).

## Security

- License: Apache-2.0.
- No API key required for core operation; all data stored locally in SQLite. MCP mode is opt-in and requires `uv`.
- Claude Code integration modifies `~/.claude/settings.json` (hooks) and installs an agent file into `~/.claude/agents/`; these execute on session lifecycle events, so reviewing the installed hook/agent contents before adoption is warranted.
- Small/early-stage project by GitHub signals (49 stars, 6 forks, 38 commits); the public issue tracker shows at least one reported correctness bug (a retired fact still surfacing via `recall`'s chunking) and third-party usage (an attempted adebench integration), indicating some real external testing but limited maturity.
- The 90.4%/LoCoMo benchmark figure and other performance claims are self-reported by the project and not independently verified in this review.
