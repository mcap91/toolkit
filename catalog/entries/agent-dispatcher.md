---
name: agent-dispatcher
title: Agent Dispatcher — repository retrieval and specialist-role routing for Claude Code and Codex
url: "https://github.com/nahid-sparktales/agent-dispatcher"
category: framework
summary: "Claude Code plugin and Codex skill pack that routes a task to one of 27 specialist roles (engineering, design, testing, research, writing, operations) and assembles a bounded context packet of source excerpts using symbols, source text, code relationships, Git history, and stack-trace frames — rather than a full-repo dump. Ships 79 bundled local skills, references 31 external skills, 8 workflow recipes, a registry of 19 MCP servers, and 50 detection signals for role/skill selection. Standard retrieval runs locally with no model or network calls; optional features (model-assisted reranking, an external 'Jev' decision-engine API, an Onboarding Explorer, procedural learning from recorded outcomes) are off by default and require the operator's own provider configuration. Installs via `claude plugin marketplace add` + `claude plugin install` for Claude Code, or `python3 install_codex.py` for Codex (installs one skill to `~/.agents/skills/agent-dispatcher/`). Invoked with `/agent-dispatcher:agent-dispatcher <request>` (Claude) or `$agent-dispatcher <request>` (Codex); roles can be forced directly (e.g. `$agent-dispatcher reviewer`). Verification is explicit: each role defines what evidence counts as done and reports which checks ran, passed, or were left unverified. Requires Python 3.10+, Git, and an authenticated Claude Code or Codex; native Windows is unsupported (WSL recommended). MIT license, single maintainer, repo created 2026-09-19 with ~50 GitHub stars and 4 forks as of this review."
tags: [claude-code-plugin, codex-skill, repository-retrieval, role-routing, context-engineering, multi-agent, mcp, verification, code-search, git-history]
reviewed: 2026-09-25
acquired: 2026-09-25
license: MIT
security_flags: [bus-factor-1, young-project, hook-requires-trust-review]
overlaps: []
source: unknown
---
## What it does

Agent Dispatcher installs as a Claude Code plugin or a Codex skill and, given a task, routes it to one of 27 specialist roles (e.g., debugger, reviewer, uidesigner) — small, obvious edits take a direct path without a role. It retrieves the code a task needs by combining paths, symbols, source text, stack-trace frames, code relationships, and Git history into a bounded context packet of actual source excerpts, each tagged with why it was selected, rather than handing the whole repository to the model. Retrieval reuses source-linked project maps and private caches stored outside the working tree; an explicitly built deep index adds broader coverage, resumable onboarding, and incremental refresh.

Bundled content: 27 roles, 79 local skills, 31 referenced external skills, 8 workflow recipes, a registry of 19 MCP servers, and 50 detection signals used to pick a role/skill set. Commands include `context explain`, `context build <request>`, `doctor`, `health`, `inventory setup`, `status`, and `on here`/`off here` to toggle automatic activation per project.

## Why it exists

Aims at two problems for coding agents: finding the right code without either grepping blind or dumping the full repository into context, and matching the depth of guidance to the size of the task — small edits stay small, substantial tasks get role-specific instructions and an explicit verification contract.

## Differentiators

**Multi-signal retrieval, not embeddings-first.** Combines symbol lookups, literal source text, code relationships, stack-trace frame matching, and Git history rather than relying on a single vector index.

**Verification is a first-class output.** Each role defines what evidence counts as "done" (passed checks, failures, zero tests, or unverified) and reports it explicitly rather than declaring completion implicitly.

**Layered opt-in features, all off by default.** Deep repository index, task-experience memory, history/semantic memory (starts in shadow mode — reports candidates without changing rankings), procedural learning from recorded outcomes (requires human-approved review), model-assisted reranking, an Onboarding Explorer that has a model investigate the index, and a "Jev" decision engine that can delegate catalog selection to an external API — each stays off until the operator explicitly enables it and supplies provider configuration.

**Dual-host install.** One codebase targets both Claude Code (marketplace plugin, commands prefixed `agent-dispatcher:`) and Codex (skill under `~/.agents/skills/`, invoked with `$agent-dispatcher`).

**Can consult other model backends.** Optionally cross-checks a problem against Gemini, OpenAI, Grok, Perplexity, Kimi, OpenRouter-routed models, or a local Ollama model for a second opinion; each requires its own credentials.

## Mechanical details

**Install (Claude Code):** `claude plugin marketplace add nahid-sparktales/agent-dispatcher` then `claude plugin install agent-dispatcher@agent-dispatcher`. Invoke with `/agent-dispatcher:agent-dispatcher <request>` or a role-specific command such as `/agent-dispatcher:agent-reviewer`.

**Install (Codex):** `git clone https://github.com/nahid-sparktales/agent-dispatcher.git && cd agent-dispatcher && python3 install_codex.py`, which installs one skill to `~/.agents/skills/agent-dispatcher/`. Invoke with `$agent-dispatcher <request>`; Codex requires explicitly reviewing and trusting the installed hook via `/hooks` before automatic activation works.

**Requirements:** authenticated Claude Code or Codex, Git, Python 3.10+ (standard library only for the core installers/validators, no third-party Python packages). CI covers Python 3.10-3.14 on Linux and Python 3.14 on macOS; native Windows is not covered (WSL recommended).

**Repo stats (as of 2026-09-25):** created 2026-09-19, 50 stars, 4 forks, 1 open issue, one contributor (108 commits), Python, MIT license.

## Security

Standard retrieval runs locally with no model or network calls; project indexes and memory are stored in private storage outside the working tree. Optional model-assisted features (reranking, Onboarding Explorer, the external Jev decision engine, consulting other model backends) send task or source information to whatever provider the operator configures — all off by default. The Codex install path adds a session hook that Codex requires the user to explicitly review and trust via `/hooks` before it activates automatically. The vendor's own docs describe an optional "gated" mode that never runs commands declared in Markdown and has no network upload path; this claim comes from the project's own documentation and was not independently verified in this review.

**security_flags:** single maintainer / bus-factor 1 (108 commits, one contributor as of this review); repository is 6 days old at time of review (created 2026-09-19) with limited external validation (50 stars, 1 open issue); Codex install requires trusting an auto-activation hook.
