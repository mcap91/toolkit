---
name: claude-peers-mcp
title: Claude Peers MCP
url: "https://github.com/louislva/claude-peers-mcp"
category: mcp-server
summary: "Novel multi-session peer messaging, but mandatory --dangerously-skip-permissions flag is a hard blocker for safe use"
tags: [multi-agent, inter-session, messaging, coordination, broker, sqlite, bun, orchestration]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-unknown
security_flags: [dangerously-skip-permissions-required, dangerously-load-development-channels-required, no-tests-observed, no-ci-observed, single-contributor, optional-openai-key-exfil-risk]
overlaps: []
source: unknown
---

## What it does

Claude Peers MCP is an MCP server that lets multiple concurrently running Claude Code instances on the same machine discover each other and exchange messages in real time. A local broker daemon (localhost:7899, SQLite backend) acts as the hub. Each Claude Code session registers with the broker via a stdio MCP server; inbound messages are pushed into the session via the `claude/channel` protocol for immediate delivery. Four tools are exposed: `list_peers` (discover running instances with directory, git repo, and summary), `send_message` (send to a peer by ID), `set_summary` (describe what you're working on), and `check_messages` (polling fallback). A CLI (`bun cli.ts`) allows out-of-band inspection and message injection. Optionally, setting `OPENAI_API_KEY` triggers an auto-summary call to `gpt-5.4-nano` on startup.

## Assessment

The peer-discovery and real-time messaging concept is genuinely novel and fills a gap — coordinating work across multiple simultaneous Claude Code sessions currently requires manual copy-paste or shared files. However, the quick-start instructions require two flags that are hard blockers for routine adoption: `--dangerously-skip-permissions` (bypasses all tool-call permission prompts) and `--dangerously-load-development-channels` (loads an unstable, pre-release channel protocol). Running with `--dangerously-skip-permissions` permanently removes the human-in-the-loop safety gate that prevents runaway tool calls. Until the channel protocol stabilizes and the permissions bypass is no longer required, this is a watch item rather than something to pilot in production workflows.

## Mechanical details

- **Runtime**: Bun (TypeScript); requires Bun and Claude Code v2.1.80+.
- **Broker**: auto-launches on first session start; listens on `localhost:7899`; SQLite database at `~/.claude-peers.db` (configurable via `CLAUDE_PEERS_DB`); auto-cleans dead peers.
- **Transport**: stdio MCP server per session; messages delivered via `claude/channel` push protocol.
- **Registration**: `claude mcp add --scope user --transport stdio claude-peers -- bun ~/claude-peers-mcp/server.ts` (user-scoped, available in every session).
- **Start command**: `claude --dangerously-skip-permissions --dangerously-load-development-channels server:claude-peers` — the alias `claudepeers` is suggested.
- **Auto-summary**: optional; requires `OPENAI_API_KEY`; calls `gpt-5.4-nano` to summarize working directory context on startup.
- **CLI**: `bun cli.ts status | peers | send <id> <msg> | kill-broker` for out-of-band management.
- **Config env vars**: `CLAUDE_PEERS_PORT` (default 7899), `CLAUDE_PEERS_DB`, `OPENAI_API_KEY`.
- **Auth**: requires claude.ai login; API-key-only auth does not support the channel protocol.

## Security

- **License**: Not stated in fetched content; marked `LicenseRef-unknown` pending inspection of the repository.
- **`--dangerously-skip-permissions`**: This flag disables Claude Code's permission prompt system entirely. Any MCP tool or shell command the agent calls during the session runs without confirmation. Combined with peer messaging (external input arriving over the broker), this creates a prompt-injection-to-unrestricted-execution path if a peer message contains adversarial instructions.
- **`--dangerously-load-development-channels`**: Loads a pre-release, unstable channel protocol. Behavior and security properties are not guaranteed.
- **Broker injection**: `bun cli.ts send <id> <msg>` lets any local process inject messages into a Claude session, bypassing the MCP input path. On a shared machine this is a lateral-movement vector.
- **OpenAI key leakage**: If `OPENAI_API_KEY` is set, the startup auto-summary call sends working-directory and git metadata to OpenAI. This is opt-in but worth noting for air-gapped or sensitive environments.
- **No tests or CI observed**: No evidence of a test suite or continuous integration in the README; code quality and regression safety are unknown.
- **Single contributor**: Supply-chain risk is higher with a solo-maintainer project at an early stage.
- **localhost-only**: The broker binds to localhost, which limits network attack surface, but the injection risk from local processes remains.
