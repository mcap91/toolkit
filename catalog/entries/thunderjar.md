---
name: thunderjar
title: Thunderjar
url: "https://github.com/dwjohnston/thunderjar"
category: cli-tool
summary: "Comparative testing framework for coding agents — holds three of four variables (codebase state, prompt configuration, model, harness) constant and varies the fourth, then applies objective measurements (compilation, test pass, file assertions, token consumption, lint compliance, correctness). For evaluating whether prompt/model/harness changes actually improve agent output. Early-stage project by dwjohnston."
license: ""
tags: [agent-testing, evaluation, benchmarking, prompts, claude-code, codex, measurement, comparison]
reviewed: 2026-07-28
acquired: 2026-07-28
overlaps: [trigger-tree]
security_flags: []
source: unknown
---

## What it is

Thunderjar is a testing/comparison framework for coding agents. The concept: agent behavior is a non-deterministic function of four variables — codebase state (C), prompt configuration (P), model (M), and harness (H). Thunderjar holds three constant and varies the fourth, then applies objective measurements against the results.

The workflow:
1. Identify a task (typically one already completed manually)
2. Capture a codebase snapshot (commit hash)
3. Check out to that commit, apply prompt configuration, run the task with a specific harness and model
4. Apply measurements: compilation/test pass, file existence assertions, lint compliance, token consumption, correctness checks, subagent spawning behavior

Measurement difficulty tiers:
- **Easy:** Total time, compilation/test pass
- **Medium:** File existence, format compliance, ts-ignore/as-any usage, documentation updates
- **Hard:** Function signature quality, naming, actual correctness (suggested approach: known-output tests against exported functions)

## Mechanical details

- **Status:** Early-stage side project. GitHub repo exists but README content was not extractable at fetch time.
- **Blog post:** https://blacksheepcode.com/posts/coding_agent_testing describes the concept and motivation
- **Relationship:** Complementary to trigger-tree (which measures directive adherence in production sessions); Thunderjar is for controlled A/B-style experiments
- **Inspiration:** Differs from PromptFoo in targeting full coding-agent sessions rather than individual prompt/response evaluation

## Security

No license or install instructions observed. Early-stage project — evaluate maturity before use. No security flags observed.