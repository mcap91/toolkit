---
name: jive
title: Jive
url: "https://github.com/merijjeyn/jive"
category: framework
summary: "Terminal coding-agent harness (TypeScript/Bun) whose planner submits one DAG ('graph call') of bash and Jev-decision nodes per turn instead of one tool call at a time, executing the plan locally and returning to the LLM only when a node's accept predicate fails; author-published, single-run benchmarks across 6 tasks report a mean 2m31s/8.7k output tokens for Jive vs 12m12s/32.7k tokens for Claude Code and ~17m40s/16.2k tokens for Codex. MIT license, single contributor, repo created 2026-09-21."
tags: [coding-agent, terminal, cli-tool, dag, graph-execution, typescript, bun, decision-model, jev, benchmarks]
reviewed: 2026-09-25
acquired: 2026-09-25
license: MIT
security_flags: [curl-pipe-sh-install, single-contributor, new-repo, self-reported-benchmarks, third-party-decision-api-dependency]
overlaps: [pi-coding-agent]
source: unknown
---

## What it does

Jive is a terminal coding agent that replaces the conventional "LLM call -> tool call -> LLM call" loop with a single "graph call" per planner turn. Instead of invoking one tool at a time, the planner model submits a JSON program (a DAG) whose executable nodes are `bash` (shell commands) and `jev` (typed, bounded decisions sent to an external decision model). `foreach`/`repeat` node groups expand into parallel batches or bounded loops; nodes reference each other's outputs via JSON-pointer `$ref`s so data flows between nodes without extra glue code from the planner; `needs` adds ordering without a data reference; `when` expresses a typed predicate that can block a node. Node execution starts as soon as its definition has streamed in, overlapping generation with execution. Every `jev` node declares an `accept` predicate over the returned answer — a false predicate hands control back to the planner with the evidence collected so far rather than continuing blindly.

The `jev` node type calls a separate hosted product, "Jev" — publicly described (by its maker, TypeSafe AI) as a "System One" decision model that takes unstructured state plus typed questions and returns schema-constrained answers with probabilities rather than generated text. The intent is to let a graph make many bounded/repetitive judgments (bulk classification, dataset triage, multi-step profiling) without a full LLM turn per decision. `JEV_API_TOKEN` is required only for graphs that use `jev` nodes; bash-only graphs run without it.

Sessions, graphs, command output, and decisions are recorded to disk and can be resumed, inspected, and replayed. Any planner model/provider can be used: OpenRouter, Anthropic, OpenAI, Google, DeepSeek, Groq, and Ollama are built in, plus any OpenAI-, Anthropic-, or Responses-compatible endpoint via `~/.config/jive/models.json`.

The README credits pi (pi.dev, cataloged separately as `pi-coding-agent`) as a direct inspiration ("carrying the torch lit by pi coding agent") for its minimal-scaffold philosophy (no built-in MCP, no sub-agents), while diverging from pi's sequential tool-call loop by batching a full DAG of steps — including bounded Jev decisions — into one planner turn.

## Benchmarks (author-published)

The README publishes a 6-task table (`conversation_eval`, `error_handling_audit`, `product_matching`, `search_latency`, `sembench_movie`, `slow_trace_search`) comparing Jive, Codex, and Claude Code on wall-clock time, tool calls, LLM calls, Jev calls, and output tokens, one run per cell. Averaged across the six tasks (computed from the published per-task numbers): Jive mean 2m31s / 8,675 output tokens; Claude Code mean 12m12s / 32,681 tokens; Codex mean 17m40s / 16,196 tokens. Jive is faster on all 6 tasks, including the 3 tasks that used zero `jev` calls, indicating part of the gain comes from batching itself rather than the Jev decision calls specifically.

A third-party reviewer (GitHub issue #1 on the repo, who read the source and docs) corroborated the general architecture but flagged methodology gaps in the table: Jive/Codex reportedly ran one model ("gpt-5.6-sol") while Claude Code ran a different model ("claude-opus-5"); each cell is a single run, with all 18 runs started together on one machine (risk of CPU-contention/rate-limit noise); the table reports output tokens only, not input tokens or cost; and it omits a task-success/quality score despite the repo's own `taskground` harness already shipping deterministic verifiers (`verify.py`, `score.py`). The same reviewer states the project's docs describe the benchmarks as "illustrative single runs, not isolated/repeated performance measurements."

## Mechanical details

- **Install**: `curl -fsSL https://raw.githubusercontent.com/merijjeyn/jive/main/install.sh | sh` (clones into `~/.jive`, installs deps, links `jive` into `~/.local/bin`; re-running the script, or `jive update`, upgrades)
- **Alt install**: `bun install -g @merijjeyn/jive` / `npm install -g @merijjeyn/jive`, or `git clone` + `bun install` (no build step — runs TypeScript sources directly through Bun)
- **Requires**: Git, and either Bun or Node.js; at least one model-provider API key (`OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.) in a `.env`; `JEV_API_TOKEN` only if using `jev` nodes
- **Demo mode**: `jive --demo` runs a simulated graph against harmless fixture commands with no network calls
- **CLI**: `jive`, `jive --headless --prompt TEXT`, `jive --run FILE [--json]`, `jive --resume ID [--search QUERY]`, `jive --sessions`, `jive --models`/`--refresh-models`, `jive --schema` (prints the `execute_graph` JSON Schema), `jive --cwd DIR --model ID`, `jive update`, `jive --version`
- **Project config**: `AGENTS.md` is snapshotted into the system prompt at session start; `.jive/skills/*/SKILL.md` declares reusable project skills/graphs; `.jev/extractors/*.ts` adds plugins that turn raw data into Jev-decision inputs; `.env` holds credentials
- **Defaults**: planner defaults to `google/gemini-3.8-flash` when an OpenRouter key is set (otherwise the first configured provider's default model); Jev decisions default to `jev-1.13.0`; overridable via `--model`/`JIVE_MODEL` and `JEV_MODEL`
- **Testing**: `bun test` (offline, fixture-based, no model calls), `bun run eval:planner --model MODEL` (opt-in live planner evaluation), `bun run taskground list` (the reproducible comparison-task suite behind the benchmark table)
- Built with TypeScript, Bun, and OpenTUI, per the project's own documentation
- Docs: `docs/USAGE.md` (interface/sessions/skills/extractors), `docs/GRAPH_CONTRACT.md` (graph language spec), `docs/CONTEXT.md` (planner context/compaction/Jev input limits), `DESIGN.md` (architecture)

## Security

- **License**: MIT
- **Repo age/activity**: created 2026-09-21, most recent push 2026-09-25 (GitHub API, same day as this review) — a 4-day-old repository
- **Maintainer**: single contributor (`merijjeyn`, 52 commits per GitHub's contributors API); no co-maintainers observed
- **Stats at review**: 113 stargazers, 9 forks, 1 open issue (GitHub API)
- **Install path**: primary documented install is a `curl | sh` pipe from `raw.githubusercontent.com`; a package-manager alternative (`bun install -g` / `npm install -g @merijjeyn/jive`) avoids piping a remote script to a shell
- **Code execution**: `bash` nodes execute arbitrary shell commands locally — inherent to a terminal coding agent, same trust model as Claude Code/Codex — but the planner commits a full multi-step plan up front rather than one command at a time, giving a human fewer natural checkpoints to interrupt mid-plan than a strictly sequential tool-call loop
- **External dependency**: `jev` nodes call a separate hosted third-party API rather than a self-hosted model; state and questions passed through `jev` nodes leave the local machine to that service
- **Language mix**: GitHub's language-detection API reports Python as the largest language by bytes (3.06 MB Python vs 1.15 MB TypeScript, plus smaller JS/CSS/HTML/Shell), which does not match the project's own description of itself as "Built with TypeScript, Bun, and OpenTUI" — most likely explained by a large Python-based `taskground` evaluation/fixture tree (the third-party issue-#1 review cites `taskground/_shared/verify.py` and `score.py`) rather than the core agent runtime
- **Benchmark integrity**: see "Benchmarks" above — the published comparison table is a same-repo, single-run, author-run benchmark with a reported cross-model confound (Jive/Codex vs Claude Code allegedly ran different underlying LLMs); no independent reproduction was found
- The same third-party reviewer noted a local filesystem path (`/Users/.../Downloads/SKILL (1).md`) apparently left in `docs/CONTEXT.md` at the time of their review — a documentation-hygiene observation, not independently re-verified for this entry
