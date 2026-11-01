---
name: firecrawl
title: Firecrawl
url: "https://github.com/firecrawl/firecrawl"
category: framework
summary: "Production-grade web scraping/search/interaction API for AI agents — clean markdown output, JS rendering, anti-bot handling, Agent endpoint with Spark models, Map/Interact/Batch Scrape, MCP server mode; 9 SDKs, AGPL-3.0, YC-backed"
tags: [web-scraping, mcp-server, rag, agent-infrastructure, markdown]
reviewed: 2026-08-17
acquired: 2026-06-19
license: AGPL-3.0-only
security_flags: []
overlaps: [crawl4ai, browser-use]
source: unknown
---

## What it does

Firecrawl is a web data API that turns websites into LLM-ready content. Core endpoints:

- **Scrape**: Extract any URL as clean markdown, HTML, screenshots, or structured JSON. Handles JavaScript rendering, proxies, and anti-bot measures. P95 latency 3.4s.
- **Search**: Web search with full page content from results in one call.
- **Interact**: Scrape a page then continue working with it — click buttons, fill forms, extract dynamic content via natural language or code.
- **Agent**: Autonomous data gathering with Spark models (spark-1-mini for most tasks, spark-1-pro for complex research). Describe what you need; no URLs required. Supports structured output via Pydantic schemas.
- **Crawl**: Scrape all URLs of a website with a single request.
- **Map**: Discover all URLs on a website instantly, with optional search-based relevance ranking.
- **Batch Scrape**: Scrape thousands of URLs asynchronously.

GitHub org migrated from `mendableai` to `firecrawl`. SDKs in Python, Node.js, Go, Java, Elixir, Rust, Ruby, .NET, and PHP. Ships an MCP server for direct integration with Claude Code, Cursor, Windsurf, and other MCP clients. Also available as a CLI skill (`npx firecrawl-cli@latest init --all --browser`).

Cloud-hosted service with free and paid tiers. Self-hosting is free under AGPL-3.0 but excludes managed-only features.

## Assessment

Strong production web scraping infrastructure. The Agent endpoint with Spark models is the biggest v2 addition — it turns Firecrawl from a scraping API into an autonomous web research tool. The MCP server mode makes it immediately useful for agent workflows that need web content — literature searches, documentation fetching, data extraction from bioinformatics portals. Overlaps with Crawl4AI (async crawler, MIT) but Firecrawl is more polished, better maintained, and has richer features. The tradeoff is AGPL-3.0 copyleft vs Crawl4AI's MIT license.

For our catalog MCP server's `fetch-url` tool, Firecrawl could serve as an upstream provider for harder-to-scrape sites. The MCP server mode is the most relevant integration path.

## Mechanical details

- **Install MCP**: `npx -y firecrawl-mcp` with `FIRECRAWL_API_KEY` env var, or full skill init: `npx -y firecrawl-cli@latest init --all --browser`
- **Cloud API**: Requires API key from firecrawl.dev
- **Self-host**: Docker compose available in repo; AGPL-3.0 applies
- **SDK install**: `pip install firecrawl-py` / `npm install firecrawl` / `go get github.com/firecrawl/firecrawl/apps/go-sdk`
- 9 SDK languages: Python, Node.js, Go, Java, Elixir, Rust, Ruby, .NET, PHP
- Covers 96% of the web per their benchmarks
- Agent onboarding skill: `curl -s https://firecrawl.dev/agent-onboarding/SKILL.md`

## Security

- **License**: AGPL-3.0 — copyleft; any network-accessible service using Firecrawl code must release source. Self-hosting is free but commercial SaaS embedding requires license review. SDKs and some UI components are MIT-licensed.
- **Supply chain**: YC-backed company, active contributor base, regular releases with CVE patches. Organization migrated from mendableai to firecrawl on GitHub.
- **Code quality**: Tests, CI, multiple SDK maintainers. SSRF hardening in Playwright service.
- **API key handling**: Cloud mode requires API key storage; standard practice.
