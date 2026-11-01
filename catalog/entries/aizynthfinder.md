---
name: aizynthfinder
title: AiZynthFinder
url: "https://github.com/MolecularAI/aizynthfinder"
category: cli-tool
summary: "AiZynthFinder performs retrosynthetic planning — given a target molecule, it finds multi-step synthetic routes back to commercially available starting materials using Monte Carlo tree search with reaction templates suggested by a trained neural network policy"
tags: [retrosynthesis, synthesis-planning, monte-carlo-tree-search, reaction-templates, drug-discovery, astrazeneca, cheminformatics]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

AiZynthFinder performs retrosynthetic planning — given a target molecule, it finds multi-step
synthetic routes back to commercially available starting materials. The default algorithm uses
Monte Carlo tree search (MCTS) that recursively breaks down molecules by applying reaction
templates suggested by a trained neural network policy.

The tool is fully customizable:

- **Search algorithms:** MCTS (default), plus pluggable alternatives
- **Expansion policies:** Neural network trained on known reaction templates; supports custom
  policies
- **Filter policies:** Optional trained network to filter infeasible reactions
- **Stock files:** Define which precursors are considered purchasable/available

## Interfaces

- **`aizynthcli`** — Command-line interface for batch processing
- **`aizynthapp`** — Interactive GUI application

Both take a YAML configuration file specifying the stock, policy networks, and search parameters.

## Quick Start

```bash
conda create "python>=3.10,<3.13" -n aizynth-env
conda activate aizynth-env
pip install aizynthfinder[all]
download_public_data my_folder
aizynthcli --config my_folder/config.yml --smiles smiles.txt
```

Public pretrained models and stock files auto-download from Figshare via `download_public_data`.

## Key Publications

- Genheden, S. et al., "AiZynthFinder: a fast, robust and flexible open-source software for
  retrosynthetic planning," *J. Cheminformatics* 12, 70 (2020).
- Thakkar, A. et al., "Datasets and their influence on the development of computer assisted
  synthesis planning tools," *Chemical Science* 11, 154–168 (2020).