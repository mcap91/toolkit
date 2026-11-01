---
name: era-empirical-research-assistant
title: ERA — Empirical Research Assistant
url: "https://github.com/google-research/era"
category: framework
summary: "Interesting LLM+tree-search loop for scientific code generation, but Gemini-locked, research-grade, and not directly applicable to Claude Code workflows today"
tags: [scientific-computing, code-generation, tree-search, llm-loop, bioinformatics, single-cell, python, google-research, research-paper]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [executes-generated-code, no-pinned-deps, not-officially-supported, api-key-required]
overlaps: [autoresearch, asi-evolve]
source: unknown
---

## What it does

ERA (Empirical Research Assistant) is an AI system that iteratively generates, executes, and scores candidate programs to converge on expert-level scientific software. It pairs a large language model with a Flat UCB Tree Search (FUTS) algorithm — a variant of PUCT (Predictor + Upper Confidence bound for Trees) — to explore a solution space across `num_iterations` iterations, always expanding the most promising node and keeping the best solution found. The user provides two callables: `generate_fn` (LLM call that produces a new candidate from a problem definition and prior solution) and `execute_fn` (scores a candidate by running it against the problem's metric in a sandbox). ERA is demonstrated on regression tasks (California Housing Kaggle) and validated in eight real-world scientific domains: epidemiology forecasting, neuroscience, theoretical physics, public health, climate, hydrology, economics, and combinatorics. Published as a 2025 Google Research paper (arXiv 2509.06503).

## Assessment

`watch` — The FUTS/PUCT loop pattern is a genuinely useful blueprint for any agentic system that needs iterative LLM-driven program synthesis with automatic scoring. That algorithmic idea is worth tracking and potentially extracting. However, ERA itself is Gemini-API-locked (`google-generativeai` SDK, `GOOGLE_API_KEY`), paper-release research code ("not an officially supported Google product"), and targets scientific Python workflows rather than Claude Code skill/agent patterns. It is not directly adoptable as a Claude Code skill or hook today. The core FUTS implementation (`futs.py`) could inspire a provider-agnostic reimplementation for bioinformatics agent loops.

## Mechanical details

- **Runtime**: Python 3.10+; dependencies: `pandas`, `numpy`, `scikit-learn`, `google-generativeai` (no pinned versions in README)
- **Entry points**: `implementation/playground_s3e1.py` (CLI example), `implementation/experiment_pipeline.ipynb` (Jupyter), `implementation/futs.py` (core search library)
- **FUTS interface**: `search(generate_fn, execute_fn, problem_def, num_iterations)` → best solution. Caller owns the LLM call and the scoring sandbox.
- **Applications directory**: `era_applications/` contains eight applied science use-cases across epidemiology, neuroscience, physics, climate, hydrology, economics, and combinatorics — useful as benchmark examples.
- **Provider swap path**: `generate_fn` is user-supplied, so swapping Gemini for Claude is straightforward at the application layer; the search algorithm itself is provider-agnostic.
- **What to extract**: The FUTS algorithm in `futs.py` is a clean, reusable tree-search loop applicable to any iterative agent workflow that can define a scoring function.

## Security

- **License**: Apache-2.0 (standard for Google Research repos; not explicitly stated in README but consistent with repository conventions — verify in `LICENSE` file before adoption)
- **Code execution**: `execute_fn` runs generated code to score it; the README mentions a "sandboxed environment" but does not specify the sandbox mechanism. This is a significant risk surface if used outside the paper's controlled setup — arbitrary code execution of LLM-generated programs.
- **Credential handling**: Requires `GOOGLE_API_KEY` as an environment variable — standard practice, but no mention of secrets management or rotation guidance.
- **Dependency pinning**: README specifies only package names without version pins (`pip install pandas numpy scikit-learn google-generativeai`); dependency drift is a supply-chain risk.
- **Maintenance**: "Not an officially supported Google product" — no SLA, security patches not guaranteed. Paper-release code typically receives minimal ongoing maintenance.
- **No CI/tests visible**: No test suite or CI configuration mentioned in README.
