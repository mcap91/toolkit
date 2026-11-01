---
name: context-graph-compressor
title: Context Graph Compressor
url: "https://github.com/Adityapal67/context-graph-compressor"
category: skill
summary: Structured JSON graph handoff with importance tagging and cross-LLM portability beats plain-text handoff skills; too new/single-contributor to adopt outright
tags: [context-management, handoff, token-reduction, json, claude-ai, cross-llm, session-resume]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [no-tests, no-ci, single-contributor, new-repo]
overlaps: [agent-session-resume]
source: unknown
---

## What it does

Compresses a long claude.ai chat conversation into a portable, minimal JSON context graph that can be pasted into a new session with any LLM. Outputs two modes: `compact` (~300–500 tokens, abbreviated keys for minimum token cost) and `readable` (full prose, for archiving or sharing). The graph encodes typed nodes (fact, decision, problem, goal, code, context), per-node importance (h/m/l), and optional relationship edges (depends_on, resolves, supersedes). Low-importance nodes are dropped in compact mode. A `handoff` top-level field provides a plain-English re-entry prompt for the receiving LLM. Installed via claude.ai Settings → Skills (upload `.skill` file). Triggered by natural-language phrases: "compress this chat", "handoff to new chat", "too many tokens, start fresh".

## Assessment

The core idea is sound and meaningfully differentiated from existing handoff approaches: most handoff skills produce markdown bullet lists that are readable but not machine-parseable and carry no importance ranking. The structured JSON schema with typed nodes and h/m/l tagging lets a receiving LLM (or a program) prioritize what it must know vs. what is optional — a real improvement for context compression accuracy. Cross-LLM portability (GPT-4, Gemini, Mistral) is a genuine differentiator over Claude-only compaction. That said, the repo is newly created by a single contributor with no release history, no tests, and no CI; it is a pure prompt skill (SKILL.md only), so "testing" is qualitative. The claimed 97% token reduction is a headline number for a specific example, not a validated benchmark. Pilot is appropriate: worth adopting for claude.ai sessions where context overflow is a real problem, but should be evaluated against actual compression quality before treating it as a reliable production handoff mechanism.

## Mechanical details

- **Installation**: Download `context-graph-compressor.skill`, upload to claude.ai Settings → Skills. No code, no dependencies, no runtime.
- **Trigger phrases**: "compress this chat", "save context", "handoff to new chat", "too many tokens, start fresh"
- **Output**: JSON object written to chat and optionally saved as a downloadable `.json` file.
- **Schema**: `v` (version), `mode` (compact|readable), `desc` (one-line summary), `n` (node array), `handoff` (re-entry prompt string). Nodes have `id`, `t` (type code), `i` (importance), `s` (summary), optional `c` (children array) and relationship fields.
- **Node types**: F=fact, D=decision, P=problem, G=goal, C=code, X=context.
- **Resume pattern**: Paste JSON into new chat preceded by "Context from previous session:" and followed by "Continue from this state."
- **What to adopt**: The node-typed, importance-tagged JSON schema is worth borrowing as a data model for any context-compression skill, even if not installing this specific `.skill` file. The `handoff` summary field pattern (one-line re-entry prompt) is a clean convention.

## Security

Pure prompt skill — no executable code, no dependencies, no network calls, no credential handling, no eval or shell injection vectors. Security risk is limited to the skill influencing Claude's behavior in ways that could be misused (e.g., if a malicious conversation caused it to produce misleading compressed output), but this is inherent to any LLM skill. The README contains no injection attempts or unusual instructions. Repo is MIT-licensed. Supply-chain risk is low given there is nothing to execute — adoption is purely a question of whether the SKILL.md prompt produces useful output.

Flags: `no-tests`, `no-ci`, `single-contributor`, `new-repo` — all expected for a tiny prompt-only skill repo; none represent executable supply-chain risk.
