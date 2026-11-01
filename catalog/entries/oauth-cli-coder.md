---
name: oauth-cli-coder
title: oauth-cli-coder
category: cli-tool
summary: OAuth-based CLI automation; adds auth complexity without solving durability
tags: [oauth, automation, cli, dispatch]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: [oauth-token-handling, no-stable-package-source]
overlaps: []
source: unknown
---

## What it does

`oauth-cli-coder` automates Claude Code CLI interactions using OAuth-based authentication rather than PTY key injection. It attempts to handle the interactive login and session flow programmatically so that the CLI can be driven in a headless or semi-automated context.

## Assessment

OAuth automation adds significant auth-layer complexity — token management, refresh logic, session state — without addressing the core durability problem of driving an interactive CLI. Dispatch needs a stable protocol surface (MCP or subprocess with defined I/O), not a workaround for the interactive login gate. Rejected in WK-0003 research alongside other TUI automation approaches.

## Mechanical details

Not recommended for install. No stable package source identified. Rejected in WK-0003 research as a dispatch path.

## Security

No stable package source was identified for this tool, which is itself a significant supply-chain risk — there is no canonical repository, versioned release, or maintained owner to audit. Any implementation obtained ad-hoc cannot be verified for integrity.

The OAuth flow introduces credential-handling surface: tokens and refresh credentials must be stored and managed at rest, expanding the local secret footprint beyond the API key that the standard Claude Code CLI requires. Because the tool was evaluated as a research candidate and rejected (verdict: skip), it should not be installed; the risks above reinforce that decision and the `agent-lockdown` skill's install-boundary controls would apply before any reconsideration.
