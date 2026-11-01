---
name: shannon
title: Shannon (AI Pentester)
url: "https://github.com/KeygraphHQ/shannon"
category: framework
summary: "Autonomous white-box AI pentester that analyzes source code and executes real exploits against web apps/APIs; AGPL-3.0, proof-by-exploitation reports, but actively mutates target state and requires authorization context"
tags: [security, pentesting, web-security, exploitation, owasp, ai-agent, docker, anthropic]
reviewed: 2026-06-17
acquired: 2026-06-17
license: AGPL-3.0-only
security_flags: [executes-exploits, mutates-target-state, agpl-copyleft, llm-cost-significant]
overlaps: []
source: unknown
---

## What it does

Shannon Lite is an autonomous, white-box AI pentester for web applications and APIs. It analyzes source code to identify attack vectors, then uses browser automation and CLI tools to execute real exploits against a running application. Only vulnerabilities with a working proof-of-concept make it into the final report.

Multi-agent architecture:
1. **Pre-reconnaissance** — scans source code for frameworks, entry points, data flows, attack surfaces
2. **Reconnaissance** — explores the live app, correlates runtime behavior with code context
3. **Vulnerability analysis** — specialized agents for Injection, XSS, SSRF, Authentication, Authorization
4. **Exploitation** — attempts real PoC attacks, discards unproven hypotheses
5. **Reporting** — compiles validated findings with evidence and remediation guidance (Markdown)

Runs in an ephemeral Docker container with isolated workspace. Supports authenticated testing (login flows, TOTP, test credentials), resumable workspaces, and configurable rules of engagement.

## Assessment

Shannon addresses a real gap: AI-accelerated code shipping outpaces annual penetration test cycles. The proof-by-exploitation approach (only report what you can actually exploit) produces high-signal reports — demonstrated against OWASP Juice Shop (20+ vulns), c{api}tal (15 critical), and crAPI (15+ critical).

However, significant constraints:
- **AGPL-3.0** — copyleft obligations limit commercial embedding
- **Actively mutates state** — creates users, submits forms, triggers outbound requests. Must run against sandboxed/staging environments only
- **Cost** — 1-1.5 hours per full run with significant LLM API costs
- **Claude-dependent** — officially supported only with Claude models; other models may be unstable
- **Prompt injection risk** — scanning untrusted codebases exposes the AI to adversarial content
- **No external contributions** — Keygraph doesn't accept PRs; issues only for bugs/features

For this project, Shannon is relevant for security testing agent infrastructure (web APIs, MCP servers) before deployment. Not directly bioinformatics-related, but valuable for hardening any web-facing tools we build.

## Mechanical details

- Install: `npx @keygraph/shannon setup` (interactive wizard)
- Run: `npx @keygraph/shannon start -u https://your-app.com -r /path/to/repo`
- Requires: Docker, Node.js 18+, Anthropic API credentials
- Shannon Pro: commercial edition adds black-box testing, SAST, CI/CD gating, SLA tracking, enterprise deployment
- Community office hours: Thursdays (US/EU + Asia time slots)

## Security

- **License**: AGPL-3.0 (Lite), commercial (Pro)
- **Supply chain**: Keygraph (commercial company), no external contributions accepted. Docker Hub worker image
- **Dangerous patterns by design**: this tool executes real exploits — that's its purpose. The safety boundary is authorization context and target environment isolation
- **Prompt injection surface**: AI agents reading source code can be manipulated by adversarial code
- **Model dependency**: Claude models required; alternative models may produce incomplete/unstable results