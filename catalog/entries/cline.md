---
name: cline
title: Cline
url: https://github.com/cline/cline
category: framework
summary: Open-source autonomous coding agent distributed as a VS Code extension, JetBrains plugin (early access), SDK, and CLI — file editing, terminal command execution, browser automation, and MCP tool integration with human-in-the-loop approval by default (diff review, checkpoints to undo agent work, optional auto-approve); project rules via .clinerules files; MCP Marketplace and hosted SaaS (Cline.bot) with free/paid/enterprise tiers; developed by Cline Bot Inc.; TypeScript; ~71k GitHub stars, 5M+ VS Code installs; Apache-2.0
tags:
  - coding-agent
  - vscode-extension
  - jetbrains
  - cli
  - sdk
  - mcp
  - browser-automation
  - human-in-the-loop
  - agent-harness
reviewed: 2026-10-29
acquired: 2026-10-29
license: Apache-2.0
security_flags: []
overlaps:
  - agentic-rag-terminal-tools
  - local-model-adversarial-workflow
source_url: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/
source: reddit
---

## What it does

Cline turns an editor into an autonomous coding agent: it reads files, writes code, runs terminal commands, drives a browser, and calls MCP tools, iterating on errors without constant hand-holding. By default it requires approval for each file change and command (human-in-the-loop), shows every edit as a reviewable/revertible diff, and tracks checkpoints to undo its own work; an auto-approve toggle allows unattended runs. Project-specific conventions (coding standards, architecture, deployment, testing) go in `.clinerules` files, picked up automatically across the VS Code extension, JetBrains plugin, and CLI. An MCP Marketplace lists third-party tool servers, and a hosted SaaS (Cline.bot) offers free, paid, and enterprise tiers.

## Security

Apache-2.0. Default human-in-the-loop approval for file writes and command execution is a built-in control; auto-approve mode removes that gate and should be scoped deliberately. ~71k GitHub stars, Cline Bot Inc. as a commercial maintainer behind the open-source core.

## Usage notes

- Practitioner report (r/Qwen_AI, Oct 2026): used at work (via Anthropic models on Amazon Bedrock) as the harness for Opus 4.8/5.5, alongside a separate self-optimized Zed + Qwen Code + SearXNG-MCP harness for self-hosted Qwen 3.8 27B. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)
