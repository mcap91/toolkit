---
name: get-shit-done
title: Get Shit Done (GSD)
url: "https://github.com/glittercowboy/get-shit-done"
category: framework
summary: deprecated (moved to GSD Redux); superpowers skill system already covers meta-prompting and spec-driven development
tags: [meta-prompting, context-engineering, spec-driven, claude-md, workflow, kb]
reviewed: 2026-05-25
acquired: 2026-05-25
overlaps: [claude-spellbook]
license: MIT
security_flags: []
source: unknown
---

## What it does

A meta-prompting, context engineering, and spec-driven development system for Claude Code. Provides structured frameworks for organizing developer-AI interactions — agents, commands, hooks, SDKs, and documentation patterns. JavaScript/TypeScript codebase with 2,922 commits and 78 releases. Had 63.7k stars. **Deprecated**: development moved to "GSD Redux" at open-gsd/get-shit-done.

## Assessment

Two reasons to skip: (1) The project is deprecated and no longer maintained at this URL — active development is at a different repository (GSD Redux). (2) Our superpowers skill system already covers the same problem space: brainstorming, writing-plans, executing-plans, subagent-driven-development, verification-before-completion, TDD, systematic-debugging, and dispatching-parallel-agents collectively address meta-prompting, context engineering, and spec-driven development. The superpowers approach is more modular (individual skills triggered contextually) vs. GSD's monolithic framework.

## Mechanical details

- Original repo: github.com/glittercowboy/get-shit-done (deprecated)
- Active fork: github.com/open-gsd/get-shit-done-redux
- JS 73.1%, TS 26.5%, Shell 0.4%
- Not worth tracking the Redux version separately unless it introduces novel patterns beyond our superpowers coverage

## Security

GSD is a prompt-engineering and context-scaffolding framework, not a package that executes arbitrary code at install time. It ships as Markdown files, CLAUDE.md templates, and JavaScript/TypeScript utilities under MIT (Copyright 2025 Lex Christopherson). The MIT license provides no warranty, which is expected for a community project of this type and does not affect adoption risk.

The main supply-chain consideration is that the original repository has migrated twice (glittercowboy → gsd-build → open-gsd/gsd-core), so any CLAUDE.md content ingested from this repo should be treated as potentially stale. No known CVEs, no network-access requirements, no credential handling, and no shell execution at install time. `security_flags` is empty.
