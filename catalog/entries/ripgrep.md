---
name: ripgrep
title: ripgrep
url: "https://github.com/burntsushi/ripgrep"
category: cli-tool
summary: "Line-oriented recursive regex search tool — respects .gitignore by default, skips hidden/binary files; SIMD-accelerated Rust regex engine; 3-30x faster than grep/ag/ack on benchmarks; PCRE2 opt-in for look-around; searches compressed files, multiple encodings; static binary; dual MIT/UNLICENSE"
tags: [grep, search, regex, cli, rust, performance, code-search, gitignore]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

ripgrep (`rg`) recursively searches directories for regex patterns. Defaults to respecting .gitignore, skipping hidden files and binary files. First-class Windows/macOS/Linux support.

Performance benchmarks on Linux kernel source (i9-12900K): ripgrep 0.082s vs git grep 0.273s vs ag 0.443s vs GNU grep 0.674s for equivalent searches. On 13GB single-file search: ripgrep 1.042s vs GNU grep 6.577s.

Key features:
- Automatic .gitignore/.ignore/.rgignore filtering (`-uuu` to disable all)
- File type filtering (`-tpy` for Python, `-Tjs` to exclude JavaScript)
- Full Unicode support without performance penalty
- Optional PCRE2 for look-around/backreferences (`-P`)
- Compressed file search (`-z`: brotli, bzip2, gzip, lz4, lzma, xz, zstd)
- Multi-encoding support (UTF-16, latin-1, GBK, EUC-JP, Shift_JIS)
- Replacements/rewriting matched output
- Arbitrary input preprocessing filters
- Configuration file support

## Mechanical details

Install: `brew install ripgrep`, `cargo install ripgrep`, `apt install ripgrep`, `winget install BurntSushi.ripgrep.MSVC`, or binary releases. Binary name is `rg`.

Built on Rust's regex engine: finite automata + SIMD + aggressive literal optimizations. Lock-free parallel recursive directory iterator. Uses RegexSet for gitignore pattern matching.

Minimum Rust 1.96.0 for building from source. Static binary available via MUSL target.

## Security

Dual MIT/UNLICENSE. Single static binary. No network calls. No telemetry.