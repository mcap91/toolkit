---
name: openwiki
title: OpenWiki
url: "https://github.com/langchain-ai/openwiki"
category: cli-tool
summary: "LangChain CLI that generates and maintains agent-oriented codebase documentation in an openwiki/ directory; auto-updates via CI (GitHub Actions / GitLab CI) on each push; appends references to AGENTS.md/CLAUDE.md so coding agents discover the wiki; supports OpenRouter, Fireworks, Baseten, OpenAI, Anthropic, and OpenAI-compatible endpoints"
tags: [documentation, codebase-wiki, langchain, ci-cd, agent-context, cli]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: []
source: unknown
---

## What it does

CLI tool that writes and maintains documentation for a codebase, targeting AI coding agents as the primary audience. On first run (`openwiki --init`), it generates documentation into an `openwiki/` directory. On subsequent runs or via `--update`, it refreshes documentation based on repository changes.

Automatically appends prompting to `AGENTS.md` and/or `CLAUDE.md` instructing coding agents to reference the wiki for context. Ships with CI workflow templates for GitHub Actions and GitLab CI that automatically open PRs/merge requests with documentation updates on push.

### Inference providers

Supports OpenRouter, Fireworks, Baseten, OpenAI, Anthropic, and any OpenAI-compatible endpoint (e.g. LiteLLM gateway). Pre-defined models include GLM 5.2, Kimi K2.6, Sonnet 5; custom model IDs accepted for each provider. Credentials stored in `~/.openwiki/.env`. Optional LangSmith tracing integration.

## Differentiators

- **Agent-first documentation** — generates docs structured for AI agent consumption, not human browsing
- **CI-driven freshness** — ships GitHub Actions and GitLab CI templates that auto-update docs on push
- **Auto-wires agent instructions** — appends to AGENTS.md/CLAUDE.md so agents discover the wiki without configuration
- **Multi-provider** — works with 6+ inference providers and arbitrary OpenAI-compatible endpoints

## Mechanical details / What to adopt

- Install: `npm install -g openwiki`
- Init: `openwiki --init` (interactive setup for provider/model/API key)
- Update: `openwiki --update` or CI workflow on push
- Interactive mode: `openwiki "prompt"` stays open for follow-ups; `-p` for one-shot
- Alternative Anthropic endpoint: set `ANTHROPIC_BASE_URL` alongside `ANTHROPIC_API_KEY`
- OpenAI-compatible: set `OPENAI_COMPATIBLE_BASE_URL` and `OPENAI_COMPATIBLE_API_KEY`

## Security

Credentials stored locally in `~/.openwiki/.env`. Sends codebase content to configured LLM provider for documentation generation. Optional LangSmith tracing sends run data to LangSmith servers. CI workflows require API keys as repository secrets.