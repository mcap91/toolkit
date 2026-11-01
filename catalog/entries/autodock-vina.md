---
name: autodock-vina
title: AutoDock Vina
url: "https://github.com/ccsb-scripps/AutoDock-Vina"
category: cli-tool
summary: "AutoDock Vina predicts how small molecules bind to protein targets by searching for the lowest-energy binding pose, supporting virtual screening, multi-ligand docking, macrocycle and hydrated-docking protocols, and both AutoDock4.2 and Vina scoring functions"
tags: [molecular-docking, virtual-screening, protein-ligand, drug-discovery, scoring-function, autodock, structural-biology]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

AutoDock Vina predicts how small molecules (ligands) bind to protein targets by searching
for the lowest-energy binding pose within a defined search space. It uses a simple empirical
scoring function combined with rapid gradient-based optimization and iterated local search
for conformational sampling.

Key capabilities:

- **Docking:** Predict binding poses and affinities for protein-ligand complexes
- **Virtual screening:** Batch mode processes compound libraries against a target
- **Multi-ligand docking:** Simultaneously dock multiple ligands
- **Macrocycle support:** Handle ring systems larger than typical drug-like molecules
- **Hydrated docking:** Protocol accounting for explicit water molecules
- **External maps:** Read and write AutoDock grid maps for custom scoring
- **Dual scoring:** Both AutoDock4.2 and Vina scoring functions available

## Python API

Python 3 bindings available on Linux and Mac for programmatic docking workflows.

## Installation

See documentation at readthedocs.org for platform-specific instructions.

## Key Publications

- Eberhardt, J. et al., "AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field,
  and Python Bindings," *J. Chem. Inf. Model.* (2021).
- Trott, O. & Olson, A.J., "AutoDock Vina: improving the speed and accuracy of docking
  with a new scoring function, efficient optimization, and multithreading," *J. Comput.
  Chem.* 31(2), 455–461 (2010).