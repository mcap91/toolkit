---
name: chemberta3
title: ChemBERTa-3
url: "https://github.com/deepforestsci/chemberta3"
category: framework
summary: "ChemBERTa-3 is a training and benchmarking framework for chemical foundation models, providing a unified pipeline to pretrain, fine-tune, and evaluate transformer and graph-pretraining architectures on molecular property prediction tasks against MoleculeNet benchmarks"
tags: [chemical-foundation-model, smiles, molecular-property-prediction, pretraining, cheminformatics, deepchem, transformer, moleculenet, benchmarking]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: ""
security_flags: []
source: unknown
---

## What it does

ChemBERTa-3 is a training and benchmarking framework for chemical foundation models. It
provides a unified pipeline to pretrain, fine-tune, and evaluate multiple model architectures
on molecular property prediction tasks.

Supported model architectures:

- **Transformer models:** ChemBERTa (masked language modeling on SMILES), MoLFormer
- **Graph pretraining models:** GROVER, InfoGraph, Infomax3D
- **Baseline supervised models:** GCN, D-MPNN, Random Forest

Pretraining datasets scale from 250K SMILES (graph models) up to 1.4B compounds from ZINC20
and PubChem. The largest pretrained MoLFormer variant (c3-MoLFormer-1.1B) trains on 100%
ZINC20 + 100% PubChem.

## Benchmarking

Fine-tuning and evaluation use MoleculeNet datasets with scaffold splits:

- **Classification:** BACE, BBBP, ClinTox, HIV, Tox21, SIDER (ROC-AUC)
- **Regression:** ESOL, BACE_R, Lipophilicity, FreeSolv, Clearance (RMSE)

Supports both DeepChem scaffold splits and MoLFormer-paper splits for reproducibility.
Triplicate runs reported with ranges.

## Featurizers

CircularFingerprint (ECFP), MolGraphConv, RDKit 3D conformers, GROVER graph features,
D-MPNN atom/bond features, and a dummy passthrough for SMILES-native models.

## Pretrained Models

Available on HuggingFace at `DeepChem` organization:

| Model | Pretrained On |
|---|---|
| c3-MoLFormer-1.1B | 100% ZINC20 + 100% PubChem |
| c3-MoLFormer-550M | 50% ZINC20 + 50% PubChem |
| c3-MoLFormer-100M | 10% ZINC20 |
| ChemBERTa-MLM-100M | 10% ZINC20 |
| ChemBERTa-MLM-10M | 1% ZINC20 |

## Installation

```bash
git clone https://github.com/deepforestsci/chemberta3
pip install --pre deepchem
pip install -r requirements.txt
```