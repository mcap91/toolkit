---
name: codex-reasoning-token-collapse
title: Codex 5.5 Reasoning-Token Collapse Evidence
url: "https://github.com/NickalasLight/codex-reasoning-bug-516-token"
category: reference
summary: "Public-safe evidence repo investigating a suspected Codex (gpt-5.5) failure where some turns terminate at exact 512-family reasoning-token counts (516/1034/1552); ships Python analyzers plus a blind multi-reviewer audit harness; across manual, rule-assisted, and blind audits, removing the suspected instruction section did not meaningfully reduce concerning clustered hits"
tags: [codex, gpt-5.5, reasoning-tokens, evidence, analysis-scripts, model-behavior, reference]
reviewed: 2026-07-09
acquired: 2026-07-09
license: ""
security_flags: [no-license-stated, single-maintainer, reads-local-transcripts]
overlaps: [codex-memory-cleanup, codex-ssd-write-bug]
source: unknown
---

## What it says

Repository documenting a suspected pattern in OpenAI Codex (model `gpt-5.5`) where some agent turns terminate at exact "512-family" reasoning-token counts — observed cluster values 516, 1034, 1552. The original suspected trigger was the final `## Intermediary updates` section of the Codex 5.5 model/base instructions; the maintainer removed that section from a local override, later added an explicit "Maximum Reasoning Intervention" instruction, then re-analyzed transcripts before/after a 2026-07-06 cutoff. The repo intentionally publishes only aggregate, anonymized usage metadata (model, phase, call count, reasoning-token counts, cluster counts) — no raw prompts, responses, tool arguments, paths, or usernames.

## Findings as reported

- Historical gpt-5.5 metadata: mean reasoning tokens ~227 before vs ~225 after the instruction-section removal (essentially flat); exact cluster-hit rate 5.73% → 4.93%. The mitigation did not eliminate 512-family hits.
- A manual 10% audit, a larger rule-assisted 30% screen, and a simulated blind three-reviewer audit all fail to show a meaningful before/after improvement in "concerning" clustered hits (turns where deeper reasoning appeared warranted). Blind-audit majority concern rate was ~44.9% before vs 50.0% after.
- A fresh 5-shot benchmark (a word problem, expected answer 21) did not reproduce the strict affected-state failure — all 5 correct, none landing on cluster values. An independent contributor (Bozentan / Ilia, PR #3) reported an affected batch of 0/5 correct all at 516, with clean-removal and hardened-override retests at 5/5.
- Stated conclusion: the suspected section is absent from active base instructions, but exact 512-family hits persist in ordinary use and average reasoning-token allocation did not materially change; benchmark-level improvement is not the same as a broad fix.

## Tooling

Ships Python scripts run against local Codex JSONL session transcripts: `scripts/analyze_reasoning_tokens.py` (emits usage metadata only, one row per token-count event, `--phase-basis session`, `--cutoff`), plus a blind-review harness (`make_blind_review_packet.py`, `aggregate_blind_review.py`) that builds a phase-blinded reviewer packet and private answer key and aggregates independent reviewer JSONL into public-safe agreement metrics (Fleiss kappa, vote tables). Evidence artifacts are committed under `evidence/`.

## Security

No license is stated in the README, so reuse terms are unclear. The analysis scripts read your local Codex session transcripts; the repo's design goal is to keep raw transcript content private and publish only aggregates, but running third-party scripts over local transcripts is the main consideration. Single-maintainer project with external PR contributions. The repository has been referenced as both `...-512-token` and `...-516-token`; the live repository resolves to the 516 name.