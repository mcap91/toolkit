---
name: hotdog
title: hotdog
url: "https://github.com/devoidfury/hotdog"
category: cli-tool
summary: "Zero-dependency TypeScript/Bun AI agent harness with tool calling — connects to any OpenAI-compatible chat-completions endpoint (local llama-swap/llama.cpp/vllm or cloud), with hook-driven extensions, profiles, skills, MCP client, subagent tasks, and an optional --sandbox mode restricting tools to non-destructive ones; MIT, single-maintainer hobby project"
tags: [agent-harness, cli-tool, bun, typescript, mcp-client, local-llm, tool-calling]
reviewed: 2026-08-25
acquired: 2026-08-25
license: MIT
security_flags: [single-maintainer, no-external-adoption-signal, minimal-guardrails-by-default]
overlaps: []
source: unknown
---

## What it does / What it says

hotdog is an AI agent harness with tool calling support, built to run on the Bun runtime with zero npm dependencies. It connects to any OpenAI-compatible chat-completions API (the author's stated primary use case is local backends — llama-swap, llama.cpp, vllm — though any compatible cloud endpoint should work), manages conversation context, and executes tools through an extensible hook-driven architecture (notification, sequential-pipeline, and gate/mutate hook patterns).

## Differentiators / Key takeaways

- Ships as a source tree with no build step and no published package artifact: install is `git clone` + `bun bin/hotdog`. `dependencies` is empty (only a dev-time type-only dependency, `@types/bun`), which the README argues removes install-time lifecycle-script and transitive-dependency attack surface.
- Feature set: tool calling (file ops, bash, HTTP, web search), extension architecture (`extension.json` + `index.ts`), profiles (composable role/tools/aspects/model configs), skills (load-on-demand guides), context compaction, MCP client (HTTP + stdio), subagent tasks, a "handoff" tool to reset context mid-task, JSONL session logging, streaming, retry-with-backoff, and prompt-injection mitigation via "marker mangling."
- Has both one-shot (`hotdog -p "..."`) and interactive CLI modes, plus a beta web UI (`hotdog webui`).
- `--sandbox` flag restricts the agent to tools without side effects; the README's own "Safety Disclaimer" recommends running on a dedicated host, VM, or container regardless, since guardrails are otherwise minimal.

## Mechanical details / What to adopt

Requires Bun >= 1.0. `git clone https://github.com/devoidfury/hotdog.git && cd hotdog && bun bin/hotdog`. Configure an LLM backend via `config/defaults.json` (`default_model`, `providers[].url`/`api_key`) or env vars (`HOTDOG_AI_URL`, `HOTDOG_API_KEY`). Author has tested only on Linux; macOS/Windows support is unverified and PRs are requested.

## Security

MIT license, copyright 2026 devoidfury / Thomas Hunkapiller. README explicitly states minimal guardrails by default and recommends a dedicated host/VM/container; `--sandbox` mode disables tools with side effects. README also flags the MCP client and skill scripts as explicit opt-in trust boundaries since they can load third-party code. Author discloses AI assistance was used in writing the code alongside manual review. This is a single-maintainer hobby project with no external adoption, audit, or CVE signal found in this review (no results on GitHub or web search beyond the repo itself); repo history/star count/CI status were not independently verified.
