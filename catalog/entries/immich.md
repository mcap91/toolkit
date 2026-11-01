---
name: immich
title: Immich
url: "https://github.com/immich-app/immich"
category: framework
summary: Production-ready self-hosted Google Photos alternative with AI search; not agent tooling but solid self-hosted media infrastructure.
tags: [self-hosted, photo-management, video, mobile, ai-search, facial-recognition, oauth, docker]
reviewed: 2026-06-10
acquired: 2026-06-10
license: AGPL-3.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Immich is a high-performance, self-hosted photo and video management platform designed as a privacy-respecting alternative to Google Photos. It provides both a mobile app (iOS/Android) and a web interface, supporting automatic photo backup, album management, shared albums, partner sharing, and public gallery links. The platform stores all media on infrastructure you control and exposes a full REST API with API key authentication.

The platform includes AI-powered capabilities baked in: semantic search via CLIP embeddings lets users find photos by natural-language description, while on-device facial recognition clusters faces and links them to named people. EXIF metadata is parsed and displayed alongside an interactive map view, and a "Memories" feature resurfaces photos from the same date in prior years. Raw camera formats (CR2, NEF, ARW, etc.) and LivePhoto/MotionPhoto files are supported natively.

Multi-user support with OAuth 2.0 / OIDC integration makes Immich deployable for families or small organizations. Storage structure is user-configurable (e.g., by date, album, or custom templates). Offline mobile access, duplicate detection, stacked photos, folder view, and tagging round out the feature set, giving it near-parity with commercial cloud photo services.

## Assessment

Immich is cataloged as `note` because it is a mature, widely-adopted infrastructure tool (50k+ GitHub stars, active release cadence) that is not directly related to agentic bioinformatics workflows. It has no Claude Code integration, no MCP server, and no scripting surface relevant to the toolkit's primary domain. However, it is worth knowing about for anyone building or operating self-hosted lab or personal infrastructure — specimen imaging archives, field photo collections, or lab documentation photo libraries could all benefit from a self-hosted media management layer.

The AGPL-3.0 license is appropriate for a self-hosted tool: you can self-host freely, but any modifications distributed publicly must be open-sourced under the same terms. The project has a very healthy contributor base and frequent releases, making it a low-risk infrastructure choice. It competes directly with PhotoPrism and Nextcloud Photos in the self-hosted space.

## Mechanical details

Deployment is via Docker Compose; the official `docker-compose.yml` and environment file are the recommended installation path. The server runs as a set of containers (server, microservices, machine-learning, database, Redis, proxy). Documentation lives at https://immich.app/docs.

Mobile apps are available on the App Store and Google Play. API access uses bearer tokens (API keys generated in the web UI). The REST API is fully documented and supports programmatic upload, search, and management. An optional machine-learning container handles CLIP embeddings and facial recognition and can be disabled if GPU/CPU resources are constrained.

Updates follow a rolling release model with semantic versioning; the project strongly recommends keeping server and mobile apps on the same version.

## Security

License is AGPL-3.0, which requires open-sourcing any modifications if distributed. No commercial restrictions on self-hosting. The project is well-maintained with a large contributor base and regular security-focused releases. No eval() usage, shell injection vectors, or credential handling issues are evident from the repository surface. The self-hosted deployment model means all data stays on the operator's infrastructure; no third-party cloud telemetry is documented. Users should follow the project's stated 3-2-1 backup recommendation, as Immich explicitly does not consider itself a primary backup solution.
