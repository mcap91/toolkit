---
name: claude-code-local-model-switching
title: Claude Code Local Model Switching
url: "https://docs.anthropic.com/en/docs/claude-code"
category: agent-pattern
summary: "Shell alias technique for swapping Claude Code between cloud Anthropic, local Ollama/LM Studio, and API-based OSS models (OpenRouter/DeepSeek) via ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN environment variables; includes KV cache fix (CLAUDE_CODE_ATTRIBUTION_HEADER=0) and Qwen 3.6 35B config"
tags: [claude-code, local-inference, ollama, lm-studio, openrouter, model-switching, env-vars]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [free-claude-code, openrouter, local-model-picks-2026]
source: unknown
---

## What it does

Describes a shell alias pattern for instantly switching Claude Code's backend between three modes:

1. **Cloud (Anthropic subscription):** unset `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN`, launch `claude` normally
2. **Local OSS (Ollama / LM Studio):** set `ANTHROPIC_AUTH_TOKEN=ollama`, `ANTHROPIC_BASE_URL=http://localhost:11434` (Ollama) or `:1234` (LM Studio), launch `claude --model <model>`
3. **Cloud OSS (OpenRouter / DeepSeek):** set `ANTHROPIC_API_KEY=<key>`, `ANTHROPIC_BASE_URL=https://openrouter.ai`, launch `claude --model deepseek/deepseek-coder`

### KV cache performance fix

Claude Code appends a changing attribution header to every prompt by default. For local models this invalidates the KV cache on every turn, degrading inference speed by ~90%. Setting `CLAUDE_CODE_ATTRIBUTION_HEADER=0` disables this.

### Qwen 3.6 35B config

Includes a sample model config block for Qwen 3.6 35B (4-bit quantized) with reasoning enabled: 64K context, 8K output, temperature 0.6, top_p 0.95, `enable_thinking: true`.

## Mechanical details / What to adopt

- Add aliases to `~/.zshrc` or `~/.bashrc`: `claude-cloud`, `claude-local`, `claude-oss-api`
- Expand Ollama model context window to at least 32K–64K in Ollama settings
- For LM Studio, swap the base URL port from 11434 to 1234
- The technique works because Claude Code routes API traffic based on `ANTHROPIC_BASE_URL` — no proxy needed

## Security

No code dependencies — shell aliases only. The `CLAUDE_CODE_ATTRIBUTION_HEADER=0` environment variable disables an Anthropic telemetry/attribution feature; behavior may change across Claude Code versions.