---
name: hve-core
title: HVE Core (Hypervelocity Engineering Core)
url: https://github.com/microsoft/hve-core
source_url: https://www.instagram.com/reel/DevVu5tSU18/
source: instagram
category: skill
summary: Microsoft's open-source agentic SDLC framework for GitHub Copilot — specialized agents (research/plan/implement/review via an RPI methodology), coding-standard instructions applied automatically, and reusable skills (slash-command entry points) encoding ~80 organizational standards, security/compliance processes, and architecture-review practices; central principle 'AI carries the rules, humans keep the judgment.' Installed as a VS Code extension or Copilot CLI plugin (copilot plugin marketplace add microsoft/hve-core); explicitly flagged by Microsoft as a highly opinionated, rapidly evolving framework best treated as a source of patterns rather than a stable production dependency. MIT, with OWASP-derived skill content under CC BY-SA 4.0.
tags:
  - github-copilot
  - agentic-sdlc
  - prompt-engineering
  - coding-standards
  - agents
  - skills
  - microsoft
  - rpi-methodology
  - open-source
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT (core); CC BY-SA 4.0 (OWASP-derived skill content)
security_flags: []
overlaps: []
---

## What it does

A structured component library for GitHub Copilot that replaces ad hoc, re-explained-every-session AI guidance with reusable, team-shared building blocks:
- **Agents** for specialized roles — research, planning, implementation, and review — driven by an "RPI" (Research, Plan, Implement, Review) methodology.
- **Instructions** that apply coding standards automatically rather than requiring the operator to restate them.
- **Skills** that add reusable workflows and tool capabilities, including slash-command entry points, encoding roughly 80 organizational standards plus security, compliance, and architecture-review processes directly into the workflow.

Stated central principle: "AI carries the rules, humans keep the judgment" — the AI carries context/standards/process guidance through a task, while people retain responsibility for judgment, tradeoffs, review, and decisions.

**Install:** the HVE Core VS Code extension (then select "RPI Agent" from Copilot Chat's agent picker), or for GitHub Copilot CLI, `copilot plugin marketplace add microsoft/hve-core` followed by `copilot plugin install hve-core@hve-core`. An "HVE Builder" skill (`/hve-builder`) helps adapt or copy patterns into an independently-maintained agentic SDLC.

**Microsoft's own caution, stated directly in the README:** HVE Core is "a highly opinionated, rapidly evolving agentic SDLC framework" whose workflows, interfaces, architecture, and practices "may change substantially, including in ways that are not backward compatible" — it is recommended as a source of patterns and learning, not as a stable platform, foundation, or production dependency.

**Repo signals:** CodeQL security analysis and OpenSSF Scorecard/Best Practices badges; governance, security policy, and a Responsible AI Transparency Note documented separately (GOVERNANCE.md, SECURITY.md, TRANSPARENCY-NOTE.md).

## Sources

- [microsoft/hve-core — GitHub README](https://github.com/microsoft/hve-core) — architecture, install paths, Microsoft's own stability caveat, licensing split (fetched directly).

## Security

MIT-licensed, with skill content derived from OWASP Foundation publications separately licensed CC BY-SA 4.0 (each affected skill identifies this in its own frontmatter plus a third-party attribution section). Microsoft publishes CodeQL and OpenSSF Scorecard/Best Practices badges, a SECURITY.md vulnerability-reporting policy, and a Responsible AI Transparency Note covering intended uses, limitations, and the responsibility boundary between HVE Core and the host platform (GitHub Copilot). Microsoft itself flags the framework as rapidly evolving and not backward-compatibility-guaranteed — a direct operational-risk disclosure for anyone depending on it as infrastructure rather than a pattern reference.
