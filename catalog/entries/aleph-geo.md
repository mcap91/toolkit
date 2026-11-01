---
name: aleph-geo
title: Aleph
url: https://github.com/Belluxx/Aleph
category: cli-tool
summary: Python CLI/dashboard (alephgeo) that downloads satellite imagery, terrain elevation, OSM buildings, Street View photos, and textured 3D meshes for any drawn area or named place, with no API key; built to give LLMs a local, structured snapshot of real-world geography; MIT license; pulls undocumented Google APIs so may break or rate-limit.
tags:
  - geospatial
  - gis
  - satellite-imagery
  - street-view
  - 3d-tiles
  - terrain
  - openstreetmap
  - cli-tool
  - python
  - llm-tooling
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags:
  - tos-violation-risk
  - undocumented-api-dependency
  - mixed-data-licensing
overlaps: []
source: instagram
source_url: https://www.instagram.com/reel/DeyBZyUDLg9/
---

## What it does

Aleph (`alephgeo` CLI, Belluxx) downloads a textured snapshot of a real-world place to a local folder, with no API key required. A browser dashboard (`alephgeo dashboard -o captures`, served at `127.0.0.1:8100` over OpenFreeMap basemaps) lets you draw a rectangle or polygon on a map and pulls everything inside it: OSM building footprints, elevation/terrain, HD satellite imagery, Street View photos, and textured 3D meshes. The CLI provides the same data for a named place or point on the fly, e.g. `alephgeo streetview --place "Colosseum, Rome" --best-match -o captures` or `alephgeo satellite --place "Colosseum, Rome" --best-match -o captures`. The README states the project was built so LLMs can quickly gather information about the physical world, though it works standalone as a way to save a piece of the Earth locally.

## Mechanical details

- Requires Python 3.11+; dependencies are Pillow, numpy, and truststore — no API keys.
- Install: `git clone`, venv, `python -m pip install .`, then `alephgeo --help`.
- Each capture (dashboard or CLI) is saved to its own folder under the given output directory (e.g. `captures`); the dashboard can open any past capture to toggle layers or explore the 3D mesh/terrain relief.
- Python project, ~390 stars as of this capture (Oct 2026); tagged 3d-city-model, 3d-tiles, gltf on GitHub.
- README explicitly warns the tool uses undocumented APIs and so may break or hit rate limits.

## Security

- MIT license on the code itself (repo LICENSE file, ~21 lines, standard MIT boilerplate).
- `tos-violation-risk` — README states downloading Street View, satellite imagery, and 3D meshes goes against Google's terms of service; the project is explicitly not affiliated with Google, and the README puts responsibility for use of the downloaded data on the user.
- `mixed-data-licensing` — OSM/geocoding data is ODbL (commercial use allowed with attribution, derivative databases must stay ODbL); terrain comes from AWS Terrain Tiles under its own open-source attribution terms; Google-sourced imagery/meshes carry no redistribution rights per the above.
- `undocumented-api-dependency` — satellite, Street View, and mesh fetching rely on undocumented Google endpoints rather than a public API, so behavior can change or be rate-limited without notice.
- No code-execution or credential-handling concerns observed in the fetched README; full source not reviewed line-by-line.
