---
name: atuin
title: Atuin
url: "https://github.com/atuinsh/atuin"
category: cli-tool
summary: "Shell history replacement backed by SQLite — records exit code, duration, cwd, hostname, session per command; full-screen search UI; encrypted sync across machines via Atuin server (self-hosted or cloud); supports bash/zsh/fish/nushell/xonsh/PowerShell; Rust; MIT"
tags: [shell-history, search, sync, encryption, sqlite, cli, rust, productivity, cross-machine]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

Atuin replaces the default shell history with a SQLite database that records additional context: exit code, command duration, timestamp, working directory, hostname, and session ID. Full-screen search UI rebinds ctrl-r and up arrow (configurable).

Key features:
- Same history across terminals, sessions, and machines
- Encrypted sync via Atuin server (self-hosted or cloud — end-to-end encrypted, server cannot read your data)
- Filter modes: current session, current directory, or global history
- Statistics (most used commands, etc.)
- Quick-jump to previous items with Alt-\<num\>
- Advanced search: `atuin search --exit 0 --after "yesterday 3pm" make`
- Does not replace the old history file

Supports: zsh, bash, fish, nushell, xonsh, PowerShell.

## Mechanical details

Install: `curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh`. Then `atuin register`, `atuin import auto`, `atuin sync`.

Self-hosted server available. Community forum at forum.atuin.sh. Discord and IRC (#atuin on libera.chat).

## Security

MIT licensed. End-to-end encrypted sync — server operator cannot access command history. Local database stored in SQLite.

## Usage notes

- Also installable via Homebrew (`brew install atuin`), alongside the curl installer recorded above (source: https://www.instagram.com/reel/DeIm-UyIzbz/)
