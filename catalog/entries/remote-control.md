---
name: remote-control
title: Remote Control
category: reference
summary: built-in feature; try for long sessions
tags: [mobile, remote, sessions]
reviewed: 2026-05-25
acquired: 2026-05-25
url: "https://code.claude.com/docs/en/remote-control"
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it says

A built-in Claude Code feature for managing running agent sessions from a mobile device. Allows monitoring and directing long-running sessions without being at the workstation. Sourced from a Reddit r/ClaudeCode post.

## Assessment

Already available as a native capability — no installation required. Worth trying during long bioinformatics pipeline runs where you want to check session status or redirect the agent without being at the machine.

## What to adopt

Try `/remote-control` during the next long-running session (pipeline execution, large dataset processing). No setup needed beyond knowing the feature exists.

## Security

Remote Control makes outbound HTTPS connections only and never opens inbound ports on the local machine. When a session starts, Claude Code registers with the Anthropic API and polls for work; messages between the remote client and the local session are routed through the Anthropic API over TLS. The connection uses multiple short-lived credentials, each scoped to a single purpose and expiring independently, so a leaked credential cannot be reused for unrelated operations.

Access requires a claude.ai subscription with OAuth authentication — API keys and third-party providers (Bedrock, Vertex, Foundry) are not supported. On Team and Enterprise plans, an admin must explicitly enable Remote Control in organization settings, and IT administrators can disable it at the device level via managed settings. Because the session runs entirely on the local machine, the local filesystem, MCP servers, and project configuration are never transferred to Anthropic infrastructure; the cloud interface is a thin relay window into the local process.
