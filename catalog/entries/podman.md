---
name: podman
title: Podman
url: "https://github.com/podman-container-tools/podman"
category: framework
summary: "Daemonless, rootless-capable container engine with a Docker-compatible CLI for managing OCI containers, pods, images, and volumes; uses Buildah for builds, Netavark/Aardvark for networking, and crun/runc as the OCI runtime; ships Podman Desktop as a GUI frontend"
tags: [containers, oci, rootless, daemonless, docker-alternative, podman-desktop, cli, buildah, netavark]
reviewed: 2026-08-09
acquired: 2026-08-09
license: Apache-2.0
security_flags: [org-migration-unclear-provenance]
overlaps: []
source: unknown
---

## What it does

Podman ("POD MANager") manages OCI/Docker-format containers, images, volumes, and pods via a Docker-compatible CLI, without a background daemon. Built on the `libpod` library (also in this repo), it supports rootless operation (containers run as the invoking user via user namespaces, with no more privilege than that user has), pods (grouped containers sharing resources), checkpoint/restore via CRIU, and both local and remote (REST API) operation. On Mac/Windows it runs via a Podman-managed VM (`podman machine`). Podman Desktop is a separate GUI project for full container/pod/Kubernetes-YAML lifecycle management.

## Differentiators / Key takeaways

- No daemon requirement (unlike Docker) — lower idle resource use and a smaller privileged attack surface; rootless-by-default operation model.
- Composes with, rather than reimplements, adjacent OCI tooling: Buildah for image builds (`podman build` delegates to Buildah's Go API), Netavark/Aardvark for networking (pasta for rootless networking), Skopeo for image signing/pushing (explicitly out of scope for Podman itself), crun/runc as the OCI runtime, Conmon for runtime monitoring.
- Releases quarterly (Feb/May/Aug/Nov) with PGP-signed releases; only the latest release gets full upstream support, though the v5.8 series was extended through June 2027 for CVE/critical-bugfix support after the Podman 6.0 release.
- Provenance note: this URL is hosted under the GitHub org `podman-container-tools`, not the long-standing `containers` org (`github.com/containers/podman`) that has historically been Podman's canonical upstream. A research pass found the `podman-container-tools` org self-describes as "a collection of open source tools for building, managing, and working with OCI containers and images... a CNCF Sandbox Project," bundling Podman, Buildah, Skopeo, and shared `container-libs`, and shows higher star/fork counts than `containers/podman`. The repo's `LICENSE` file matches upstream Podman's Apache-2.0 text. Whether this org represents an official reorg/migration of the CNCF project or a separate entity was not conclusively resolved by this research pass.

## Mechanical details / What to adopt

- Quick start: `podman run quay.io/podman/hello`.
- Security disclosures go to security@lists.podman.io (private list), not public issues.
- Community meetings (bi-monthly community call, weekly office hours) run through CNCF/Linux Foundation Zoom; calendar on the Podman Container Tools LFX Meetings page.
- Full command reference and Docker-CLI mapping documented at docs.podman.io.

## Security

Apache-2.0 license, confirmed by fetching the repo's `LICENSE` file directly (text matches standard Apache-2.0). Rootless-by-default design is a meaningful security property relative to daemon-based, root-requiring container engines. The primary flag for this entry is provenance: verify whether `podman-container-tools/podman` is the intended canonical location before pinning CI/tooling to it, given the long-established `containers/podman` org is what most existing documentation, package repos, and tutorials reference.

## community

Comparison: Xurrent published a detailed Podman vs Docker comparison guide covering architecture (daemonless vs daemon), security (rootless-by-default vs root-default), Kubernetes integration, Docker Compose compatibility, and migration considerations. Source: https://www.xurrent.com/blog/podman-vs-docker-complete-2025-comparison-guide-for-devops-teams

Container security tip (r/AI_Agents): .dockerignore should use deny-by-default pattern — start with `*` to ignore everything, then `!`-whitelist only what the build needs. Researchers found private keys in 28,000+ of 300,000 scanned public Docker images. Secrets baked into any layer never truly disappear. Applies equally to Podman's Buildah-based image builds.
