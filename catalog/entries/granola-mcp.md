---
name: granola-mcp
title: Granola MCP
url: "https://www.granola.ai/blog/granola-mcp"
category: mcp-server
summary: "MCP server from Granola that gives AI tools (Claude, ChatGPT, Cursor, Claude Code) access to meeting notes — search conversations, pull context, create follow-ups from what was discussed; remote server at mcp.granola.ai/mcp; requires paid Granola plan"
tags: [mcp-server, meetings, notes, context, granola]
reviewed: 2026-07-06
acquired: 2026-07-06
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it does

MCP server that connects AI tools to Granola's meeting notes. Once connected, the AI tool can access the user's meeting transcripts and notes on demand — search past conversations, pull relevant context into current work, create action items and follow-ups.

**Use cases from announcement:**
- In Claude Code or Cursor: create tickets for bugs discussed in meetings, scaffold features based on agreements
- Sprint planning: update Linear boards from standup notes
- Sales calls: draft CRM notes from actual discussion
- Proposals: use discovery conversations as context

## Differentiators

- **First-party MCP** from Granola (the meeting notes product)
- **Native integrations** in Claude (Settings → Connectors) and ChatGPT (Settings → Apps) — search for "Granola" and toggle on
- **Manual connection** for Cursor, Claude Code, or any MCP client via `https://mcp.granola.ai/mcp`
- Enterprise plan available with admin controls, usage monitoring, advanced access controls (early access beta, off by default)

## Mechanical details / What to adopt

- **Claude/ChatGPT:** Settings → Connectors/Apps → search "Granola" → authenticate → toggle on
- **Claude Code / Cursor:** connect manually using URL `https://mcp.granola.ai/mcp`
- Requires paid Granola plan
- Enterprise: admin-toggled in Settings > Security

## Security

Proprietary/commercial service. Requires Granola account authentication. Enterprise plan has admin controls and is off by default. Meeting notes are transmitted to the connected AI tool when requested. No self-hosted option mentioned.