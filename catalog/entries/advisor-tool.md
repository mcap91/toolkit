---
name: advisor-tool
title: Advisor Tool (Claude Code / Claude API)
url: "https://code.claude.com/docs/en/advisor"
category: reference
summary: "Anthropic server-side tool that lets Claude consult a second, at-least-as-capable model at decision points (before committing to an approach, on recurring errors, before declaring done); the advisor receives the full conversation and returns guidance Claude applies; configured via /advisor, advisorModel, or --advisor; billed at the advisor model's rates; the concrete feature behind the advisor-strategy concept"
tags: [claude-code, claude-api, advisor, model-escalation, cost-optimization, anthropic, server-tool]
reviewed: 2026-07-09
acquired: 2026-07-09
license: proprietary
security_flags: [proprietary-feature, anthropic-api-only, token-billing-exposure]
overlaps: [advisor-strategy, agent-teams]
source: unknown
---

## What it is

The advisor tool is an Anthropic server-executed tool that lets the main Claude model consult a second, typically stronger model at key moments in a task. The advisor always receives the full conversation (every tool call and result) and returns guidance that Claude applies before continuing. It runs server-side on Anthropic's infrastructure for both subscription and API-billed accounts; you choose the advisor model and Claude decides when to call it. This is the concrete product behind the `advisor-strategy` concept entry. It is documented in both the Claude Code docs and the Claude API docs (as a Messages-API server tool).

## Configuration

Set the advisor three ways: the `/advisor` command (saves to `advisorModel` in user settings, persists across sessions), the `advisorModel` settings key, or the `--advisor` flag (single session, takes precedence). The advisor must be at least as capable as the main model; the docs give an accepted-pairing table by main model (e.g. Haiku/Sonnet/Opus mains accept Fable/Opus/Sonnet advisors under capability-ranking rules; Fable 5 accepts only Fable). Aliases `opus`/`sonnet`/`fable` resolve to the latest version; full IDs such as `claude-opus-4-8` also work. Subagents inherit the advisor and re-check the pairing against their own model. Claude Code validates the pairing before each request and silently declines to attach an under-capable or unrecognized advisor.

## Behavior, cost, requirements

Claude decides when to consult (typically before committing, on recurring errors, before declaring done); you can request a consultation in-prompt ("consult the advisor before you continue"). The transcript shows an "Advising" line; Ctrl+O expands the guidance. Claude generally follows the guidance but surfaces conflicts when its own evidence (a failing step, contradicting file contents) contradicts it. Each call sends the full conversation to the advisor and is billed at the advisor model's input/output rates (or counts toward plan usage on subscriptions); toggling the advisor does not invalidate the main model's prompt cache, but the advisor's own read of the conversation is never cached. Requires Claude Code v2.1.98+ (a Fable 5 advisor needs v2.1.170+) and the Anthropic API only — not available on Amazon Bedrock, Google Cloud, or Microsoft Foundry. Disable per-session with `/advisor off` or globally with `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1`.

## Security

Proprietary Anthropic feature with no installable artifact or third-party code. The main operational consideration is cost/billing: advisor calls consume tokens at the advisor model's rates in addition to the main model, and there is no setting to cap or force advisor frequency (control it via instructions). The advisor is a server tool available only through the Anthropic API path; through an `ANTHROPIC_BASE_URL` gateway, availability depends on whether the gateway forwards the request intact.