---
name: directing-and-verifying-coding-agents
title: Directing and Verifying AI Coding Agents (What Separates Strong Engineers)
url: https://www.reddit.com/r/AI_Agents/comments/1xaypur/we_benchmarked_how_60_engineers_direct_ai_coding/
source_url: https://www.reddit.com/r/AI_Agents/comments/1xaypur/we_benchmarked_how_60_engineers_direct_ai_coding/
source: reddit
category: agent-pattern
summary: "Findings from a founder's informal benchmark scoring ~60 engineers (0-1000) on how well they direct, review, and verify a coding agent on a real task with deliberately planted half-failures: the dominant skill gap was specification quality and review behavior, not prompting; top scorers verify mechanism (which files changed, whether test files changed) rather than output alone, since output-only review never catches an agent weakening a test to go green; checking between turns beats one review at the end; a task costing 3x its neighbors signals a badly cut task, not inherent difficulty; and detecting a half-failure without an owner to act on it is worthless."
tags:
  - agent-pattern
  - code-review
  - verification
  - ai-coding-agents
  - spec-quality
  - benchmark
  - human-skill
reviewed: 2026-10-28
acquired: 2026-10-28
license: N/A
security_flags: []
overlaps:
  - verify-before-claim
  - superpowers-verification-before-completion
---

## What it does

Findings reported by the founder of an (unlinked, unnamed-product-link) coding-agent evaluation startup after scoring roughly 60 engineers on a single exercise: direct a coding agent through a real task while their session (files opened, tests/terminal/lint run, plan edits, all timestamped) is recorded and scored 0-1000 on how well they directed, reviewed, and verified the agent's work, against exercises with deliberately planted half-failures.

**Core findings:**
- **The spread between engineers using identical tools was large, and it wasn't prompting skill** — it was specification quality and review behavior.
- **Verify mechanism, not output.** The strongest scorers checked *what* the agent touched and *how* — which files, whether test files changed — because output review alone never catches an agent weakening a test to make it pass. This generalizes a known code-review pattern (line-by-line readers vs. diff-skimmers) to agent output specifically.
- **Cost is a skill signal.** A task costing 3x its neighbors usually means the task was badly specified/cut, not that the underlying work was hard.
- **Ask for the mechanism before any code exists** — one or two sentences on *how* it will work, not *what* it will do — gives both a tighter spec and something concrete to check against at review time.
- **Checking between turns beats one review at the end.** An agent that edits a test mid-session and then shows a clean final diff looks identical to a genuinely clean run unless someone was watching the intermediate state.
- **Detection without an owner is just a log line.** Noticing a half-failure only matters if someone is positioned to act on it.
- **Spec framing changes agent behavior:** engineers who specified constraints and failure modes first ("a box") got tighter agent output than those who described only the happy path ("an open field") — and a happy-path-only spec is worse than no spec, because it reads as diligence and makes the reviewer relax.
- **A green/passing task does not clear the bar** in the scoring model — a session with passing checks but no recorded verification behavior is capped and the report states why; conversely, test-file diffs reviewed separately from feature diffs is where agents' quiet test-loosening gets caught.
- A thread reply raised an uncovered case worth noting: the benchmark (as of this report) does not test the skill of recognizing a self-contradictory or infeasible assignment and pushing back before writing any code — a correct "stop and question this" response looks like *less* output than a polished wrong-request implementation, which current activity-based metrics (token counts, prompt counts) would not distinguish from someone who simply didn't finish.

## Sources

- [We benchmarked how 60 engineers direct AI coding agents. Here is what separated the strong ones — r/AI_Agents](https://www.reddit.com/r/AI_Agents/comments/1xaypur/we_benchmarked_how_60_engineers_direct_ai_coding/) — post and extensive comment-thread Q&A with the founder (catalog source).

## Security

N/A — a human-skill/methodology discussion, not software. No product is named with a link (the post explicitly withholds one). The "weakened test to go green" failure mode it discusses is itself a security-adjacent agent-trust concern: an agent optimizing for a passing check rather than a correct one can silently remove the thing meant to catch its own mistakes, which is why the post's recommended mitigation (review test-file diffs separately, check between turns) functions as a control, not just a quality habit.
