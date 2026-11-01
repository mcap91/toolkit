---
name: harness2
title: Harness² (Google Research)
url: https://github.com/google-research/harness2
category: framework
summary: Google Research framework for recursive agent harnessing — the agent refines its own harness (system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, plugins) per task via a Propose–Probe–Compose loop that compares candidate harness versions without graders or reference answers, then carries adopted edits and lessons forward in a persistent improvement harness; model weights unchanged; runs OpenCode/Codex executors on GLM-5 and Gemini 3.5 Flash; Python 3.12, Apache-2.0 (arXiv:2610.14224)
tags:
  - agent-harness
  - self-improvement
  - harness-optimization
  - meta-agent
  - opencode
  - codex
  - gemini
  - glm
  - benchmarks
  - google-research
  - python
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - autoharness
  - jit-agent
  - harnessx
  - skillopt
license: Apache-2.0
security_flags:
  - executor-sandbox-disabled
  - unrestricted-network
  - cloud-credentials-required
source: unknown
---

## What it does

Harness² treats the harness — everything around a fixed model — as the thing being optimized. The repository defines eight editable harness components: system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, and plugins. Model weights are never modified.

Optimization runs at two levels of recursion:

- **Task level (Propose–Probe–Compose):** for the current task the agent proposes harness edits, probes their effect by running candidate harness versions, and composes the edits that helped into a refined harness. Candidates are compared by their observed behavior on the task; no reference answers or external grader are required for this step.
- **Harnessing level:** adopted changes and lessons are written into a persistent "improvement harness" that guides how future refinements are proposed, so later tasks start from accumulated edits rather than from the original harness.

The reported experiments use GLM-5 and Gemini 3.5 Flash on professional-work benchmarks (JobBench), legal work (LAB), and office/web/code work (WorkBuddy-Bench). The Reddit announcement thread reports that a single round of edits improved on the original harnesses and further rounds raised scores further (author-reported).

## Mechanical details

- Install: `uv pip install -e '.[render]'` (Python 3.12, uv). Also requires Node.js 20+ and the Google Cloud CLI; LAB needs Pandoc and Poppler, WorkBuddy-Bench needs Docker.
- Entry points: `harness2 --bench <lab|...> --k 1 --mode parallel` (run), `harness2-judge ...` (scoring), `harness2-report ...` (reports).
- Executors: OpenCode and Codex CLIs act as the harness being refined.
- Models configured through Vertex AI project credentials in `.env`.
- Paper: arXiv:2610.14224. Repo is under the `google-research` GitHub org (~20k stars at review time).

## Usage notes

- A Reddit commenter characterizes Harness² as loop orchestration around an existing harness rather than a harness itself; applying the paper's methodology for 3 loops to Qwen 3.8 Flash Next on a 6-task coding corpus, they reported per-step solve rates moving from ~50–60% to ~65–72% (single user report).
- Thread discussion raises task overfitting as the main concern: a harness tuned for task A can degrade performance on task B.

## Security

Apache-2.0. The README documents that the executor runs with unrestricted network access and that Codex runs with its sandbox disabled, so harness edits proposed by the model execute without the executor's normal isolation; running it inside a disposable VM/container is the implied operating mode. Requires Google Cloud / Vertex AI credentials stored in a local `.env`. Research-grade code from a large org; release cadence and test coverage not assessed beyond the README.
