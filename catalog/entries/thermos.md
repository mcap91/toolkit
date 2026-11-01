---
name: thermos
title: Thermos (Thermo-Nuclear Review, Cursor Plugin)
url: https://github.com/cursor/plugins/tree/main/thermos
source_url: https://www.instagram.com/reel/DePGBFXtswr/
source: instagram
category: plugin
summary: "Cursor plugin running two parallel diff-scoped review subagents and synthesizing deduped findings: thermo-nuclear-review (deep branch audit for bugs, breakages, security, devex, feature-gate leaks) and thermo-nuclear-code-quality-review (strict maintainability audit — 'code judo' restructurings, a 1,000-line file limit, spaghetti-conditional growth, architectural-boundary leaks). Supersedes the thermo-nuclear-code-quality-review skill previously shipped standalone in Cursor's cursor-team-kit plugin. MIT; installs via /add-plugin thermos."
tags:
  - cursor
  - plugin
  - code-review
  - code-quality
  - security-audit
  - subagents
  - mcp
  - open-source
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags: []
overlaps:
  - pstack
  - ponytail
---

## What it does

A Cursor plugin for running an unusually strict, two-pronged review against a git branch/diff:
- **`thermo-nuclear-review`** — a deep audit for bugs, breakages, security issues, developer-experience problems, and feature-gate leaks.
- **`thermo-nuclear-code-quality-review`** — a strict maintainability audit looking specifically for "code judo" opportunities (behavior-preserving restructurings that make code dramatically simpler), enforcing a 1,000-line file-size rule, flagging ad-hoc conditional/spaghetti growth, and checking architectural boundary leaks.

The top-level `thermos` skill runs both as parallel, diff-scoped subagents (`thermo-nuclear-review-subagent`, `thermo-nuclear-code-quality-review-subagent`) against `git diff main...HEAD` plus the full contents of changed files, then synthesizes a prioritized, deduplicated finding list. Either review can also be invoked standalone, in the main agent or via its matching subagent, after gathering the same diff context.

**History:** `thermo-nuclear-code-quality-review` previously shipped alone inside Cursor's `cursor-team-kit` plugin; Thermos absorbed it alongside the new deep-review skill and the orchestrating `thermos` skill. The README instructs removing the old `cursor-team-kit` thermo entries when installing Thermos, to avoid duplicates.

**External reception** (per independent review, not Thermos's own docs): one practitioner running it against recent commits on an open-source project found roughly 5 of 7 suggestions genuinely useful; the broader characterization is that the rubric's ambition produces more false positives but also surfaces real issues that would otherwise be missed, and that it has no dedicated focus on tests or seams.

**Install:** `/add-plugin thermos`.

## Sources

- [cursor/plugins/thermos — README](https://github.com/cursor/plugins/tree/main/thermos) — architecture diagram, skill/agent table, migration note from cursor-team-kit (fetched directly).
- [Can Cursor's HARDCORE Review Skill Stop The Slop? — daily.dev](https://daily.dev/posts/can-cursor-s-hardcore-review-skill-stop-the-slop--sjkerp9tv) — independent trial (5/7 useful findings), noted gap around test/seam coverage.

## Security

MIT. First-party Cursor plugin in the official `cursor/plugins` monorepo. Functions as a strict code-review rubric plus subagent orchestration — it reads diffs and file contents and produces findings; it does not itself execute or modify code. No dangerous runtime components identified at review time.
