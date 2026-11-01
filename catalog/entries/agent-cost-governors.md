---
name: agent-cost-governors
title: "Agent Cost Governors & Circuit Breakers"
category: agent-pattern
summary: "Three-layer cost governance pattern for autonomous agents — hard token leases per step, circuit breakers on retry-without-progress, and step cost degradation (frontier → local model fallback) to prevent denial-of-wallet from recursive error loops"
tags: [cost-control, circuit-breaker, agent-safety, token-budget, denial-of-wallet]
reviewed: 2026-09-16
acquired: 2026-09-16
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it says

Autonomous agents that run in loops (plan, act, observe, retry) can incur unbounded costs when they get stuck — e.g., repeatedly retrying a failing step, or escalating to expensive frontier models without making progress. This is described as a "Denial of Wallet" risk: an availability-style failure mode where the attacker (or a buggy agent) doesn't take a system offline but instead drains its budget through unchecked API/compute spend. The source describes three cost-governance mechanisms meant to bound this risk at the execution-step level:

1. Hard Token Leases — every agent is issued a strict token budget per step.
2. Automated Circuit Breakers — if an agent retries 3 times without state progress, the circuit trips and halts execution.
3. Step Cost Degradation — as budget thresholds are approached, the system falls back from expensive frontier models to smaller local models.

## Key takeaways

- Hard token leases: a fixed, strict token budget allocated per execution step, rather than a global/session-only cap.
- Circuit breakers: execution halts automatically after 3 retries that produce no state progress.
- Step cost degradation: model selection downgrades from frontier to smaller local models as budget thresholds near, rather than continuing at the original model tier.

## What to adopt

- Hard token leases operate at the step granularity: each individual step (not just the overall session) is metered against its own token budget, so a single step cannot consume the whole session's allowance.
- Circuit breakers key off state progress, not just retry count alone — the trigger condition is "retried 3 times AND no state progress," distinguishing legitimate multi-step work from a stuck loop.
- Step cost degradation is threshold-triggered: as the remaining budget nears a defined threshold, the executing model is swapped downward (frontier → smaller local model) for subsequent steps, rather than being an all-or-nothing cutoff.

## Security

n/a — conceptual pattern, no code artifact.
