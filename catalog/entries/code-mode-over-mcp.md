---
name: code-mode-over-mcp
title: Code Mode over MCP (execute_code pattern)
category: agent-pattern
summary: "Architecture pattern where an agent exposes a single execute_code tool instead of N MCP tools — the agent writes code against an SDK/API to perform actions, keeping token cost constant per turn instead of scaling linearly with tool count; 78–99% token savings at scale (benchmarked at 500+ tools); Cloudflare, Anthropic, and Bifrost implementations"
tags: [mcp, token-optimization, code-execution, agent-architecture, cost-reduction, tool-scaling]
reviewed: 2026-09-03
acquired: 2026-09-03
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it says

The pattern replaces a large MCP tool surface with a single `execute_code` (or `executeToolCode`) tool. Instead of injecting all tool definitions into every prompt turn — where cost scales linearly with the number of registered tools — the agent receives one tool that lets it write and execute code against an SDK or API. The SDK provides the same capabilities as the MCP tools, but tool definitions are loaded on demand inside the code sandbox rather than in the prompt context.

The argument: MCP's design requires the entire tool surface to ride along in every prompt. At 5 servers with 30 tools each, that's 150 tool definitions before any user content. At 500+ tools, it exceeds 1M input tokens per query. The execute_code pattern holds token cost constant regardless of how many capabilities are available.

## Key takeaways

- MCP token cost scales linearly with registered tools; execute_code cost is constant per turn
- Benchmarked savings: Cloudflare API (2,500 endpoints) dropped from 1.17M to ~1K tokens; Bifrost (508 tools) saw 14x reduction; general benchmarks show 78.5% fewer input tokens
- An 8-turn MCP conversation can collapse to a single execute_code call (75% fewer model invocations)
- 30–40% latency improvements from eliminating back-and-forth tool calls
- Adding new capabilities has near-zero marginal cost per query — the model only loads what it uses
- The pattern does NOT replace MCP for narrow agents with few tools, local-host control (file I/O, shell), or cases where code sandbox setup outweighs token savings
- MCP was designed for local host control; the execute_code pattern targets remote API surfaces with many endpoints

## What to adopt

- When building agents that connect to APIs with many endpoints (>~6 tools), consider exposing a search + execute_code pair instead of individual MCP tools
- The crossover point is roughly 6 tool calls — below that, direct MCP tools are simpler and sufficient
- Local MCP (filesystem, shell, git) remains appropriate — the token cost is low and the sandboxing overhead is unnecessary
- Subagent isolation (giving a task its own context window) is a complementary strategy that works with either pattern

## Security

- Code execution requires a sandboxed runtime — the agent's generated code must not escape the sandbox
- The pattern shifts trust from tool-definition validation to code-sandbox containment
- API credentials must be available inside the sandbox without leaking into the prompt context