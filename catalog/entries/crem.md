---
name: crem
title: CReM
url: "https://github.com/DrrDom/crem"
category: framework
summary: "CReM generates chemically valid molecular structures by swapping, adding, or linking fragments that share the same chemical context, via four modes — mutate, grow, link, and make-cycle — scoring competitively on the GuacaMol goal-directed benchmark"
tags: [molecular-generation, fragment-based, matched-molecular-pairs, cheminformatics, drug-design, guacamol, rdkit]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [reinvent4]
license: BSD-3-Clause
security_flags: []
source: unknown
---

## What it does

CReM generates chemically valid molecular structures by swapping, adding, or linking
fragments that share the same chemical context — similar to matched molecular pairs. A
fragment database stores context–fragment relationships extracted from molecular datasets.

Four generation modes:

- **`mutate_mol`** — Replace an existing fragment with an interchangeable one
- **`grow_mol`** — Decorate a molecule by replacing hydrogens with fragments
- **`link_mols`** — Connect two molecules with a linker fragment
- **`make_cycle`** — Form new rings or macrocycles via ring-closure fragments

All generators share options for context radius, fragment-size windows, frequency thresholds,
atom protection, custom filter/sample functions, deterministic seeding, and multiprocessing.

## Fragment Databases

Build from any SMILES file:
```bash
cremdb_create -i input.smi -o fragments.db -s chembl
```

Precompiled ChEMBL databases available for download. Databases support multiple fragment sets,
property columns, and sharded/parallel builds.

## Benchmarks

CReM scores 17.919 on the GuacaMol goal-directed benchmark (20 tasks), competitive with
Graph GA (17.983) and above SMILES LSTM (17.341). Achieves perfect 1.000 on all rediscovery,
similarity, deco hop, and scaffold hop tasks.

## Installation

```bash
pip install crem
```

Requires `rdkit>=2025.3.5`. Optional: `guacamol` (benchmarks), `zstandard` (.zst input).

## Key Publications

- Polishchuk, P., "CReM: chemically reasonable mutations framework for structure generation,"
  *J. Cheminformatics* 12, 28 (2020).
- Polishchuk, P., "Control of Synthetic Feasibility of Compounds Generated with CReM,"
  *J. Chem. Inf. Model.* 60, 6074–6080 (2020).