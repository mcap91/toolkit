---
name: shadow-mode-progressive-trust-approval
title: Shadow-Mode Progressive Trust for Agent Approval Gates
category: agent-pattern
summary: "Review-load design pattern for human-in-the-loop agent approval: tier actions by risk/reversibility rather than by tool, run gated actions in shadow mode (agent logs what it would decide without executing, compared against the human's actual call) to measure per-action-type agreement rather than one global rate, write explicit promotion/demotion rules (agreement above threshold for N decisions with no high-severity miss loosens the gate a notch; a drop or miss tightens it) so oversight shrinks as the agent earns it instead of staying flat, keep approval UI to a few lines of what/why/evidence, and convert any judgment call the human keeps approving the same way into a deterministic code rule instead of re-reviewing it"
tags:
  - agent-pattern
  - human-in-the-loop
  - approval-gates
  - shadow-mode
  - progressive-trust
  - risk-tiering
  - governance
  - review-load
reviewed: 2026-10-30
acquired: 2026-10-30
license: N/A
security_flags: []
overlaps:
  - agent-software-engineering-fundamentals
  - governance-first-multi-agent-architecture
  - agent-execution-governance
source_url: https://www.reddit.com/r/AI_Agents/comments/1xcqkgw/anthropics_own_data_suggests_were_becoming_middle/
source: reddit
---

## What it does

A pattern for deciding which agent actions need a human to look at them, and for shrinking that review load over time instead of leaving it fixed. The starting problem: once an agent can take far more actions per hour than a human can review, flat strategies (sample a fixed percentage, or read everything) never improve as the agent gets more reliable — the review load stays constant regardless of agent quality.

The pattern has several parts, drawn from a Reddit discussion where multiple practitioners converged on the same design independently:

1. **Tier by risk, not by tool.** Internal, reversible, read-only actions execute and are only logged. Low-risk but customer-facing actions get sampled. Anything that writes externally, spends money, or deletes data always waits for a human.
2. **Shadow mode as the measurement step.** For gated actions, the agent logs the decision it would have made without executing it, then that logged decision is compared against what the human actually approved, rejected, or edited. Agreement is tracked per action type/slice, not as one global number — one practitioner found ~98% agreement on one action type and far lower on another, which a single global gate had been treating identically.
3. **Write the promotion/demotion rule before looking at the numbers**, to avoid rationalizing a threshold after seeing the data. Example rule: agreement stays above a threshold for N consecutive decisions with no high-severity miss → loosen that action type's gate one notch (always-approve → sample-approve → log-only). A drop in agreement or any high-severity miss tightens it back. This gives the agent an explicit, evidence-based path to earn reduced oversight, rather than a permanent flat review load.
4. **Cheap-to-decide approvals.** The approval surface should state what the agent wants to do, why, and the supporting evidence in a few lines; if approving requires reading the full output, the approval UI is badly designed.
5. **Self-check before human review.** Define what "done" looks like for a task and run cheap automated checks first, so a human only sees exceptions rather than everything.
6. **Promote repeated judgment calls into deterministic code.** When the agent and human keep agreeing on the same call made the same way, pull that decision out of the model and write it as a plain code rule — cheaper, testable, and it never needs reviewing again, narrowing what the agent still handles to genuinely ambiguous cases.
7. **One owner per approval queue/workflow** — distributing review across several people was reported to make nobody actually accountable for it.

The thread names LangGraph (interrupts) and Orq.ai (per-tool approval cards) as implementations of the gating mechanism itself, but the pattern — risk tiering, shadow-mode measurement, and trust that is earned rather than assumed — is tool-agnostic.

## Security

N/A — a design pattern, not software. Applying it correctly depends on getting the risk tiers and high-severity-miss definitions right; an under-tiered action category that gets promoted to log-only prematurely is the main failure mode the pattern itself warns against.
