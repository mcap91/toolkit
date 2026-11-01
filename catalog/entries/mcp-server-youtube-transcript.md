---
name: mcp-server-youtube-transcript
title: MCP Server YouTube Transcript
url: "https://github.com/kimtaeyoon83/mcp-server-youtube-transcript"
category: mcp-server
summary: "MCP server exposing a single get_transcript tool for YouTube videos — language fallback, optional timestamps, ad-strip filtering, zero transcript-fetch dependencies; fills the YouTube-to-markdown gap for learning-vault capture"
tags: [mcp, youtube, transcript, video, media-ingestion]
reviewed: 2026-06-19
acquired: 2026-06-19
license: MIT
security_flags: [single-contributor]
overlaps: []
source: unknown
---

## What it does

MCP server that retrieves transcripts/captions from YouTube videos via a single `get_transcript` tool. Accepts full URLs, Shorts URLs, or bare video IDs. Features:

- **Language fallback**: requests a language code (default `en`), falls back automatically to available languages
- **Timestamps**: optional `[0:05]`-style timestamp prefixes per line
- **Ad stripping**: filters sponsorship/ad segments using chapter markers (on by default)
- **Zero external dependencies** for the transcript fetch itself (uses YouTube's internal caption endpoint)

Installable via npx (`@kimtaeyoon83/mcp-server-youtube-transcript`) — no build step for end users.

## Assessment

Directly useful for capturing lecture and conference video content into markdown for agent-readable knowledge bases. The single-tool surface is clean and the ad-strip feature is a practical differentiator over raw transcript dumps. Combined with faster-whisper (for caption-less videos), this covers the YouTube ingestion pipeline.

Single contributor is the main risk — bus factor 1. The tool relies on YouTube's undocumented caption endpoint, which could break without notice (same risk as youtube-dl/yt-dlp transcript features). No rate-limiting or auth, so bulk use may hit YouTube's abuse detection.

## Mechanical details

- **Runtime**: Node.js 18+, stdio transport
- **Install**: `npx -y @kimtaeyoon83/mcp-server-youtube-transcript` in MCP config
- **Tool**: `get_transcript` — params: `url` (required), `lang` (optional), `include_timestamps` (optional), `strip_ads` (optional)
- **Testing**: has test suite (`npm test`) and MCP eval harness
- **Config**: standard MCP server JSON block in Claude Desktop or `.mcp.json`

## Security

- **License**: MIT — no restrictions
- **Dependencies**: claims zero external deps for transcript fetching; npm package has standard MCP SDK deps
- **Code quality**: tests exist, eval harness, MCP Inspector debugging documented
- **Supply chain**: single contributor (kimtaeyoon83), published on npm, Smithery-listed
- **Dangerous patterns**: none observed — input validation documented, timeout handling, graceful error handling
- **Maintenance**: active as of review date, listed in awesome-mcp-servers