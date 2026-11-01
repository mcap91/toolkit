---
name: drugex
title: DrugEx
url: "https://github.com/CDDLeiden/DrugEx"
category: framework
summary: "DrugEx generates novel drug-like small molecules using deep learning generative models within a multi-objective reinforcement learning framework, supporting RNN, SMILES-transformer, and scaffold-constrained graph-transformer generator architectures with Pareto-based multi-objective optimization"
tags: [de-novo-design, reinforcement-learning, multi-objective-optimization, drug-design, transformer, graph-transformer, scaffold-constrained, cheminformatics, generative-chemistry]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [reinvent4, gentrl]
license: MIT
security_flags: []
source: unknown
---

## What it does

DrugEx generates novel drug-like small molecules using deep learning generative models
within a multi-objective reinforcement learning framework. It supports three generator
architectures spanning four versions of development:

- **RNN (GRU/LSTM):** Sequential SMILES generation with exploitation-exploration strategy
- **SMILES-based Transformer:** Attention-based generation with BRICS/RECAP fragmentation
- **Graph-based Transformer:** Enables scaffold-constrained generation — sample molecules
  containing specific substructures

Multi-objective optimization uses Pareto-based RL to simultaneously optimize multiple
properties (activity, selectivity, ADMET, novelty) without collapsing them into a single
scalar reward.

## Pretrained Models

Available on Zenodo for multiple architectures and datasets:

| Dataset | RNN (GRU) | RNN (LSTM) | SMILES Transformer | Graph Transformer |
|---|---|---|---|---|
| ChEMBL 27 | — | yes | — | yes |
| ChEMBL 31 | yes | yes | — | yes |
| Papyrus 05.5 | yes | yes | yes (BRICS/RECAP) | yes (BRICS/RECAP) |

## Installation

```bash
pip install git+https://github.com/CDDLeiden/DrugEx.git@master
# With QSAR model support
pip install "drugex[qsprpred] @ git+https://github.com/CDDLeiden/DrugEx.git@master"
```

Requires CUDA-compatible GPU with ≥8 GB VRAM for full model suite. Multiple GPUs
recommended for transformer models.

## Key Publications

- Sicho, M. et al., "DrugEx: Deep Learning Models and Tools for Exploration of Drug-like
  Chemical Space," *J. Chem. Inf. Model.* 63, 12 (2023).
- Liu, X. et al., "DrugEx v3: Scaffold-Constrained Drug Design with Graph Transformer-based
  Reinforcement Learning," *J. Cheminformatics* 15, 24 (2023).