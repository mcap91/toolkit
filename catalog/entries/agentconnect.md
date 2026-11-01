---
name: agentconnect
title: AgentConnect
url: "https://github.com/agentconnect-md/agentconnect"
category: framework
summary: "Open-source multi-agent platform where teams and AI agents collaborate across Slack, Telegram, Discord, Lark, GitHub, GitLab, Gitea, and Linear — agents can call one another, carry memory/skills, and work from messages, issues, PRs, webhooks, or schedules; supports Claude Code, Codex, Grok Build, DeepSeek, Pi, and any ACP-compatible runtime; self-hosted Docker/K8s; Apache-2.0"
tags: [multi-agent, platform, slack, discord, github, orchestration, acp, collaboration, self-hosted]
reviewed: 2026-09-14
acquired: 2026-09-14
license: Apache-2.0
security_flags: []
overlaps: [a2a-protocol, agent-link]
source: unknown
---

## What it does

AgentConnect is an open-source platform for multi-agent and human-agent collaboration across communication and development platforms. Teams create agents with different roles, link them to bots in Slack/Telegram/Discord/Lark or repositories on GitHub/GitLab/Gitea/Linear, and let them work alongside humans in shared conversations.

Core capabilities:
- **Multi-runtime**: Claude Code, Codex, Grok Build, DeepSeek, Pi, and any ACP-compatible agent runtime run side by side
- **Cross-platform**: agents connect to Slack, Telegram, Discord, Lark, GitHub, GitLab, Gitea, Linear
- **Agent-to-agent**: agents can call one another within workflows
- **Memory and knowledge**: each agent gets its own memory and skills; reviewed Knowledge is published for all agents to find on demand
- **Triggers**: work starts from messages, issues, PRs, webhooks, or schedules
- **Access control**: per-agent visibility, repository/tool permissions, and agent-to-agent call policies

Use cases: issue triage with multi-agent investigation, cross-workspace support, recurring operations with human-in-the-loop, upstream fork monitoring, customized multi-reviewer code review.

Architecture:
- **Daemon**: runs agents over ACP, owns workspaces/session state, maintains platform connections and schedules, sends model traffic directly
- **Relay** (optional): accepts callback ingress and webchat, proxies MCP and OpenConnector access
- **Control Plane + Web UI**: manages auth, config, placement, permissions, metadata, observability; stores approved organization knowledge

## Mechanical details

- **Stack**: Node >= 24.12.0, pnpm 11, PostgreSQL
- **Deployment**: Docker Compose (default loopback/no-auth for eval) or Helm chart (`oci://ghcr.io/agentconnect-md/charts/agentconnect`)
- **Setup**: ships a setup skill for Claude Code/Codex that runs an interactive tutorial
- **Auth**: Logto-based browser auth; configurable GitHub, Slack, Google, Lark/Feishu apps
- **Optional**: Mem0 for agent memory

## Security

- **License**: Apache-2.0
- **Self-hosted**: full stack runs in your environment
- **Default loopback**: Docker Compose binds to 127.0.0.1 with local no-auth for evaluation
- **Data plane isolation**: live messages and ACP streams stay on daemon/relay; Control Plane stores only coordination metadata, not message bodies or attachments
- **Resilience**: if Control Plane is unavailable, established sessions and daemon-local schedules continue