---
name: paperless-ngx
title: Paperless-ngx
url: "https://github.com/paperless-ngx/paperless-ngx"
category: framework
summary: Mature self-hosted document management system — useful for archiving research docs but not an agent tool or developer library
tags: [document-management, self-hosted, ocr, search, archive, docker, paperless]
reviewed: 2026-06-10
acquired: 2026-06-10
license: GPL-3.0
security_flags: [cleartext-storage, no-encryption-at-rest, curl-pipe-bash-install]
overlaps: []
source: unknown
---

## What it does

Paperless-ngx is a self-hosted web application that transforms physical and digital documents into a searchable online archive. It succeeds the original Paperless and Paperless-ng projects and is community-maintained by a distributed team. The system ingests documents (via scanner, email, or manual upload), runs OCR on them, tags and classifies them, and presents a searchable web interface for retrieval.

The platform is deployed via Docker Compose and provides a full-stack web UI for document management. It supports multiple languages via Crowdin-based community translations and has active support channels through GitHub Discussions and a Matrix room. A public demo is available at demo.paperless-ngx.com.

In a bioinformatics or research context, Paperless-ngx could serve as an archive for lab reports, sequencing manifests, vendor invoices, regulatory documents, and grant correspondence — any paper-heavy administrative layer around a research operation.

## Assessment

Paperless-ngx is a solid, production-ready self-hosted platform for document management, not an agent framework, developer library, CLI tool, or skill. It does not integrate into Claude Code workflows or LLM agent pipelines in any documented way. The verdict is **note** rather than **adopt** or **pilot** because there is no direct activation path within the catalog's primary use cases (agent tooling, bioinformatics pipelines).

The project has demonstrated longevity — it is the third-generation successor to the original Paperless project, with an active multi-team contributor community. For users who manage significant volumes of physical or PDF documents in a research environment, this is worth knowing about. However, it competes with and overlaps with Stirling PDF (already cataloged as pilot) in the document-processing space, though Stirling PDF focuses on PDF manipulation rather than archival and retrieval.

The explicit security disclaimer in the README — that documents are stored in clear text and the project should never run on untrusted hosts — is important context for any deployment decision.

## Mechanical details

Deploy with Docker Compose using the official install script:

```
bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"
```

Images are pulled from the GitHub Container Registry. Migration from Paperless-ng is drop-in (replace the Docker image). Full documentation at https://docs.paperless-ngx.com.

The system requires a database (PostgreSQL or SQLite), a Redis broker, and optionally a Tika/Gotenberg instance for enhanced document conversion. All components are wired together in the Docker Compose files under `/docker/compose/`.

There is no MCP server, CLI tool, or API client library provided — integration with external systems requires the REST API that the web application exposes.

## Security

**License:** GPL-3.0. Copyleft obligations apply if distributing modified versions; no restrictions on self-hosted use.

**Encryption:** The README explicitly states data is stored in clear text with no encryption at rest. This is the primary security concern for sensitive document archives. The project recommends running only on a trusted local network with backups.

**Supply chain:** Community-maintained with multiple active contributor teams. No signed releases noted. Docker images pulled from GitHub Container Registry (ghcr.io), which is reasonable for a community project of this size.

**Deployment risk:** The install script uses a curl-pipe-bash pattern which is a known supply chain risk vector. Verify the script before running in any environment.
