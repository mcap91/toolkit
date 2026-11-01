---
name: zed
title: Zed
url: https://github.com/zed-industries/zed
category: framework
summary: Rust code editor (from the team behind Atom and Tree-sitter) with a native Agent Panel for agentic AI workflows — built-in agent reads/writes/runs code in a project; external coding agents (Claude, Codex, OpenCode, Copilot, Cursor, Gemini CLI, Qwen Code) connect via the Agent Client Protocol (ACP), with Zed hosting the thread UI while the external agent owns its runtime; inline edit predictions and multiplayer collaboration; editor core open-source, paid tiers sell Zed-hosted AI and admin controls; ~90k GitHub stars
tags:
  - code-editor
  - rust
  - agent-client-protocol
  - ai-agent
  - multiplayer
  - tree-sitter
  - acp
reviewed: 2026-10-29
acquired: 2026-10-29
license: mixed (GPL-3.0/Apache-2.0 core; paid Zed-hosted AI tiers)
security_flags: []
overlaps:
  - attention-control
source_url: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/
source: reddit
---

## What it does

Zed is a code editor with a native Agent Panel: Zed's own built-in agent can read, write, and run code in a project, and the editor also hosts third-party coding agents (Claude, Codex, OpenCode, GitHub Copilot, Cursor, Gemini CLI, Qwen Code) through the Agent Client Protocol (ACP) — Zed renders the conversation/thread UI while the external agent process owns its own runtime and tool execution. Other editor features include inline edit predictions and multiplayer collaborative editing.

## Security

Editor core is open source (GPL-3.0/Apache-2.0 mix across the codebase); AI add-ons (Zed-hosted model access, org admin layer) are a paid tier on top of the open core. External agents connected via ACP run in their own process and retain their own permission model — Zed does not describe ACP as adding a sandbox around them.

## Usage notes

- Practitioner report (r/Qwen_AI, Oct 2026): used as the editor in a self-optimized harness for self-hosted Qwen 3.8 27B — Zed + Qwen Code + a SearXNG MCP server, run at xhigh reasoning effort. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)
