---
name: openclaw
title: OpenClaw
url: "https://openclaw.ai/"
category: framework
summary: ecosystem signal for agentic workspaces; not a concrete kb comparison
tags: [assistant, orchestration, local-first, kb]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it does

A local-first assistant orchestration platform with cross-app integrations. Positions itself as an agentic workspace for connecting local tools, assistants, and applications. Ecosystem signal for the direction the local-first AI orchestration space is moving.

## Assessment

OpenClaw is more ecosystem context than a concrete kb comparison. There is no direct feature overlap to analyze — it targets cross-app integration rather than knowledge management or dispatch orchestration. Worth revisiting if kb needs cross-app integration patterns, but not actionable now.

## Mechanical details

Do not install. No concrete concepts identified for adoption into kb. Monitor as ecosystem signal for local-first agentic workspace patterns if the kb roadmap expands toward cross-app integration.

## Security

OpenClaw is self-hosted and local-first — the agent runs on the user's own machine and acts with broad system access (file system, browser, email, calendar, API keys). The marketing site describes instances "accessing your files, Gmail, calendar, everything about you" continuously, and users report it autonomously opening browsers, configuring OAuth tokens, and controlling system processes. The exact license could not be confirmed from public sources; the product is described as open source but the GitHub repository was not reachable at review time.

Because the agent runs with wide OS-level permissions and integrates outbound messaging channels (WhatsApp, Telegram, Discord), the attack surface is broad: compromised skills, prompt injection via messages, or a malicious inbox item could trigger unintended actions. The verdict is skip/ecosystem-signal, so installation is not recommended; if evaluated, scope its permissions tightly and treat inbound messages from external channels as untrusted input.
