---
name: local-model-adversarial-workflow
title: Local Model + Cloud Adversarial Workflow
category: agent-pattern
summary: "Multi-model orchestration pattern — local 27B model (Qwen) handles drafting, planning, and implementation; cloud models (Opus, GPT) do adversarial code reviews; repeated review loops until green; domain-specific MCP tools for database/web verification reduce hallucinations and token costs"
tags: [multi-model, local-inference, adversarial-review, qwen, cost-optimization, code-review, domain-tools, orchestration]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [advisor-strategy]
license: ""
security_flags: []
source: unknown
---

## What it does

A practitioner-reported workflow pattern for cost-effective AI-assisted development using a local small model (Qwen 27B) as the primary workhorse with cloud frontier models (Opus, GPT) for quality gates:

1. **Draft a plan** with local 27B model
2. **Iterate over the plan** and output a spec markdown
3. **Review the spec** with Opus/GPT, adjust with findings
4. **Implement** with local 27B, create a PR
5. **Adversarial code reviews** from Opus, GPT, and 27B independently. Collect all findings and summarize a complete review with Opus.
6. **Implement changes** with 27B
7. **Re-review loop** with Opus/27B until everything passes

Key observations from the practitioner:

- Local 27B consistently finds issues that Opus/GPT miss in adversarial reviews — different model architectures surface different blind spots.
- Having Opus rate the quality of all reviews (including its own and 27B's) provides a meta-quality signal.
- Domain-specific MCP tool extensions (database copy queries, cached domain-specific web search, structured data loading) let the local model do work that would otherwise consume heavy token budgets on cloud models.
- The workflow keeps cloud model costs under a $20/month subscription budget while maintaining high code quality through adversarial review diversity.

## Assessment

Validates the advisor-strategy pattern (executor/advisor split) with a concrete implementation. The novel contributions are: (1) adversarial review diversity across model architectures rather than just capability tiers, (2) meta-review quality rating, and (3) domain-specific tool extensions that shift verification from LLM reasoning to deterministic tool calls. The pattern is directly relevant to the project's existing multi-model setup (Sonnet subagents + Opus main agent).

## Security

Not applicable — this is a workflow pattern, not executable code.

## Usage notes

- **Qwen + Claude overseer pipeline (r/ClaudeCode):** Setup: Windows rig (64GB DDR5, R9 9950x3d, RTX 5090) runs Qwen 3.8 Q6_K in LM Studio (low thinking, temp 0.7, 55K context), accessible over VPN to Mac running Cline. Claude subscription used for an "overseer" skill where Claude knows it's working with a weaker model, makes plans for it, then verifies Qwen's implementation. User reports daily-driving this for over a month — Claude plans, Qwen executes, Claude reviews. Wants to automate the message-passing so human only does final code review.
