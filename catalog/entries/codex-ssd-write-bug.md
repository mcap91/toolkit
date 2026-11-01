---
name: codex-ssd-write-bug
title: Codex Desktop SSD Write Issue
url: "https://reddit.com"
category: reference
summary: "Codex Desktop's logs_2.sqlite writes ~7MB/s continuously (~222TB/year annualized); disable analytics first, SQLite trigger workaround cuts 96.5% — cautionary reference for long-running AI tool resource costs"
tags: [codex, operational, ssd, logging, resource-management]
reviewed: 2026-06-22
acquired: 2026-06-22
license: ""
security_flags: []
overlaps: [codex-memory-cleanup]
source: unknown
---

## What it says

Measured analysis of Codex Desktop's local logging on an always-on Mac. The `~/.codex/logs_2.sqlite` process writes ~846MB per 2-minute sample (~7MB/s). Annualized at sustained rate: ~222TB/year. The author's internal SSD reports 54.8TB total written with 2% wear, so this is meaningful but not immediately catastrophic.

Key findings:
- SQLite file size (~1.8GB) understates actual write volume — WAL checkpointing rewrites pages
- The write rate is from continuous inserts into the `logs` table
- Casual users (few hours/day) are unlikely to notice
- Heavy users running Codex as persistent automation layer should check

## Assessment

Useful operational awareness for anyone running Codex long-term. The broader lesson applies to all long-running AI tools (Claude Code, Cursor, etc.): persistent agents convert human-driven burst IO into continuous machine IO, amplifying small per-turn costs. Worth checking `~/.codex/` periodically.

Related to the existing `codex-memory-cleanup` entry which covers state/log file maintenance for performance.

## Mechanical details

**Low-risk mitigation** — disable analytics:
```toml
# ~/.codex/config.toml
[analytics]
enabled = false
```

**Aggressive mitigation** — SQLite trigger to block log inserts (96.5% write reduction):
```bash
sqlite3 ~/.codex/logs_2.sqlite "PRAGMA busy_timeout=10000; CREATE TRIGGER IF NOT EXISTS block_log_inserts BEFORE INSERT ON logs BEGIN SELECT RAISE(IGNORE); END;"
```

**Rollback**:
```bash
sqlite3 ~/.codex/logs_2.sqlite "DROP TRIGGER IF EXISTS block_log_inserts;"
```

**Check trigger exists**:
```bash
sqlite3 ~/.codex/logs_2.sqlite "SELECT name, sql FROM sqlite_master WHERE type='trigger';"
```

Note: uninstalling Codex does not remove `~/.codex/` — the trigger persists. Reinstalling won't revert it.

## Security

No security concerns — operational diagnostic information. The SQLite trigger approach trades diagnostic capability for reduced disk wear.