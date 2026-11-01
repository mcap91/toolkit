---
name: medley
title: Medley
url: "https://www.medley.sh/"
category: plugin
summary: "Y Combinator-backed Claude Code/Codex plugin providing /mission command for multi-agent orchestration — decomposes goals into coordinated plans across multiple models (Claude, GPT, Gemini, Grok, Qwen, DeepSeek, Ollama), with browser-based mission board for visibility"
tags: [claude-code, codex, multi-agent, orchestration, plugin, multi-model, yc]
reviewed: 2026-07-12
acquired: 2026-07-12
license: proprietary
security_flags: [requires-api-keys, cloud-service, waitlist]
overlaps: [pilotfish, scheduled-multi-agent-coordinator]
source: unknown
---

## What it is

Medley is a plugin for Claude Code and Codex that adds a `/mission` command for multi-agent task orchestration. When invoked, it decomposes a goal into a structured plan, assigns steps to a coordinated team of agents (potentially using different models), and executes them sequentially, in parallel, or overnight. A browser-accessible URL shows the mission board with task tree, status, and handoffs.

## Capabilities

- **Multi-model coordination.** Brings Claude, GPT, Gemini, Grok, Qwen, DeepSeek, Ollama/Llama into Claude Code or Codex as a unified team.
- **Scope beyond code.** Missions can include research, outreach, docs, calendar tasks — integrates with GitHub, Slack, Notion, Linear, Jira, Gmail, Google Drive, Figma, and 30+ other tools.
- **Visible structure.** Each mission produces a URL showing the task tree, agent assignments, and progress.
- **Permission gates.** Agents ask before publishing, sending outbound, spending, or contacting people.

## Benchmarks claimed

SWE-Bench Pro public set (731 tasks): Medley multi-agent 88.09% vs Claude Fable 5 solo 80.0% vs Claude Opus 4.8 69.2% vs GPT-5.6 Sol 64.6% vs Gemini 3.1 Pro 54.2%. Claims +8.09 pts over best single model.

## Status

Free to use (bring your own API keys). Currently in waitlist/early-access phase. Backed by Y Combinator.

## Security

Proprietary closed-source plugin. Requires user-provided API keys for model access. Missions route through Medley's service for coordination and the browser dashboard — data leaves the local machine. Permission gates prevent autonomous outbound actions without approval. No source code available for audit.