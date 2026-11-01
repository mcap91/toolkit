---
name: deepseek-harness
title: DeepSeek Harness (dsh)
url: "https://github.com/deepseek-ai/deepseek-harness"
category: framework
summary: "Open-source agent harness from DeepSeek AI built on Cordis, a reversible plugin meta-framework — models, tools, skills, sessions, sandboxes, storage, loops, scheduling, and the UI are all swappable plugins composed via configuration. MIT-licensed developer preview, open-sourced August 13, 2026 alongside DeepSeek-V4-Pro; quick start is `npx @deepseek-ai/dsh web`."
tags: [agent-harness, plugin-architecture, cordis, deepseek, coding-agent, model-agnostic, sandboxing, session-replay, open-source, developer-preview]
reviewed: 2026-08-25
acquired: 2026-08-25
license: MIT
security_flags: [developer-preview-breaking-changes, partial-sandbox-enforcement-reported]
overlaps: [harness-engineering, claw-code]
source: unknown
---
## What it does

DeepSeek Harness (dsh) is an open-source agent harness developed by DeepSeek AI, open-sourced August 13, 2026 alongside the DeepSeek-V4-Pro model release. It is currently in developer preview ("iterating rapidly... THERE WILL BE COMPATIBILITY-BREAKING CHANGES" per the README) and is licensed MIT.

Its architectural premise is "everything is a plugin," built on **Cordis**, a meta-framework whose design is described in the paper *A Programming Paradigm for Spatiotemporal Composability*. Cordis manages plugin mounting, unmounting, and dependencies, splitting dynamic composition into temporal composability (fully reverting a component's effects on unload) and spatial composability (declaring and reactively managing inter-component dependencies). Cordis predates dsh — it has been the plugin kernel of the open-source Koishi chatbot framework for roughly four years — and is itself a standalone MIT project that dsh builds on.

Every agent capability — models, tools, skills, sessions, sandboxes, storage, loops, scheduling, and the UI — is a Cordis plugin, so any of them can be selected, swapped, or extended via configuration without touching dsh's source. A running dsh instance is a plugin tree composed at boot from ordered layers (profile → bundles → patch files), with `dsh --profile web --dump-config` printing the tree a given machine boots.

## Mechanical details

**Quick start:** install Node.js, then `npx @deepseek-ai/dsh web` starts a Web UI at `http://127.0.0.1:3080` (opened automatically for local launches; SSH launches print the host URL only, since the SSH client/editor owns the forwarded address; `--no-open` suppresses the browser). Running from source: `git clone https://github.com/deepseek-ai/deepseek-harness.git && cd deepseek-harness && pnpm install && pnpm run build && pnpm dsh web`.

**Session log:** the append-only `SessionEvent` log (`core/session`, `ctx.sessions`) is the durable source of everything the model sees — system prompts, reasoning, tool calls/results, subagent scheduling, and context injections. `deriveMessages()` projects model history from the log; a runtime invariant asserts that anything reaching a model request is reconstructable from it. Resume, fork, search, and replay (via a Trajectory view) all operate on this same event stream.

**Runtime modes:** four presets load different default plugin sets — **Standard** (full coding agent: filesystem tools, shell, web search, subagents, plan mode), **Minimal** (a persistent bash shell plus a `str_replace_editor` only — no web search, skills, or subagents; used for some published benchmark evaluations), **Code/PTC** (tools are exposed to the model as a generated TypeScript SDK it programs against, rather than individual function calls, collapsing multi-step tool sequences into one call), and **Creator** (inherits Standard, adds runtime inspection, in-memory plugin experimentation, and preset-authoring tooling).

**Model-agnostic:** model providers register on the `ctx.llm` adapter seam; per third-party reporting and the harness's own capability-seam design, supported providers include DeepSeek, Anthropic, OpenAI, Bedrock, Azure, and Gemini. A "subagent provider" seam is similarly generic — sources describe Claude Code and Codex as installable as subagents/sub-agent instances alongside dsh's own agent loop, most recently as installable "Profile Bundles" with non-interactive permission modes and named instances (per GitHub release notes, not independently verified against the release itself).

**Core packages** contributing to the Cordis tree include `core/session` (session log), `core/system-prompt` (prompt/tool-schema assembly), `core/tools` (scoped tool registry + guarded execution pipeline), `core/agent`/`core/agent-loop` (the `Agent` interface and its default driver), `core/scope` (per-agent scoped registration), and `llm/llm` (the model adapter seam).

**Community:** GitHub Discussions for feedback/bugs, a Discord community, and a `dsh-plugin` GitHub topic for third-party plugin discoverability. Tech press (VentureBeat, MarkTechPost, and others) reported explosive early adoption — over 20,000 GitHub stars within roughly an hour of launch and over 2,000 community plugin proposals within the first two days — figures from secondary reporting, not independently verified here.

## Security

**License:** MIT, stated directly in the repository README; third-party dependency licenses are disclosed separately in `THIRD_PARTY_NOTICES.md`.

**Sandboxing:** subprocess execution runs through a `ctx.sandbox` backend with OS-specific enforcement — Linux Landlock (via a Node addon written by DeepSeek), macOS Seatbelt, and a Windows ACL restricted-token runner, layered under permission tiers (reported inconsistently across secondary sources as three or four tiers, spanning read-only through workspace-write to a full/danger-unrestricted mode). This sandbox description is drawn from third-party technical analysis, not confirmed directly against dsh's own source in this review.

**security_flags:**
- `developer-preview-breaking-changes` — the project explicitly warns of compatibility-breaking changes while in developer preview; not yet a stability guarantee.
- `partial-sandbox-enforcement-reported` — third-party analysis reports the sandbox enforcement is platform- and version-dependent, with older Linux Landlock ABIs and the Windows ACL runner's handling of `Everyone`/hard-links documented as partial rather than complete confinement, and notes the shipped default permission table pairs only `workspace-write`+`ask` and `danger-full-access`+`never` (no default `read-only` pairing). This has not been independently verified against dsh's own documentation in this review and should be re-checked against current source before relying on it.

## Usage notes

- Reported user experience (unverified, practitioner discussion): running against a local Qwen 3.8 Q6 model, one user reported DSH "just took off" once thinking effort was set correctly, with an effectively very long usable context compared to OpenCode in the same setup. A separate report described a 16-hour, 20M+ token run on a single RTX 3090 completing all assigned tasks using default DSH with no extra plugins — unsloth ud q4_k_m XL quantization, llama.cpp with MTP and ngram enabled, at 92k context.

- Reported run (unverified, practitioner discussion): DSH on a Windows PC used over LAN against a separate inference box ("NInfer") serving Qwen3.8-27B at 262K context, with all shell/file operations kept on the client and the server doing inference only. An 8+ hour session reportedly logged 966 model calls, ~131.2M input / 853.3K output tokens, 972 model-facing tool calls, 1,421 local tool operations, 31 auto-compaction attempts, ~105 output tokens/sec, and zero model-generation failures. Commenters on the report noted its API-cost comparison did not account for cache discounts.
