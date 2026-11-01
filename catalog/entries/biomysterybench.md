---
name: biomysterybench
title: BioMysteryBench
url: "https://huggingface.co/datasets/Anthropic/BioMysteryBench-full"
category: reference
summary: 99-problem bioinformatics research benchmark from Anthropic — directly useful for evaluating agent performance on real research tasks.
tags: [benchmark, bioinformatics, evaluation, dataset, research, anthropic]
reviewed: 2026-06-10
acquired: 2026-06-10
license: CC-BY-4.0
security_flags: [access-gated]
overlaps: []
source: unknown
---

## What it does

BioMysteryBench is a bioinformatics research benchmark created by Anthropic, hosted on HuggingFace. It contains 99 problems designed to test whether AI models can perform genuine bioinformatics research tasks. Each problem includes a question prompt, an answer rubric with expected results, allowed network domains for the solving environment, and associated data files. Problems are tagged with whether at least one human benchmarker solved them, providing a human-solvability baseline. The dataset ships as CSV/Parquet for problem metadata and per-problem ZIP archives containing the working data.

## Assessment

**Pilot.** This is directly relevant to evaluating bioinformatics agent capabilities — exactly the kind of benchmark needed to measure whether toolkit skills and workflows actually produce correct research outputs. The problems span real bioinformatics research tasks with ground-truth rubrics, which is rare. The access gate (must agree to evaluation-only terms) is a minor friction but reasonable. Worth running a subset against current agent configurations to establish a baseline. Could move to adopt once we have a harness for running problems systematically.

## Mechanical details

- **Format:** `problems.csv` / `problems.parquet` with columns: `id`, `question`, `answer_rubric`, `allowed_domains`, `human_solvable`.
- **Data:** Per-problem ZIP archives under `data/<id>.zip`; extract into working directory before solving.
- **Access:** Gated — must accept terms on HuggingFace (evaluation/benchmarking only, no training/fine-tuning/distillation).
- **Size:** 99 problems (full set).
- **What to adopt:** Use as an evaluation suite for agent bioinformatics capabilities. Run problems in isolated environments with network access limited to `allowed_domains`. Compare agent answers against `answer_rubric`. Track human-solvable vs. agent-solvable overlap.

## Security

- **License:** CC-BY-4.0 for problem statements, rubrics, and task formulation. Data archives are anonymized derivatives of public-archive submissions and retain their original data-use policies.
- **Dependency health:** N/A — this is a dataset, not software.
- **Code quality / CI:** N/A.
- **Supply chain:** Published by Anthropic (the model vendor). Single authoritative source on HuggingFace.
- **Dangerous patterns:** None — static data files. No executable code in the dataset.
- **Data privacy:** Problems are derived from public data archives. No PII concerns noted.
- **Maintenance:** Published as a complete benchmark; unlikely to receive frequent updates.
- **security_flags rationale:** `access-gated` — requires HuggingFace login and terms acceptance before download.