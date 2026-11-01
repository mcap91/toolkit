---
name: emdly
title: emdly
url: "https://emdly.com/"
category: framework
summary: "Platform for discovering, comparing, and sharing SKILL.md files for AI agents — curated marketplace with human review and sandboxed safety screening; CLI installer (npx @emdly/cli add), synced to public GitHub repo (emdly-stack); ~24+ skills across engineering (PR review, debugging, commit messages, dependency upgrades), analytics (GA4 funnels, SQL explainer, dashboard metrics), content (SEO briefs, brand voice, landing pages), ops (incident postmortem, K8s triage, standup synthesis), commerce (product feeds, cart sequences), and gaming (balance review, playtest triage)"
tags: [agent-skills, marketplace, skill-md, discovery, cli, curated, community, cross-platform]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [skills-cli, agent-skills-spec, community-skills-stack-2026]
license: Unknown
security_flags: [license-unclear]
source: unknown
---

## What it does

emdly is a curated marketplace for SKILL.md files — structured instruction files for AI coding agents. It provides discovery, comparison, and one-command installation of skills across domains.

Key capabilities:

- **Curated marketplace**: Skills are human-reviewed and pre-screened in a sandboxed AI environment for safety before publishing.
- **CLI installer**: `npx @emdly/cli add <publisher>/<skill>` installs any skill. Compatible with Claude Code, Codex, OpenClaw, and other agents that support the SKILL.md format.
- **Public GitHub sync**: The full collection is synced to a public `emdly-stack` GitHub repo, so skills aren't locked inside the platform.
- **Publisher namespacing**: Skills are addressed as `publisher/skill-name` (e.g., `kernelpanic/pr-review-ritual`, `sevzero/incident-postmortem`).

**Notable skills in the catalog:**
- `querydeck/sql-query-explainer` — explains SQL queries in plain language, flags missing indexes
- `shopmetric/ga4-funnel-analyst` — finds checkout funnel drop-offs by step, device, source
- `pixelforge/playtest-feedback-triage` — sorts playtest notes into balance, UX, bugs, feel
- `sevzero/incident-postmortem` — drafts blameless postmortems from timeline + channel export
- `kernelpanic/pr-review-ritual` — structured code review discipline for agents
- `sevzero/k8s-incident-triage` — ranks probable causes from kubectl output, read-only commands only
- `shiplog/changelog-composer` — turns merged PRs into human-readable changelogs
- `promptsmith/skill-author-guide` — how to write skills that pass emdly review

## Security

License unclear — not documented on the site. Skills are human-reviewed and sandboxed before publishing. The public GitHub sync provides transparency into published content. Individual skills should be reviewed before installation as with any third-party code.

## How to use it

npx @emdly/cli add <publisher>/<skill>
