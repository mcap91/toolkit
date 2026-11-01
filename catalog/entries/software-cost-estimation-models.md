---
name: software-cost-estimation-models
title: "Software Cost Estimation Models (COCOMO II & Alternatives)"
category: reference
summary: "Reference on algorithmic software cost-estimation models — COCOMO II's three sub-models and effort/schedule formulas, plus alternatives (Putnam/SLIM, Function Point Analysis, SEER-SEM, story points, Wideband Delphi, analogy-based) — and their fit for git-derived, zero-touch size metrics."
tags: [cost-estimation, cocomo-ii, putnam-slim, function-points, software-metrics, git-metrics]
reviewed: 2026-07-22
acquired: 2026-07-22
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it says

Covers COCOMO II (Constructive Cost Model, USC) and its alternatives as inputs to an automated, git-derived cost estimator.

- **COCOMO II sub-models:** Application Composition (early prototyping; Object Points), Early Design (requirements known, pre-architecture; Function Points + a small cost-driver set), and Post-Architecture (construction phase; detailed SLOC and up to 17 cost multipliers).
- **Core formulas:** effort `Effort(PM) = A × Size^E × ∏(cost drivers)` with `A ≈ 2.94` and `E` a scaling exponent derived from five scale factors (precedentedness, development flexibility, architecture/risk resolution, team cohesion, process maturity); schedule `TDEV = C × Effort^F` with `C ≈ 3.67`.
- **Alternatives:** functional/algorithmic (Function Point Analysis; SLIM, a proprietary tool on Putnam's Rayleigh-curve model; SEER-SEM), agile/empirical (story points & planning poker, velocity-based estimation), and expert/analogy (Wideband Delphi, analogy-based ANGEL), with a comparison table of primary metric, best use, advantage, and limitation for each.
- **Flattened-Putnam proposal:** the public-domain Putnam equation `Effort(person-years) = (Size / (PP × Time^{4/3}))^3`, made deterministic by fixing `Time = 1.0` year and pinning process-productivity `PP` to a language baseline (e.g. `PP = 12` for high-level languages), collapsing it to a single-variable function of git-derived KSLOC.

## Assessment

Both COCOMO II and the flattened Putnam model can be driven purely from git-derived KSLOC and rest on publicly documented, citable constants (the USC COCOMO II 2000 constants; Putnam's Rayleigh framework). The source's own comparison highlights the distinction relevant to an automated git pipeline: COCOMO II's near-linear size exponent (`Size^E`, `E ≈ 1.01–1.2`) versus Putnam's cubic exponent (`Size^3`), which amplifies the effect of code-churn outliers — large refactors or automated dependency bumps captured in a diff — on the estimate. The source concludes in favor of COCOMO II for a zero-touch git estimator, citing its more stable, defensible scaling; that conclusion is the source's, reported here as content, not a catalog recommendation.

## Security

Pure conceptual/reference material — mathematical models and formulas, with no code, no installation surface, and no network calls. COCOMO II's constants originate from public USC academic work and the Putnam/Rayleigh framework is public-domain mathematics; no license artifact accompanies this content, so `license` is recorded as unknown. No `security_flags` apply.