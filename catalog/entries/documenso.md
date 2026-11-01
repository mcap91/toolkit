---
name: documenso
title: Documenso
url: "https://github.com/documenso/documenso"
category: framework
summary: "Open-source DocuSign alternative for digital document signing — self-hostable TypeScript/React Router v7/Hono/Prisma stack with PDF signature support (@libpdf/core), i18n, Stripe billing, E2E tests (Playwright); Docker/K8s/Railway deployment; AGPL-3.0"
tags: [document-signing, self-hosted, typescript, react, pdf, open-source, docusign-alternative]
reviewed: 2026-09-14
acquired: 2026-09-14
license: AGPL-3.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Documenso is an open-source digital document signing platform, positioned as a self-hostable alternative to DocuSign. Built on a TypeScript stack with React Router v7, Hono server, Prisma ORM, and PostgreSQL.

Core capabilities:
- **PDF signing**: digital signatures via @libpdf/core, viewing via pdf.js, manipulation via @cantoo/pdf-lib
- **Self-hostable**: Docker, Docker Compose, Railway, Kubernetes, or manual deployment
- **Internationalization**: Lingui-based i18n
- **Payments**: Stripe integration
- **Email**: react-email templates, Inbucket for local dev
- **UI**: shadcn/ui + Radix UI + Tailwind CSS

Tech stack: TypeScript, React Router v7, Hono, Prisma, tRPC, Tailwind, Playwright (E2E), Biome (linting). Requires Node.js v24+, PostgreSQL.

## Security

- **License**: AGPL-3.0
- **Security policy**: private vulnerability reports via GitHub Security Advisories
- **Self-hostable**: full data control
- **No external PRs accepted**: closed contributor model with trusted contributors only