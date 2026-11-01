---
name: inbox-zero
title: Inbox Zero
url: "https://github.com/elie222/inbox-zero"
category: framework
summary: "AI-powered self-hostable email management app — strong open-source email assistant, not a developer/agent toolkit."
tags: [email, ai-assistant, gmail, productivity, self-hosted, open-source]
reviewed: 2026-06-10
acquired: 2026-06-10
license: AGPL-3.0
security_flags: [requires-oauth-credentials, processes-email-content, cloud-or-self-hosted]
overlaps: []
source: unknown
---

## What it does

Inbox Zero is a full-stack, AI-powered email management web application. It connects to Gmail (and Microsoft accounts) via OAuth and applies AI rules to automatically organize, label, archive, and draft replies to emails. The AI assistant learns the user's tone and style to pre-draft replies, can block cold emails, and tracks which threads need a response (Reply Zero feature). It integrates with Slack and Telegram so users can manage their inbox from those apps without opening Gmail.

Beyond basic AI sorting, Inbox Zero offers: a bulk unsubscriber that detects and unsubscribes from mailing lists in one click, a bulk archiver for cleaning old emails, email analytics dashboards showing activity trends, meeting briefs that pull context from email and calendar before scheduled meetings, and smart filing that auto-saves attachments to Google Drive or OneDrive.

The project is positioned as an open-source, self-hostable alternative to Fyxer. It has a hosted SaaS offering at getinboxzero.com and supports self-hosting via a one-command Docker CLI setup (`npx @inbox-zero/cli setup`). The stack is Next.js + Prisma + Upstash + Turborepo, with Docker images published on every main-branch commit.

## Assessment

Inbox Zero is a polished, actively maintained consumer/prosumer email productivity application. It is not a developer toolkit, agent framework, MCP server, or composable skill — it is a standalone platform for managing one's personal inbox. Its value is clear for end-user email management, but it does not integrate into agentic coding workflows or bioinformatics pipelines in any direct way.

A `note` verdict is appropriate here: the project is cataloged for awareness (it's a strong open-source AI email tool worth knowing about), but it is not something to adopt into agentic development workflows. The Slack/Telegram integration and "AI rules in plain English" design pattern are worth noting as reference points for anyone building similar AI-driven communication automation.

The AGPL-3.0 license means any derivative service that is deployed publicly must also be open-sourced — relevant if someone were to embed or fork this for a custom tool.

## Mechanical details

Self-hosting is via Docker + Node.js v24+:

```
npx @inbox-zero/cli setup   # one-time wizard (sets up OAuth, env, DB)
npx @inbox-zero/cli start   # starts containers
# then open http://localhost:3000
```

For local development: clone the repo, run `docker compose -f docker-compose.dev.yml up -d` (Postgres + Redis), install with pnpm, run `npm run setup` for env config, migrate with Prisma, then `pnpm dev`. Google and Microsoft OAuth emulators are available for local development without live credentials.

Docker images are auto-built on every push to main and tagged with the commit SHA; the `latest` tag always points to the newest main build; formal releases use semver tags (e.g., `v2.26.0`).

## Security

License is AGPL-3.0, which requires derivative services deployed publicly to release their source. This is a strong copyleft license — relevant if forking or embedding for a custom deployment.

The application requires broad OAuth scopes to read, categorize, and draft email on the user's behalf. All email content flows through the application and through AI model API calls if using the hosted version. Security considerations:

- `requires-oauth-credentials`: Needs Gmail/Microsoft OAuth tokens with broad mailbox access.
- `processes-email-content`: All email bodies and metadata pass through the system and through AI APIs; sensitive correspondence is exposed to the AI provider.
- `cloud-or-self-hosted`: The hosted version (getinboxzero.com) processes your email on third-party infrastructure; self-hosting mitigates this concern.

No dangerous code patterns (eval, shell injection) are evident from the README. The project has CI/CD via GitHub Actions with Docker images built on every push, indicating active testing infrastructure. Self-hosting is the recommended path for privacy-sensitive deployments.
