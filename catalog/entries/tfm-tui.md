---
name: tfm-tui
title: tfm — Terminal File Manager
url: "https://github.com/clarkarch/tfm-tui"
category: cli-tool
summary: "Mouse-first terminal file manager with places sidebar, grid view, drag-and-drop, image/video thumbnails (kitty graphics protocol), dual pane, embedded terminal, network locations (sftp/smb/WebDAV/FTP via gvfs), XDG trash, archive operations, tabs, 30+ themes, TypeScript plugin system; Linux only, built with Bun; MIT"
tags: [file-manager, tui, terminal, kitty-graphics, dual-pane, drag-and-drop, bun, linux, plugins]
reviewed: 2026-09-18
acquired: 2026-09-18
license: MIT
security_flags: [install-script-curl-pipe]
overlaps: []
source: unknown
---

## What it does

tfm is a terminal file manager designed around mouse interaction rather than keyboard-only workflows. Runs inside a terminal emulator but provides GUI-like features: click to select, rubber-band selection, right-click context menus, inline rename, and drag-and-drop between folders.

Key features:
- Dual pane with independent tabs, path bar, sort, and search per side
- Places sidebar with GTK bookmarks, recent files, XDG trash with restore, clipboard
- Image/video thumbnails via kitty graphics protocol (kitty, ghostty, WezTerm, Konsole); falls back to Nerd Font glyphs
- Network locations: sftp://, smb://, WebDAV, FTP via gvfs with in-app credential prompts
- Embedded terminal (right-click → Open Terminal Here)
- Archive extract and compress via right-click menu
- Auto-hide panes: sidebar/preview/terminal collapse to edges and slide back on mouse hover
- TypeScript plugins in ~/.config/tfm/plugins/ with hot reload, custom commands/keybinds, context menus, previews, event hooks, and UI slots

Cross-app drag-and-drop requires kitty. Linux only. Configuration via TOML at ~/.config/tfm/config.toml.

## Security

- License: MIT
- Install: curl-pipe install script available; also buildable from source with Bun
- Platform: Linux only