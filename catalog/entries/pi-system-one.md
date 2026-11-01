---
name: pi-system-one
title: pi-system-one
url: "https://iamaamir.github.io/system-one/"
category: plugin
summary: "Pi coding-agent extension registering a single system_one tool for bounded decisions (choice, noul, score) with calibrated probabilities; a thin wrapper over the provider-neutral system-one-core SDK, so any compatible 'System One' backend (TypeSafe Jev, Reflex, custom /v1/systemone endpoints) can sit behind it; pi-bifrost (same author) is a separate consumer of the same SDK"
tags: [pi, pi-coding-agent, decision-making, tool-calling, provider-neutral, classification, extension, system-one-core, judge]
reviewed: 2026-09-25
acquired: 2026-09-25
license: NOASSERTION
security_flags: [no-license]
overlaps: [jev]
source: unknown
---

## What it does

pi-system-one is an extension for the Pi coding agent (github.com/earendil-works/pi) that registers a single `system_one` tool for bounded, calibrated decisions inside an agent session. The tool exposes three question types:

- **choice** — pick among bounded options; returns a probability per option plus a confidence score
- **noul** — binary true/false proposition; returns the probability the statement is true (no confidence field, since it's already binary)
- **score** — ordered scalar rating; returns a continuous score plus distribution and confidence

Results come back as calibrated, state-conditional probabilities rather than free-text estimates. The tool/skill is documented as expecting the calling agent to have already retrieved relevant facts — it weighs supplied state, it does not perform its own fact retrieval.

pi-system-one is a thin Pi-side wrapper around `system-one-core`, a separate provider-neutral npm package (same monorepo, github.com/iamaamir/system-one) that defines a `SystemOneProvider` interface, a `SystemOne` client, typed builders (`choice`, `noul`, `score`), an `HttpSystemOneProvider` for any backend exposing `POST /v1/systemone`, fail-closed response validation, and a mock provider for tests. Because the Pi extension depends on system-one-core rather than one backend, it can run against any compatible provider. The author's announcement states this was a deliberate extraction: pi-system-one originally hard-wired to TypeSafe Jev as "the decision engine inside Pi"; once open alternatives surfaced (Laya, von, Reflex were named), hard-wiring to one provider stopped making sense.

A separate project, pi-bifrost (same author), is described as another, independent consumer of the same system-one-core SDK for routing/policy decisions — it does not depend on pi-system-one or vice versa.

## Differentiators / Key takeaways

- Provider-neutral by design: documented as tested against TypeSafe Jev (resolved jev-1.13.0) and Reflex (run locally against Qwen3.5-2B), plus generic `/v1/systemone` endpoints and custom `SystemOneProvider` implementations — same client code, different `baseUrl`/`apiKey`/`model`.
- Ships a `/judge` prompt shortcut that expands into an explicit `system_one` tool call, for short unstructured asks (e.g., "should I ship this?") without relying on the model to infer when to invoke the tool.
- Design philosophy stated by the author: "provider-neutral," "policy-free," "fail-closed," "testable" — routing strategy, model tiers, and confidence thresholds are deliberately left to the calling application rather than baked into the tool.
- Catalog also holds a `jev` entry (TypeSafe AI's System One classification model) — jev is one of the interchangeable backends pi-system-one can target, not a competing implementation of pi-system-one itself.

## Mechanical details / What to adopt

- Install: `pi install npm:pi-system-one`, or via "Oh My Pi": `omp install npm:pi-system-one` (registry) / `omp install /path/to/pi-system-one` (local checkout)
- Required config: `SYSTEM_ONE_BASE_URL` (provider endpoint). Optional: `SYSTEM_ONE_MODEL`, `SYSTEM_ONE_API_KEY`
- Runtime config commands: `/so config` (in-session only, not persisted across sessions), `/so status` (inspect current settings)
- Repository: github.com/iamaamir/system-one, a monorepo containing `system-one-core` and `pi-system-one`. As of research (Sept 2026): ~59 stars, 3 forks, 102 commits, active recent PRs (tool-calling schema robustness, fail-closed score validation, OMP extension manifest). Latest referenced tag: `pi-system-one@1.1.0`.
- `system-one-core` is installable standalone via `npm install system-one-core` for non-Pi TypeScript use.

## Security

- No license file / no declared license found on github.com/iamaamir/system-one as of research (Sept 2026) — GitHub reports no repository license, so default all-rights-reserved copyright applies. A downstream project (AgentDock, via a GitHub issue) explicitly declined to reuse source, tests, fixtures, or package names from this repo for that reason, treating it as an architectural reference only pending published reuse terms.
- Single-maintainer project (author: iamaamir) with no independent third-party security review found beyond that one GitHub issue reference.
- Requires outbound network access to an operator-configured `SYSTEM_ONE_BASE_URL`, optionally with an API key (`SYSTEM_ONE_API_KEY`) sent to that endpoint; credential handling/storage was not independently verified beyond the documented env vars and session-only `/so config`.
- Author describes response validation as "fail-closed" (malformed provider responses are rejected rather than guessed at), per project documentation — not independently verified against source.

## Usage notes

- **pi-bifrost routing pattern (r/PiCodingAgent):** Author positions Jev as "a probabilistic switch statement" — `prompt → JEV → best model` for model routing instead of using an LLM to decide which LLM to call. pi-bifrost (`pi install npm:pi-bifrost`) provides the integration. Open-source alternatives mentioned: von (github.com/wfzyx/von), laya (github.com/NandhaKishorM/laya) — no per-request cost.
