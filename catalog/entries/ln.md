---
name: ln
title: ln
url: https://github.com/fogleman/ln
category: framework
summary: Michael Fogleman's Go library/renderer that draws 3D scenes as vector line art instead of raster images — paths are chopped to a resolution, each point ray-cast toward the camera to test occlusion, and visible paths projected to 2D and output as PNG or SVG; supports primitives (sphere, cube, triangle, cylinder), OBJ/STL mesh import, CSG (union/intersection/difference), and custom vector-based texturing; built for pen-plotter output; last pushed 2019-07-19; MIT.
tags:
  - line-art
  - hidden-line-removal
  - vector-graphics
  - pen-plotter
  - ray-casting
  - csg
  - go
  - generative-art
  - 3d-rendering
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - unmaintained
  - single-maintainer
source: instagram
source_url: https://www.instagram.com/reel/DemMV03uWzP/
---

## What it does

ln renders 3D scenes as line drawings rather than shaded raster images. It chops a scene's paths into segments at a given resolution, then for each point casts a ray toward the camera: an unobstructed point is visible, an obstructed one is hidden and dropped. Visible paths are transformed into 2D space via the camera's projection matrices and written out as PNG or SVG. It was built with physical pen-plotter output in mind (the author's own README cites plotting drawings on a Makeblock XY Plotter). Primitives include spheres, cubes, triangles, cylinders, and arbitrary 3D functions; it can import triangle meshes from OBJ/STL, supports CSG operations (union, intersection, difference) via a `Contains` method on its `Shape` interface, and supports custom vector-based texturing.

## Mechanical details

- Go library; install via `go get github.com/fogleman/ln/ln`.
- `Shape` interface requires `Paths()`, `Intersect()`, `Contains()`, `BoundingBox()`. Scene rendering takes camera parameters (eye, center, up, FOV, near/far planes) and a path resolution.
- Last pushed 2019-07-19 (per GitHub repo metadata); 3,499 stars, 143 forks as of this review.

## Security

Source-available, MIT licensed. Runs entirely locally over in-memory mesh/path data and camera parameters; no network calls documented. Single-maintainer project (Michael Fogleman) with no commits since 2019.

## Usage notes

- Used to draw a mesh built by Michael Fogleman's sdf library (itself derived from a dlaf coral structure): ln sliced the mesh at 131 heights and removed hidden lines, cutting roughly three quarters of the raw line pixels (example: 554,006 px of line input down to 139,619 px visible at 131 slices, vs 50,288 px visible at 51 slices) while still reading as solid coral; fewer slices gave a lighter drawing (source: https://www.instagram.com/reel/DemMV03uWzP/).
