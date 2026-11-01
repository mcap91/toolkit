---
name: zoxide
title: zoxide
url: "https://github.com/ajeetdsouza/zoxide"
category: cli-tool
summary: Smarter cd command — learns which directories you use most frequently for instant jumps; frecency-based ranking; interactive selection via fzf; supports bash/zsh/fish/nushell/PowerShell/elvish/xonsh/tcsh/POSIX; imports from autojump/z/fasd/atuin; Rust; MIT
tags: [cd, directory-navigation, frecency, shell, cli, rust, fzf, productivity]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

zoxide remembers which directories you visit most frequently and lets you jump to them with a few keystrokes. `z foo` changes to the highest-ranked directory matching "foo". `zi foo` opens interactive fzf selection.

Works like a regular cd for absolute/relative paths, `..`, and `-` (previous directory). Frecency algorithm scores directories by frequency and recency of access.

Supports all major shells: bash, zsh, fish, nushell, PowerShell, elvish, xonsh, tcsh, and any POSIX shell. Imports history from autojump, z, z.lua, zsh-z, fasd, and atuin.

## Mechanical details

Install: `brew install zoxide`, `cargo install zoxide --locked`, `winget install ajeetdsouza.zoxide`, or distro package managers. Setup: `eval "$(zoxide init bash)"` (or equivalent for other shells).

Config via env vars: `_ZO_DATA_DIR` (database location), `_ZO_ECHO` (print matched dir), `_ZO_EXCLUDE_DIRS` (glob exclusions), `_ZO_MAXAGE` (max entries, default 10000), `_ZO_FZF_OPTS` (custom fzf options), `_ZO_RESOLVE_SYMLINKS`.

Optional fzf integration (v0.51.0+) for completions and interactive selection. Tab completion available in bash 4.4+, fish, and zsh.

## Security

MIT licensed. Single static binary. No network calls. Database stored locally.