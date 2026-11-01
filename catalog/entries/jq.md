---
name: jq
title: jq
url: "https://github.com/jqlang/jq"
category: cli-tool
summary: "Lightweight command-line JSON processor — slice, filter, map, and transform structured data; portable C with zero runtime dependencies; sed/awk/grep for JSON; MIT"
tags: [json, cli, data-processing, filter, transform, c, unix, pipe]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

jq is a command-line JSON processor analogous to sed, awk, and grep but for JSON data. Written in portable C with zero runtime dependencies.

Core operations: slice arrays, filter objects, map values, transform structure, compute aggregates. Expression language supports conditionals, string interpolation, regex, try/catch, reduce, recursive descent, and user-defined functions.

Usage: `cat data.json | jq '.items[] | select(.active) | .name'`

## Mechanical details

Install: prebuilt static binaries from GitHub releases (rename to `jq`, `chmod +x`), Docker image (`ghcr.io/jqlang/jq`), or build from source (requires libtool, make, automake, autoconf).

Documentation at jqlang.org. Interactive playground at play.jqlang.org.

Build from source: `autoreconf -i && ./configure --with-oniguruma=builtin && make -j8`. Static linking: `make LDFLAGS=-all-static`.

## Security

MIT licensed (documentation CC BY 3.0). Zero runtime dependencies. Single static binary. No network calls.

## Usage notes

- Also installable via Homebrew (`brew install jq`), in addition to the release binaries and source build recorded above (source: https://www.instagram.com/reel/DeIm-UyIzbz/)
