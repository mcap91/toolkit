---
name: perplexity-mcp-server
title: Perplexity MCP Server
url: "https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server"
category: mcp-server
summary: "Official Perplexity MCP server providing real-time web search, conversational AI, and advanced reasoning tools to MCP-compatible clients; one-click install for Claude Code, Cursor, Codex; npm package @perplexity-ai/mcp-server; requires Perplexity API key"
tags: [mcp-server, perplexity, web-search, reasoning, ai-search]
reviewed: 2026-07-06
acquired: 2026-07-06
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it does

Official MCP server from Perplexity that connects AI assistants to Perplexity's search and reasoning capabilities. Enables real-time web search, conversational AI, and advanced reasoning within any MCP-compatible client's workflow.

## Differentiators

- **Official first-party** MCP server from Perplexity
- **One-click installers** for Claude Code, Cursor, Codex
- **Broad client support** — Claude Code, Cursor, Codex, Claude Desktop, VS Code, Windsurf, Google Antigravity, and any standard mcpServers-compatible client
- **Multiple install methods for Claude Code:** CLI command (`claude mcp add`), plugin marketplace, or manual JSON config

## Mechanical details / What to adopt

- **Install (Claude Code, recommended):** `claude mcp add perplexity --env PERPLEXITY_API_KEY="your_key" -- npx -y @perplexity-ai/mcp-server`
- **Install (plugin):** `/plugin marketplace add perplexityai/modelcontextprotocol` → `/plugin install perplexity`
- **Install (Codex):** `codex mcp add perplexity --env PERPLEXITY_API_KEY="your_key" -- npx -y @perplexity-ai/mcp-server`
- **Install (Cursor/others):** add to `mcp.json` with `npx -y @perplexity-ai/mcp-server` command
- **npm package:** `@perplexity-ai/mcp-server`
- **Requires:** Perplexity API key
- **Transport:** stdio via npx

## Security

Proprietary/commercial service. Requires Perplexity API key. Search queries are sent to Perplexity's servers. npm package from official Perplexity organization.