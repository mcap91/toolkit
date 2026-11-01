---
name: codex-memory-cleanup
title: Codex Memory Cleanup
category: reference
summary: "operational tip: delete state/log/global-state files if Codex performance degrades"
tags: [codex, maintenance, performance]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it says

An operational tip from Reddit r/codex: if Codex performance degrades (slow responses, stale context, erratic behavior), deleting accumulated state and log files restores baseline performance. Three files accumulate over time and are safe to delete: `.codex/state_5.sqlite`, `.codex/logs_2.sqlite`, and `.codex/.codex-global-state.json`. Codex recreates them on the next run.

## Assessment

Not a tool or skill — a maintenance procedure. Worth noting because performance degradation from accumulated state is non-obvious and the fix is not documented in standard Codex docs. Relevant if Codex is used alongside Claude Code on this machine.

## What to adopt

If Codex performance degrades, delete these files before escalating to other debugging steps:
- `.codex/state_5.sqlite`
- `.codex/logs_2.sqlite`
- `.codex/.codex-global-state.json`

These files are in the Codex data directory (typically `~/.codex/` or the project `.codex/` folder depending on configuration).

## Security

This entry describes a local file deletion procedure, not a third-party tool — there is no installation surface and no network activity involved. The files targeted (`.codex/state_5.sqlite`, `.codex/logs_2.sqlite`, `.codex/.codex-global-state.json`) are local SQLite databases and a JSON state file written by Codex itself; deleting them carries no supply-chain or injection risk.

The only security consideration is accidental data loss: the procedure is irreversible (no backup step). Users with meaningful conversation history stored in the global-state file should confirm they do not need to recover that data before deleting. No elevated privileges are required and the operation has no effect on system files outside the `.codex/` directory.
