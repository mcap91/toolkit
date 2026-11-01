---
name: geolibre
title: GeoLibre
url: "https://github.com/opengeos/GeoLibre"
category: framework
summary: "Lightweight, cloud-native open-source GIS platform (opengeos) for visualizing, exploring, and analyzing geospatial data locally. Built on Tauri v2, React, MapLibre GL JS, DuckDB-WASM Spatial, and deck.gl; the same workspace runs as a native desktop app, native Android app, in the browser, and inside Jupyter, with 700+ browser-side GIS tools and Earth + planetary basemaps. MIT."
license: MIT
tags: [gis, geospatial, mapping, duckdb-wasm, deck-gl, maplibre, tauri, jupyter]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it is

GeoLibre is a free, open-source, lightweight cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data while keeping data local and private. The same workspace runs as a native desktop app (Windows/macOS/Linux), a native Android app, in any modern web browser, and inside Jupyter notebooks via a Python package, adapting responsively to mobile. It is built with Tauri v2, React, TypeScript, MapLibre GL JS, DuckDB-WASM Spatial, deck.gl, and Turf.js. Capabilities include 3D tiles and extruded city data, a time slider, a SQL workspace, an attribute table, styling/symbology with auto-generated legends, vector and terrain analysis, 700+ browser-side geoprocessing tools, plugins, and embedding. Basemaps cover Earth and planetary bodies (Moon, Mars, Mercury, Venus, the Galilean moons, Titan, Pluto, Charon) with per-project ellipsoids. Authored by Qiusheng Wu (opengeos); releases are archived on Zenodo with a DOI.

## Mechanical details

- **Use:** GeoLibre Web (nothing to install) at geolibre.app; desktop installers for Windows/macOS/Linux; Android app; Docker; or run from source
- **Jupyter:** a Python package provides an in-notebook panel
- Full docs, user guide, and tutorials at geolibre.app; project format, plugin API, and architecture documented in the repo

## Security

MIT licensed. GeoLibre is described as local-first — data stays on the user's device — and processing (including the 700+ tools and DuckDB-WASM Spatial) runs client-side in the app or browser. Optional integrations and remote basemap/tile sources involve outbound requests to those providers. No security flags recorded from the observed material.

## Usage notes

- Tool count has grown to 1,000+ geoprocessing tools (up from 700+ recorded above), and GeoLibre now ships a Model Builder + AI assistant for building reusable geoprocessing workflows from plain-English descriptions (source: https://www.instagram.com/reel/DcZJhbjxXoB/)

## How to use it

geolibre.app (web) / desktop installers / pip (Jupyter package)
