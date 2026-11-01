---
name: ergon-wrong-turn-logger
title: ergon-wrong-turn-logger
url: "https://github.com/ergon-automation-labs/ergon-wrong-turn-logger"
category: cli-tool
summary: "CLI that logs development 'wrong turns' (bad assumptions, missed edge cases, broken designs) to a searchable local SQLite database, with list/stats/search commands; framed for solo, team, and AI-assisted workflows."
tags: [decision-log, knowledge-capture, sqlite, retrospective, lessons-learned, bash, cli]
reviewed: 2026-07-22
acquired: 2026-07-22
license: MIT
security_flags: [install-sh-script]
overlaps: []
source: unknown
---

## What it does

A command-line tool that records "wrong turns" — bad assumptions, missed edge cases, or designs that broke — to a searchable SQLite database at `~/.ergon/wrong-turns.db`. Each entry captures a type (technical/process/pattern), a description, a "should have done" correction, and optional impact, tags, and project. Commands: `log` (via flags or interactive prompts), `list` (last 10, filterable by `--type`), `stats` (counts by type), `search "<term>"`, and `init`. The README frames three use cases — individual retrospection, shared team knowledge, and logging corrections when an AI assistant (e.g. Claude) suggests something wrong — and positions the tool within a broader "agent-operable infrastructure" methodology, closing with a consulting pitch from Ergon Automation Labs.

## Assessment

A single-purpose logger: a bash CLI plus a local SQLite schema (`wrong_turns` with id, timestamp, type, description, should_have_done, impact, tags, project). It performs no network calls, contacts no external services, and contains no AI/LLM integration itself — the "AI workflow" framing refers to a human manually logging AI mistakes. The repository README doubles as marketing for a paid consulting engagement. License is MIT.

## Mechanical details

- **Install:** `git clone … && cd ergon-wrong-turn-logger && ./install.sh` — installs the `ergon-wrong-turn` command to `~/.local/bin/` and creates the database at `~/.ergon/wrong-turns.db`. Manual path: copy `bin/ergon-wrong-turn` to `~/.local/bin/`, `chmod +x`, `mkdir -p ~/.ergon`, then `ergon-wrong-turn init`
- **Log:** `ergon-wrong-turn log --type technical --description "…" --should-have-done "…" --impact "…"`, or bare `log` for interactive prompts
- **Query:** `list` (optionally `--type technical|process`), `stats`, `search "<term>"`
- **Storage:** SQLite table `wrong_turns` (id, timestamp, type, description, should_have_done, impact, optional tags, optional project)

## Security

License is MIT. The adoption surface is an `install.sh` shell script that copies a CLI into `~/.local/bin/` and initializes a SQLite database under `~/.ergon/`; the documented manual-setup path performs the same steps without running the script, so the installer can be bypassed after review. The tool runs locally with no documented network access, no credential handling, and no external service calls. Data is stored as plaintext SQLite on the local filesystem, so anything written into a description or impact field is readable by any local process. `security_flags` reflects the shell-script installer. Test/CI presence was not verified from the README.