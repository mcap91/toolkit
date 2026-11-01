---
name: start-cheap-escalate-on-fail-routing
title: "Start Cheap, Escalate on Fail: Measured Model/Effort Routing"
url: https://www.instagram.com/reel/De4PXaltWfP/
source_url: https://www.instagram.com/reel/De4PXaltWfP/
source: instagram
category: agent-pattern
summary: "A measured cost-routing strategy for coding agents: define a task as work with a pass/fail test (the SWE-bench model — FAIL_TO_PASS plus PASS_TO_PASS), always attempt it first on the cheapest model/effort tier, run the test, and only escalate model/effort on failure. Demonstrated on 6 SWE-bench tasks (2 quick/medium/hard) across Sonnet, Opus, and Fable at varying effort: on one quick task, Fable at max effort cost $2.10/~5min while Sonnet at low effort cost $0.07/14s and both passed the identical test. Even counting the cost of failed escalation attempts, starting cheap came out cheaper across all six tasks tested. Suggests logging (task features, tier tried, pass/fail, cost) and fitting a classifier (e.g. scikit-learn) on that log to build a task router that predicts where to start for a given task shape."
tags:
  - model-routing
  - cost-optimization
  - swe-bench
  - agent-pattern
  - effort-tiering
  - task-classification
  - scikit-learn
reviewed: 2026-10-28
acquired: 2026-10-28
license: N/A
security_flags: []
overlaps:
  - swe-bench
  - engineering-team-claude-code-setup
  - jev
---

## What it does

Defines a measurable approach to the "which model, which effort level" question for a given coding task, rather than guessing:

**Definition of a task:** a piece of work with a test that decides pass/fail — the SWE-bench pattern (FAIL_TO_PASS: the issue's own test must flip to passing; PASS_TO_PASS: every pre-existing test must stay green). If a project has no such test, the recommendation is to build one first (patterned on how SWE-bench itself builds them) before trying to route cost by task.

**Measurement:** six official SWE-bench tasks (2 rated quick, 2 medium, 2 hard by SWE-bench's own difficulty labels) were each run on Sonnet, Opus, and Fable at multiple effort levels. On one quick task, Fable at max effort cost $2.10 and took ~5 minutes; Sonnet at low effort cost $0.07 and took 14 seconds — and both passed the exact same test. The general finding: a cheaper model/lower effort tier can often complete the same task as a more expensive one, so defaulting to the expensive tier wastes money without buying correctness on those tasks.

**Strategy:** always start a task on the cheapest model/effort tier available; run the task's test; only step the model and/or effort up when the test fails. Even counting the cost of the failed cheap-tier attempts that do need escalation, this came out cheaper in aggregate across all six measured tasks — i.e., the failed-attempt cost did not outweigh the savings from the tasks the cheap tier solved outright. The caveat given directly: results will vary by one's own task mix, so define the test first and measure on real tasks rather than assuming the ratio transfers.

**Building a router from the data:** log every attempt (task features, tier tried, pass/fail, cost, time); feed that log into a classifier (e.g., scikit-learn) to learn which starting tier a new task's features predict — turning the one-off escalation ladder into a standing task router rather than a fixed rule applied blindly to every task.

A previously published artifact by the same creator, called "Task Router," is referenced as an implementation of this idea, but no URL or further detail was captured from this item — see the creator's own profile for that link.

## Sources

- [Instagram reel (creator signs off as "Kermit Glitch Cat Club")](https://www.instagram.com/reel/De4PXaltWfP/) — all measurements and the routing strategy description (catalog source; no external link provided in the post itself).

## Security

N/A — a cost/routing methodology, not software. No code or service is distributed by this item.
