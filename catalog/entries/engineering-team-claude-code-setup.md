---
name: engineering-team-claude-code-setup
title: Claude Code as a Guardrailed Engineering Team (Solo-Operator Case Study)
url: https://www.reddit.com/r/ClaudeCode/comments/1xbxoza/my_claude_code_setup_it_runs_like_a_small/
source_url: https://www.reddit.com/r/ClaudeCode/comments/1xbxoza/my_claude_code_setup_it_runs_like_a_small/
source: reddit
category: agent-pattern
summary: "Detailed solo-operator case study (45-year developer, $100/mo plan, 1,160 issues closed across 15 projects in 60 days) structuring Claude Code as a small team with enforced process rather than a chat window: rules live in PreToolUse hooks (not CLAUDE.md prose) once a correction repeats twice; a self-hosted GitLab plus a ~90-tool custom MCP server acts as the system of record with an issue state machine the model cannot bypass (raw API calls forbidden); work is routed across model tiers (Haiku/Sonnet/Opus, plus a non-generative classifier below Haiku) by task difficulty, with the main thread only planning/dispatching; memory is a typed, dated, version-controlled knowledge base instead of free text; and 'verify before asking or asserting' is a hard rule enforced through checks (file hashes, compile checks, render-then-view for documents) rather than trust."
tags:
  - claude-code
  - hooks
  - agent-orchestration
  - model-routing
  - issue-tracker
  - state-machine
  - memory-architecture
  - mcp-server
  - verification
  - gitlab
  - case-study
reviewed: 2026-10-28
acquired: 2026-10-28
license: N/A
security_flags: []
overlaps:
  - jev
  - boris-cherny-claude-md
  - claude-md-high-impact-lines
  - agent-cost-governors
---

## What it does

A single operator's end-to-end Claude Code architecture, written up after the operator asked Claude itself to describe the setup for a Reddit post (disclosed in the post). Organized around nine standing design decisions:

1. **Hooks enforce, CLAUDE.md only points.** Rule of thumb: a behavior corrected twice becomes a `PreToolUse` hook that denies the call, rather than another line of prose the model drifts from. Enforced this way: deletes are blocked and rewritten as a move to `_archive/`; all git commands route through one wrapper script (avoids the re-approval-per-directory problem of `cd <repo> && git ...` commands); commit messages can't contain issue-closing keywords or an AI co-author trailer; writes to day-job systems are blocked without per-action approval while reads are allowed; work content is blocked from non-approved model vendors with no override.
2. **The issue tracker is the system of record, not the model.** A self-hosted GitLab plus a ~90-tool custom MCP server enforce a `type::`/`status::` state machine on every issue (`backlog→ready` human-only; `ready→in-progress→blocked|review→done` agent-driven but gated — `review→done` requires operator sign-off). Closing an issue is one tool call that runs the whole protocol (cross-reference commits, log effort, set terminal status, sync the wiki). Raw API calls are forbidden because they bypass the state machine — the workflow rules live inside the tool surface, not in instructions the model could ignore.
3. **Model-tiered routing, clean orchestrator context.** The main session plans and dispatches, never edits code directly: Haiku for trivial/cheap tasks, Sonnet for implementation against a clear spec, the strongest model for unresolved bugs and real architecture tradeoffs, and a non-generative typed-judgment classifier (Jev) below all three for decisions that aren't really "writing" (is this issue ready, is this alert noise, does this MR match its diff). A second vendor's coding agent can be dispatched for a second opinion inside a disposable git worktree that never writes to the real repo; the primary agent reviews what comes back.
4. **Classifier break-even, measured, not assumed.** The standing rule is "the classifier decides, Claude writes; when the classifier is unsure, Claude decides" — see [[jev]] for the measured cost/accuracy numbers behind this (break-even point, credential-leak safety lesson from production use).
5. **Skills package repeated multi-step workflows as one command**, e.g.: work the ready queue (one subagent per issue, its own worktree, validate→implement→review, never merges/closes itself); groom the backlog (check against a definition of ready, draft acceptance criteria from actual code, promote only named issues); work a milestone end-to-end except for what needs the operator; "ask the board" (a panel of persona-modeled engineers argues a decision from different angles — useful specifically as a check against the operator talking themselves into something).
6. **Memory is a typed, dated knowledge base, not free text.** Each fact is its own file with typed frontmatter (identity, feedback, project state, reference); `stale_after` dates trigger a session-start re-check hook; deprecated facts are marked `status: deprecated` rather than deleted; `verified: by human` outranks a model-inferred fact; a hook validates every memory write and regenerates the index; the whole store is version-controlled. Entries explicitly tagged `TRAP` (costly past mistakes, e.g. "this command exits 0 but does nothing") are called out as the single most valuable category.
7. **Domain-specific MCP servers over generic ones**, each with a `help()` tool as its own catalogue so the model looks up capabilities instead of guessing; a read-only work-mailbox server deliberately ships no send/delete verb at all — "the safest permission is a capability that doesn't exist."
8. **Standing infrastructure rules applied in one pass**, e.g. any new VM/host/container is registered in inventory (reachability proven by a real command, not a ping), given a start-page tile if it has a web UI, and has its timezone set — with CI failing any container service missing a timezone.
9. **Verify, don't assert, as a hard rule**: deliveries verified by file hash, not by poking at the running app; Word documents go through a docx→PDF→images render loop the model actually looks at before the operator sees them; code gets a compile check before every deploy.

**Author's own "what people get wrong" list:** prose rules expected to stick (use hooks); no system of record (let a tracker's state machine decide "done," not the model); one model for everything (route by difficulty, keep the orchestrator's context clean); memory as a dumping ground (type it, date it, mark what's verified, record traps); generic MCPs only (the best servers are the ones written for your own domain with your rules built in); trusting "done" (make verification part of the workflow); using an expensive model for every decision without measuring the break-even (small piles can cost more through a classifier, not less).

Credited sources for two components: the backlog-grooming skill idea is adapted from a skill by Matt Pocock; "ask the board" is adapted from an idea in an Austin Marchese YouTube video (neither linked in the post). The operator reports building all of it by prompting Claude rather than writing code directly, and later had Claude scaffold a sanitized public write-up repo at github.com/aaraujo666/ClaudeCodeSetup.

## Sources

- [My Claude Code setup: it runs like a small engineering team with guardrails, not like a chat window — r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1xbxoza/my_claude_code_setup_it_runs_like_a_small/) — full write-up and comment-thread clarifications (catalog source).

## Security

N/A — operator workflow/configuration description, not distributed software; no code or package is shipped by this post itself. Two of its own design choices are notable security patterns in their own right: capability minimization (a mailbox MCP server with no send/delete verb, rather than a send/delete verb gated by a permission check) and secret-aware content screening before sending data to a third-party classification API (added only after a credential leaked through a screen that wasn't looking for secrets — see [[jev]]).
