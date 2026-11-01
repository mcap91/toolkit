---
name: tolvi
title: Tolvi — Engineering Decision Vault
url: "https://github.com/tolvi-labs/tolvi"
category: framework
summary: "Solid CAG/RAG dual-mode decision-capture design but pre-1.0, small project, and overlaps with kb already in use"
tags: [decisions, knowledge-management, adr, vault, claude-code-skill, rag, cag, go-cli, agent-integration]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [pre-release, unverified-release-signing]
overlaps: []
source: unknown
---

## What it does

Tolvi is a per-repo engineering knowledge vault. It stores decisions, session notes, and patterns as Markdown files with YAML frontmatter under `<repo>/vault/`, using a defined format spec (`tolvi-format-v1`). Two retrieval modes coexist on the same vault format:

- **Local / CAG arm:** The Go CLI loads the entire vault into Anthropic context via prompt caching, then answers natural-language queries with `tolvi ask`. Zero infrastructure; requires only an Anthropic API key.
- **Server / RAG arm:** A self-hostable TypeScript Fastify server with Postgres + pgvector + Ollama embeddings supports multi-tenant, shared-index retrieval for teams that outgrow the local context window.

Two capture modes complement each other:

- **Mechanical (CLI):** `tolvi sync` writes a single explicit note; `tolvi commit` gates on a session note existing for today. Deterministic, scriptable, no LLM.
- **Synthesized (skill):** The Claude Code `/tolvi` slash command or Cursor `.cursorrules` integration reconstructs a whole working session into decisions, patterns, and a session log. High fidelity but agent-dependent and non-deterministic.

A pre-commit hook integration (`tolvi precommit install`) flags commits touching decision-likely files (deps, infra, tooling, large diffs) to nudge capture at the right moment.

## Assessment

**watch** — The architecture is thoughtful: the CAG/RAG split on a single portable vault format is a clean design, and first-class Claude Code skill integration (`/tolvi` slash command in `integrations/claude-code/`) is directly relevant here. The pre-commit nudge pattern is useful.

However: (1) this repo already uses `kb` for the same purpose — structured wiki with schema, search, dispatch, and agent retrieval; adopting Tolvi would duplicate the concern; (2) the project is pre-1.0 (v0.1.1), from a new lab with a small contributor base, and distribution channels (Homebrew, npm, Docker Hub) are still in progress; (3) the CAG approach trades token cost for zero infrastructure, which may not scale well for large vaults.

Worth monitoring as a potential complement (especially the format spec and pre-commit integration pattern) or as a case study in CAG-vs-RAG trade-off for decision retrieval.

## Mechanical details

- **Install:** `go install github.com/tolvi-labs/tolvi/cli/cmd/tolvi@latest` (Go required) or release binary
- **Config:** `~/.config/tolvi/config.yaml` or `ANTHROPIC_API_KEY` env var
- **Core CLI commands:** `init`, `sync`, `ask`, `recall`, `commit`, `precommit`, `version`
- **Vault format:** `tolvi-format-v1` — Markdown + YAML frontmatter under `<repo>/vault/`; JSON Schemas in `spec/schemas/`
- **Server stack:** Fastify + Postgres + pgvector + Ollama; Docker Compose self-host; OpenAPI spec at `spec/openapi.json`
- **TypeScript SDK:** `@tolvi-labs/sdk` — typed client over the server HTTP API
- **Agent integrations:** Claude Code skill (Tier 1, `/tolvi`), Cursor `.cursorrules` (Tier 2), Aider/OpenHands/Continue skeletons (Tier 3)
- **Pre-commit hook:** flags commits touching deps, infra, tooling, or large diffs
- **License:** Apache 2.0

## Security

- **License:** Apache-2.0 — clean, permissive, no copyleft obligations.
- **API key handling:** Requires `ANTHROPIC_API_KEY`; stored in `~/.config/tolvi/config.yaml`. Standard pattern; no evidence of key logging or exfiltration in the README, but the codebase should be audited before use in sensitive environments.
- **Pre-1.0 / small project:** v0.1.1 from a new lab. Release signing is not mentioned; Homebrew tap is pending a token. Supply chain surface is relatively low (Go static binary), but contributor count and review depth are unknown.
- **Go CLI binary:** Static binary reduces runtime dependency surface compared to Node-based tools.
- **Server arm:** Self-hostable; pgvector + Ollama means no data leaves the host if configured correctly. Docker Compose deployment is standard.
- **No obvious dangerous patterns** from README inspection: no eval, no shell injection vectors described, no unsafe deserialization.
- **Flags:** `pre-release` (v0.1.1, APIs may change), `unverified-release-signing` (no mention of signed releases or SLSA provenance).
