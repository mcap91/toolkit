---
name: castem-first-principles-model-mediated-work
title: "CASTEM: First Principles for Model-Mediated Work"
url: "https://www.linkedin.com/pulse/castem-first-principles-model-mediated-work-bryan-downie-ph-d--58mnc/"
category: reference
summary: "Portable 6-criterion mnemonic (Credible, Auditable, Supervised, Traceable, Explainable, Monitored) for AI governance in regulated settings — good design checklist, no tooling."
tags: [ai-governance, compliance, regulated-ai, mnemonic, audit, validation, oversight]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-copyright-author
security_flags: []
overlaps: [ai-needs-what-alcoa-gave-records]
source: unknown
---

## What it says

Bryan Downie introduces CASTEM — a six-question mnemonic synthesized from the regulatory landscape (FDA credibility guidance, EU AI Act, banking model-risk rules, insurance bulletins) as of April 2026. It is the follow-up to his prior piece on ALCOA+ applied to AI records.

The six criteria:

- **Credible** — Has the model been shown fit for this specific use with evidence proportional to the risk? Not "does it work in general?" but "is it appropriate for this decision?"
- **Auditable** — Is there a durable, tamper-evident trail: configuration used, model version, who reviewed, what they decided, when?
- **Supervised** — Is a qualified person accountable, with authority to review, override, or reject before the output takes effect? Post-hoc review is not oversight.
- **Traceable** — Can a specific output be followed back through the sources and transformations it rests on? This is lineage, not event history — the worksheet behind the line.
- **Explainable** — Can the reasoning be expressed in terms a domain expert (clinician, actuary, auditor, judge) can examine and challenge?
- **Monitored** — Is the system watched post-deployment so drift or degradation triggers investigation, revalidation, or withdrawal? Fitness established once is not fitness forever.

The article draws the analogy explicitly: ALCOA+ made record integrity portable; CASTEM attempts to make model credibility portable.

## Assessment

`note`: The framework is well-constructed and grounded in real regulatory sources rather than invented requirements. It has direct applicability to anyone designing AI pipelines for regulated environments (clinical, pharmaceutical, financial). However, it is an editorial article — no code, no tooling, no implementation scaffold — so there is nothing to adopt or pilot beyond internalizing the checklist. Worth referencing when designing agent validation, audit logging, human-in-the-loop, and drift-monitoring subsystems. Overlaps with and extends the prior ALCOA+ article already in the catalog.

## What to adopt

Use the six questions as a design checklist when architecting regulated AI pipelines:

1. Before deploying: can you answer Credible (use-specific evidence) and Explainable (reviewable reasoning)?
2. At build time: plan for Auditable (tamper-evident logs, versioned config) and Traceable (output lineage back to source data).
3. Operationally: enforce Supervised (qualified human with override authority pre-effect) and Monitored (post-deployment drift detection and revalidation triggers).

The distinction Downie draws between Auditable (event history) and Traceable (output lineage) is particularly useful for designing separate audit log vs. data provenance subsystems.

## Security

Pure editorial article — no code, no dependencies, no installable components. No security assessment applicable. License is not stated; content is copyright the author as published on LinkedIn.
