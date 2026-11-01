---
name: opensandbox
title: OpenSandbox
url: "https://github.com/opensandbox-group/OpenSandbox"
category: framework
summary: "General-purpose sandbox runtime platform for AI applications (Alibaba-originated) — multi-language SDKs (Python, Java/Kotlin, JS/TS, C#/.NET, Go), unified sandbox lifecycle/execution APIs, Docker and Kubernetes runtimes, and an osb CLI plus MCP server for coding agents, GUI agents, agent evaluation, code execution, and RL training; Apache-2.0"
tags: [sandbox, code-execution, agent-infrastructure, kubernetes, docker, mcp-server, isolation]
reviewed: 2026-08-25
acquired: 2026-08-25
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does / What it says

OpenSandbox is a general-purpose sandbox platform for AI applications, providing multi-language SDKs, unified sandbox lifecycle/execution APIs, and Docker/Kubernetes runtimes for use cases such as coding agents, GUI agents, agent evaluation, AI code execution, and RL training. It defines a "Sandbox Protocol" (lifecycle + execution API specs) so custom sandbox runtimes can be built against the same interface. Originated from Alibaba (mirrored/published under both `alibaba/OpenSandbox` and `opensandbox-group/OpenSandbox`); listed in the CNCF Landscape per third-party sources.

## Differentiators / Key takeaways

- Strong isolation options: supports gVisor, Kata Containers, and Firecracker microVM secure container runtimes in addition to standard Docker/Kubernetes.
- Ships built-in Command, Filesystem, and Code Interpreter primitives, plus example integrations for coding-agent CLIs (Claude Code, Gemini CLI, OpenAI Codex CLI, OpenCode, Qwen Code, Kimi CLI), browser automation (Chrome, Playwright), and desktop environments (VNC, VS Code/code-server).
- Includes a Credential Vault for injecting secrets into sandbox outbound requests without exposing real credentials to the workload, and a unified ingress gateway plus per-sandbox egress network controls.
- Ships an `osb` terminal CLI (`pip install opensandbox-cli`) and an MCP server (`opensandbox-mcp`) exposing sandbox creation, command execution, and file operations to MCP clients like Claude Code and Cursor.
- Official container images are signed keylessly with Cosign and include provenance attestations, published to Docker Hub, GHCR, and Alibaba Cloud Container Registry.

## Mechanical details / What to adopt

Python: `pip install opensandbox`. Local server: `uvx opensandbox-server init-config ~/.sandbox.toml --example docker` then `uvx opensandbox-server`. Example (async Python SDK): `Sandbox.create(image, entrypoint=..., env=..., timeout=...)`, then `sandbox.commands.run(...)`, `sandbox.files.write_files(...)`/`read_file(...)`, optionally layer a `CodeInterpreter.create(sandbox)` for code execution, then `sandbox.kill()`. Repo layout: `sdks/`, `specs/`, `server/` (Python FastAPI lifecycle server), `cli/`, `kubernetes/`, `components/execd|ingress|egress/`, `sandboxes/`, `examples/`.

## Security

Apache-2.0 license. README documents a release-verification guide advising production images be pinned by digest and verified against the OpenSandbox GitHub Actions identity before deployment (keyless Cosign signing + provenance attestations). Strong-isolation runtime options (gVisor/Kata/Firecracker) are opt-in per the "Secure Container Runtime Guide" referenced in the README, implying the default Docker runtime alone does not provide microVM-level isolation. No independent audit or CVE history was surfaced in this review.
