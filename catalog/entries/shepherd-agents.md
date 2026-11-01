---
name: shepherd-agents
title: Shepherd (shepherd-agents/shepherd)
url: "https://github.com/shepherd-agents/shepherd"
category: framework
summary: "Python runtime substrate that records agent runs as durable, inspectable, reversible execution traces — agent-written outputs land as retained proposals (changesets) that a human selects, applies, releases, or discards, with OS-level (Seatbelt/Landlock) enforcement of per-task read/write permission grants declared in function signatures"
tags: [agent-framework, sandbox, reversible-execution, git, meta-agents, claude-code, permissions, python, landlock, seatbelt, research-paper]
reviewed: 2026-09-16
acquired: 2026-09-16
license: MIT
security_flags: [early-alpha-api-instability]
overlaps: [deepseek-harness, landlock-lsm]
source: unknown
---

## What it does

Shepherd is a runtime substrate for agent work that needs inspection, reversibility, and supervision. A task is written as a plain Python function with no body — its signature and docstring are the contract an agent fulfils at runtime, including declared permissions (e.g. `repo: sp.GitRepo` for a writable workspace handle, or `May[GitRepo, ReadOnly]` for read-only inspection). Running a task launches an agent (e.g. Claude Code via the `claude` CLI, using a subscription token or `ANTHROPIC_API_KEY`) inside a sandbox; its file writes are captured as a "changeset" — a retained output held to one side rather than written directly into the workspace. The user (or a calling meta-agent) then inspects the changeset and settles it via `select`, `apply` (three-way merge onto a workspace that moved on), `release`, or `discard`. A keyless "offline quickstart" runs the same retained-output machinery through a deterministic provider with no agent/API key. An example package, `shepherd-check-citations`, audits a PDF's bibliography using pdfplumber and Claude Code (headless Opus).

## Differentiators

- Couples an agent and its environment in what the repo describes as a copy-on-write fork "~5x faster than `docker commit`", with "~95% KV-cache reuse on replay" (repo's own claims, not independently verified here).
- Permission grants are read off the task's Python signature (`GitRepo`, `May[GitRepo, ReadOnly/ReadWrite]`) and enforced at the OS syscall layer via macOS Seatbelt or Linux Landlock (the latter runs inside a privileged container) — a write to a read-only-granted repo, or an unbound path, is refused by the kernel/sandbox, not merely checked at a later merge gate.
- Every run's outcome (write_program, donut.py demo, etc.) is a reviewable, git-like trace that can be forked, replayed, or reverted — positioned as infrastructure for "meta-agents" that supervise, optimize, or train other agents, rather than a single agent runtime.
- Backed by an academic paper, "Shepherd: Enabling Programmable Meta-Agents via Reversible Agentic Execution Traces" (arXiv:2605.10913, Yu, Chong, Nandi, Soylu, Sun, Manning, Shi), with a companion repo `shepherd-agents/shepherd-experiments` bundling the frozen substrate snapshot used to produce the paper's benchmark numbers.
- Distinct from several unrelated GitHub projects also named "shepherd" in the agent-tooling space (e.g. `kyashp/shepherd`, a transactional execution kernel for coding-agent teams; `agentshepherd/agentshepherd-releases`, a proprietary commercial CLI/MCP product) — and from `andrefogelman/shepherd`, which is built on top of this same substrate.

## Mechanical details

- Install: `pip install shepherd-ai` (requires Python 3.11+); editable dev install via `python -m venv .venv && pip install -r requirements-dev.txt`.
- Platforms: macOS (Seatbelt) and Linux (Landlock, privileged container) for OS-level grant enforcement; Windows is unsupported ("enforcement would be advisory-only at best") — use WSL.
- CLI: `shepherd init` (turn a directory into a workspace), `shepherd doctor claude` (checks CLI/auth/sandbox readiness, `--probe` does a live auth round-trip), `shepherd demo`, `shepherd run list/changeset/show/select/apply/discard`, `shepherd task show` (renders a task's permission surface).
- Agent backend: Claude Code CLI — a long-lived `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`) is recommended for sandboxed runs since short-lived signed-in sessions can't refresh from inside the sandbox; alternatively `ANTHROPIC_API_KEY`. A keyless deterministic provider is available for the offline quickstart.
- Workspace bindings: `ws.bind(root=..., name=...)` plus `workspace.run(task, bindings={...})`; grants are whole-profile per named binding (a bound repo is entirely read-only or entirely writable — no sub-path grants in this release).
- Docs: docs.shepherd-agents.ai (in-repo source under `docs/shepherd/`); dev gates: `make dev-install`, `uv run pytest integration-tests/test_quickstart_core.py -q`, `make baseline`.

## Security

- License: MIT.
- README states the project "is in early alpha and under active development. APIs may still change between releases."
- Filesystem write enforcement is native OS sandboxing (Seatbelt on macOS, Landlock on Linux) rather than advisory-only checks; Linux enforcement specifically requires running inside a privileged container.
- An agent's own written output never touches the real workspace until explicitly `select`ed or `apply`ed — the retained-output/changeset model is itself a security-relevant design choice (reviewable before merge).
- No CVEs, dependency-audit findings, or maintenance-lapse signals surfaced during this review; supply-chain and dependency posture were not independently audited.
