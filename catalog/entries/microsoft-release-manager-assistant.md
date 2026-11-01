---
name: microsoft-release-manager-assistant
title: Release Manager Assistant (RMA)
url: "https://github.com/microsoft/release-manager-assistant"
category: framework
summary: "Microsoft solution accelerator that augments release managers with a multi-agent system (Planner, JIRA Agent, Azure DevOps Agent via MCP, Visualization Agent, Fallback Agent) for cross-system release planning, scheduling, and readiness reporting; built on Azure AI Foundry + Microsoft Agent Framework + Redis; ships mock/synthetic-data MCP servers for JIRA and Azure DevOps so it can be evaluated without live system access; MIT"
tags: [azure, multi-agent, mcp, azure-devops, jira, agent-framework, azure-ai-foundry, redis, release-management, solution-accelerator]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: [jira-http-basic-auth-not-for-production, byoai-only-no-shared-quota]
overlaps: []
source: unknown
---

## What it does

A multi-agent assistant for the software release-management lifecycle: a Planner agent routes natural-language queries to specialized agents — a JIRA Agent (JQL-optimized issue queries with custom-field support), an Azure DevOps Agent (via a dedicated MCP server: work items, builds/releases, repos/PRs, teams/iterations), a Visualization Agent (interactive charts via Azure AI Foundry's code interpreter), and a Fallback Agent for graceful degradation when an upstream service is unavailable. Aims to replace manually compiled cross-system release-readiness reports and dependency mapping with a single conversational interface.

## Differentiators / Key takeaways

- Ships mock MCP servers with synthetic JIRA and Azure DevOps data (`USE_JIRA_MCP_SERVER`, `USE_AZURE_DEVOPS_MCP_SERVER` env vars) so the accelerator can be evaluated end-to-end without live JIRA/DevOps credentials.
- BYOAI-only: the repo states it currently only supports bring-your-own-Azure-OpenAI scenarios "due to resource quota issues" — no shared/pooled quota path.
- Azure DevOps integration goes through a dedicated MCP server with auto-discovery of tools/capabilities rather than a hand-rolled REST client, and supports both Azure CLI and Personal Access Token auth.
- Uses Redis for session management and WebSocket message queuing (the Session Manager must be running before the frontend will connect) and Azure Key Vault + Azure Storage for secret/data management.

## Mechanical details / What to adopt

- Prerequisites: Azure subscription with AI Foundry access, Node.js 20+ (Azure DevOps MCP server), Python 3.12 (agent runtime), Docker runtime, VS Code recommended.
- Deploy via the linked deployment guide (`azd`-based, per repo convention); local dev supported.
- Frontend is React/Vite; documented troubleshooting covers WebSocket/Session Manager ordering issues and Node version conflicts (16+ recommended for the frontend build despite the 20+ MCP server requirement).
- MIT license, per repo README ("This project is licensed under the MIT License. See LICENSE for details.").

## Security

MIT-licensed. Uses Key Vault-managed secrets and supports PAT or Azure CLI auth for Azure DevOps. The repo carries an explicit, self-reported warning that its JIRA plugin "uses HTTP BASIC authentication which is not recommended for Production workloads" and instructs users to configure OAuth-based token auth themselves before production use. Azure DevOps API access inherits whatever permissions are granted to the configured PAT/identity — the repo notes access is "subject to user permissions" and to configure scopes carefully for the MCP server's full tool surface (work item write access, build/release data, repo/PR access).
