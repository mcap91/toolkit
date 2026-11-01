---
name: tldr-pages
title: tldr-pages
url: "https://github.com/tldr-pages/tldr"
category: cli-tool
summary: "Community-maintained simplified man pages — practical examples for common CLI commands; covers UNIX/Linux/macOS/FreeBSD/Windows/Android/Cisco IOS; official clients in Python, Rust (tlrc), and Node.js; web client with offline PWA; 40+ language translations; CC BY 4.0"
tags: [man-pages, cheatsheets, cli, documentation, examples, community, cross-platform]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: CC-BY-4.0
security_flags: []
source: unknown
---

## What it does

tldr-pages provides simplified, example-focused help pages for command-line tools as a complement to traditional man pages. Instead of exhaustive documentation, each page shows the most common use cases with practical examples.

Coverage: UNIX, Linux, macOS, FreeBSD, NetBSD, OpenBSD, SunOS, Android, Windows, Cisco IOS, and DOS commands.

Official clients: Python (`pipx install tldr`), Rust (`brew install tlrc` / `cargo install tlrc`), Node.js (`npm install -g tldr`). Web client at tldr.inbrowser.app with offline PWA support. PDF versions available for offline use.

40+ language translations. Community-maintained via GitHub PRs.

## Mechanical details

Pages are written in Markdown. Contributing is straightforward — add examples or new pages via pull request.

Similar projects: cheat.sh (aggregates from multiple sources), devhints, eg, navi (interactive cheatsheet), Cheat, Command Line Interface Pages.

## Security

CC BY 4.0 licensed. No network calls beyond fetching page content. No telemetry.