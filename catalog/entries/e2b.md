---
name: e2b
title: E2B
url: "https://github.com/e2b-dev/e2b"
category: framework
summary: "Open-source cloud sandbox infrastructure for AI agents — Firecracker microVMs with ~150ms boot, Python/JS SDKs, Code Interpreter, self-hostable on AWS/GCP via Terraform; Apache-2.0, 8.9K stars"
tags: [sandbox, code-execution, cloud, agent-infrastructure, microvm]
reviewed: 2026-06-23
acquired: 2026-06-23
license: Apache-2.0
security_flags: [cloud-hosted, sends-code-externally, api-key-required]
overlaps: [blaxel]
source: unknown
---

## What it does

E2B provides isolated cloud sandboxes (Firecracker microVMs) that let AI agents safely execute code, run commands, access filesystems, and manage processes. Sandboxes boot in ~150ms and are destroyed automatically when the last process exits.

Core components:
- **Sandbox SDK** (Python + JS/TS): Create, control, and destroy sandboxes programmatically
- **Code Interpreter SDK**: Execute code snippets with `runCode()` and get structured results
- **Templates**: Define custom sandbox environments with pre-installed dependencies
- **Desktop Sandbox**: Graphical environment for computer-use agents (1.4K stars separately)

Integrations: smolagents, LangChain, AutoGen, CrewAI, and other agent frameworks use E2B as their sandboxed execution backend.

## Assessment

Strong infrastructure choice for agent code execution. The Firecracker microVM approach provides real isolation (not container-level), fast boot times, and clean teardown. The dual-SDK strategy (Python + JS/TS) covers the two dominant agent ecosystems. Self-hosting via Terraform on AWS/GCP removes the cloud-vendor lock-in concern for sensitive workloads.

The main tradeoff is that primary usage sends code to E2B's cloud for execution — acceptable for most agent workloads but not for sensitive data without self-hosting. Already referenced by smolagents (in this queue) as a recommended sandbox backend.

## Mechanical details

```bash
pip install e2b                      # Python SDK
npm i e2b                            # JS/TS SDK
pip install e2b-code-interpreter     # Code Interpreter
```

API key required: sign up at e2b.dev, set `E2B_API_KEY` env var.

Self-hosting: `terraform apply` with the e2b-dev/infra repo on AWS or GCP. Azure not yet supported.

## Security

- **License**: Apache-2.0 — permissive, no copyleft obligations
- **Isolation model**: Firecracker microVMs, not containers — hardware-level isolation per sandbox
- **Supply chain**: ~8.9K stars, active development (last updated April 2026), YC-backed company, multiple contributors
- **Data flow**: Code sent to E2B cloud by default; self-hosting eliminates this
- **Code quality**: CI, tests, well-maintained SDKs with typed interfaces
- **API key**: Required for both cloud and self-hosted; stored in env var (standard pattern)

## Usage notes

- **Sandbox best practices** (applies to E2B, Blaxel, Docker): Set memory/CPU limits, implement execution timeouts, monitor resource usage. Run with minimal privileges, disable unnecessary network access, use env vars for secrets. Keep dependencies minimal with fixed package versions. Always ensure proper cleanup to avoid dangling resources.
- **Two sandbox approaches**: (1) Run just code snippets in sandbox (`executor_type="e2b"` in smolagents) — easier setup, no API key transfer needed, but no multi-agent support. (2) Run entire agentic system in sandbox — supports multi-agents and full isolation but requires transferring API keys and more manual setup.
