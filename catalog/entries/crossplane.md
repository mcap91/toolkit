---
name: crossplane
title: Crossplane
url: "https://github.com/crossplane/crossplane"
category: framework
summary: "CNCF framework for building cloud-native control planes without writing code: an extensible Kubernetes-based backend that orchestrates applications and infrastructure wherever they run, plus a configurable frontend that lets you define the schema of the declarative API it offers. v2.x is current (v2.3, May 2026); v1.20 is the final v1 minor release on extended critical-fix-only support."
tags: [kubernetes, control-plane, infrastructure-as-code, cncf, cloud-native, composition, declarative-api, platform-engineering]
reviewed: 2026-08-17
acquired: 2026-08-17
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---
## What it does

Crossplane is a framework for building cloud-native control planes without writing code. It provides a highly extensible backend that lets you build a control plane to orchestrate applications and infrastructure regardless of where they run, and a highly configurable frontend that puts you in control of the schema of the declarative API it exposes. It is a Cloud Native Computing Foundation (CNCF) project, built on Kubernetes-style declarative APIs and controllers, commonly used for platform engineering and infrastructure composition.

## Mechanical details

- **Install/quickstart:** see Crossplane's Get Started docs (install + resource quickstarts).
- **Release cadence:** roughly quarterly minor releases with published EOL dates. As of this review, current v2 line includes v2.1 (Nov 2025), v2.2 (Feb 2026), v2.3 (May 2026), with v2.4–v2.6 scheduled through 2027. v1.20 (May 2025) is the final v1 minor release, receiving extended critical-fixes-only support (EOL TBD).
- **Community/governance:** public GitHub-project roadmap, numerous SIGs (e.g. sig-cli, sig-composition-functions, sig-upjet, sig-v2-migration), 4-weekly community meetings, Slack.
- **Ecosystem:** providers and composition functions extend the backend; `upjet` (sig-upjet) generates providers from Terraform providers.

## Security

- **License:** Apache-2.0 (permissive, no copyleft).
- **Supply chain / governance:** CNCF project with an open maintainer team, documented release process (`crossplane/release`), and published maintained-release/EOL schedule — stay on a maintained release for security fixes.
- As a control plane, Crossplane holds broad credentials to the cloud/infrastructure it orchestrates; provider credential scoping and RBAC on the Kubernetes API it exposes are the primary operational security concerns (standard for infrastructure-orchestration tooling).
