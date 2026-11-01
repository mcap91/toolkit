---
name: verify-before-claim
title: Verify Before Claim (Third Brain V5)
url: "https://github.com/Mark393295827/third-brain-v5-skills"
category: reference
summary: superpowers verification-before-completion covers this; confidence model is the novel addition
tags: [verification, quality, confidence-model]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it says

Third Brain V5's verify-before-claim skill enforces that no completion claim is made without fresh verification evidence — a new command run, not a citation of prior output. Includes explicit exit code checking as a discrete step. Produces structured validation reports with confidence scores rather than a binary pass/fail gate. The confidence model is probabilistic (poker psychology: expected value reasoning) rather than binary, enabling claims like "80% confident this pipeline is correct." Also flags claims backed by only a single source as inherently weaker.

## Assessment

`superpowers verification-before-completion` covers the core rule ("evidence before assertions always") and uses verification as a gate. The two approaches are functionally equivalent for the common case. The novel contribution from Third Brain V5 is the probabilistic confidence model — useful if the stack ever needs to express partial confidence rather than binary verified/unverified status.

| Aspect | Third Brain V5 | Superpowers |
|---|---|---|
| Core rule | "No completion claims without fresh verification evidence" | "Evidence before assertions always" |
| Fresh evidence | Must run new command, not cite prior output | Must run verification commands |
| Exit code check | Explicit step | Implicit |
| Confidence model | Expected value (poker psychology) — probabilistic, not binary | Binary: verified or not |
| Single-source flagging | Flags claims backed by only one source | No single-source concept |
| Output | Structured validation reports with confidence scores | Verification is a gate, not a document |

## What to adopt

No immediate action. If a future skill or workflow needs probabilistic confidence reporting rather than binary verification, revisit the confidence model from this source. The single-source flagging concept is also worth incorporating if hallucination rates on reference-backed claims become a concern.

## Security

This is a pure prompt/skill file — no executable code, no binaries, no network calls, and no dependencies beyond the agent runtime that already loads it. The MIT license imposes no usage restrictions. Installation copies Markdown files into the agent's skills directory (`~/.claude/skills/` or `.claude/skills/`), so the only adoption surface is the text of the skill itself being added to the agent's context.

No security flags apply. The skill does not request elevated permissions, does not touch the filesystem beyond what the calling agent already has access to, and does not introduce supply-chain risk beyond trusting the upstream GitHub repository's Markdown content.
