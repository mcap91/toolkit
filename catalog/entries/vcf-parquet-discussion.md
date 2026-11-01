---
name: vcf-parquet-discussion
title: VCF vs Parquet for Genomic Variants (Reddit Discussion)
url: "https://reddit.com"
category: reference
summary: "Former VCF spec maintainer explains why VCF persists: the real problem is representing complex variation (SVs, translocations, ploidy changes), not the container format — Parquet wouldn't solve schema complexity; VRS is the ongoing effort"
tags: [vcf, parquet, genomic-variants, file-formats, bioinformatics, vrs, ga4gh]
reviewed: 2026-06-17
acquired: 2026-06-17
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---

## What it says

A Reddit discussion where a former VCF specification maintainer explains why VCF remains the dominant format for variant data despite its quirks, and why switching to Parquet as a container wouldn't solve the fundamental problems. Key points from the maintainer:

1. **VCF isn't the actual problem.** The real challenge is consistently representing complex variation (inversions, translocations, structural variants, ploidy changes, variants-inside-variants). No one has fully solved this.

2. **Simple variation works fine in VCF.** For SNPs and short indels, VCF is adequate. De/serialization is rarely the pipeline bottleneck. Libraries exist for every language.

3. **Complex variation defies clean schemas.** Even the GA4GH Variation Representation Specification (VRS), which aims for a general schema for arbitrarily complex variation, becomes extremely complex as it approaches generality.

4. **Bioinformatics rarely deals with exact variants.** What VCF actually contains is *evidence for variants* based on upstream experiments, with associated uncertainty (breakpoint imprecision, genotype probabilities). This distinction matters for complex variation.

5. **Graph genomes haven't replaced linear representations** despite a decade of development, because they're too complex to be drop-in replacements for the hundreds of downstream tools expecting simple chr-pos-ref-alt input.

6. **Opposing requirements**: comprehensive representation vs. simple observation-feature matrices for downstream analysis (including ML). VCF is a compromise.

## Assessment

This is a high-quality primary-source explanation from someone who participated in VCF spec development and GA4GH discussions. The core insight — that the problem is biological representation complexity, not file format inefficiency — is foundational context for anyone working with genomic variants or considering format modernization.

Directly relevant for bioinformatics agent workflows that handle VCF data: understanding *why* VCF exists as it does prevents wasting effort on format-swap projects that don't address the real bottleneck.

## What to adopt

- Use as context when evaluating tools that claim to "replace VCF" — check whether they actually solve the schema problem or just change the container
- VRS (GA4GH Variation Representation Specification) is the current active effort toward a general variation schema — worth tracking
- Graph genomes are useful research tools but not pipeline replacements

## Security

Not applicable — discussion content, no installable software.