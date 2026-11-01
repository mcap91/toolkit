---
name: fzf
title: fzf
url: "https://github.com/junegunn/fzf"
category: cli-tool
summary: "General-purpose command-line fuzzy finder and interactive terminal toolkit — processes millions of items in milliseconds; event-driven architecture for custom workflows; shell integration (CTRL-R history, CTRL-T files, ALT-C directories) for bash/zsh/fish/nushell; preview window with image support; popup mode (tmux 3.3+/Zellij); single Go binary; MIT"
tags: [fuzzy-finder, shell, cli, go, interactive, preview, productivity, terminal-toolkit]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

fzf is a general-purpose fuzzy finder for the command line. Pipe any list to it, get interactive fuzzy search with instant results. Also serves as a building block for rich terminal applications via its event-driven architecture.

Key capabilities:
- **Shell integration**: CTRL-R (history search), CTRL-T (file picker), ALT-C (directory jump) for bash, zsh, fish, nushell
- **Fuzzy completion**: `vim **<TAB>`, `cd **<TAB>`, `kill -9 **<TAB>`, `ssh **<TAB>`
- **Preview window**: inline file/image preview with syntax highlighting (via bat/highlight)
- **Display modes**: fullscreen, `--height`, `--popup` (tmux 3.3+/Zellij 0.44+)
- **Search syntax**: fuzzy match, exact (`'word`), prefix (`^music`), suffix (`.mp3$`), inverse (`!fire`), OR (`|`)
- **Programmable bindings**: `become()`, `execute()`, `reload()`, `transform()` for building custom workflows

## Mechanical details

Install: `brew install fzf`, distro packages, `git clone` + install script, or binary releases. Single binary, zero dependencies.

Vim/Neovim plugin via junegunn/fzf + junegunn/fzf.vim (or fzf-lua for Neovim). Style presets: default, full, minimal. Full color/border/label customization.

Performance: optimized for millions of items. `--scheme` option for input-type-specific tuning (default, path, history). Image preview via Kitty graphics protocol, iTerm2 inline images, or Sixel.

## Security

MIT licensed. Single static binary. No network calls. No telemetry.