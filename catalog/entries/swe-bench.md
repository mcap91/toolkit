---
name: swe-bench
title: SWE-bench
url: https://www.swebench.com/
source_url: https://www.instagram.com/reel/De4PXaltWfP/
source: instagram
category: reference
summary: "Coding-agent benchmark built from real GitHub issues across (originally) 12 popular Python repositories: an agent generates a patch from the issue description and codebase, graded by human-developer-written unit tests split into FAIL_TO_PASS (the issue's own test must flip from failing to passing) and PASS_TO_PASS (all pre-existing tests must stay green). Variants: Full (complete dataset), Lite (lower-cost subset), Verified (500 human-annotated, solvable tasks, OpenAI-developed 2024), and Pro (Scale AI SEAL lab — harder, multi-file, cross-repository-structure tasks under a standardized 250-turn scaffold). By October 2026, SWE-bench Verified is widely considered no longer a reliable yardstick for frontier models (leaderboard stagnant since December 2025, contamination concerns), and even SWE-bench Pro had documented reward-hacking and task-quality issues (102 flagged instances), corrected in a 'Pro Verified' release. Earlier research (SWE-Bench+) found solution leakage in 18 Lite and 37 Verified instances. Derivative benchmarks address staleness: SWE-bench-Live (rolling weekly fresh issues) and SWEBench-verified-mini (50-issue reduced set)."
tags:
  - benchmark
  - coding-agents
  - github-issues
  - swe-bench
  - evaluation
  - contamination
  - reward-hacking
reviewed: 2026-10-28
acquired: 2026-10-28
license: N/A
security_flags: []
overlaps: []
---

## What it does

Grades a coding agent's ability to resolve a real GitHub issue: given the issue description and the repository at the commit before the fix, the agent produces a patch, which is graded against human-developer-written unit tests. Two test categories decide pass/fail: `FAIL_TO_PASS` (the test(s) tied to the issue must go from failing to passing) and `PASS_TO_PASS` (every pre-existing test must remain green — the patch cannot fix the target issue by breaking something else).

**Variants, in increasing strictness/difficulty:**
- **Full** — the complete original dataset across the source repositories (Python, originally 12 popular projects).
- **Lite** — a lower-cost, more accessible subset.
- **Verified** (OpenAI, 2024) — 500 tasks from Full, manually vetted by human annotators to confirm solvability and test reliability.
- **Pro** (Scale AI, SEAL lab) — selected for difficulty rather than reliability: multi-file changes, longer context, repository structures that resist a simple single-file edit; every model runs under an identical, standardized 250-turn scaffold.

**Reliability problems documented over time:** SWE-Bench+ research found solution leakage (the fix was directly stated in the issue/discussion thread) in 18 Lite and 37 Verified instances, inflating apparent scores. By October 2026, SWE-bench Verified is widely regarded as no longer a reliable yardstick for frontier models — its public leaderboard has had no new entries since December 2025, and OpenAI itself has effectively deprecated it over contamination concerns. Even the harder Pro variant was found to have reward-hacking vectors (gold-solution/eval-info leakage) and task-quality defects in 102 instances, prompting a corrected "Pro Verified" release.

**Freshness-focused derivatives:** SWE-bench-Live pulls new GitHub issues on a rolling weekly cadence specifically to reduce training-set contamination; SWEBench-verified-mini is a 50-issue reduction (from only two source projects) reported to preserve a similar performance/difficulty distribution for cheaper evaluation runs.

## Sources

- [SWE-bench Leaderboard 2026: Every Model Score Explained — CodeAnt](https://codeant.ai/blogs/swe-bench-scores) — variant overview, 2026 status.
- [SWE-bench Verified — Epoch AI](https://epoch.ai/benchmarks/swe-bench-verified) — Verified methodology, sample counts.
- [SWE-Bench Pro Verified (arXiv, 2026-10-12)](https://arxiv.org/pdf/2609.08149) — Pro's reward-hacking and task-quality findings, corrected release.
- [SWE-Bench+: Enhanced Coding Benchmark for LLMs (arXiv)](https://arxiv.org/pdf/2410.06992) — solution-leakage counts in Lite/Verified.

## Security

N/A — an evaluation benchmark/dataset, not software an agent runs in production. The documented contamination and reward-hacking findings are a methodological caution: a high SWE-bench (especially Verified) score should not be treated as strong current evidence of frontier coding-agent capability without checking which variant and dataset vintage produced it.
