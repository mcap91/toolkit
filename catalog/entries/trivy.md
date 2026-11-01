---
name: trivy
title: Trivy
url: "https://github.com/aquasecurity/trivy"
category: cli-tool
summary: "Aqua Security's all-in-one security scanner (Go) — finds vulnerabilities (OS packages + language dependencies), IaC misconfigurations, secrets, and licenses across container images, filesystems, git repos, VM images, Kubernetes clusters, and AWS accounts; generates and scans SBOMs (SPDX/CycloneDX); single static binary, offline-capable DB, CI-native; Apache-2.0, ~38k stars"
tags: [security-scanner, vulnerabilities, containers, sbom, secrets-detection, iac, kubernetes, devsecops, supply-chain, go]
reviewed: 2026-09-10
acquired: 2026-09-10
license: Apache-2.0
security_flags: []
overlaps: [crowdsec]
source: unknown
---

## What it does

Trivy is the most widely used open-source security scanner, covering multiple **targets** — container images, local filesystems/rootfs, git repositories, VM images, Kubernetes clusters, AWS accounts — and multiple **scanners** per target:

- **Vulnerabilities:** OS packages (Alpine, Debian/Ubuntu, RHEL, etc.) and language dependencies (npm, PyPI, Go modules, Cargo, Maven, and more) against aggregated advisory databases
- **Misconfigurations:** IaC scanning for Terraform, CloudFormation, Kubernetes manifests, Helm charts, Dockerfiles (absorbed the former tfsec engine)
- **Secrets:** hardcoded credentials, API keys, tokens
- **Licenses:** dependency license detection
- **SBOM:** generates and consumes SPDX and CycloneDX

## Differentiators

- Single static Go binary; the vulnerability DB downloads automatically and supports air-gapped operation — near-zero setup compared to server-based scanners.
- One tool spans image, code, IaC, secret, and cloud scanning, replacing several single-purpose scanners; it is the default scanner embedded in Docker Desktop extensions, Harbor, GitLab, and many CI templates.
- Client/server mode for centralizing the DB; Kubernetes operator (trivy-operator) for continuous in-cluster scanning.
- Backed by Aqua Security with a fast advisory-refresh cadence.

## Mechanical details

- Install: brew/apt/yum/binary releases or `aquasec/trivy` container image.
- Usage: `trivy image python:3.12`, `trivy fs .`, `trivy repo <url>`, `trivy k8s cluster`, `trivy config ./iac`, `trivy sbom ./sbom.json`; `--severity`, `--ignore-unfixed`, `--exit-code` for CI gating; `.trivyignore` for accepted findings.
- Go, Apache-2.0, ~37.9k stars, 675 forks, 271 open issues; created 2019; pushed same day as review; docs at trivy.dev; discussions enabled.

## Security

- **License:** Apache-2.0.
- Mature, org-backed, heavy CI usage across the industry; signed releases and an established security policy.
- Scanning is read-only against its targets; cloud/K8s scanning requires credentials whose scope the operator controls.
- Detection quality depends on DB freshness — offline copies age; scheduled DB updates are part of correct operation.