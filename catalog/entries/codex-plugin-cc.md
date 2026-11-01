---
name: codex-plugin-cc
title: Codex Plugin for Claude Code
url: "https://github.com/openai/codex-plugin-cc"
category: plugin
summary: "Official OpenAI plugin enabling Codex usage from within Claude Code — code review (/codex:review), adversarial review, task delegation (/codex:rescue), session transfer, and background job management; requires ChatGPT subscription or OpenAI API key"
tags: [claude-code-plugin, codex, openai, code-review, cross-agent, delegation]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: []
source: unknown
---

## What it does

Official OpenAI plugin that lets Claude Code users delegate work to Codex without leaving their session. Provides seven slash commands:

- **/codex:review** — runs a Codex code review on uncommitted changes or branch diff (`--base <ref>`); supports `--background`
- **/codex:adversarial-review** — steerable review that challenges implementation and design decisions, pressure-tests assumptions and tradeoffs; accepts custom focus text
- **/codex:rescue** — delegates a task to Codex via a `codex-rescue` subagent (investigate bugs, try fixes, continue previous tasks); supports `--model`, `--effort`, `--resume`, `--fresh`
- **/codex:transfer** — creates a persistent Codex thread from the current Claude Code session, prints a `codex resume <session-id>` command for continuing in Codex
- **/codex:status** — shows running and recent Codex jobs for the current repo
- **/codex:result** — shows final output for a finished job, includes session ID for reopening in Codex
- **/codex:cancel** — cancels an active background job
- **/codex:setup** — checks Codex install/auth, optionally enables a review gate (Stop hook that runs targeted Codex review on Claude's responses)

## Differentiators

- **Official OpenAI authorship** — first-party cross-agent bridge from OpenAI
- **Session transfer** — uses Codex's external-agent session importer to create continuable Codex threads from Claude Code transcripts
- **Review gate** — optional Stop hook that blocks Claude's response if Codex review finds issues (warning: can create long-running loops and drain usage)
- **Model selection** — pass `--model gpt-5.4-mini` or shorthand `spark` (maps to `gpt-5.3-codex-spark`) for rescue tasks
- Reviews and rescues can run in `--background` with status polling

## Mechanical details / What to adopt

- **Install:** `/plugin marketplace add openai/codex-plugin-cc` → `/plugin install codex@openai-codex` → `/reload-plugins` → `/codex:setup`
- **Requirements:** ChatGPT subscription (incl. Free) or OpenAI API key; Node.js 18.18+; Codex CLI (`npm install -g @openai/codex`)
- Uses local Codex CLI and app server — same install, same auth state, same repo checkout
- Codex config (`~/.codex/config.toml` or `.codex/config.toml`) is respected for model and reasoning effort defaults

## Security

Official OpenAI repository. Uses local Codex CLI — no separate runtime. Review commands are read-only. Rescue commands can make changes. Review gate carries risk of runaway loops draining usage limits. All work happens locally using existing Codex authentication.