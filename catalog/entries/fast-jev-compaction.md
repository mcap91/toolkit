---
name: fast-jev-compaction
title: Fast Jev Compaction
url: "https://github.com/tamaratran/fast-jev-compaction"
category: plugin
summary: "Claude Code plugin/npm library that replaces the built-in compaction summary with a Jev (TypeSafe AI) scored prune of tool calls/results; depends on Claude Code's unshipped function-hooks feature and an early-access third-party API, and a filed issue shows its hook events go unrecognized (silent no-op) on a recent Claude Code build"
tags: [token-reduction, compaction, claude-code, plugin, hooks, context-management]
reviewed: 2026-09-25
acquired: 2026-09-25
license: MIT
security_flags: [external-api-dependency, api-key-required, unshipped-feature-dependency, known-compatibility-bug, unverified-stars]
overlaps: [headroom, distill]
source: unknown
---

## What it does

fast-jev-compaction is both an npm library (`fast-jev-compaction`) and a Claude Code plugin (repo root doubles as `hooks/` + `.claude-plugin/`). It replaces Claude Code's built-in `/compact` and auto-compaction summary with a pruned version of the *original* transcript instead of an LLM-written summary. Every `tool_use`/`tool_result` pair (matched by `tool_use_id`) outside the pinned first message and the newest `preserveRecentMessages` (default 6) messages is a candidate for removal. The whole conversation so far — oldest first, tool inputs and user/assistant text included verbatim, tool results replaced by a short note — is sent to TypeSafe AI's Jev "System One" model (`api.typesafe.ai/v1/systemone`) with two yes/no ("noul") questions per candidate call: should the call stay, should its result stay verbatim. Below `keepThreshold` (default 0.5) a result is truncated to `truncateHeadChars` (300) characters plus a note; below both thresholds the call and result are removed entirely. Text messages are never rewritten or removed in the output — only tool calls/results are dropped or truncated. If the state doesn't fit `maxStateTokens` (25k, estimated via a character-based heuristic, not a real tokenizer), it is progressively degraded (input truncation, text head/tail abridgment, old-message collapsing) before Jev is asked. API failures, malformed responses, a missing key, or an unfittable history throw; the Claude Code hook catches this and falls back to Claude Code's built-in summary.

As a library it also exports composable primitives (`collectToolCalls`, `fitState`, `batchCalls`, `decideCall`, `applyDecisions`, a `JevAsker` interface, `buildJevRequest`/`parseJevResponse`) so a caller can supply their own transport instead of calling TypeSafe directly.

## Assessment

- **Depends on two things that don't ship yet.** (1) Claude Code function hooks ("Mods") — an experimental, default-off, actively-redesigned Claude Code feature gated by `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`, tracked in `anthropics/claude-code#91870` (opened by an Anthropic engineer 2026-09-03; explicitly "hasn't shipped yet" per Anthropic's own comments). (2) TypeSafe AI's Jev/System One model, itself only in early access behind a waitlist since 2026-09-15. Both are moving targets independent of this plugin.
- **Confirmed broken on at least one recent build.** Repo issue #21 reports that on Claude Code 2.1.272 the plugin's declared hook events (`session.compact`, `turn.complete`) are not recognized at all — `claude plugin details` shows "Hooks (0)" and only a pre-existing `PreCompact` (block-only) hook exists in that build's changelog. The plugin installs cleanly and silently does nothing rather than failing loudly — the reporter calls this "a worse failure mode than refusing to install." No maintainer response as of this review. The README's own reference to a "Claude Code 2.1.274 type reference" suggests the plugin targets a build most users won't have.
- **Sends full conversation state to a third party.** Every compaction pass sends all tool inputs, all user/assistant text, and abbreviated tool results to `api.typesafe.ai`. This is the same class of trust-boundary crossing as `headroom`'s proxy mode (already in this catalog): any secrets, file contents, or credentials that passed through tool calls during the session leave the machine.
- **Popularity signals are inconsistent.** External coverage (blog posts, aggregator search snapshots) cites GitHub star counts ranging from roughly 700 to 6.8k for the same repo and a Reddit thread reportedly over 300 upvotes; a direct API check was not available in this environment (`gh api` calls were blocked), so treat adoption numbers as unverified rather than as evidence of maturity.
- The library layer (`compact`/`compactMessages`, pluggable `JevAsker`) is decoupled from Claude Code and from TypeSafe specifically — a team could point it at a self-hosted scorer — but no such alternative is shipped or referenced.
- Unit tests run against a fake Jev and never touch the network; only `npm run demo` exercises the real API. A macOS-only SwiftUI demo app additionally exists purely for screen recording and never calls the API.

## Mechanical details

- Library install: `npm install fast-jev-compaction`; reads `TYPESAFE_API_KEY` from the environment by default for the `apiKey` option.
- Plugin install: set `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` and `TYPESAFE_API_KEY` in `~/.claude/settings.json` env, then `claude plugin marketplace add tamaratran/fast-jev-compaction` + `claude plugin install fast-jev-compaction@fast-jev-compaction`; restart or `/reload-plugins`. From a checkout: `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude --plugin-dir .`.
- Key options: `model` (default `jev-latest`), `baseUrl` (`https://api.typesafe.ai/v1/systemone`), `keepThreshold` (0.5), `preserveRecentMessages` (6), `maxStateTokens` (25000), `maxRequestTokens` (30000, must stay under Jev's 32k request limit), `truncateHeadChars` (300), `goal` (defaults to the last 3 user prompts).
- `result.stats` reports before/after message and character counts, per-reason decision counts, estimated state token size, which degrade stage was needed, and request count — usable to audit what a compaction pass actually removed.
- Dev commands: `npm run typecheck`, `npm test` (fake Jev, no network), `npm run build`, `npm run validate:plugin` (wraps `claude plugin validate`), `npm run demo` (live network call, needs a real key).

## Security

- **License**: MIT (LICENSE file present in the repo) — permissive.
- **security_flags**:
  - `external-api-dependency` — full conversation state (tool inputs, user/assistant text, abbreviated tool results) is sent to `api.typesafe.ai` on every compaction; anything sensitive that passed through the session leaves the machine.
  - `api-key-required` — requires a `TYPESAFE_API_KEY`; README guidance is limited to "never commit the key," with no described scoping or rotation story.
  - `unshipped-feature-dependency` — the Claude Code plugin path depends entirely on function hooks, an unshipped, default-off, still-changing Claude Code feature (`anthropics/claude-code#91870`).
  - `known-compatibility-bug` — repo issue #21 documents the plugin's hook events going unrecognized on Claude Code 2.1.272, with a silent no-op failure mode instead of an install error; open and unresolved as of this review.
  - `unverified-stars` — third-party coverage reports GitHub star counts that vary widely (~700–6.8k) for the same repo across sources/snapshots; not independently confirmed here.
- The fetched README shows no other unusual code-execution surface beyond the expected (a Claude Code hook script plus an HTTP call to TypeSafe); the `hooks/fast-jev.ts` source itself was not reviewed line-by-line in this pass.
