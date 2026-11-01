---
name: synfrag
title: SynFrag
url: "https://github.com/simmzx/SynFrag"
category: cli-tool
summary: "SynFrag predicts whether a molecule is easy or hard to synthesize using a two-stage AttentiveFP graph neural network — pretrained on 9.18M unlabeled molecules via fragment-assembly generation, then fine-tuned on 800K labeled molecules — with attention-heatmap interpretability"
tags: [synthetic-accessibility, fragment-assembly, drug-discovery, cheminformatics, pretraining, attentivefp, interpretability]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: ""
security_flags: []
source: unknown
---

## What it does

SynFrag predicts whether a molecule is easy or hard to synthesize, mimicking how chemists
assess synthetic feasibility. The approach uses a two-stage training pipeline:

1. **Pretrain (Stage 1):** An AttentiveFP graph neural network learns fragment assembly
   patterns via autoregressive generation on 9.18M unlabeled molecules, using a BRICS+2
   fragmentation vocabulary
2. **Fine-tune (Stage 2):** The pretrained encoder transfers to binary SA classification
   on 800K labeled molecules

Output is a score between 0 and 1 (≥0.5 = easy to synthesize). The model provides
interpretability via attention heatmaps that highlight reactive sites and fragment assembly
patterns corresponding to synthetic difficulty.

## Usage

```bash
# Single molecule
python synfrag.py --smiles "CCO"

# CSV batch
python synfrag.py --input_file compounds.csv
```

Input CSV requires a `smiles` column. Output adds a `SynFrag` score column.

## Custom Training

```bash
# Generate fragment vocabulary
python ./scripts/utils/mol/cls.py --input smiles.txt

# Pretrain on unlabeled SMILES
python synfrag_pretrain.py --dataset smiles.txt --vocab fragment.txt

# Fine-tune on labeled data
python synfrag_finetune.py --input_model_file gnn_pretrained.pth --dataset dataset.csv
```

## Requirements

Python ≥ 3.8, PyTorch, RDKit, DGL, DGL-Life, DeepChem. Training requires 4x V100 GPUs.

## Key Publication

Zhang, X. et al., "SynFrag: Synthetic Accessibility Predictor based on Fragment Assembly
Generation in Drug Discovery," *J. Chem. Inf. Model.* (2026).