---
name: aider
title: Aider
url: "https://github.com/Aider-AI/aider"
category: cli-tool
summary: "Terminal AI pair-programming tool (Python) — edits code in a local git repo via chat with cloud or local LLMs, builds a repo map for large codebases, auto-commits each change with sensible messages, runs linters/tests after edits; 100+ languages, voice-to-code, image/web-page context; Apache-2.0, ~49k stars, last pushed May 2026"
tags: [coding-agent, terminal, pair-programming, git, repo-map, python, multi-provider, local-llm, cli-tool]
reviewed: 2026-09-10
acquired: 2026-09-10
license: Apache-2.0
security_flags: [stale-4-months, high-open-issue-count]
overlaps: [pi-coding-agent]
source: unknown
---

## What it does

Aider is one of the earliest and most widely used terminal AI pair-programming tools (created May 2023 by Paul Gauthier). It runs as a chat REPL inside a git repository: the user asks for changes, aider sends relevant files plus a repository map to an LLM, applies the returned edits directly to the working tree, and automatically commits each change with a generated commit message so every AI edit is diffable and revertible with normal git tooling.

Core capabilities:

- **Model connectivity:** works with most cloud LLMs (Claude, GPT/o-series, DeepSeek, Gemini) and local models; provider selected via `--model` and `--api-key` flags (litellm under the hood)
- **Repo map:** builds a ranked map of the entire codebase (tree-sitter based) so the model has cross-file context in large projects without sending every file
- **Git integration:** auto-commit per change, easy undo/diff via familiar git commands
- **Lint/test loop:** optionally runs linters and test suites after each edit and feeds failures back for fixing
- **Input modalities:** voice-to-code, images and web pages as chat context, IDE integration via "AI comments" in code
- **Copy/paste mode:** structured workflow for using web-chat-only LLMs without API access

## Differentiators

- Git-native workflow — every AI change is a commit, making review/undo a git operation rather than a custom UI feature; this predates and influenced later coding agents.
- The tree-sitter repo map is the signature technique for scaling chat-driven editing to large codebases.
- Publishes its own LLM code-editing leaderboards (aider polyglot benchmark), widely cited for model comparisons.
- Pair-programming interaction model (user-driven chat, per-request edits) rather than autonomous multi-step agent loops — no tool registry, subagents, or MCP.

## Mechanical details

- Install: `python -m pip install aider-install && aider-install`; run `aider --model sonnet --api-key anthropic=<key>` (or `deepseek`, `o3-mini`, etc.) inside the project directory.
- Python, Apache-2.0, ~48.9k stars, ~4.9k forks, 265 watchers; homepage/docs at aider.chat with installation, configuration, LLM-connection, and troubleshooting guides; Discord community.
- Repo created 2023-05; last push 2026-05-22 — no commits in ~4 months at review time; 1,860 open issues.

## Security

- **License:** Apache-2.0 — permissive.
- `stale-4-months` — main branch last pushed 2026-05-22; the project's release cadence has visibly slowed relative to its 2023–2025 pace.
- `high-open-issue-count` — 1,860 open issues at review time.
- Sends code context to the configured LLM provider; API keys supplied via CLI flags, env vars, or config files. Local-model operation avoids external code transfer.
- Edits are constrained to the local repo and are individually committed, so the blast radius of a bad edit is a git revert.