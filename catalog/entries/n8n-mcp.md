---
name: n8n-mcp
title: n8n MCP Server
url: "https://github.com/czlonkowski/n8n-mcp"
category: mcp-server
summary: powerful workflow automation bridge but heavy dependency; evaluate when pipeline orchestration needs outgrow kb dispatch
tags: [mcp, n8n, workflow-automation, orchestration, integrations]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: [api-key-required, credentials-exposure-risk, production-workflow-ai-edit-warning]
overlaps: [gstack]
source: unknown
---

## What it does

An MCP server that connects AI assistants (Claude, Copilot, Cursor) with n8n's workflow automation platform. Provides 20+ tools for node search/retrieval/validation, workflow CRUD, execution management, credential handling, and security auditing. Covers 1,851 n8n nodes (822 core + 1,029 community), 2,352 workflow templates, and 265 AI-capable tool variants. Offers a cloud dashboard (100 free daily calls), self-hosting via npx/Docker/Railway, and IDE-specific integration guides. 21.3k stars, 1,016+ commits.

## Assessment

kb dispatch already handles our orchestration needs (subagent dispatch, handoff lifecycle). n8n would add value for external service integrations (Slack notifications, webhook triggers, scheduled pipeline monitoring) that kb doesn't cover natively. However, it's a heavy dependency (n8n instance + API keys + MCP server) for capabilities we don't currently need. Revisit when we have concrete automation requirements connecting bioinformatics pipelines to external systems (e.g., triggering Nextflow runs from webhooks, posting QC results to Slack).

## Mechanical details

- Quick start: cloud dashboard at dashboard.n8n-mcp.com (100 daily calls, no install)
- Self-host: `npx @czlonkowski/n8n-mcp` or Docker
- Requires `N8N_API_URL` and `N8N_API_KEY` for workflow management
- Claude Code integration via `.mcp.json` configuration
- Safety emphasis: never edit production workflows directly with AI

## Security

- **License:** MIT — no copyleft, no commercial restrictions on library or self-hosted use.
- **API key exposure:** the management tool set requires `N8N_API_URL` and `N8N_API_KEY` in the MCP environment; any process that can invoke the MCP server inherits full n8n API access, including credential read/write and workflow deployment. Scope the API key to the minimum required permission and never pass it through shared environment variables in multi-user setups.
- **Production workflow risk:** the upstream README carries an explicit safety warning — AI-generated workflow edits should always be tested in a development environment first, never applied directly to production. The `n8n_audit_instance` tool performs security scanning of the n8n instance itself, which is useful for hardening before connecting an AI agent. The project documents a dedicated "Security & Hardening" guide covering trust model and workflow restrictions.

## How to use it

npx @czlonkowski/n8n-mcp
