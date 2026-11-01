---
name: trinity-coordinator
title: "Trinity: Evolved LLM Coordinator"
url: "https://arxiv.org/abs/2512.04695"
category: agent-pattern
summary: "Sakana AI paper (ICLR 2026) on a 0.6B coordinator trained via evolutionary strategy (sep-CMA-ES) to orchestrate pools of LLMs through multi-turn role assignment (Thinker/Worker/Verifier); 86.2% on LiveCodeBench, zero-shot transfer to unseen tasks. Companion to Conductor (RL approach)."
license: ""
tags: [multi-agent, orchestration, evolutionary-strategy, llm-coordination, role-assignment, cma-es, reasoning, sakana-ai]
reviewed: 2026-09-04
acquired: 2026-09-04
overlaps: [conductor-orchestration, agent-teams]
security_flags: []
source: unknown
---

## What it does

Trinity is a lightweight coordinator (0.6B-parameter language model + ~10K-parameter head) that orchestrates collaboration among pools of LLMs on complex tasks. Optimized with sep-CMA-ES (separable Covariance Matrix Adaptation Evolution Strategy), the coordinator processes queries over multiple turns, assigning one of three roles at each turn — Thinker (reason about the problem), Worker (produce a solution), or Verifier (check the output) — to a selected worker LLM from the pool. This offloads complex skill acquisition to the large worker models while keeping the coordinator extremely compact.

The coordinator's hidden-state representations contextualize inputs to select both the right model and the right role at each turn. Training uses evolutionary optimization rather than RL because, under high dimensionality and strict parameter budgets, sep-CMA-ES exploits potential block-epsilon-separability more efficiently than reinforcement learning, imitation learning, or random search.

## Assessment

Trinity is the companion paper to Conductor (arXiv:2512.04388) — both from Sakana AI, both ICLR 2026, same research team (Jinglue Xu, Stefan Nielsen, et al.). Where Conductor uses a 7B model with RL to learn communication topologies and prompt engineering, Trinity uses a much smaller coordinator (0.6B + 10K head) with evolutionary optimization and a fixed three-role framework (Thinker/Worker/Verifier). Trinity achieves 86.2% on LiveCodeBench and transfers zero-shot to unseen tasks (AIME, BigCodeBench, MT-Bench, GPQA). Both papers feed into Sakana's commercial product Fugu, which combines the approaches. The key insight for toolkit design: a sub-billion-parameter model can effectively route and role-assign among frontier models, and the Thinker/Worker/Verifier decomposition is a reusable multi-turn pattern.

## Mechanical details

- **Coordinator size:** ~0.6B parameters (compact LM) + ~10K parameters (lightweight head)
- **Optimization:** sep-CMA-ES (derivative-free evolutionary strategy), not RL or imitation learning
- **Role assignment:** Three roles per turn — Thinker (reason), Worker (solve), Verifier (check)
- **Multi-turn:** Each query processed over multiple turns with different model+role assignments
- **Zero-shot generalization:** Transfers to unseen tasks without retraining
- **Benchmarks:** 86.2% LiveCodeBench; outperforms individual models on coding, math, reasoning, domain knowledge
- **Commercial product:** Sakana Fugu combines Trinity and Conductor approaches

## Security

Academic paper; no standalone installable artifact. Same considerations as Conductor: the approach calls multiple LLM provider APIs, inheriting each provider's trust and cost model. The coordinator's role assignments are learned (not hand-designed), so delegation behavior is opaque at the decision level.