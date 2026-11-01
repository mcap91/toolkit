---
name: lazygit
title: lazygit
url: "https://github.com/jesseduffield/lazygit"
category: cli-tool
summary: "Terminal UI for git — interactive staging (hunks/lines), interactive rebase (squash/fixup/drop/edit/reorder), cherry-pick, bisect, worktrees, custom patches, undo/redo via reflog, commit graph, diff comparison, GitHub PR integration; Go; MIT"
tags: [git, tui, terminal, interactive-rebase, staging, go, productivity, version-control]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

lazygit provides a full terminal UI for git operations. Makes complex git workflows accessible without memorizing commands.

Key features:
- **Stage hunks or lines**: focus a file's diff, stage hunks with space, switch to line-by-line with `a`, range select with `v`
- **Interactive rebase**: press `i` to start, then squash/fixup/drop/edit/move commits; also works as one-off operations
- **Cherry-pick**: copy commits with Shift+C, paste with Shift+V
- **Bisect**: mark commits good/bad with `b`
- **Worktrees**: create from branches with `w` for parallel work without stashing
- **Custom patches**: extract hunks from old commits, move to new commits, apply in reverse
- **Undo/redo**: `z`/Shift+Z via reflog
- **Commit graph**: visual graph with author colors and parent highlighting
- **Diff comparison**: mark a commit with Shift+W, select another to compare
- **GitHub PR integration**: shows PR status icons on branches (requires `gh` CLI), Shift+G opens PR in browser
- **Custom commands**: flexible system for adding your own operations
- **Filter**: `/` to filter any view

## Mechanical details

Install: `brew install lazygit`, `sudo pacman -S lazygit`, `scoop install lazygit`, `choco install lazygit`, `winget install lazygit`, `go install`, or binary releases.

Alias recommendation: `alias lg='lazygit'`. Supports changing directory on exit. Configurable via YAML. Git flow support when installed.

## Security

MIT licensed. No network calls beyond git operations. No telemetry.

## Usage notes

- Default keybindings beyond staging: `c` opens the commit prompt, Shift+P pushes the current branch (source: https://www.instagram.com/reel/DeIm-UyIzbz/)
