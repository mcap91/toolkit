---
name: benzi
title: Benzi
url: https://github.com/oooscoos/benzi
category: framework
summary: "Code-intelligence agent/tool that compiles a codebase into a queryable index (tree-sitter-based: symbols, call edges, references, class inheritance) before answering questions or editing, instead of grepping/globbing raw source into an LLM's context window. Ships as a VS Code extension, a headless CLI (benzi-headless), and an MCP server (benzi-mcp) for other agents, sharing one login. The VS Code/CLI agent additionally runs a runtime tracer, gates edits against a fresh parse, checks blast radius before/after writes, self-escalates to a larger model mid-task, and keeps persistent per-repo memory with one-step rollback. Covers 10 languages (Python deepest) plus an HTML/CSS/DOM-JS markup engine; 35+ query tools. Free during beta, BYOK against Anthropic/OpenAI/DeepSeek/Groq/Kimi/compatible APIs; self-published 82.4% SWE-bench Verified result. The GitHub repo is documentation only (no source), with GitHub reporting no recognized open-source license (license key: other/NOASSERTION)."
tags:
  - code-intelligence
  - tree-sitter
  - code-graph
  - mcp-server
  - vs-code-extension
  - cli-tool
  - byok
  - closed-source
  - swe-bench
  - runtime-tracer
reviewed: 2026-10-28
acquired: 2026-10-28
license: Proprietary
security_flags:
  - closed-source
  - requires-account
  - byok-sends-code-to-third-party-model
  - runtime-tracer-executes-target-code
overlaps:
  - codegraph
  - repowise
  - atomic-claude
  - cartographer
source: instagram
source_url: https://www.instagram.com/reel/Dd5RAFqyPjh/
---

## What it does

Benzi parses an entire codebase with a tree-sitter-based compiler before answering any question or making any edit, producing a precise map of every symbol, call edge, reference, and class-inheritance link — in contrast to agents that grep/glob raw source into an LLM's context window or embed it for retrieval. Three interchangeable surfaces share one login: a VS Code extension, a headless CLI (`benzi-headless`), and an MCP server (`benzi-mcp`) that exposes the compiled index as tools to an existing agent (Claude Code, Cursor, or any MCP client).

The VS Code/CLI agent (not available over plain MCP) adds: a runtime tracer that executes the target code and overlays real call targets and argument values onto the static map; static-analysis-gated edits, where a write that breaks parsing is auto-reverted instead of built on; blast-radius checks (callers, holders, parameter feeders) before and after every edit; self-escalation to a larger model mid-task via `BENZI_ESCALATE_MODEL`; and persistent per-repo memory with one-step rollback via index snapshots.

Supports 10 languages (Python, JavaScript, TypeScript, Java, C#, C++, C, Go, Rust, Ruby) through tree-sitter grammar plugins, plus a separate markup engine for HTML/CSS/DOM-JS (including frontend embedded in Python strings). Python has the deepest support and is the only language with a working runtime tracer — the tracer was reported broken for comprehensions/lambdas/generator expressions and most Python 3.9–3.10 method calls as of October 14, 2026. Every call site and file is tagged with one of six states: resolved, external, candidate, unresolved, observed, or unindexed — static analysis that can't settle a reference is flagged rather than guessed, and running the program is what settles it.

Exposes 35+ query/edit tools (16 documented publicly), including `get_callers`, `call_tree`, `trace_path`, `external_calls`, `forwardflow`, `backflow`, `profile`, `get_definition`, `search_symbols`, `get_hierarchy`, `skim_source`, `execute_from`, `check_last_execution`, `execute_generated_testcase`, `rollback_edit`, and `upgrade_to_pro`.

Free to use during beta; bring-your-own-key (BYOK) against Anthropic, OpenAI, DeepSeek, Groq, Kimi, or other compatible model APIs — Benzi does not charge, but model calls are billed by the chosen provider. A public web demo (varianttech.net/demo) indexes any public GitHub repo live, read-only, server-side, capped at 2,000 files / 2MB each, and deletes the clone after the session.

**Self-published benchmarks:** 82.4% (412/500) on SWE-bench Verified running DeepSeek V4.1-Flash at pass@1 inside official per-instance Docker images (network blocked), for $12.96 total (~3¢ per resolved instance), with 97.6% of input tokens served from cache. A separate 24-bug comparison reports Benzi+Sonnet reading 9,125 lines of source vs. Claude Code+Sonnet's 20,704 (2.3×) and a "DeepSeek Harness"+DeepSeek baseline's 43,598 (4.8×) for the same bugs.

## Mechanical details

- **Loop:** compile (tree-sitter parse, resolve imports, build class ancestry) → query (agent calls structured tools over the index) → edit, gated (write checked against a fresh parse; broken parse reverts) → verify by running (focused repro under the runtime tracer) → reindex incrementally (only changed files re-parsed each turn) → repeat.
- **Install:** `pip install benzi` (Python 3.11–3.14, Windows/macOS/Linux) installs `benzi-login`, `benzi-headless`, `benzi-mcp`; or install the VS Code extension from the Marketplace. One shared config (`benzi-login`) across VS Code, CLI, and MCP.
- **MCP registration:** `claude mcp add --scope user benzi -- benzi-mcp [/path/to/repo]` — omit the path to have it serve whichever folder the client starts in.
- **Headless run:** `benzi-headless . "fix the failing test in parser.py"`.

## Security

The GitHub repo (`oooscoos/benzi`) is documentation and a marketing site only — primary language HTML, ~31KB, no source code — and GitHub's repository API reports `license.key: "other"`, `spdx_id: "NOASSERTION"` (no recognized open-source license detected). The actual compiler and agent are distributed as closed packages via PyPI and the VS Code Marketplace; with no published source, the vendor's claims about local-only execution and data handling are not independently auditable. Using any surface requires creating an account (an email address plus a one-time code sent by Benzi's own login service). The BYOK architecture sends the code snippets the agent reads to the user's chosen third-party model provider, the same exposure as any LLM coding agent. The runtime tracer executes the target project's own code locally to record call behavior, which is inherent arbitrary-code-execution risk when tracing untrusted code.
---