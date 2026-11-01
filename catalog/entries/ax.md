---
name: ax
title: AX (Google)
url: "https://github.com/google/ax"
category: framework
summary: "Google's open-source declarative orchestrator for AI agent workloads on Kubernetes — four Kubernetes-style primitives (Task, Workspace, Gateway, Model) run agents as sandboxed, suspendable actors on top of Agent Substrate; Go, Apache-2.0, gRPC + Redis control plane, kubectl-shaped CLI; early-stage/pre-stable"
tags: [agent-infrastructure, kubernetes, orchestrator, sandbox, suspend-resume, go, grpc, declarative, agent-substrate, google]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Apache-2.0
security_flags: []
overlaps: [opensandbox]
source: unknown
---

## What it does / What it says

AX is a high-throughput, declarative orchestrator for running autonomous AI agent workloads on Kubernetes, released open-source by Google. It runs on top of "Agent Substrate," a separate execution runtime for dense actor multiplexing, and treats each agent run as an isolated, sandboxed actor rather than a stateless microservice or run-to-completion batch job. The stated rationale is that agents are stateful, bursty, and idle frequently while waiting on model or tool calls, so AX checkpoints and suspends idle sandboxes (sub-second suspend/resume) to reclaim compute and multiplex many tasks onto shared workers. Everything is expressed as `ax.io/v1alpha1` YAML manifests applied with a kubectl-shaped CLI (`ax apply`, `ax get`, `ax describe`, `ax watch`, `ax delete`, plus `ax ssh`, `ax suspend`, `ax resume`).

## Differentiators / Key takeaways

- Four declarative primitives: **Task** (smallest unit of isolated execution — container image/command, CPU/memory requests+limits, env vars, one or more Workspace references), **Workspace** (pre-wires Git repos cloned to specific paths/branches, MCP servers/registries, and skill registries before the agent starts; supports a natural-language `goal` that a bootstrap agent uses to finish environment setup), **Gateway** (restricts sandboxed agents' outbound traffic to explicit host/port allowlists and handles credential injection into outbound requests), and **Model** (named LLM configuration — provider, model ID, sampling parameters, and a reference to a Kubernetes Secret holding the API key, centralizing credential/version management cluster-wide).
- `ax ssh` gives an interactive shell into a running sandbox for debugging (requires `spec.debug: true` on the Task); `ax suspend`/`ax resume` manually checkpoint and resume a task's actor state.
- `ax` follows the active `kubectx` context and transparently tunnels to that cluster's control plane, so switching clusters is just switching kube contexts.
- Positioned as a low-level infrastructure/compute primitive for large-scale, long-running agentic fleets (production agent deployment, RL loops, sandboxed trajectory collection, benchmark evaluation) rather than a high-level application-orchestration framework like LangGraph or CrewAI.
- Explicitly early-stage: the README warns core concepts/protocols/specs are still being refined and breaking changes are likely before a stable release. Roadmap items still in progress include stabilizing the core specs, idle-detection/auto-suspend, stateful task branching, dynamic workspace curation from repo inspection, SPIFFE workload identity, and OpenTelemetry trajectory export.
- Generated significant attention on release (#1 on Hacker News, Sept 21 2026; InfoQ coverage). Commentary cited by InfoQ contrasts it with alternatives like Scion, described as wrapping existing agent harnesses on Kubernetes rather than requiring adoption of the full Agent Substrate stack, and flags early operational rough edges (egress proxy dropped connections, rudimentary secrets management) plus the overhead of running Kubernetes/`ko`/custom CRDs for smaller teams.
- No bioinformatics-specific tooling or examples; this is general-purpose agent infrastructure.

## Mechanical details / What to adopt

Requires a Kubernetes cluster with Agent Substrate already installed (exposes a Control API at `api.ate-system.svc.cluster.local:443`), Go, `kubectl`, and `ko` (`brew install ko`) plus a container registry the cluster can pull from. Install the CLI: `go install github.com/google/ax/cmd/ax@latest` (binary lands in `$(go env GOPATH)/bin`). Deploy the control plane: `make deploy AX_IMAGE_REPO=<your-registry>` — deploys Redis then the control plane (built/pushed via `ko`) into the `ax-system` namespace. Apply a manifest bundling Task + Workspace + Model (or + Gateway) in one multi-document YAML file: `ax apply -f examples/task.yaml`, then `ax get tasks`, `ax watch task <name>`, `ax ssh <name> -- <cmd>`. `metadata.name`/`metadata.atespace` must be lowercase RFC 1123 labels; `ax apply` validates this up front. `./demo.sh` runs the full lifecycle end to end (apply, wait for readiness, `ax ssh` commands, suspend).

## Security

Apache-2.0 license. Task sandboxing and outbound network restriction (via the Gateway primitive's host/port allowlists) are the two built-in security-relevant controls; Model credentials are sourced from Kubernetes Secrets rather than inline config. The project is explicitly pre-stable (README: "We are still actively refining our core concepts, protocols, and specifications. We will likely introduce major breaking changes prior to a stable release."), so specs, RBAC/permission boundaries, and the Gateway/credential-injection mechanics should be expected to change. InfoQ-reported community discussion flagged early teething issues including egress proxy dropped connections and "rudimentary secrets management." No independent security audit or CVE history was surfaced in this review.
