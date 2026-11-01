---
name: gentrl
title: GENTRL
url: "https://github.com/insilicomedicine/GENTRL"
category: framework
summary: "GENTRL generates novel small molecules optimized for synthetic feasibility, biological activity, and novelty using a variational autoencoder with a tensor-decomposition-parameterized learned prior, trained in a pretrain-then-RL-optimize two-stage pipeline"
tags: [generative-chemistry, variational-autoencoder, reinforcement-learning, de-novo-design, drug-discovery, tensor-decomposition, ddr1, insilico-medicine]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [reinvent4]
license: ""
security_flags: []
source: unknown
---

## What it does

GENTRL generates novel small molecules optimized for synthetic feasibility, biological
activity, and novelty. The architecture is a variational autoencoder (VAE) with a learned
prior distribution parameterized by tensor decompositions, which encode relationships between
molecular structures and properties while handling missing data.

Training is two-stage:

1. **Pretrain:** Learn a latent manifold mapping of chemical space by maximizing the evidence
   lower bound (ELBO) on a molecular dataset (e.g., MOSES)
2. **RL optimization:** Freeze all parameters except the learnable prior; explore the latent
   space to maximize a reward function (e.g., predicted activity against a target)

## Key Result

In the original publication, GENTRL designed potent DDR1 kinase inhibitors. Six compounds
were synthesized; two showed strong DDR1 inhibition (IC50 of 10 nM and 21 nM). One lead
demonstrated favorable pharmacokinetics in mice. The design-to-validation cycle took 46 days
total (21 days for generation, 25 for synthesis and testing).

## Installation

```bash
python setup.py install
```

Requires RDKit and MOSES. Includes Jupyter notebooks for pretraining (`pretrain.ipynb`)
and RL optimization (`train_rl.ipynb`).

## Key Publication

Zhavoronkov, A. et al., "Deep learning enables rapid identification of potent DDR1 kinase
inhibitors," *Nature Biotechnology* 37, 1038–1040 (2019).