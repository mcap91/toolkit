---
name: reinvent4
title: REINVENT 4
url: "https://github.com/MolecularAI/REINVENT4"
category: framework
summary: "REINVENT 4 generates optimized small molecules matching a user-defined multi-component property profile via reinforcement learning over RNN and transformer generative models, supporting de novo design, scaffold hopping, R-group replacement, linker design, and library design"
tags: [molecular-design, de-novo-design, reinforcement-learning, generative-chemistry, smiles, drug-design, scaffold-hopping, astrazeneca, cheminformatics]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

REINVENT 4 generates optimized small molecules compliant with a user-defined multi-component
property profile. The core loop uses reinforcement learning to steer generative models (RNN
and transformer architectures operating on SMILES strings) toward desired molecular properties.

Supported design modes:

- **De novo design:** Generate novel molecules from scratch matching a property profile
- **Scaffold hopping:** Replace a molecular scaffold while preserving activity-relevant features
- **R-group replacement:** Explore substitutions at defined positions on a scaffold
- **Linker design:** Generate molecular linkers connecting two fragments (e.g., for PROTACs)
- **Molecule optimization:** Iteratively improve an existing molecule's properties
- **Library design:** Generate focused compound libraries

Transfer learning pre-trains or fine-tunes models toward a target chemical space. Curriculum
learning stages objectives progressively during RL.

## Architecture

- **Generators:** Recurrent neural networks (Reinvent, LibInvent, LinkInvent) and transformers
  (Mol2Mol) for different design tasks, unified under one framework
- **Scoring:** Plugin-based scoring subsystem using Python namespace packages — custom scorers
  drop into `reinvent_plugins/components/` without modifying core code
- **Configuration:** TOML (primary), JSON, or YAML config files specify run mode, model,
  scoring components, and parameters
- **Prior models:** Pre-trained models hosted on Zenodo; internal priors referenced via dot notation

## Installation

```bash
conda create --name reinvent4 python=3.11
conda activate reinvent4
git clone git@github.com:MolecularAI/REINVENT4.git
cd REINVENT4
python install.py cu126  # or rocm6.4, xpu, mac, cpu
```

Also supports `uv sync` for faster setup.

## Key Publication

Loeffler, H. H. et al., "Reinvent 4: Modern AI-driven generative molecule design,"
*Journal of Cheminformatics* 16, 20 (2024). Open access.