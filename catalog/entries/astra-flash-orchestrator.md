---
name: astra-flash-orchestrator
title: Astra Flash Orchestrator
url: "https://github.com/ethanplusai/astra-flash-orchestrator"
category: skill
summary: "Codex skill that reserves GPT-6 Astra for planning/architecture/review and routes discovery, implementation, testing, and reporting to DeepSeek V4.1 Flash via a native astra_flash_builder subagent role and an existing Codex Router route; author's one field build measured 98.9% less Astra input per 1K implementation lines ($10/$50 per-1M-token Astra pricing vs $0.15-0.30/$0.60-1.20 for Flash); installs a skill under ~/.agents/skills/, a pinned agent role under $CODEX_HOME/agents/, and a scoped policy block in $CODEX_HOME/AGENTS.md, with preview/apply, backups, and an undo receipt; MIT"
tags: [codex, astra, deepseek, orchestration, cost-optimization, multi-agent, model-routing, subagents, codex-router]
reviewed: 2026-09-25
acquired: 2026-09-25
license: MIT
security_flags: [writes-to-user-home, api-key-required, self-reported-benchmarks, single-maintainer]
overlaps: [codex-workflow, deepseek-and-destroy, pilotfish]
source: unknown
---

## What it does

Astra Flash Orchestrator is a Codex skill/installer implementing the "expensive model plans and reviews, cheap model builds" pattern for Codex specifically (vs. Claude Code or generic multi-harness tools). The loop: Astra defines scope, produces a design, and writes task briefs → a native `astra_flash_builder` subagent role (pinned to DeepSeek V4.1 Flash) explores the repo, implements the task, runs tests, and reports evidence → Astra reviews the patch and either accepts it or requests fixes → integrate, checkpoint, next task. There is no mode switch — the package always routes substantial implementation this way, while trivial work and explicit single-agent requests stay with the root session, and security/architecture/payments/tenancy/migration-risk work can still get targeted additional Astra review.

Originated from a Reddit post (r/vibecoding) by the author ("Ethan+" / Ethan Rogers) describing hitting Astra weekly usage limits on a 20x plan shortly after launch, and iterating from ad hoc subagent delegation (Sol/Luna/Opus/Sonnet, ~10% savings) to a Flash-only worker loop (60% savings) to the current phased Astra→Flash→Astra workflow (98%+ savings across the author's tests, including a 7-hour build using 2% of weekly usage vs. a prior 5-hour build using 28%).

## Pricing basis for the savings claim

Per 1M tokens (author's figures, matching the GitHub README's "API-equivalent estimate" table — Astra has no public API SKU, so these are not ChatGPT/Codex subscription charges):

| | Astra (estimated) | DeepSeek V4.1 Flash | Astra premium |
|---|---|---|---|
| Uncached input | $10.00 | $0.15-$0.30 | 33-67x |
| Cached input | $1.00 | $0.003-$0.006 | 167-333x |
| Output | $50.00 | $0.60-$1.20 | 42-83x |

The README reports one measured field build at 8.56M Astra-equivalent input tokens/1K implementation lines for an all-Astra baseline vs. 95.9K for Astra+Flash (98.9% reduction), with total compute per 1K lines down 97.0-97.7% and 39% more implementation/test lines produced in the same measured phase.

## Mechanical details

- **Requirements:** a Codex client with native subagent support and standalone custom agent TOML files under `$CODEX_HOME/agents/`, GPT-6 Astra as the root model, Python 3.11+ (no third-party deps), and an existing Codex Router installation already configured/authenticated for a reviewed DeepSeek V4.1 Flash route (default `deepseek/deepseek-v4.1-flash`; OpenRouter, opencode Go, Command Code, Nous Research, and Ollama Cloud routes are also supported). The installer does not install Router, add credentials, or select the root model.
- **Install:** `python3 -B install.py` (dry run/preview) then `python3 -B install.py --apply`. Writes: a skill + references/templates/doctor/plan-validator under `~/.agents/skills/astra-flash-orchestrator/`, `$CODEX_HOME/agents/astra_flash_builder.toml` (nested agents disabled), and a marked/scoped policy block appended to `$CODEX_HOME/AGENTS.md` (or `AGENTS.override.md` if present) — other instructions in that file are preserved. Originals are backed up under `$CODEX_HOME/astra-flash-install-backups/` with a guarded undo receipt (`install.py --undo <receipt>`).
- Explicitly does not run paid inference, start services/workers, or commit/push/deploy during installation; installer rejects non-loopback Router URLs, embedded credentials, and unexpected paths.
- `doctor.py` and `doctor.py --check-local-router` validate local config/catalog and make a local `/models` GET only — neither proves paid inference actually works end to end.
- OpenCode desktop is supported via a separate adapter (file-only, no Python, no Codex Router required); the Codex-specific instructions and the benchmark table above are specific to the native Codex/Router workflow.
- Offline test suite: `python3 -B -m unittest discover -s tests -v`.

## Security

MIT licensed (Ethan Rogers, 2026). Single-maintainer, "early release" per the README — offline installation tests pass and one field build was measured, but the author is explicit that results describe that run, not guaranteed savings ("results below describe that run, not guaranteed savings," "your savings will differ"). No independent benchmark or third-party audit found; the 98.9% figure is self-reported from one uneven field comparison, not a controlled trial. Multiple GitHub accounts host what appear to be forks with identical descriptions (jorgefspereira, JaredReabow, KelvinZee) — consistent with ordinary GitHub forking of the `ethanplusai/astra-flash-orchestrator` original, not verified as independent implementations.

Installation writes outside the project directory: it appends a policy block to the user's global `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`) and installs a subagent role and skill files under the user's home directory (`~/.agents/skills/`, `$CODEX_HOME/agents/`). This is the standing global instruction file for every future Codex session on the machine, not scoped to one repo — review the installed policy block and the `astra_flash_builder.toml` role before trusting it, same as any other change to global agent instructions. Requires an already-configured, already-authenticated external model route (DeepSeek API or OpenRouter, etc.) via Codex Router — this package does not itself request, read, or store the credential, but downstream task content is sent to that third-party provider once the route is exercised. No sandboxing or scope restriction is imposed on what the Flash worker can touch beyond whatever the host Codex client's own permissions allow.
