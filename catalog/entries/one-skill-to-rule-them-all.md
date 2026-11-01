---
name: one-skill-to-rule-them-all
title: One Skill to Rule Them All
url: "https://github.com/rebelytics/one-skill-to-rule-them-all"
category: meta-skill
summary: proposes NEW skills from observed patterns; complementary to superpowers routing
tags: [meta-skill, pattern-detection, skill-generation]
reviewed: 2026-05-25
acquired: 2026-05-25
license: CC-BY-4.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Watches your work across sessions, finds repeated patterns in how you fix problems or structure workflows, drafts candidate skills, and suggests updates to existing ones. It operates at the meta level — not executing tasks but observing how tasks get executed and extracting reusable structure from repeated behaviors. Good fit when you notice yourself fixing the same class of mistake repeatedly or repeating the same multi-step setup. Best paired with a strict session-start trigger so it runs consistently.

## Assessment

This is complementary to `superpowers using-superpowers`, not competing with it. Superpowers routes you to skills that already exist. One-skill-to-rule-them-all proposes new skills from patterns it observes — addressing the gap where no skill yet exists for a recurring workflow. Together they form a complete skill lifecycle: observe → propose → route → execute. Piloting is low risk since it only drafts skills for human review rather than auto-installing them.

## Mechanical details

Install from the GitHub repo. Best activated at session start via a hook or trigger in settings.json so it consistently observes work rather than being invoked ad hoc. Review its draft proposals before adding to the skills directory — treat output as suggestions, not final artifacts.

## Security

Licensed under CC BY 4.0 — free to use, adapt, and redistribute (including commercially) with attribution. The upstream repo lists a "Security audit" section but leaves it empty, meaning no formal third-party audit has been published. The skill itself is a pure text/prompt artifact with no executable code, runtime dependencies, or network calls of its own; its attack surface is limited to prompt-injection risk common to any observation-style meta-skill (it reads session context and writes recommendation files to the filesystem). The recommended mitigation is already baked into the design: the observer never modifies skills directly — all changes require human review before being applied. No known CVEs or active security issues.
