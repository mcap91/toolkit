---
name: claude-autoresearch
title: Claude Autoresearch (uditgoenka)
url: "https://github.com/uditgoenka/autoresearch"
category: plugin
summary: "Claude Code / OpenCode / Codex skill+command pack generalizing Karpathy's autoresearch loop (constraint + mechanical metric + autonomous iteration + git rollback) to any domain — 14 commands (autoresearch, plan, debug, fix, security, ship, scenario, predict, learn, reason, probe, improve, evals, regression), a v2.2 orchestrator that derives a success predicate from a plain-language goal, and 9 always-on safety hooks; MIT"
tags: [autoresearch, karpathy, agent-loop, claude-code, opencode, codex, hooks, iteration, autonomous-agents]
reviewed: 2026-07-09
acquired: 2026-07-09
license: MIT
security_flags: [always-on-session-hooks, tool-call-interception, npx-or-plugin-install, ephemeral-db-migration-command]
overlaps: [autoresearch, andrej-karpathy-skills]
source: unknown
---

## What it is

An installable command/skill pack that generalizes Andrej Karpathy's `autoresearch` (an autonomous ML-experiment loop) into a domain-agnostic "improvement engine" for Claude Code, OpenCode, and OpenAI Codex. The core loop is: review state + git history + results log → make one focused change → commit (before verification) → run mechanical verification → keep if improved, `git revert` if worse → log to TSV → repeat until N iterations or the goal is met. It explicitly credits Karpathy's original (catalogued separately as `autoresearch`).

## Commands and structure

14 commands: `/autoresearch` (core loop, default 25 iterations; v2.2 adds an orchestrator mode that classifies a plain-language goal, derives a verifiable Success predicate, confirms once, then chains subcommands) plus `plan`, `debug`, `fix`, `security` (STRIDE + OWASP, read-only unless `--fix`), `ship`, `scenario`, `predict` (5-persona panel), `learn` (docs), `reason` (adversarial blind-judge refinement), `probe`, `improve` (PRD generation), `evals` (TSV trend/plateau analysis), and `regression` (green→red stability gate). v2.1 rebuilt a monolithic SKILL.md (~813 lines) into a thin router plus self-contained command files (~5–8K tokens/invoke, ~95% reduction). Every looping command is bounded by default; `Iterations: unlimited` opts back in. Results log to TSV; a `Guard:` command adds a "did anything else break?" safety net.

## Safety hooks

Ships 9 hooks that fire on every session (not only autoresearch commands): PreToolUse blocks (`scout-block` for node_modules/.git/etc., `privacy-block` for .env / SSH keys / credentials, `dangerous-cmd-block` for force-push / `rm -rf` / `git reset --hard`), UserPromptSubmit injections (`iteration-context`, `dev-rules-reminder`, `simplify-gate` which warns at 400 and blocks at 800 LOC), `subagent-context`, `session-init`, and `stop-notify` (terminal notification + optional webhook). All on by default, each disableable via `AR_DISABLE_*` env vars; blocked directories are customizable via a `.ckignore` file.

## Install

`npx skills add uditgoenka/autoresearch`, or plugin (`/plugin marketplace add uditgoenka/autoresearch` → `/plugin install autoresearch@autoresearch`), or manual copy of `.claude/skills` + `.claude/commands`, or `./scripts/install.sh`. OpenCode uses underscore command names (`/autoresearch_debug`); Codex uses `$autoresearch` mention syntax. Start a fresh session after install (reference files are not resolvable in the install session).

## Security

MIT-licensed. The notable surface is the 9 always-on hooks: once installed they intercept tool calls (PreToolUse) and inject context into prompts (UserPromptSubmit) for every session, and register an optional SessionEnd webhook — review the hook scripts and settings wiring before installing globally. Several hooks are defensive (blocking secret reads and destructive git commands), but they modify session behavior repo-wide. The `regression` command's `data-migration` dimension is hard-guarded (opt-in, refuses non-ephemeral / non-allowlisted DB URLs, forward-only by default). Installation pulls third-party code via npx / plugin / git.