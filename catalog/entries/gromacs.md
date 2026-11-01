---
name: gromacs
title: GROMACS
url: "https://github.com/gromacs/gromacs"
category: framework
summary: "GROMACS is a widely used molecular dynamics simulation package for proteins, lipids, and nucleic acids, optimized through multi-level parallelism (SIMD, GPU offloading via CUDA/OpenCL/SYCL, and MPI) with support for AMBER/CHARMM/GROMOS/OPLS force fields and free-energy calculations"
tags: [molecular-dynamics, simulation, gpu-computing, hpc, force-field, protein-simulation, free-energy, structural-biology, parallel-computing]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [openmm]
license: LGPL-2.1
security_flags: []
source: unknown
---

## What it does

GROMACS is one of the most widely used molecular dynamics simulation packages, primarily
designed for simulations of proteins, lipids, and nucleic acids. It is extremely optimized
for computational performance through multi-level parallelism:

- **Intra-node:** SIMD vectorization, multi-threading
- **GPU offloading:** CUDA (NVIDIA), OpenCL, SYCL for compute-intensive kernels
- **Inter-node:** MPI for distributed computing on HPC clusters
- **Hybrid:** Combined MPI + threads + GPU for maximum throughput

Key simulation capabilities:

- **Force fields:** AMBER, CHARMM, GROMOS, OPLS families
- **Free energy calculations:** Thermodynamic integration, free energy perturbation
- **Enhanced sampling:** Replica exchange MD, metadynamics (via PLUMED plugin)
- **Coarse-grained:** Martini force field support
- **Analysis:** Extensive built-in trajectory analysis tools (gmx commands)

## Building

```bash
cmake .. -DGMX_GPU=CUDA -DGMX_MPI=ON
make -j$(nproc)
make install
```

See the installation guide at manual.gromacs.org for platform-specific options.

## Development

Primary development and issue tracking on GitLab (`gitlab.com/gromacs/gromacs`).
The GitHub repository is a public mirror/backup.

## Key Publications

- Abraham, M.J. et al., "GROMACS: High performance molecular simulations through
  multi-level parallelism from laptops to supercomputers," *SoftwareX* 1, 19–25 (2015).
- Hess, B. et al., "GROMACS 4: Algorithms for highly efficient, load-balanced, and
  scalable molecular simulation," *J. Chem. Theory Comput.* 4, 435–447 (2008).