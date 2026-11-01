---
name: north-star-osint
title: North Star
url: "https://nstarlive.com/"
category: framework
summary: "Commercial SaaS OSINT platform unifying nine intelligence sectors — a live 250,000+ camera globe with local YOLOv8 detection, username/breach-database lookup, multi-chain crypto wallet tracing, network/port/.onion scanning, photo geolocation, radio-spectrum monitoring, trackable-link visitor telemetry (Fisherman), and 100+-registry public-records search — behind a paid subscription with no self-hosting or open-source code"
tags: [osint, geospatial, geolocation, crypto-tracing, network-scanning, saas, surveillance]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Proprietary
security_flags: [closed-source, new-project, unverified-vendor-claims, third-party-data-capture]
overlaps: [gods-eye-view]
source: unknown
---

## What it does

North Star is a browser-based, subscription-only OSINT (open-source intelligence) platform bundling nine "intelligence sectors" behind one interface:

1. **Camera Globe** — 250,000+ live public cameras plotted on a 3D globe; YOLOv8 object detection (people, vehicles, 80+ classes) runs locally in the browser; a geofenced AI search scans every camera inside a drawn boundary; GeoCLIP estimates location from an uploaded photo and reads its EXIF (GPS, camera model, timestamp).
2. **Username Research** — cross-platform username search, breach/leak database cross-referencing, IP/domain/ASN lookups tied to an identity, exposed-device/service discovery, linked-email discovery, exportable case reports.
3. **Crypto Tracing** — wallet address analysis across 22+ chains (Bitcoin, Ethereum and other EVM chains, Solana, Tron, XRP, Cardano); hop-by-hop transaction graph with exchange/mixer labelling, time-window isolation, and case export.
4. **NetScan** — accepts an IP, domain, CIDR range, or .onion address; WHOIS/DNS/subdomain enumeration from six independent sources; port, service-version, TLS, and OS fingerprinting; Tor-routed scanning of hidden services; historical scan data and related-host discovery with known CVEs.
5. **Hawk** — geolocates a photograph by matching it against satellite and street-level imagery, plus OCR of signage, phone prefixes, and licence-plate formats.
6. **Skywave** — radio-frequency lookup (service/band plan/licensee), ranks public receivers by distance, reports real-time propagation for maritime and shortwave bands.
7. **Fisherman** — generates trackable links; each visit is logged with timestamped browser, device, referrer, IP, ASN, and (if location is shared) GPS coordinates.
8. **Catalogue** — fans a single search across 100+ official public-record sources (courts, corporate filings, sanctions/PEP lists, property/vital records); falls back to a pre-filled deep link where a source has no API.
9. **Watchtower** (founders-tier only) — live vessel/aircraft tracking, natural-hazard feeds, and infrastructure layers (submarine cables, pipelines, power).

Built on OpenStreetMap, NASA Earth Observatory imagery, MaxMind GeoIP, GeoCLIP, and Ultralytics YOLOv8.

## Mechanical details

Access is subscription-only through the web app — no install, no self-hosting, no public source code. Individual "Founders" tier: £20/month for all nine sectors and 5 case seats. Team "Professional" tiers add analyst seats, API access, and additional forensic sectors (Genie, Echo, Mirage, file forensics, facial recognition, threat intel): Emerald £80/mo (5 seats, no API), Sapphire £150/mo (12 seats, 100 API credits), Diamond £300/mo (25 seats, 1,000 API credits). An Enterprise tier is available on contact. The company also runs a public referral/affiliate program offering commission or free access for promotion.

## Security

No open-source code to audit — proprietary, closed-source SaaS with no self-hosted option (license set to Proprietary; no SPDX identifier applies). The Terms of Service disclaim responsibility for the accuracy, completeness, or legality of any output (camera feeds, scans, OSINT results, crypto traces) and place the entire legal-compliance burden on the user, while stating the service "does not authorize surveillance, harassment, unlawful deception, unauthorized system access, or unlawful personal data processing." The privacy policy states camera viewing and object detection run client-side (not server-processed) and that personal data is not sold or used to train models without separate permission.

Independent verification is thin: third-party registrar/review-aggregator lookups show the domain is new (~2 months old at time of review, first indexed by review sites in July 2026) with no independent user reviews found. The Team/About pages describe "a small, remote team of engineers and designers" without naming individuals. All feature claims in this entry (camera count, breach-database coverage, chain coverage, registry count) are vendor-stated and unverified by this review.

The Fisherman sector is a link-based visitor-tracking mechanism that captures IP, ASN, device, browser, and GPS data (when shared) from anyone who clicks a generated link — a third-party data-capture capability inherent to the product, separate from how the camera/OSINT sectors are used.