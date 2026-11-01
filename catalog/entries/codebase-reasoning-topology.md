---
name: codebase-reasoning-topology
title: Codebase Reasoning Topology
category: reference
summary: heavy for daily use but interesting as a pre-flight checklist concept
tags: [invariants, state-ownership, blast-radius, checklist]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it says

A structured prompt framework from Karpathy's 12 Rules (same source as the `karpathy-12-rules` entry) that defines four invariants for reasoning about a codebase before making changes. The four invariants are: (1) state ownership — what owns each piece of state and what can mutate it; (2) feedback and observability — how failures surface and how you know something worked; (3) blast radius — what breaks if this change goes wrong and how to scope the impact; (4) timing and ordering — what must happen before this, what depends on this completing first. The framework also includes a friction loop (where repeated manual steps indicate missing automation) and a verification gate (evidence required before claiming completion).

## Assessment

The four invariants are conceptually sound but the full framework is too heavyweight for routine use. Most value is in the blast-radius and state-ownership invariants, which are underrepresented in current workflow habits. Interesting as a pre-flight checklist for high-impact changes rather than a daily prompt.

## What to adopt

Consider the blast-radius and state-ownership invariants as optional pre-flight questions for high-impact changes (schema migrations, pipeline refactors, config changes with broad effect). No tooling adoption needed — these are reasoning prompts, not installation artifacts.

## Security

This entry is a pure text-based reasoning framework — no executable code, network calls, package installation, or external dependencies. There is nothing to install or run, so the attack surface is effectively zero. No credential handling, no file system writes, and no agent tool use are involved.

License information is not formally published for this framework (it originates from a prose checklist attributed to Andrej Karpathy's "12 Rules" material). As a reasoning prompt rather than a software artifact, typical open-web attribution norms apply; there is no proprietary restriction identified. No security flags are raised.
