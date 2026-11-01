---
name: asi-evolve
title: ASI-Evolve
url: "https://github.com/GAIR-NLP/ASI-Evolve"
category: framework
summary: "Impressive autonomous research-loop results but arbitrary code execution per round, no stated license, and very new (2026 academic repo)"
tags: [autonomous-research, agentic, evolutionary-search, experiment-automation, bioinformatics, llm-driven, multi-agent, orchestration]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-unknown
security_flags: [arbitrary-code-execution, no-license-stated, no-tests-observed, no-ci-observed]
overlaps: [era-empirical-research-assistant]
source: unknown
---

## What it does

ASI-Evolve is a general agentic framework that automates iterative research: it runs a LEARN → DESIGN → EXPERIMENT → ANALYZE loop autonomously, round after round, until it finds improved solutions. Three specialized agents drive each round — a Researcher (retrieves prior knowledge, proposes next candidate program), an Engineer (executes the candidate, collects structured metrics via a user-supplied eval script), and an Analyzer (distills outcomes into transferable lessons). Two persistent memory systems prevent circular exploration: a Cognition Store (FAISS-backed vector store seeded with domain knowledge, papers, and heuristics) and an Experiment Database (stores every trial with motivation, code, result, and analysis; parent selection uses UCB1, greedy, random, or MAP-Elites island sampling). The framework is domain-agnostic — the user supplies a problem description, a baseline program, and an evaluation script returning a numeric score; ASI-Evolve handles the rest. Published results cover neural architecture search (+0.97 pts over DeltaNet), pretraining data curation (+18 pts MMLU), RL algorithm design (+12.5 pts AMC32 vs GRPO), and drug-target interaction (+6.94 AUROC).

## Assessment

The benchmark results are frontier-level and independently impressive. The architecture is principled — memory-augmented evolutionary search with structured logging is the right approach for automated research. However: (1) the framework is brand new (2026 academic release), with no observable test suite or CI; (2) each evaluation round executes arbitrary LLM-generated code via a user-supplied shell script, which is a meaningful operational risk if used against sensitive infrastructure or with untrusted eval environments; (3) the ERA — Empirical Research Assistant framework is already cataloged at watch with closely overlapping scope. Worth tracking as it matures and gains production hardening. The bioinformatics use case (drug-target interaction) is directly relevant to this toolkit's mission, making it worth revisiting once the repo stabilizes.

## Mechanical details

- **Entry point**: `python main.py --experiment <name> --steps N --sample-n K --eval-script /path/to/eval.sh`
- **Experiment layout**: each experiment is a directory under `experiments/` containing `input.md` (problem description), `config.yaml` (API key + overrides), `initial_program` (baseline), `init_cognition.py` (domain knowledge seed), `evaluator.py`, and `eval.sh`
- **LLM backend**: any OpenAI-compatible API (GPT-4o, Claude, Gemini, local models via LiteLLM); configured in `config.yaml` under `api.model`
- **Sampling strategies**: UCB1, greedy, random, MAP-Elites island — selectable per experiment
- **Parallelism**: `pipeline.parallel.num_workers` (2–4 recommended for production runs)
- **Config layering**: repo-root `config.yaml` → experiment `config.yaml` → explicit `--config` file (later overrides earlier)
- **Skill variant**: a lightweight `skills/evolve` Claude Code skill is included for quick try-outs; full pipeline runs produce higher search quality than the skill-based shortcut
- **Demo**: `experiments/circle_packing_demo/` — SOTA-level results in ~17 rounds
- **Install**: `pip install -r requirements.txt`; Python 3.10+, bash required; W&B optional for tracking

## Security

**License**: Not stated in the README. The repo is from SJTU/GAIR (academic); no SPDX identifier found. Treat as all-rights-reserved until confirmed — do not use in commercial products without clarification.

**Arbitrary code execution**: The core evaluation loop executes LLM-generated programs via a user-supplied `eval.sh` shell script each round. This is by design, but means the framework will write and execute arbitrary code on the host machine. Run in an isolated environment (container, VM, or sandbox) — never against production infrastructure or on a machine with access to sensitive credentials.

**Dependency health**: `requirements.txt` pinning not inspectable from README alone; no pinned hashes mentioned. FAISS and LiteLLM are the notable transitive dependencies — both have active maintenance but the specific versions used are unknown.

**Supply chain**: Fresh 2026 academic repo from GAIR-NLP (SJTU). No signed releases, no observable CI configuration, contributor count unknown at review time.

**Prompt injection surface**: The Researcher agent ingests content from the Cognition Store and Experiment Database; adversarial content in seeded knowledge or eval outputs could influence subsequent hypotheses. Not a critical concern for controlled research use, but worth noting for any deployment that ingests external documents automatically.
