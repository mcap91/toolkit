---
name: qwen-code
title: Qwen Code
url: https://github.com/QwenLM/qwen-code
category: cli-tool
summary: Alibaba's open-source terminal coding-agent CLI, forked from Gemini CLI and adapted for the Qwen3-Coder model family on agentic coding tasks — asks permission before file edits by default, integrates Git conversationally, reads files as needed without manual context-adding, and auto-switches to vision-capable models when images appear in input; installable via npm (@qwen-code/qwen-code), Homebrew, or from source; Qwen OAuth free-tier auth; companion qwen-code-action GitHub Action and open-computer-use MCP service; TypeScript, Apache-2.0, ~29k GitHub stars
tags:
  - cli
  - coding-agent
  - qwen
  - terminal
  - mcp
  - gemini-cli-fork
  - agentic
  - alibaba
reviewed: 2026-10-29
acquired: 2026-10-29
license: Apache-2.0
security_flags: []
overlaps: []
source_url: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/
source: reddit
---

## What it does

Qwen Code is a terminal AI coding agent forked from Google's Gemini CLI and re-tuned for Qwen3-Coder models, with an enhanced parser and tool-call support for that model family. It asks for permission before modifying files by default, makes Git operations conversational (e.g. "what files have I changed?"), reads project files as needed instead of requiring manual context attachment, and automatically switches to a vision-capable model when it detects images in the input. Install via `npm install -g @qwen-code/qwen-code`, `brew install qwen-code`, or from source. The recommended auth method, Qwen OAuth, is free with generous quotas. The QwenLM org also ships `qwen-code-action` (a GitHub Action wrapper) and `open-computer-use` (an MCP-based computer-use service controlling macOS/Linux/Windows via accessibility APIs).

## Security

Apache-2.0. Default file-edit confirmation prompt is a built-in control. On Terminal-Bench, Qwen Code paired with Qwen3-Coder-480A35 scored 37.5 — a vendor/community-reported benchmark figure, not independently reproduced here.

## Usage notes

- Practitioner report (r/Qwen_AI, Oct 2026): used as the CLI harness (with Zed as editor and a SearXNG MCP server for web research) for self-hosted Qwen 3.8 27B, run at xhigh reasoning effort via vLLM on a single 48GB NVIDIA L40S. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)
