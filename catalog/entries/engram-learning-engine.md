---
name: engram-learning-engine
title: Engram (Learning Engine)
url: "https://github.com/nagisanzenin/engram"
category: plugin
summary: "Evidence-based Claude Code learning plugin — FSRS spaced repetition, free-recall verification with blind assessor grading, first-principles concept graphs, interactive HTML explorables; three commands (/learn, /review, /coach); Python 3 stdlib only, local JSON storage"
tags: [claude-code-plugin, spaced-repetition, learning, fsrs, retrieval-practice]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Claude Code plugin that turns the agent into a personal tutor with evidence-based learning mechanics. Three commands:

- **/learn <topic>** — decomposes any topic (code or non-code) into a first-principles concept graph ordered by chains of necessity, not textbook chapter order
- **/review** — 2–4 minute free-recall sessions on FSRS-scheduled concepts; the scheduler fits to the learner's own review history over time
- **/coach** — shows retention stats and serves a local HTML dashboard

Implements four replicated learning-science findings: structure (dependency-ordered decomposition), generation (predict/attempt before being told — pretesting effect), retention (testing as learning via free recall), honest adaptation (adapts from measured retention, not learning styles).

## Differentiators

- **Blind assessor architecture** — a separate assessor agent grades answers using a rubric without seeing the lesson, preventing the tutor's optimism bias from inflating scores. The author reports the tutor rated a session as successful while the assessor scored "1 recalled, 4 partial, 1 lapsed."
- **No learning styles** — explicitly rejects learning-style adaptation (citing Pashler et al. 2008 refutation); adapts from measured retention instead
- **Threshold concept explorables** — generates interactive HTML artifacts with sliders and prediction gates for concepts that benefit from visual/interactive exploration
- **Hard rule: "never invent the learner's confidence"** — discovered during development that the tutor was fabricating confidence scores the learner never stated; now enforced as a constraint
- Also runs on OpenAI Codex (omni-repo)

## Mechanical details / What to adopt

- **Install:** `claude plugin marketplace add nagisanzenin/engram` then `claude plugin install engram@engram`
- **Requirements:** Python 3 (stdlib only), no pip installs
- **Storage:** plain JSON in `~/.claude/learning/`; nothing leaves the machine
- **Research foundations cited:** Chi & Wylie 2014 (ICAP), Mayer/Paivio (multimedia), VanLehn 2011 (step-level tutoring), FSRS (modern Anki scheduler), Roediger & Karpicke 2006 (testing effect)

## Security

MIT licensed. Python stdlib only — no third-party dependencies. All data local to `~/.claude/learning/`. No network calls, no accounts, no external services. The assessor agent runs within the same Claude Code session.