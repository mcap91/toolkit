---
name: distill
title: Distill
url: "https://github.com/samuelfaj/distill"
category: cli-tool
summary: Local 1.7B model pipe-filter for CLI output compression is a real problem but requires 8–16 GB RAM and relies on an unaudited HuggingFace model; overlaps with rtk.
tags: [token-reduction, cli, pipe, local-model, output-compression]
reviewed: 2026-06-10
acquired: 2026-06-10
license: NOASSERTION
security_flags: [no-license-in-readme, single-contributor, unaudited-hf-model, npm-global-install]
overlaps: [rtk]
source: unknown
---

## What it does

Distill is an npm CLI tool installed globally (`npm i -g @samuelfaj/distill`) that acts as a Unix pipe filter: you pipe any command's output into `distill "question"` and it returns a short, focused answer instead of the raw output. The compression is done locally by a custom fine-tuned 1.7B parameter 4-bit quantized MLX model (`samuelfaj/distill-1.7B-MLX` on HuggingFace). The claimed compression ratio is up to 99% token reduction (e.g., 7648 tokens → 99 tokens in the shown example). It also advertises a "Distill Language" that teaches the LLM to reason more efficiently, though no details are provided in the README.

## Assessment

The problem is real: verbose CLI output (logs, stack traces, ripgrep results) wastes context window tokens in agentic workflows. The pipe-filter approach is ergonomic and composable. However, several factors keep this at **watch** rather than pilot:

1. **Resource requirement:** The local model requires 8–16 GB RAM, which is a non-trivial ask for a developer machine and makes this unsuitable for CI/headless agents.
2. **Unaudited model:** The compression model is a custom upload to HuggingFace by a single author. There is no independent audit of the model's output quality or safety.
3. **Overlap with rtk:** The catalog already contains `rtk` (pilot), which targets the same token-reduction-for-CLI-output niche with a lighter footprint.
4. **Supply chain risk:** npm global install from a single-contributor project with no visible license or signed releases.
5. **Unknown maintenance posture:** README is sparse; no CI, no test suite, no issue tracker activity visible from the fetched content.

Worth revisiting if the project gains contributors, publishes a license, and the model quality is independently validated.

## Mechanical details

- **Install:** `npm i -g @samuelfaj/distill`, then run `distill` for onboarding (which presumably downloads/configures the local model).
- **Usage pattern:** `<command> | distill "<natural-language question>"` — the tool reads stdin and returns a compressed answer on stdout.
- **Model:** `samuelfaj/distill-1.7B-MLX` (HuggingFace) — 1.7B parameters, 4-bit quantized, MLX format (Apple Silicon optimized).
- **RAM:** 8 GB minimum recommended, 16 GB comfortable.
- **Platform:** MLX format suggests primary target is macOS/Apple Silicon; cross-platform support is unclear.

## Security

- **License:** Not stated in the README; NOASSERTION until confirmed.
- **Model provenance:** The compression model is a custom fine-tune uploaded to HuggingFace by a single author (`samuelfaj`). No model card with training data, evaluation metrics, or safety checks is visible from the fetched content.
- **npm global install:** Installs into PATH, running on all CLI output piped through it. Malicious or buggy behavior would affect all piped commands in a session.
- **No tests / no CI:** No evidence of a test suite or continuous integration from the README.
- **Single contributor:** Higher bus-factor and supply-chain risk.
- **No dangerous code patterns** visible in the README itself, but the model inference path (local MLX model execution) is opaque without reviewing the source.
