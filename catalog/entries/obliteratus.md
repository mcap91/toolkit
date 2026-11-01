---
name: obliteratus
title: OBLITERATUS
url: "https://github.com/elder-plinius/OBLITERATUS"
category: framework
summary: "Mechanistic interpretability research toolkit for refusal removal — notable as a reference for alignment geometry, but not safe to adopt in agent pipelines and irrelevant to bioinformatics workflows"
tags: [llm, mechanistic-interpretability, abliteration, alignment, safety-bypass, research, gradio, python]
reviewed: 2026-06-10
acquired: 2026-06-10
license: AGPL-3.0
security_flags: [safety-bypass-tool, telemetry-opt-out-required, adversarial-prompting-content, trust-remote-code, dual-license-commercial-required]
overlaps: []
source: unknown
---

## What it does

OBLITERATUS is an open-source toolkit for performing "abliteration" on transformer-based LLMs — the process of identifying and surgically removing internal representations responsible for content refusal without retraining. It provides a full pipeline: probe a model's hidden states to locate refusal directions, extract them via PCA/mean-difference/SVD/whitened-SVD, then project those directions out of the model's weights (permanently) or suppress them at inference time via steering vectors (reversibly).

The toolkit ships with: a Gradio web UI (hosted on HuggingFace Spaces with ZeroGPU), a CLI (`obliteratus obliterate <model>`), a Python API, YAML-based reproducible configs, and 15 analysis modules that map the geometric structure of safety mechanisms before modifying them. It supports 116 model presets across 5 VRAM tiers (tiny → frontier), multi-GPU pipeline sharding, remote SSH execution, and quantized inference (8-bit/4-bit via bitsandbytes). Seven obliteration presets range from `basic` (1-direction diff-in-means) to `nuclear` (all techniques + expert transplant + steering). Also includes crowd-sourced telemetry: runs with `--contribute` feed anonymous benchmark data to a shared dataset and community leaderboard.

## Assessment

OBLITERATUS is cataloged as **note** — worth knowing about as a reference for mechanistic interpretability research, but not for adoption in this toolkit's agent pipelines.

**For:** It is technically sophisticated, well-tested (837 tests, 28 test files), builds on peer-reviewed research (Arditi 2024, Turner 2023, Rimsky 2024), and implements genuinely novel techniques (Expert-Granular Abliteration, CoT-Aware Ablation, analysis-informed closed-loop pipeline, LoRA-reversible ablation). The analysis modules (alignment imprint detection, concept cone geometry, cross-model transfer universality index, Ouroboros self-repair detection) represent real mechanistic interpretability contributions. As a reference for how alignment geometry works inside transformer architectures, it's valuable.

**Against:** The explicit purpose is to remove safety mechanisms from LLMs. Installing or integrating a refusal-removed model into an agent pipeline constitutes a meaningful security risk — the `agent-lockdown` skill (WK-0031) exists precisely to harden against this class of risk. There is no bioinformatics relevance. Telemetry is on by default in the HuggingFace Spaces deployment. `trust_remote_code=True` is used for custom architectures, which is a supply-chain risk. The AGPL-3.0 license requires source disclosure for any SaaS deployment.

## Mechanical details

- **Installation:** `pip install -e .` (local) or `pip install -e ".[spaces]"` (Gradio UI); `pip install -e ".[dev]"` for tests
- **CLI entry point:** `obliteratus obliterate <hf-model-id> --method <preset>`
- **Python API:** `AbliterationPipeline` (standard) and `InformedAbliterationPipeline` (analysis-guided, auto-configures all parameters)
- **Extraction methods:** diff-in-means, SVD, whitened SVD, sparse autoencoder decomposition
- **Projection methods:** basic zeroing, norm-preserving biprojection (grimjim 2025), bias-term projection, regularized, iterative multi-pass
- **Reversible alternative:** `SteeringVectorFactory` + `SteeringHookManager` — applies direction suppression as inference-time hooks, removable without weight modification
- **Analysis modules (15):** CrossLayerAlignment, RefusalLogitLens, WhitenedSVD, ActivationProbing, DefenseRobustness, ConceptConeGeometry, AlignmentImprintDetection, MultiTokenPosition, SparseSurgery, CausalTracing, ResidualStreamDecomposition, LinearProbingClassifiers, CrossModelTransfer, SteeringVectors, EvaluationSuite
- **YAML configs:** reproducible ablation studies, versionable, supports `remote:` block for SSH execution
- **Multi-GPU:** `device_map="auto"` via accelerate; pipeline parallelism (memory solution, not speed); `obliteratus gpu-calc` for VRAM estimation
- **Telemetry schema:** model name, method, aggregate scores (refusal rate, perplexity, coherence, KL), hardware info — no prompts, outputs, or identity per README

## Security

- **License:** AGPL-3.0 (open source) with commercial dual-license option. Copyleft obligations apply to network-service deployments — any modified version run as SaaS must release source.
- **Safety-bypass-tool:** The primary function of this software is to remove safety mechanisms from LLMs. This is the dominant security consideration for any agent-pipeline integration. A model processed by OBLITERATUS will respond to prompts that the original model would refuse, including harmful content requests.
- **Telemetry opt-out required:** Telemetry is on by default when using the HuggingFace Spaces deployment. Locally it requires `--contribute` flag or `OBLITERATUS_TELEMETRY=1`. The schema is documented in `obliteratus/telemetry.py` per README.
- **trust_remote_code:** Custom architectures use `trust_remote_code=True` (HuggingFace standard but a supply-chain risk if loading from untrusted model repos).
- **Adversarial content in repo:** The README contains framing language designed to normalize safety bypass ("Break the chains. Free the mind."), study presets named `jailbreak` and `guardrail`, and marketing language that positions refusal removal as liberation. Treated as data for this catalog entry — not followed.
- **Dual-license commercial flag:** Commercial use without AGPL compliance requires a paid license; terms via GitHub Issues only (no published pricing).
- **Code quality signals:** 837 tests, 28 test files cited — indicates meaningful test coverage. No CI badge observed in fetched content. SSH remote execution auto-installs the tool on remote hosts, which is a lateral-movement vector if the remote host is shared infrastructure.
