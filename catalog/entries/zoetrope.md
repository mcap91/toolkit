---
name: zoetrope
title: Zoetrope
url: "https://github.com/furkankly/zoetrope"
category: cli-tool
summary: "Rust TUI that visualizes Claude Code sessions as live flow graphs — reads JSONL transcripts from ~/.claude/projects/, shows agents/subagents/workflows as nodes with tool calls, status, and token counts; time-travel scrubbing, live following, gap compression, agent detail panels with prompts and tool timings; also runs in-browser via WASM; zero network, read-only; MIT"
tags: [claude-code, visualization, tui, rust, observability, session-replay, flow-graph, wasm, ratatui]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

Zoetrope reads Claude Code's JSONL session transcripts and renders them as a live, interactive flow graph in the terminal or browser. Each agent (main session, subagents, workflow children) appears as a node with status, current tool, tool count, and output tokens. Edges animate while agents work.

Key capabilities:

- **Live following**: Point at a running session and it updates in real-time as new events append. Point at a finished transcript and it replays paced by the session's own timestamps.
- **Time travel**: Scrubbable timeline indexed by event (not wall-clock). Seek backwards to see the session exactly as it stood at that moment — agents un-finish, tool counts fall, the graph shrinks back.
- **Agent inspection**: Click any agent for its spawn prompt, reasoning, model, and every tool call with timings. Session info overlay shows mode, permissions, queued ops, file edits, last prompt.
- **Headless mode**: `zoe inspect <file.jsonl>` prints the session tree without a TUI — works in CI or pipelines.
- **Browser version**: Same engine compiled to WASM via ratzilla. Drop a transcript on the hosted page for the same graph, fully local.
- **Zero network**: No HTTP client in the dependency tree. `tokio` pulled without `net` feature. Verifiable via `cargo tree`.

**Usage:**
```
zoe                          # follow current project's live session
zoe <file.jsonl>             # replay a recording
zoe <file.jsonl> --follow    # open at live edge
zoe <file.jsonl> --speed N   # playback speed (default 8.0)
```

## Mechanical details

Built on ratatui (TUI framework), rataflow (node-graph widget), ratzilla (WASM backend). Portable core library with no IO compiles for any target. Two separate frontends: native (`zoe` binary) and browser (`zoetrope-web` crate). Install via Homebrew, Cargo, or prebuilt binaries (macOS/Linux/Windows). Reads the undocumented Claude Code JSONL transcript format — degrades gracefully on unrecognized records.

## Security

MIT licensed. Read-only — never writes to transcripts or makes network requests. Zero network dependency is a verifiable property (`cargo tree`), not just a claim. Transcripts stay on-device; browser version runs fully local in WASM.

## How to use it

brew install furkankly/tap/zoetrope
