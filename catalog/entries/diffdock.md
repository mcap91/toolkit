---
name: diffdock
title: DiffDock
url: "https://github.com/gcorso/DiffDock"
category: framework
summary: "DiffDock predicts protein-ligand binding poses with a generative diffusion model operating over the SE(3) space of ligand translations, rotations, and torsion angles, ranking candidate poses by a learned confidence score instead of scoring pre-sampled poses"
tags: [molecular-docking, diffusion-model, protein-ligand, drug-discovery, deep-learning, structural-biology, esmfold]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [autodock-vina]
license: MIT
security_flags: []
source: unknown
---

## What it does

DiffDock predicts protein-ligand binding poses using a generative diffusion model that
operates over the SE(3) product space of ligand translations, rotations, and torsion angles.
Instead of scoring pre-sampled poses, it generates poses by running a learned reverse
diffusion process, producing a distribution of candidate binding conformations ranked by a
learned confidence score.

DiffDock-L (February 2024) extends the original with improved generalization to unseen
binding pockets.

## Input/Output

- **Protein input:** PDB file or amino acid sequence (auto-folded with ESMFold)
- **Ligand input:** SMILES string, SDF, or MOL2 file
- **Output:** Ranked binding poses as SDF files with confidence scores
- **Batch mode:** CSV file with multiple complexes for virtual screening

Confidence score interpretation:
- `c > 0`: high confidence
- `-1.5 < c < 0`: moderate confidence
- `c < -1.5`: low confidence

## Usage

```bash
# Single complex
python -m inference --config default_inference_args.yaml \
  --protein_path protein.pdb --ligand "COc(cc1)ccc1C#N" --out_dir results/

# Batch from CSV
python -m inference --config default_inference_args.yaml \
  --protein_ligand_csv data/protein_ligand_example.csv --out_dir results/
```

Local GUI available via `python app/main.py` (Gradio at localhost:7860).

## Installation

```bash
conda env create --file environment.yml
conda activate diffdock
```

Docker: `docker pull rbgcsail/diffdock`

## Limitations

Designed for small molecule docking to proteins only. Not suitable for protein-protein or
protein-nucleic acid interactions. Does not predict binding affinity directly — confidence
score correlates with pose quality, not binding strength.

## Key Publications

- Corso, G. et al., "DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking,"
  *ICLR* (2023).
- Corso, G. et al., "Deep Confident Steps to New Pockets: Strategies for Docking
  Generalization," *ICLR* (2024).