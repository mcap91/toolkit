---
name: pi-coding-agent
title: Pi Coding Agent
url: "https://github.com/earendil-works/pi"
category: framework
summary: "Minimal, extensible terminal coding agent harness by Mario Zechner (Earendil Works). Four core tools (read, write, edit, bash), ~200-token system prompt, 37+ models across 20+ providers (Anthropic, OpenAI, Google, Bedrock, etc.). Extensible via TypeScript extensions, skills, prompt templates, themes, and packages — deliberately omits MCP, sub-agents, plan mode, and permission popups in favor of user-built alternatives. Tree-structured sessions with branching, compaction, and forking. SDK/RPC modes for embedding. MIT. ~78k GitHub stars."
license: MIT
tags: [coding-agent, terminal, cli-tool, extensible, multi-provider, sdk, typescript, sessions, skills, themes]
reviewed: 2026-07-28
acquired: 2026-07-28
overlaps: []
security_flags: []
source: unknown
---

## What it is

Pi is a minimal terminal coding agent harness from Mario Zechner (badlogic, creator of libGDX) under Earendil Works / pi.dev. It provides an interactive coding agent with four built-in tools (read, write, edit, bash) and a system prompt of approximately 200 tokens. It supports 37+ models across 20+ providers via API keys or subscriptions (Anthropic Claude Pro/Max, OpenAI ChatGPT Plus/Pro, GitHub Copilot, Google Gemini/Vertex, Azure, Bedrock, Mistral, Groq, xAI, OpenRouter, llama.cpp, and others).

Pi runs in four modes:
- **Interactive** — full TUI with editor, file references (@), image paste, message queue (steering + follow-up), keyboard shortcuts
- **Print** — single prompt, print response, exit (`pi -p`)
- **JSON** — all events as JSON lines for machine consumption
- **RPC** — stdin/stdout protocol for process integration

Sessions are tree-structured JSONL files supporting in-place branching (`/tree`), forking (`/fork`, `/clone`), and context compaction (manual or automatic). The monorepo also ships `@earendil-works/pi-ai` (unified multi-provider LLM API) and `@earendil-works/pi-agent-core` (agent framework).

## Mechanical details

- **Install:** `npm install -g --ignore-scripts @earendil-works/pi-coding-agent` or `curl -fsSL https://pi.dev/install.sh | sh`
- **Customization layers:** TypeScript extensions (tools, commands, UI, event handlers), skills (Agent Skills standard / SKILL.md), prompt templates (Markdown with `{{variables}}`), themes (hot-reloadable), pi packages (npm or git distribution)
- **No built-in:** MCP, sub-agents, plan mode, permission popups, todos, background bash — all available via extensions or packages
- **Context files:** Loads AGENTS.md / CLAUDE.md from global, parent dirs, and cwd
- **Config:** `~/.pi/agent/settings.json` (global) and `.pi/settings.json` (project)
- **Platforms:** Windows, macOS, Linux, Termux (Android), tmux
- **SDK:** `createAgentSession()` API for embedding in Node.js apps

## Security

MIT licensed. Extensions execute arbitrary code with full system access. Skills can instruct the model to perform any action including running executables. The README advises reviewing source code before installing third-party packages. Telemetry is opt-out (install/update pings to pi.dev; provider attribution headers for OpenRouter/Cloudflare/NVIDIA). No security flags observed in the core tool.

## Usage notes

- Community harness comparison: Pi is lightweight and purpose-built for local LLMs — optimizes for minimal context and runs ~2-3x faster than heavier harnesses; can self-generate extensions/skills on the fly via the Pi marketplace.
- Trade-off: no built-in guardrails — one user reported it ran `rm -rf` without confirmation — requiring more DIY setup than feature-rich harnesses like OpenCode.
- Comparison point from the same discussion: OpenCode is feature-rich/out-of-the-box with built-in guardrails, but reported as bloated and slower with local models due to heavy system-prompt overhead.

- **Community-recommended extensions for local LLM use** (from a week-long practitioner report running Pi without Claude): `u/ff-labs/pi-fff:src`, `u/juicesharp/rpiv-ask-user-question`, `u/juicesharp/rpiv-todo`, `u/juicesharp/rpiv-web-tools`, `context-mode:build/adapters/pi/extension.js`, `pi-caveman:caveman.ts`, `pi-mcp-adapter`, `pi-quiet-tools:src`, `pi-rtk-optimizer`, `pi-subagents`, `pi-tps-status`. Also: "oh my pi" (omp) exists as an upgrade layer but reported as less reliable than base Pi for complex tasks.
- **Local LLM model tips with Pi**: Qwen3.8-27B is capable but Qwen3.6-35B preferred for speed. KV cache at q8 solves issues that q4 KV introduces. Splitting q4/q8 KV causes a large performance hit. Parallel tasks on a single 24GB GPU (5090m) didn't work well — GPU scheduling conflicts with other workloads (e.g., ComfyUI).

- Local-model quantization report (forum, Sep 2026): running a modified pi.dev harness against a local 27B-class model at Q4 / 90K context (llama.cpp, 3090 + 64GB RAM) produced frequent tool-call loops; the same class of model at Q8 on 48GB VRAM (DeepSeek harness) solved real tasks with no loops. Workaround at Q4: set reasoning to high and use the local model as orchestrator/reasoner rather than implementer.
- `/advisor` pattern with local Qwen (forum, Sep 2026): local Qwen 3.8 27B is a capable worker but confidently wrong; before trusting a plan, prompt "Ask /advisor for the hidden assumptions, failure modes, and black swans in your answer" so a frontier model (pi_advisor) reviews it — Qwen then routinely rewrites half the answer. Rule of thumb: let the local model draft and do bulk work, spend a few frontier tokens trying to prove it wrong.

- **Local Qwen 3.8 as Opus replacement**: Practitioner report using Pi with llama.cpp backend on Strix Halo 128GB — Qwen 3.8 27B replaces Opus 4.6–4.8 for agentic coding if 2–3x longer task times are acceptable. $0/month, fully offline. LlamaStash manages llama.cpp launches and presets.

- Practitioner report (r/LocalLLM, Oct 2026): a user running Pi on a 65K-context local model reports Pi needs about 1.5K tokens to start a session, vs an estimated 10-14K for Codex/Claude Code out of the box — a gap of 15-20% of a 65K window before any work starts. They add local OpenAI-compatible backends (e.g. LM Studio) via a `providers` block in `~/.pi/agent/models.json` (`baseUrl`, `api: "openai-completions"`, `apiKey`, and a per-model `id`/`contextWindow`/`maxTokens`/`input` list). (source: https://www.reddit.com/r/LocalLLM/comments/1xgqyz4/125_tokens_per_second_on_an_rtx_4070_ti_super_how/)

## How to use it

npm install -g --ignore-scripts @earendil-works/pi-coding-agent
