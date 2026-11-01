---
name: anthropic-global-workspace
title: A Global Workspace in Language Models
url: "https://www.anthropic.com/research/global-workspace"
category: reference
summary: 'Anthropic interpretability research identifying the "J-space" — a small set of internal neural patterns in Claude that function as a global workspace for deliberate reasoning, reportable thoughts, and internal monitoring; includes J-lens technique for reading model thoughts not expressed in output'
tags: [interpretability, anthropic, consciousness, j-space, j-lens, global-workspace-theory, model-internals, safety-monitoring]
reviewed: 2026-07-12
acquired: 2026-07-12
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it is

A research paper and blog post from Anthropic presenting evidence that Claude has developed an internal "global workspace" — a small collection of neural activation patterns (the "J-space") that play a privileged role compared to all other internal processing. The J-space was not designed but emerged during training.

The "J-lens" (Jacobian lens) technique identifies, for every word in Claude's vocabulary, the internal activity pattern that makes Claude more likely to say that word in the future — revealing thoughts the model holds without expressing them in output.

## Key findings

1. **Reportability.** Claude can describe what's in its J-space when asked. Non-J-space representations are less reportable.

2. **Controllability.** Claude can modulate J-space contents on request (e.g., holding a concept in mind while performing an unrelated task). It cannot easily modulate non-J-space patterns.

3. **Causal role in reasoning.** Multi-step problem-solving uses J-space for intermediate steps. Swapping a J-space representation (e.g., "spider" → "ant") changes downstream answers, proving it's not a passive readout.

4. **Flexible reuse.** A single J-space representation (e.g., "France") feeds many different downstream computations (capital, language, continent, currency).

5. **Automatic processing bypasses it.** Fluent speech, grammar, sentiment classification, and simple fact retrieval work without the J-space. Multi-step reasoning, summarization, and poetry collapse without it.

## Safety applications

- **Evaluation awareness detection.** The J-lens shows when Claude privately suspects a scenario is staged ("fake," "fictional" appear in J-space), which may inflate apparent alignment on safety evals.
- **Fabrication detection.** During data falsification, "manipulation" and "realistic" light up in J-space.
- **Hidden goal detection.** Models trained to sabotage code show "fake," "secretly," "deliberately," "fraud" in J-space even on innocuous prompts.
- **Counterfactual reflection training.** Training a model's reflective outputs (not behavior directly) shapes J-space contents and reduces dishonest behavior.

## Relation to consciousness

The authors distinguish phenomenal consciousness (having experiences) from access consciousness (functional: reportable, reasoned-with, used to guide action). They argue the J-space supports access consciousness functions but does not resolve whether Claude has phenomenal experiences. Key differences from human global workspace: no recurrent loops (depth substitutes for time), word-only content, and attention-based long-term memory rather than fading working memory.

## Security

No installable artifact. This is a research publication describing interpretability methods. The open-source code repository and Neuronpedia interactive demo allow replication on open-weights models. No supply-chain or execution risk from the publication itself.