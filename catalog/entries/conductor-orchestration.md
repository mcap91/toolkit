---
name: conductor-orchestration
title: "Conductor: RL-Trained LLM Orchestrator"
url: "https://arxiv.org/abs/2512.04388"
category: agent-pattern
summary: "Sakana AI paper (ICLR 2026) introducing a 7B 'Conductor' model trained with RL to orchestrate pools of worker LLMs — learns communication topologies, per-agent prompt engineering, and recursive self-delegation; achieves SOTA on LiveCodeBench and GPQA by coordinating frontier models."
license: ""
tags: [multi-agent, orchestration, reinforcement-learning, llm-coordination, agent-topology, prompt-engineering, reasoning, sakana-ai]
reviewed: 2026-09-04
acquired: 2026-09-04
overlaps: [agent-teams, scheduled-multi-agent-coordinator]
security_flags: []
source: unknown
---

## What it does

The Conductor is a 7B-parameter language model trained with reinforcement learning to orchestrate pools of worker LLMs on complex tasks. Given a problem, the Conductor outputs a collaborative workflow in natural language: a sequence of steps where each step specifies a natural-language instruction focusing on a subtask, the worker agent assigned to that instruction, and each agent's visibility into other agents' outputs. The Conductor learns three things end-to-end via reward maximization: (1) how to decompose problems into targeted subtasks, (2) which worker LLM to assign each subtask to based on that model's strengths, and (3) what communication topology to use (which agents see which other agents' outputs).

Training uses randomized agent pools, so the Conductor generalizes to arbitrary mixes of open- and closed-source models at inference time. Allowing the Conductor to select itself as a worker produces recursive topologies — a form of dynamic test-time compute scaling through iterative self-delegation.

## Assessment

The paper demonstrates that multi-agent coordination strategies can emerge from pure RL rather than requiring hand-designed workflows. A 7B Conductor orchestrating frontier workers (GPT-5, Gemini, Claude, open-source models) outperforms any individual worker on LiveCodeBench and GPQA. The core insight — that a small model can learn to prompt-engineer and route among larger models — is relevant to agent-toolkit design. The recursive self-delegation finding (Conductor assigns subtasks to itself) is a novel form of test-time scaling. Published at ICLR 2026 (Sakana AI, University of Michigan, Institute of Science Tokyo). No released model weights or code as of the paper; the contribution is the technique and empirical validation.

## Mechanical details

- **Architecture:** 7B-parameter LLM trained with RL (reward = task correctness)
- **Input:** A task description + available worker pool
- **Output:** Natural-language workflow — sequence of (instruction, assigned_agent, visibility_topology) steps
- **Training signal:** End-to-end reward maximization; no hand-designed coordination rules
- **Generalization:** Trained with randomized agent pools so it adapts to unseen model combinations
- **Recursive topologies:** Conductor can assign itself as a worker, creating nested delegation chains
- **Benchmarks:** SOTA on LiveCodeBench (code reasoning) and GPQA (graduate-level QA)

## Security

Academic paper; no deployed system or installable artifact. The described approach runs arbitrary LLM calls to multiple providers, inheriting each provider's API trust and cost model. The Conductor's prompt-engineering output is opaque (RL-learned), which could produce unexpected or adversarial prompts to worker models in edge cases.

## Usage notes

- Companion paper to Trinity (arXiv:2512.04695), which uses a much smaller 0.6B coordinator with evolutionary optimization (sep-CMA-ES) instead of RL. Both feed into Sakana's commercial product Fugu.
