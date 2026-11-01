---
name: maxun
title: Maxun
url: "https://github.com/getmaxun/maxun"
category: framework
summary: "Capable no-code web data platform with MCP support and LLM extraction, but early-stage and AGPLv3 copyleft limits commercial embedding"
tags: [web-scraping, data-extraction, no-code, mcp-server, llm, crawling, self-hosted]
reviewed: 2026-06-10
acquired: 2026-06-10
license: AGPL-3.0
security_flags: [early-stage, agpl-copyleft, handles-auth-credentials]
overlaps: []
source: unknown
---
## What it does

Maxun is an open-source no-code web data platform that turns websites into structured, API-accessible data without writing code. It has four core robot types: Extract (point-and-click recorder or natural-language LLM mode), Scrape (full page to Markdown/HTML/screenshot), Crawl (multi-page site traversal), and Search (automated web search with time filters). Results can be exported to Google Sheets, Airtable, or consumed via a RESTful API. A developer SDK and CLI exist for programmatic control. The platform also exposes an MCP server interface, making it callable from Claude and other MCP-compatible agents. It handles pagination, infinite scroll, login-gated content, and scheduled runs. Self-hosting is supported via Docker Compose; a hosted SaaS (app.maxun.dev) is also available.

## Assessment

**Watch** — the feature set is genuinely useful for AI agent workflows: LLM-ready Markdown output, MCP integration, and headless scheduling cover real data-ingestion needs in bioinformatics-adjacent research (literature scraping, public database harvesting, clinical trial registries). However, three factors hold it back from pilot:

1. **Early-stage**: The README explicitly warns the project is in early development, meaning breaking changes are likely and API stability cannot be assumed.
2. **AGPLv3 copyleft**: Any service that wraps or integrates Maxun must itself be AGPL-licensed or obtain a commercial license. This sharply limits embedding in proprietary or mixed-license pipelines.
3. **Credential handling scope**: The "extract behind login" feature implies the platform stores or processes credentials — this is a meaningful attack surface that needs vetting before production use.

Once the project matures past early-stage and copyleft implications are evaluated per-deployment, it warrants reassessment at pilot.

## Mechanical details

- **Runtime**: Node.js / TypeScript (inferred from SDK/CLI presence and repository structure); Docker Compose for the full stack
- **Robots**: Four types — Extract (recorder + AI mode), Scrape, Crawl, Search
- **MCP integration**: Exposes an MCP server, allowing Claude Code and other MCP hosts to invoke extraction directly as a tool
- **SDK**: Full programmatic API for scheduling, robot management, and data retrieval
- **CLI**: `maxun` CLI for robot creation, run triggering, and data fetching
- **Outputs**: Structured JSON, Markdown, HTML, screenshots, Google Sheets, Airtable, RESTful endpoints
- **Scheduling**: Built-in cron-style scheduling for unattended runs
- **Self-hosting**: Docker Compose setup; also supports Neon (serverless Postgres) as the backing store
- **AI extraction**: LLM-powered natural language mode — user describes desired data, LLM drives extraction logic

## Security

- **License**: AGPLv3 — strong copyleft; any networked service incorporating Maxun must release source under AGPL or negotiate a commercial license
- **Early-stage flag**: Explicit upstream warning of active, possibly breaking development; not suitable for dependency pinning without vendoring
- **Credential handling**: "Extract Behind Login" implies storage or transit of authentication credentials; the security model for credential storage is not described in the README and requires review before use
- **No code audit evidence**: No mention of security audits, CVE response process, or signed releases in the available content
- **MCP surface**: The MCP server integration means Maxun could be invoked from an agent context; prompt injection via scraped page content reaching the LLM extraction pipeline is a realistic attack vector to assess
- **Supply chain**: Unknown pinning status of transitive dependencies; early-stage projects often have looser lockfile discipline
