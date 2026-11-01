---
name: pii-detection
title: PII Detection / Compliance Skills
category: skill
summary: HIPAA/CCPA/PCI-DSS coverage; pilot if handling sensitive data
tags: [pii, compliance, hipaa, ccpa, security]
reviewed: 2026-05-25
acquired: 2026-05-25
url: "https://github.com/gosprinto/compliance-skills"
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Automatically fires during planning, code generation, and repo audits to detect personally identifiable information and flag regulatory compliance gaps. Covers eight regulatory frameworks: CCPA, HIPAA, PCI-DSS, COPPA, GLBA, BIPA, FERPA, and the FTC Act. Operates as a background check rather than an on-demand command — it intercepts risky operations before they complete. Source is `gosprinto/compliance-skills/pii-detector`, discovered via Reddit r/claudeskills.

## Assessment

Clinical and genomic datasets in bioinformatics frequently carry HIPAA obligations. A skill that intercepts PII exposure automatically during code generation and repo audits reduces the risk of accidental data leakage without requiring developers to manually audit every operation. Pilot is conditional on handling sensitive data — not needed for purely synthetic or public datasets.

## Mechanical details

Source is `gosprinto/compliance-skills/pii-detector`. No public repo URL confirmed at review time. Keep behind a review gate (human confirmation before any flagged action proceeds) until the repo is directly fetched and the skill behavior is verified. Pilot trigger: when the workflow touches clinical data, patient identifiers, or datasets with HIPAA/CCPA obligations.

## Security

The skill is published under the MIT license by Sprinto (a compliance-tooling vendor) and carries no `security_flags` at this time. Because it intercepts live agent operations — scanning code being generated, planned actions, and repo contents — it runs with broad read access to the working tree; no network egress or external API calls are made by the skill itself. The primary adoption risk is trust in the skill's detection logic: false negatives (missed PII) could create a false sense of compliance, while false positives could interrupt legitimate operations. Mitigate by keeping the human-confirmation review gate in place (as noted in Mechanical details) until the skill behavior has been directly verified against a known-PII fixture in your environment.
