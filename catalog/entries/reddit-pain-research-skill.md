---
name: reddit-pain-research-skill
title: Reddit Pain Research Skill
url: "https://github.com/haseebeqx/reddit-pain-research-skill"
category: skill
summary: "Codex skill for evidence-based Reddit customer-discovery research — plans a study, collects and clusters pain-point evidence, and produces falsifiable monetization hypotheses via deterministic Python helpers, gated by a human approval checkpoint before evidence collection begins."
tags: [reddit, customer-research, market-research, codex-skill, pain-points, monetization, evidence-based, deterministic-helpers]
reviewed: 2026-08-09
acquired: 2026-08-09
license: LicenseRef-unknown
security_flags: [no-license-stated, single-author]
overlaps: []
source: unknown
---

## What it does

A manually-invoked Codex skill for structured customer-discovery research on Reddit. Given a topic (e.g. "recurring invoicing pain among freelance designers"), it plans a study, verifies relevant subreddit communities, collects and deduplicates evidence via traceable canonical URLs, clusters recurring pain points, scores commercial signal separately from pain intensity, and writes ranked, falsifiable monetization hypotheses with contrary evidence and falsification tests. The skill requires Codex with skill and web-research support, Python 3.9+, and internet access; it is manual-only and never triggers implicitly.

The workflow has an explicit human checkpoint: after producing `research_config.json` (the reviewed research plan) Codex presents it for inspection/editing and requires explicit approval before evidence collection starts. Supports resuming from an existing `research_config.json` or `analysis.json`.

## Differentiators

The author (source Reddit post) built this to replace a bespoke Reddit research agent — a separate agent loop/runtime, LLM client, nested agents, custom browsing/search layer, dedicated UI, and orchestration framework — with a Codex skill plus small deterministic Python helpers used only where determinism matters: validation, scoring, canonical URL generation, deduplication, and artifact generation. The stated architecture is `Codex harness → SKILL.md workflow → deterministic helpers`, in contrast to a full custom `agent → model integration → tools → search → state → UI → orchestration → report generation` stack. Because it runs inside a normal Codex conversation, the session doesn't end when the report is produced — the user can continue investigating a finding, challenge an assumption, or build from the result in the same context.

## Mechanical details

- Install: `cp -R reddit-pain-research "${CODEX_HOME:-$HOME/.codex}/skills/"`, restart/open a new Codex session.
- Invoke explicitly, e.g. "Use $reddit-pain-research to research recurring invoicing pain among freelance designers in 2026." Optional controls (publication year, max results per query, max clusters, output directory, resume) can be expressed in natural language.
- Outputs, one artifact per stage: `research_config.json` (reviewed plan), `analysis.json` (sourced/clustered/scored evidence), `monetization_report.md` (ranked hypotheses, scorecards, contrary evidence, falsification tests).
- Existing output directories require one directory-level overwrite decision; overwrite removes only the three skill-owned artifacts. JSON writes use atomic replacement.
- Repo layout: `reddit-pain-research/SKILL.md`, `agents/openai.yaml`, `references/schemas.md`, `scripts/build_reports.py`, `scripts/create_research_config.py`, `tests/test_helpers.py`.
- Validate: `python3 -m unittest discover -s tests -v`; also validatable with Codex's `skill-creator` `quick_validate.py` helper when available.

## Security

No SPDX license identifier is stated in the fetched README, though the repo layout lists a `LICENSE` file — treat as unverified until confirmed. Single-author project (haseebeqx) with no independent star count, review, or adoption signal found via web search at review time — this appears to be a small/new repository. The skill is prompt + deterministic-Python-helper based (no network calls beyond Reddit/web research Codex already performs); the Python helpers handle validation, scoring, canonical URLs, dedup, and artifact writes rather than executing arbitrary code. Has a dependency-free unittest suite. The human-approval checkpoint before evidence collection and the explicit "pain does not imply willingness to pay" / "conclusions are hypotheses, not business validation" framing are notable design safeguards against over-trusting output.
