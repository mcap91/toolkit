---
name: automation-credit-dependency
title: Automation Credit Dependency Pattern
url: "https://reddit.com"
category: agent-pattern
summary: Map who gets credit for the work before automating it — treat visibility as a technical dependency; invisible automation can damage careers even when it works perfectly
tags: [automation, human-factors, workflow-design, agent-pattern]
reviewed: 2026-06-22
acquired: 2026-06-22
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it says

Practitioner account of automating an ops coordinator's 3-hour daily exception-handling workflow (Shippo → Airtable → Slack) into a 20-minute sanity check via n8n. The automation worked perfectly but made the coordinator's contribution invisible — she was pulled into a performance review because her manager could no longer see her work. The CEO had previously name-dropped her as the person "keeping the trains running."

The author's takeaway: during discovery, ask "who gets credit for the work I'm about to automate?" and "who looks good because this thing runs the way it runs?" Treat that answer as a technical dependency — same weight as API keys or credentials.

## Assessment

Directly applicable to agent-assisted automation design. When building agents that automate human workflows, the credit/visibility dependency is real and non-obvious. Concrete mitigations mentioned: keep the person on approvals, build a daily digest with their name on it, route notifications through them. The pattern generalizes: any automation that removes a human from a visible loop should include a visibility-preservation mechanism.

## What to adopt

- Add "credit dependency" as a discovery question when designing automation agents
- When automating a workflow, identify the human whose reputation depends on that work being visible
- Build in visibility mechanisms: approval gates, named digests, attribution in notifications
- If the automation removes someone from a Slack channel's daily flow, replace that signal with something equivalent

## Security

No security considerations — this is a design pattern, not software.