---
name: openmm
title: OpenMM
url: "https://github.com/openmm/openmm"
category: framework
summary: "OpenMM runs molecular dynamics simulations as a standalone engine or embeddable library, with custom forces and integrators, CUDA/OpenCL GPU acceleration, AMBER/CHARMM/OpenFF/GAFF force fields, and support for arbitrary PyTorch models as ML/MM force terms"
tags: [molecular-dynamics, gpu-computing, simulation, force-field, protein-simulation, custom-forces, machine-learning-potentials, structural-biology]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

OpenMM runs molecular dynamics simulations with a focus on extensibility and GPU performance.
It can function as a standalone simulation engine or as a library called from custom code.

Key capabilities:

- **Custom forces:** Define novel interaction functional forms with minimal code — single
  implementation runs on all hardware (CPU, CUDA, OpenCL). Includes CustomBondForce,
  CustomNonbondedForce, CustomAngleForce, CustomHbondForce, CustomManyParticleForce, etc.
- **Custom integrators:** Define new integration algorithms via CustomIntegrator. Built-in
  LF-Middle Langevin (allows doubling step size), Nosé-Hoover, multiple time step Langevin
- **GPU acceleration:** CUDA (NVIDIA) and OpenCL (AMD/Intel) with single or mixed precision
- **Force fields:** AMBER, CHARMM, OpenFF, GAFF, GLYCAM; extensible to custom force fields
- **ML potentials (OpenMM 8):** Arbitrary PyTorch models as force terms — enables ML/MM
  hybrid simulations and differentiable simulation

## APIs

- **Python API:** Primary interface for most users, full access to all features
- **C++ API:** For performance-critical applications and extensions

## Installation

Available via conda-forge:
```bash
conda install -c conda-forge openmm
```

## Key Publications

- Eastman, P. et al., "OpenMM 7: Rapid development of high performance algorithms for
  molecular dynamics," *PLoS Comput. Biol.* 13(7), e1005659 (2017).
- Eastman, P. et al., "OpenMM 8: Molecular Dynamics Simulation with Machine Learning
  Potentials," *J. Phys. Chem. B* (2024).