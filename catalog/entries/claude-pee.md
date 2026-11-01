---
name: claude-pee
title: claude-pee
category: cli-tool
summary: "PTY wrapper driving interactive CLI; inherently brittle, breaks on CLI version changes"
tags: [pty, automation, cli, dispatch]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it does

`claude-pee` is a PTY wrapper that drives the Claude Code interactive CLI programmatically by injecting keystrokes and reading terminal output. It attempts to automate headless dispatch by treating the interactive terminal session as a subprocess target. Because it depends on the exact output format and interactive behavior of the CLI, it breaks whenever Claude Code updates its terminal UI.

## Assessment

PTY automation is inherently brittle: any CLI version change that alters prompt text, cursor behavior, or output formatting will silently break automation. It provides no durability guarantees and adds a fragile intermediary layer between dispatch and the model. The kb dispatch requirement is a durable, version-stable integration surface — PTY scraping is the opposite.

## Mechanical details

Not recommended for install. No stable package source identified. Rejected in WK-0003 research as a dispatch path.

## Security

License is unknown — no stable package source was identified for this tool, so no license terms are available. The security_flags list is empty because no specific vulnerabilities or red-flag behaviors were documented; the tool was rejected on reliability grounds rather than security grounds.

The primary risk profile is operational rather than security-related: PTY automation grants the wrapper full read/write access to the terminal session, which means any malformed input injection or output-parsing bug could produce unintended CLI actions. Because no stable distribution exists and the tool is not recommended for install, there is no supply-chain surface to evaluate. Risk is rated low-but-moot — the verdict is skip, so installation is not expected.
