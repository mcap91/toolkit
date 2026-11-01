---
name: frontier
title: Frontier
url: "https://github.com/WellDunDun/frontier"
category: plugin
summary: Well-architected multi-harness orchestration runtime for Claude Code; early preview but the token-economics argument and delegation model are sound
tags: [claude-code, orchestration, multi-model, delegation, pi, codex, ollama, omlx]
reviewed: 2026-06-16
acquired: 2026-06-16
license: Apache-2.0
security_flags: []
overlaps: [autoharness, claude-peers-mcp]
source: unknown
---

## What it does

An orchestration runtime installed as a Claude Code plugin that delegates bounded work (research, implementation, testing, log reduction) to other harnesses and model providers. The orchestrator (your frontier model in Claude Code or Codex) keeps planning, synthesis, and final review; workers handle token-heavy tasks on cheaper or local models via Pi and Codex harness adapters. Supports three backend flavors: oMLX (local Apple Silicon inference), Ollama, and any OpenAI-compatible server (LM Studio, vLLM, llama.cpp, cloud gateways). Ships five slash commands (`delegate`, `status`, `result`, `cancel`, `setup`), a `frontier-worker` agent, and a companion CLI runtime (`frontier-companion.mjs`) that owns all harness details.

## Assessment

The problem statement is well-grounded: agentic coding burns 1000x more tokens than ordinary code chat, with high variance and diminishing returns. Frontier's answer — keep judgment with the frontier model, route bounded scans/implementation/log reduction to cheaper workers — is architecturally clean. The separation of orchestration from model access is the right abstraction. However, it's in early public preview with evolving provider support, depends on Pi and Codex harness availability (Pi is less mainstream), and the plugin marketplace installation path needs more maturity. Watch until the provider surface stabilizes and real-world usage reports emerge. The orchestration skill and delegation patterns are worth studying now for our own multi-agent work.

## Mechanical details

- Installs via Claude Code plugin marketplace: `/plugin marketplace add WellDunDun/frontier`
- Backend auto-detection ladder: oMLX → Ollama; OpenAI-compatible requires explicit `frontier.config.json`
- Companion runtime (`frontier-companion.mjs`) owns all CLI composition — no agent ever builds raw shell strings
- Structural guardrail: Codex path refuses unless the profile exists in `~/.codex/config.toml`; Pi path refuses unless the provider exists in `~/.pi/agent/models.json`; both refuse if the backend is unreachable
- Background jobs supported with `--background` flag, status polling, and result retrieval
- Model pinning per task with `--model` flag
- Secret handling: env vars, file-based keys with jsonPath, inline literals (discouraged); secrets never logged
- Config validation: malformed JSON or unknown flavors are hard errors, never silent fallbacks
- `npm run check` validates plugin metadata, marketplace consistency, frontmatter, scripts, forbidden flags

## Security

- **License**: Apache-2.0 with LICENSE and NOTICE files
- **Dependency health**: Companion runtime is a single `.mjs` file; minimal dependency surface. No package.json dependencies visible from the README
- **Code quality signals**: `npm run check` functional validation exists; AGENTS.md for development guidance; CONTRIBUTING.md and SECURITY.md present
- **Supply chain**: Appears small team or single contributor; CHANGELOG.md tracks releases; plugin marketplace distribution
- **Dangerous patterns**: None observed — the companion runtime deliberately prevents raw CLI composition by agents, config validation is strict with hard errors on malformed input, and secrets are handled through env var indirection with no logging. The structural guardrail against implicit provider fallback is a positive security property
- **Maintenance**: Early public preview; active development based on comprehensive documentation and feature surface