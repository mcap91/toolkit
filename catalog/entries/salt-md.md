---
name: salt-md
title: salt.md
url: https://github.com/saltmd/salt.md
category: framework
summary: Self-hosted open-source workspace for people and AI agents — single static Go binary with embedded frontend, SQLite storage, and a built-in MCP server so Claude, Codex, Cursor, Gemini CLI, ChatGPT or any MCP client read and write the same pages and databases under the same per-person permissions; block editor, typed collections (select/date/person/relation/rollup/formula) with table/board/list/gallery/calendar/timeline/form views, full-text search, realtime co-editing, comments, activity log, graph view; macOS/Linux desktop shell; used for task pages where agents leave 'why' notes so another agent can pick up the work; AGPL-3.0
tags:
  - workspace
  - knowledge-base
  - mcp-server
  - self-hosted
  - go
  - sqlite
  - agent-handoff
  - cross-agent
  - notion-alternative
  - realtime-collaboration
  - kanban
  - wiki
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - kb
  - openwiki
  - storybloq
  - agent-session-resume
license: AGPL-3.0
security_flags:
  - curl-pipe-sh-install
  - network-service
  - copyleft-license
  - new-project
source: unknown
---

## What it does

salt.md is a self-hosted documentation and project workspace (Notion-like) whose MCP server ships inside the same binary, so AI agents operate on the same pages, databases, search, comments, and presence as human users, with the same permissions. The author's stated use (r/vibecoding, Oct 2026): every task gets a page; the agent reads the rules on that page, does the work, and leaves notes there; when switching from Claude Code to Codex, the next agent reads the notes and continues. Lesson stated: make agents record why they did something, not only what. Commenters compared it to Obsidian or a `/docs` folder plus CHANGELOG.md/DECISIONS.md; the author positions per-task pages as the difference.

## Mechanical details

- Server: one Go binary (CGO disabled, pure-Go SQLite driver) with embedded frontend; data is one SQLite file plus an uploads directory. Linux/macOS (amd64, arm64), Windows (amd64).
- Install: `curl -fsSL https://raw.githubusercontent.com/saltmd/salt.md/main/install.sh | sh`, or `docker run -d -p 8420:8420 -v salt-data:/data ghcr.io/saltmd/salt.md:latest`.
- Desktop app: macOS/Linux window onto a self-hosted server; mobile via PWA (native iOS planned).
- MCP tools cover pages, databases, search, bulk imports, comments, presence. Agents act with the access of the person whose credentials they carry; the server explicitly refuses agent actions such as account creation, token issuance, backups, and settings changes.
- Features: block editor with slash menu, typed collections, multiple views, full-text search, live cursors, comments/activity log, graph visualization.
- ~168 stars, Go, ~206 commits at review.

## Security

AGPL-3.0 (network-use copyleft applies if modified and offered as a service). Runs as a network service on port 8420; exposure depends on deployment. Install script is curl-piped to sh (review before running, or use the Docker image). Agent access is permission-scoped per user, with administrative actions denied to agents. No telemetry described in the README.

## Usage notes

- Author confirmed (r/vibecoding, Oct 2026): the wiki is currently searchable only through an agent, with a direct search UI acknowledged as a planned gap; the native iOS app in progress is specifically Swift, and Android has no work started yet. The marketing video for salt.md was itself produced with Claude Code (Opus 5.5), [[hyperframes]] for rendering, and [[elevenlabs]] for music/voiceover (source: https://www.reddit.com/r/vibecoding/comments/1wyxpef/look_what_i_built/)
