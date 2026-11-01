---
name: sdf
title: sdf
url: https://github.com/fogleman/sdf
category: framework
summary: Michael Fogleman's Python library for building 3D (and 2D) models from signed distance functions — primitives (sphere, box, torus, cylinder, cone, Platonic solids) composed with boolean ops (union, difference, intersection, including smooth/blended variants), transforms (translate, rotate, scale, twist, bend), and repetition (linear/circular arrays); meshes via Marching Cubes and exports STL natively plus 20+ formats (OBJ, PLY, ...) via meshio; also renders 2D SDFs from text/images for extrusion; actively maintained (pushed 2026-09-30); MIT.
tags:
  - signed-distance-functions
  - procedural-modeling
  - mesh-generation
  - marching-cubes
  - constructive-solid-geometry
  - stl-export
  - python
  - generative-art
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - single-maintainer
source: instagram
source_url: https://www.instagram.com/reel/DemMV03uWzP/
---

## What it does

sdf represents 3D (or 2D) shapes as signed distance functions — functions that take a numpy array of points (shape (N,3) for 3D, (N,2) for 2D) and return, for each point, the signed distance to the shape's surface (negative inside, positive outside). Shapes are built from a library of primitives (sphere, box, torus, cylinder, cone, pyramid, Platonic solids) combined with Python operators for boolean union/difference/intersection, including smooth/blended variants, plus transforms (translate, rotate, scale, twist, bend) and linear/circular repetition. `sdftext.py` renders 2D SDFs from text or images, which can then be extruded into 3D. Meshing uses Marching Cubes; output is natively STL, with 20+ other formats (OBJ, PLY, etc.) available via the `meshio` dependency.

## Mechanical details

- Example: `f = sphere(1) & box(1.5)` for intersection; similar operators cover union (`|`) and difference (`-`), with smooth/blended variants documented separately.
- Dependencies: NumPy, SciPy, scikit-image (Marching Cubes), Pillow, meshio, optional matplotlib for visualization.
- Actively maintained — last pushed 2026-09-30 (per GitHub repo metadata); 2,018 stars, 173 forks as of this review.

## Security

Source-available, MIT licensed. Runs entirely locally — evaluates functions over NumPy point arrays and writes mesh files; no network calls documented. Single-maintainer project (Michael Fogleman), though unlike the other three tools in this family it has recent commit activity.

## Usage notes

- Used to mesh a particle-growth structure: a 3D coral grown by Michael Fogleman's dlaf (6,000 particles, each with a parent link) had every parent link turned into a capsule shape, blended via sdf's smooth-union, thickened where more branches met a point; sdf then cut a flat bottom, added a base, and wrote a closed STL mesh about 8 cm wide (966,012 triangles, 80 x 82 x 55 mm), later sliced into a line drawing by Michael Fogleman's ln (source: https://www.instagram.com/reel/DemMV03uWzP/).
