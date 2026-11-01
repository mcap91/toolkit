---
name: strands-agents
title: Strands Agents SDK
url: "https://github.com/strands-agents/harness-sdk"
category: framework
summary: "Open-source Python/TypeScript SDK for building and running AI agents in-process — agent loop with lifecycle controls, tools, MCP, multi-agent patterns, memory/sessions, guardrails, tracing, and evals; defaults to Amazon Bedrock with Anthropic, OpenAI, Gemini, and Ollama provider support"
tags: [agent-framework, agent-harness, agent-loop, multi-agent, model-agnostic, mcp, python, typescript, guardrails, tracing, bedrock]
reviewed: 2026-09-16
acquired: 2026-09-16
license: Apache-2.0
security_flags: []
overlaps: [crewai, smolagents, deepseek-harness, harnessx]
source: unknown
---

## What it does

Strands Agents is an open-source SDK for building and running AI agents in Python and TypeScript. It runs in-process (no hosted control plane) and positions itself as a replacement for a hand-rolled agent loop, bundling: lifecycle controls (turn limits, token budgets, cancellation, stop reasons), tools and structured output, MCP client/server support, multi-agent patterns, memory and sessions, model-provider portability, streaming (including an experimental bidirectional-streaming mode), guardrails, hooks that can intercept and redirect any step of the loop, steering handlers for self-correction, tracing, and evals.

The repo (`strands-agents/harness-sdk`) is a monorepo containing: `strands-py/` (Python SDK — agent loop, model providers, tools), `strands-ts/` (TypeScript SDK — same scope), `site/` (the strandsagents.com documentation site, Astro/Starlight), and `team/` (governance docs: tenets, decisions, PR/compatibility guidelines, design proposals). It consolidates what were previously separate `sdk-python` and `sdk-typescript` repos.

Model support is provider-agnostic: both SDKs default to Amazon Bedrock (Claude Sonnet via Bedrock, requiring AWS credentials), with first-class support for Anthropic, OpenAI, and Gemini plus additional and custom providers (Ollama among them); application code is intended to stay the same when swapping providers.

## Differentiators

- **In-process, no control plane**: runs as a library inside the caller's process rather than requiring a hosted service, distinguishing it from managed agent-platform offerings.
- **Dual-language parity**: Python and TypeScript SDKs are maintained together in one monorepo with shared design docs (`team/`), rather than one language being a port of the other.
- **Explicit lifecycle primitives**: turn limits, token budgets, cancellation, and stop reasons are built into the agent loop rather than left to the caller to implement.
- **Steering handlers**: a mechanism for agents to self-correct mid-run rather than failing silently, described as distinct from guardrails (which block/redirect) and hooks (which observe/intercept).
- **Strands Robots**: an extension allowing agents to interact with robots and devices over Zenoh, AWS IoT, and a "Model Hardware Standard (MHS)"; the project reports a 99.95% score on ARC-AGI-3 using the same minimal harness shipped to production, announced August 27, 2026.
- **Backing/scale signals**: sponsored by Anthropic PBC, Bloomberg, Hudson River Trading, Meta, NVIDIA, and Microsoft, with infrastructure sponsorship from AWS, Datadog, Fastly, Google, Sentry, and Depot; the project reports 25 million downloads and one year of public availability as of May 15, 2026.

## Mechanical details

**Python** (requires Python 3.10+):
```bash
pip install strands-agents strands-agents-tools
```
```python
from strands import Agent
from strands_tools import calculator

agent = Agent(tools=[calculator])
agent("What is the square root of 1764")
```

**TypeScript** (requires Node.js 22+):
```bash
npm install @strands-agents/sdk
```
```typescript
import { Agent } from '@strands-agents/sdk'

const agent = new Agent()
const result = await agent.invoke('What is the square root of 1764?')
console.log(result)
```

Development: `strands-py/` uses `hatch` (`hatch test`, `hatch fmt`); `strands-ts/` uses npm (`npm ci`, `npm run build`, `npm test`) from the repo root; `site/` is a separate Astro project (`npm install`, `npm run dev`, served at `localhost:4321`). Git operations (commits, branches, PRs) are done from the monorepo root. Per web search, the TypeScript SDK reached v1.0 on April 30, 2026, and the latest PyPI package (`strands-agents` 1.56.0) was published September 15, 2026.

Documentation: strandsagents.com (User Guide, Quick Start, Agent Loop, Examples, Production & Deployment Guide, separate Python/TypeScript API references).

## Security

License is Apache-2.0 (`LICENSE.APACHE` in the repo). No installation scripts requiring elevated privileges or curl-pipe execution were observed — both SDKs install via standard package managers (`pip`, `npm`). Default model provider (Amazon Bedrock) requires AWS credentials and Bedrock model access to be configured by the user. The README references a CONTRIBUTING guide for reporting security issues but no vulnerability disclosures or CVEs were surfaced during this review. Backing sponsors include Anthropic, AWS, Microsoft, Meta, and NVIDIA, indicating active multi-organization maintenance.
