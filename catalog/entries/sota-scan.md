---
name: sota-scan
title: sota-scan
url: "https://github.com/MerlijnW70/sota-scan"
category: skill
summary: "Useful comparative benchmarking skill for Claude Code, but single-contributor, no tests, and high token cost for exhaustive mode"
tags: [benchmarking, competitive-analysis, code-quality, claude-code, skill]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [no-tests, single-contributor]
overlaps: []
source: unknown
---
## What it does

sota-scan is a Claude Code skill that benchmarks your project against the top real-world projects in the same space. It uses Claude's internet access to identify comparable projects, reads their repositories, and produces a scored gap analysis (0–100%) with a ranked to-do list. Each gap cites a specific real project that already solves it — no vague advice. Three depth modes are available: `quick` (~80–150k tokens, top 3 gaps), `standard` (~150–350k tokens, full scorecard), and `exhaustive` (~400k+ tokens, deepest scan). Progress is persisted in a `.sota/` directory so you can re-run and track improvement over time.

Installation is two files: `SKILL.md` copied to `~/.claude/skills/sota-scan/` and `workflows/sota-scan-fanout.js` copied to `~/.claude/workflows/`. Invoked via `/sota-scan` or plain English ("Is my project top-tier?").

## Assessment

The concept is sound and the output format is well-designed — concrete citations, peer-sorted comparisons (optional-flag for cross-paradigm borrowing), and ranked worst-first action items make this more actionable than typical LLM feedback. The three-tier depth model with transparent token cost estimates is good UX. The `.sota/` progress-tracking layer adds real value for tracking improvement across runs.

Pilot rather than adopt because: (1) single contributor with no test suite or CI, so quality and maintenance durability are unproven; (2) the core value depends entirely on Claude's internet-search quality and hallucination rate — non-deterministic results are inherent to the approach; (3) token costs are non-trivial for exhaustive mode (400k+). Worth testing on a real project to validate output quality before building it into any workflow.

## Mechanical details

- Install: copy `SKILL.md` to `~/.claude/skills/sota-scan/` and `workflows/sota-scan-fanout.js` to `~/.claude/workflows/` (cross-platform instructions provided for Mac/Linux and Windows).
- Invocation: `/sota-scan [quick|exhaustive]` — defaults to standard depth.
- Requires Claude Code with internet access enabled.
- Output is a scored standing report plus a ranked gap list, each gap citing the real project to copy from. Results written to `.sota/` for progress tracking.
- The JS workflow file (`sota-scan-fanout.js`) runs inside Claude Code's workflow runner — it does not execute arbitrary shell commands.
- No server, no credentials, no persistent background process.

## Security

MIT license — permissive, no copyleft obligations. The skill installs two local files with no network listeners or credential handling. The workflow JS runs inside Claude Code's own sandboxed workflow runner. No `eval()` or shell-injection vectors are visible in the described architecture. Main risks are the inherent non-determinism of LLM internet research (false gaps, missed gaps) and the supply-chain immaturity of a single-contributor project with no stated tests or CI. The README's self-scan claim ("came out top-tier") is unverifiable marketing, not evidence. Treat output as a starting point for human review, not ground truth.
