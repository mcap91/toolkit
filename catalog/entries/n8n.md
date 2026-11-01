---
name: n8n
title: n8n
url: "https://github.com/n8n-io/n8n"
category: framework
summary: "Fair-code workflow automation platform (TypeScript) — visual node-based editor plus custom JS/Python code, 400+ integrations, native AI/agent capabilities (LangChain-based AI nodes, MCP client and server support), triggers/webhooks/schedules; self-hostable via Docker or paid n8n Cloud; Sustainable Use License + n8n Enterprise License (fair-code, not OSI open source); ~204k stars"
tags: [workflow-automation, low-code, integrations, self-hosted, ai-agents, mcp, typescript, ipaas, fair-code]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-SUL-fair-code
security_flags: [fair-code-license-restrictions, workflow-credential-store]
overlaps: [n8n-mcp, langflow]
source: unknown
---

## What it does

n8n is a workflow automation platform combining a visual node-graph editor with custom code (JavaScript/Python nodes). Workflows connect 400+ built-in integrations (SaaS APIs, databases, files, messaging) through triggers (webhooks, schedules, app events) and data-transforming nodes. Native AI capabilities are first-class: LangChain-based AI Agent nodes, model nodes for all major providers, vector-store nodes, and MCP support in both directions (n8n as MCP client calling external tools; n8n exposing workflows as an MCP server) — reflected in its `mcp`, `mcp-client`, `mcp-server` repo topics.

Deployment is self-hosted (Docker, npm) or the paid n8n Cloud. The visual editor, execution history, credential vault, and error-workflow mechanics are the operational core.

## Differentiators

- The dominant self-hostable alternative in the Zapier/Make space (~204k stars, ~61k forks — one of GitHub's largest projects), with per-node data inspection while debugging.
- Code-when-you-need-it: any node's output can be transformed with real JS/Python rather than expression-language-only.
- The AI-agent story is integrated rather than bolted on: agent nodes, tool-calling against any of the 400+ integrations, and MCP interop make it a common orchestration substrate for agent workflows.
- Fair-code model: source-available with revenue-generating restrictions, funding a commercial company (n8n GmbH; raised at a multi-billion valuation in 2025-26 on AI-automation growth).

## Mechanical details

- Self-host: `docker run -it --rm -p 5678:5678 n8nio/n8n` (or `npx n8n`); production setups add Postgres, queue mode (Redis + workers), and webhook processors.
- Workflows are JSON documents — exportable, versionable, and generatable by LLMs; a large template library exists at n8n.io/workflows.
- TypeScript; ~204k stars, 1,142 open issues; created 2019; pushed same day as review; docs at docs.n8n.io.

## Security

- **License:** `fair-code-license-restrictions` — Sustainable Use License + n8n Enterprise License, not OSI-approved open source; free to self-host for internal business purposes, but embedding/reselling and offering n8n-as-a-service are restricted.
- `workflow-credential-store` — n8n centralizes credentials for every connected system; a compromised n8n instance yields all of them. Encryption at rest uses an instance key (`N8N_ENCRYPTION_KEY`) the operator must manage; exposed editors/webhooks need auth and network controls.
- Community nodes are npm packages installed at the operator's risk — third-party supply chain surface.
- Large company-backed project with an established security process and regular releases.