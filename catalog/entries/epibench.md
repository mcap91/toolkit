---
name: epibench
title: EpiBench
url: "https://latch.bio/epibench"
category: reference
summary: "Verifiable 106-task benchmark for AI agents on short-horizon epigenomics analysis (ATAC/ChIP/CUT&Tag/methylation); no model-harness pair passed a majority (best 45%), with failures concentrated in assay-specific scientific judgment."
tags: [benchmark, epigenomics, evaluation, bioinformatics, agents]
reviewed: 2026-06-18
acquired: 2026-06-18
license: NOASSERTION
security_flags: [license-unconfirmed, dataset-availability-unconfirmed]
overlaps: [biomysterybench]
source: unknown
---

## What it does / What it says

EpiBench (arXiv:2606.13602, submitted 11 Jun 2026 by Harihara Muralidharan, Reema Baskar, Soo Hee Lee, Tim Proctor, and Kenny Workman of Latch.bio) is a **verifiable benchmark for short-horizon epigenomics analysis**. It deconstructs real analysis workflows into 106 deterministic evaluations and tests whether an agent can make a well-defined analysis decision from a realistic mid-workflow state and return a deterministically gradable answer.

Each task starts from a realistic workflow state immediately *before* a target result. The agent is handed files, metadata, and task context, must inspect the data, and submits a structured answer that is graded against the provided data — no LLM judge, no fuzzy matching.

Assay coverage (106 tasks total):

- **CUT&Tag / CUT&RUN** — 47 tasks
- **DNA methylation (methylation-seq)** — 25 tasks
- **ATAC-seq** — 24 tasks
- **ChIP-seq** — 10 tasks

Headline result: across **5,088 valid trajectories from 16 model-harness pairs, no system passed a majority of attempts.**

- GPT-5.5 / Pi — 45.0% (143/318; 95% CI 36.3–53.7)
- GPT-5.5 / OpenAI Codex — 39.9% (127/318; 95% CI 31.6–48.3)
- Claude Opus 4.8 Max / Pi — 39.0% (124/318; 95% CI 30.2–47.8)
- GPT-5.4 / Pi — 39.0% (124/318; 95% CI 31.0–47.0)

Per-assay pass rates are uneven (ATAC-seq lowest at ~22.8%, CUT&Tag/CUT&RUN highest at ~34%). The authors' key finding: agents **frequently found the right files and computed useful intermediate results, but failed when the task required deeper, assay-specific scientific judgment** (units reasoning, peak calling, feature annotation, design-aware statistics).

## Assessment

Directly on-topic for this toolkit's core purpose: an empirical, *deterministically graded* measure of how well current agents handle real epigenomics decisions — the exact class of work bioinfo agents are pointed at. Its value here is as a **yardstick and a diagnosis**, not an installable tool. The diagnosis is the useful part: today's frontier agents are competent at mechanics (finding files, running steps) and weak at the scientific judgment layer. That argues for keeping a human/expert gate on analysis decisions and for building skills that encode assay-specific reasoning rather than just orchestration.

Complements [[biomysterybench]] (broad 99-problem research benchmark from Anthropic): EpiBench is narrower and deeper — short-horizon, single-decision, epigenomics-specific, deterministic grading — where BioMysteryBench is wider-scope research-task evaluation. The two together give coverage across both "can it run the research" and "can it make the right per-step call." Also relevant to [[autoharness]], whose catalog note flags that we want eval criteria before piloting — EpiBench is a concrete reference point for what rigorous, gradable agent evals in this domain look like.

**Disambiguation:** there is a *different, unrelated* paper also titled "EpiBench" (arXiv:2604.05557, "Benchmarking Multi-turn Research Workflows for Multimodal Agents"). This entry is the Latch.bio epigenomics benchmark only.

## Mechanical details / What to adopt

- **Deterministic grading from a fixed mid-workflow state** is the transferable design idea. Rather than scoring a full open-ended trajectory, snapshot the workflow right before a decision, hand the agent the real artifacts, and grade one structured answer. This is reproducible and cheap to re-run across models — a pattern worth copying for evaluating our own skills/subagents.
- **Model-harness pairing** as the unit of evaluation (e.g. "GPT-5.5 / Pi", "Claude Opus 4.8 Max / Pi") — performance is a property of model *and* harness, not the model alone. Useful framing when we benchmark our own Claude Code skill stack.
- The benchmark family is tracked with new models over time at **benchmarks.bio**; a plain-language writeup is on the LatchBio Substack ("EpiBench: AI agents still struggle with epigenomics analysis", 11 Jun 2026).

## Security

- **License: unconfirmed.** The manuscript landing page (latch.bio/epibench) 308-redirects to the arXiv abstract; no license is stated there. Set to `NOASSERTION` pending confirmation — `license-unconfirmed`.
- **Dataset/harness availability: unconfirmed.** Could not confirm a public GitHub repository or a downloadable dataset/harness from the abstract, blog post, or search; access appears to route through latch.bio / benchmarks.bio. Treated as `dataset-availability-unconfirmed`. This is a *reference* entry — no code is being adopted, so the practical risk is low; the flags mark what to verify before any attempt to run the benchmark locally.
- Content reviewed is an academic abstract and blog summary; no embedded instructions or injection attempts. Nothing executable.
