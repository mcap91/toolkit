---
name: slack-mcp-server-korotovsky
title: Slack MCP Server (korotovsky)
url: "https://github.com/korotovsky/slack-mcp-server"
category: mcp-server
summary: "Feature-rich MCP server for Slack workspaces — 18 tools covering channel history, thread replies, message search, unread messages, DMs/group DMs, message posting, reactions, saved items, user search, user groups; stealth mode (no bot install required), OAuth mode, Enterprise/GovSlack support; Go, Stdio/SSE/HTTP transports; MIT"
tags: [mcp-server, slack, messaging, workspace, enterprise]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

MCP server for Slack workspaces providing 18 tools across messaging, search, reactions, saved items, and user management. Supports three authentication modes: stealth (browser tokens xoxc/xoxd, no bot install or permissions needed), OAuth (xoxp user tokens), and bot (xoxb, limited access). 30,000+ monthly visitors, 9,000+ users.

**18 tools:**
1. `conversations_history` — channel/DM messages with smart date/count-based limits
2. `conversations_replies` — thread messages with pagination
3. `conversations_add_message` — post to channels/DMs (disabled by default, channel-restrictable)
4. `conversations_search_messages` — search with filters (date, user, channel, mentions, threads-only)
5. `channels_list` — list channels with type filtering and popularity sorting
6. `reactions_add` / `reactions_remove` — emoji reactions (disabled by default)
7. `users_search` — search by name/email/display name, returns DM channel ID
8. `usergroups_list` / `create` / `update` / `users_update` / `me` — full user group management
9. `conversations_unreads` — unread messages across all channels with priority sorting (DMs > partner > internal)
10. `conversations_mark` — mark as read (disabled by default)
11. `saved_list` / `saved_update` / `saved_clear_completed` — Slack "Save for Later" management

## Differentiators

- **Stealth mode** — works with browser tokens (xoxc/xoxd) without requiring bot installation, OAuth app creation, or any workspace permissions
- **Smart history** — fetch by date ranges (1d, 7d, 1m, 90d) or message count, not just cursor pagination
- **Unread priority sorting** — DMs > partner channels (Slack Connect) > internal channels, with @mention filtering
- **Write safety** — message posting, reactions, and mark-as-read all disabled by default; enable per-channel via env vars with allowlist/blocklist syntax
- **Enterprise/GovSlack** — `SLACK_MCP_GOVSLACK` routes to slack-gov.com FedRAMP-compliant endpoints
- **Three transports** — Stdio, SSE, HTTP with proxy support
- **Resource endpoints** — `slack://<workspace>/channels` and `slack://<workspace>/users` expose workspace directories
- **User/channel caching** — local cache files for faster access; #name and @user lookups

## Mechanical details / What to adopt

- **Install:** `npx` or `go run mcp/mcp-server.go --transport stdio`
- **Auth options:** xoxc+xoxd (stealth), xoxp (user OAuth), xoxb (bot, limited)
- **Key env vars:** `SLACK_MCP_ADD_MESSAGE_TOOL` (enable posting, `true` or comma-separated channel IDs), `SLACK_MCP_REACTION_TOOL`, `SLACK_MCP_MARK_TOOL`, `SLACK_MCP_ENABLED_TOOLS` (whitelist specific tools)
- **Cache:** users and channels cached to OS-specific cache directories
- **Debugging:** MCP Inspector support via `npx @modelcontextprotocol/inspector`

## Security

MIT licensed. Write operations disabled by default with granular per-channel enable via env vars. Stealth mode uses browser session tokens which bypass Slack's OAuth permission model — powerful but the tokens grant the same access as the logged-in user. Custom TLS handshake and proxy support for enterprise environments. Not an official Slack product.