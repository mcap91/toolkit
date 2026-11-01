---
name: stirling-pdf
title: Stirling PDF
url: "https://github.com/Stirling-Tools/Stirling-PDF"
category: cli-tool
summary: Self-hosted REST API for 50+ PDF operations enables privacy-preserving agentic PDF workflows without external services
tags: [pdf, self-hosted, rest-api, docker, ocr, document-processing, automation]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [open-core-commercial-features]
overlaps: [open-data-loader-pdf, markitdown]
source: unknown
---

## What it does

Stirling PDF is a self-hosted, open-source PDF platform offering 50+ PDF operations through a browser UI and a REST API. Core capabilities include merging, splitting, compressing, converting (PDF↔Office, PDF↔images), OCR, redacting, signing, adding watermarks, rotating pages, and flattening forms. It can run as a desktop app, a browser-based tool, or a Docker-deployed server exposing a private REST API. Automation workflows can be composed directly in the UI (no-code pipelines) or driven programmatically via the API. Enterprise features (SSO, audit logging) are available in a paid tier.

## Assessment

**Pilot.** The REST API surface makes Stirling PDF genuinely useful as an agent tool — an agent can dispatch PDF manipulation tasks (OCR a paper, redact PII from a report, merge supplementary files) to a local server without sending documents to external services. This is a meaningful privacy win for bioinformatics workflows that involve patient data or confidential research. The Docker quick-start is simple (`docker run -p 8080:8080 ...`). However, it requires a running server, which adds operational overhead compared to CLI tools like MarkItDown or OpenDataLoader PDF. The open-core model means some features (SSO, enterprise auditing) require a commercial plan; the free tier is broad enough for most agent use cases. It earns pilot rather than adopt because of the server dependency and because MarkItDown already covers the primary "read a PDF" agent pattern — this is the complement for write/transform operations.

## Mechanical details

- **Deployment**: Docker image (`docker.stirlingpdf.com/stirlingtools/stirling-pdf`); also Kubernetes and desktop installers.
- **API**: Full REST API documented at https://docs.stirlingpdf.com — nearly every tool has an API endpoint. Supports bulk/batch processing.
- **Integration pattern**: Agent calls REST endpoint with PDF payload → receives transformed PDF or extracted text. No LLM calls; pure document processing.
- **Languages**: 40+ UI languages; API is language-agnostic.
- **Build tooling**: Uses `task` (Taskfile) as the unified command runner. `task install` bootstraps development.
- **Overlap**: MarkItDown handles PDF→text extraction (simpler, no server). OpenDataLoader PDF is a lighter CLI extraction tool. Stirling PDF complements both by covering write-side and transform operations MarkItDown does not support.

## Security

- **License**: Open-core. The base project is MIT-licensed; enterprise/advanced features are commercial. The `open-core-commercial-features` flag reflects that some capabilities are gated behind a paid plan.
- **Privacy**: By design, all processing is local/self-hosted — no documents leave the deployment boundary. This is a security positive for sensitive data.
- **Attack surface**: Exposes an HTTP server; standard web application risks apply (unauthenticated access if not behind auth, SSRF from URL-based inputs). The enterprise tier adds SSO to mitigate access control concerns.
- **Supply chain**: High-profile project (#1 PDF app on GitHub by stars), active community, public CI. No signed release artifacts noted in the README.
- **Dangerous patterns**: No agent-side code execution; PDF operations run in the server container, limiting blast radius if a malformed PDF triggers a parser bug.
- **Recommendation**: Deploy behind an auth layer or firewall. Do not expose the API publicly without authentication. Review open issues for known CVEs before deploying with sensitive documents.
