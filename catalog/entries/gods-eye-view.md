---
name: gods-eye-view
title: "God's Eye View"
url: "https://github.com/bilawalsidhu/gods-eye-view"
category: framework
summary: "Browser-based open-source spatial-intelligence globe (vanilla JS + CesiumJS + Vite) fusing live public feeds — 11k+ aircraft, ships, satellites, earthquakes, fires, ~800 public CCTV cameras, radio, launches — onto a photorealistic 3D Earth, with an OpenAI Realtime voice agent (28 tools) for hands-free control; keyless baseline, MIT per README; ~24k stars, #1 GitHub Trending Aug 2026"
tags: [osint, geospatial, spatial-intelligence, cesiumjs, 3d-globe, flight-tracking, voice-agent, openai-realtime, satellite-tracking, javascript, local-first]
reviewed: 2026-09-10
acquired: 2026-09-10
license: MIT
security_flags: [lan-sharing-key-exposure, metered-api-spend, data-source-terms-vary]
overlaps: []
source: unknown
---

## What it does

God's Eye View (Bilawal Sidhu and Sameh Khamis, Halfpixel; formerly WorldView) is a "spy-satellite simulator" that runs locally in the browser and fuses live public data onto a photorealistic 3D globe: 11,000+ live aircraft (OpenSky/adsb.lol), military ADS-B traffic, global ships (AISStream), an 838-object satellite catalog (CelesTrak, SGP4-propagated), USGS earthquakes, NASA FIRMS fires, ~800 public CCTV cameras projected into 3D space (Austin/Caltrans/TfL), geolocated world radio, bikeshare, rocket launches, and bundled static datasets (4,351 datacenters, 704 dams, 712 submarine cables). Thirteen layers; eleven work with no API key.

A realtime voice agent (OpenAI Realtime API, 28 tools) flies the camera, annotates real boundaries, answers analyst queries against live layers ("Which ships are headed to Oakland?"), and operates the console hands-free. Features include click-to-track with trails and telemetry, cockpit mode riding live flights over real terrain, GLSL sensor styles (NVG, FLIR, CRT), detection overlays, a military HUD, scene director, and shareable state URLs.

## Differentiators

- Keyless baseline: Esri imagery + keyless terrain with OSM fallback; keys are in-app upgrades (Cesium ion for photorealistic 3D, Google Maps metered, OpenAI for voice) via a POWER UP panel with a live session-spend readout, $2 warning, and $5 hard cap on voice.
- No framework: vanilla JavaScript + CesiumJS + Vite; one module per data layer, explicitly designed for extension ("add a layer, send the PR").
- Server-side credential brokering: every private key (OpenAI, AISStream, OpenSky OAuth, camera frames) goes through a hardened localhost proxy with SSRF protection, response caps, and sanitized errors; only Google Maps/Cesium ion keys reach the browser.
- Explicit ethics line: no named-person search, face recognition, or individual tracking; such PRs are rejected. "People are not a query type here."
- Honest-data labeling: traffic is simulated on real roads, CCTV poses are estimated priors, launch replays are marked RECONSTRUCTED ESTIMATE.

## Mechanical details

- Install: Pinokio 8.2+ one-click, or `git clone && npm ci && npm run doctor && npm run dev` (Node 24.14+/26.x) → localhost:4173; macOS `./scripts/dev-fresh.sh` pulls keys from Keychain.
- Keys land in repo-root `.env` (or Pinokio ENVIRONMENT), owner-only permissions, git-ignored; `npm run doctor` reports provider readiness without printing values.
- Rate governors: OpenSky credit governor, TomTom daily tile budget, disk-cached TLEs; per-IP throttles (`GEV_RATELIMIT_*`) for LAN sharing.
- JavaScript, ~24.3k stars, ~5k forks, 180 open issues; created 2026-06, active; #1 GitHub Trending (daily and weekly) Aug 2026; hosted version announced at Halfpixel (maptheworld.ai).

## Security

- **License:** README states MIT; GitHub shows "Other" because bundled/live datasets carry their own terms (DATA_SOURCES.md) and media assets are restricted — check per-source terms before redistribution.
- `lan-sharing-key-exposure` — binding to 0.0.0.0 brokers your configured API keys to anyone on the LAN; SECURITY.md documents the threat model, and Provider Settings disables itself when shared. Pinokio LAN/Cloudflare sharing is deliberately disabled.
- `metered-api-spend` — Google Maps and OpenAI keys are metered; app-level throttles and the $5 voice cap are not billing caps; provider quotas/budget alerts still required.
- `data-source-terms-vary` — Cesium ion free tier is personal/non-commercial only; GIF media not licensed for standalone reuse.
- Disclaimer: exploratory visualization; not for navigation, emergency response, or safety-critical use.