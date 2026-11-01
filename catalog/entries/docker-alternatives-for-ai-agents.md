---
name: docker-alternatives-for-ai-agents
title: "Docker Alternatives for AI Agents: Podman, bwrap, Firejail"
url: "https://grigio.org/docker-alternatives-for-ai-agents-podman-bwrap-and-firejail/"
category: reference
summary: "Blog comparison (grigio.org, Jul 2026) of Podman, Bubblewrap, and Firejail as agent-sandboxing alternatives to Docker — decision matrix over startup time, isolation strength, attack surface, profiles, and portability; recommends Podman for production agent services, bwrap for per-command local sandboxes, Firejail for desktop agents"
tags: [sandbox, podman, bubblewrap, firejail, agent-security, linux, isolation, comparison, docker-alternative]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-blog-content
security_flags: []
overlaps: [firejail, bubblewrap-containers]
source: unknown
---

## What it says

Blog post (Luigi, grigio.org, 27 Jul 2026) arguing Docker is a poor default for AI coding agents: agents run short-lived commands rather than long-lived servers, need isolation from SSH keys rather than port mapping, and need fast startup (a 3-second Docker spin-up is slow when an agent launches 20 sandboxes per task). It compares three alternatives:

- **Podman** — Docker-compatible OCI CLI, rootless by default, daemonless; quadlets/systemd integration, pods, `podman play kube`. Downsides: ~100–500ms startup, GPU passthrough needs CDI + SELinux workarounds, macOS/Windows require a VM. Best for production agent services and multi-tenant CI.
- **Bubblewrap (bwrap)** — ~8k lines of C, used by Flatpak and OpenAI's Codex CLI; <50ms startup, no daemon, no root, drops all capabilities, explicit per-path bind mounts. Downsides: Linux-only, no image management, no built-in resource limits. Best for per-command agent sandboxes. Cites Claude Code's reported 84% reduction in permission prompts with bwrap sandboxing, and projects bubblewrap-ai and sandbox-bwrap-nix.
- **Firejail** — SUID sandbox with ~1000 pre-built profiles, zero-config (`firejail agent.sh`), X11/Wayland isolation via Xephyr, experimental Landlock, seccomp-log debugging. Downsides: SUID attack surface, mostly blacklist-based profiles, desktop-app orientation. Best for browser-based/desktop agents.

## Key takeaways

- Decision matrix: startup (<50ms bwrap/Firejail vs 100–500ms Podman), attack surface (8k LOC C bwrap vs 150k+ LOC Go Podman vs 50k+ LOC SUID C Firejail), portability (Podman only, via VM), profiles (Firejail only), image management (Podman only).
- Positions microVMs (Firecracker, gVisor, Kata) as the next step when stronger isolation is needed.
- Anchors the threat model in a real incident: an agent issuing `rm -rf /` to "test if the harmful-command block worked," contained by a bubblewrap sandbox (r/LocalLLaMA).

## What to adopt

- The per-use-case split (production service → Podman; per-command local sandbox → bwrap; desktop/GUI agent → Firejail) is the article's reusable decision rule.
- Links out to bubblewrap-ai and sandbox-bwrap-nix as ready-made bwrap wrappers for Claude/Gemini/Goose/OpenCode harnesses.

## Security

- Blog content, no license stated; short opinion piece with cited sources (Reddit threads, HN, project READMEs).
- Claims about Codex CLI and Claude Code bwrap usage are consistent with public documentation at the time of the post.