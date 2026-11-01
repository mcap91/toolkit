---
name: ggwas
title: ggwas
url: "https://github.com/bczech/ggwas"
category: framework
summary: "Modern ggplot2 GWAS visualization R package — 17 plot types (Manhattan, QQ, Miami, PheWAS, colocalization, fine-mapping, genetic correlations, karyogram, enrichment), journal themes (Nature/Science/Cell/PLOS), smart downsampling for 10M+ variants, auto-detects PLINK/REGENIE/GCTA/GEMMA; MIT"
tags: [gwas, visualization, r-package, ggplot2, manhattan-plot, bioinformatics, genomics, publication-ready]
reviewed: 2026-06-25
acquired: 2026-06-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

R package for publication-ready GWAS visualizations built on ggplot2. 17 plot types covering the full GWAS-to-post-GWAS analysis pipeline:

- **Core**: Manhattan (with broken y-axis for extreme p-values), QQ (with CI and lambda), Miami (discovery vs replication), locus zoom (with LD and gene track)
- **Novel**: circular Manhattan (multi-ring), enrichment Manhattan, multi-trait Manhattan (pleiotropy overlay), p-value heatmap, effect-size volcano, SNP density karyogram, density-vs-signal, GWAS summary dashboard
- **Post-GWAS**: PheWAS, colocalization, fine-mapping (PIP/SuSiE), genetic correlation (LDSC), architecture plot

Auto-detects column names from PLINK (.assoc/.linear/.logistic), REGENIE, GCTA MLMA, GEMMA, and generic files. Smart downsampling preserves all significant variants while binning non-significant background — renders 10M+ variant datasets in seconds (up to 8.8x faster than qqman). 6 journal themes (Nature, Science, Cell, PLOS, presentation, poster) and 14 colorblind-safe palettes.

Every function returns a composable ggplot object — standard ggplot2 layering, faceting, and theming all work.

## Assessment

Directly relevant to bioinformatics workflows. Fills a major gap — qqman (the current standard) offers only Manhattan and QQ plots with no ggplot2 composability, no post-GWAS visualizations, no journal themes, and no smart downsampling. CMplot adds circular Manhattan but uses base R graphics. ggwas provides all of these plus 10 novel plot types not available in any existing package.

The performance benchmarks are notable: 8.8x faster than qqman on 1.37M variants via intelligent downsampling that preserves visual fidelity. The auto-detection of input formats (PLINK, REGENIE, GCTA, GEMMA) eliminates boilerplate column mapping.

DOI-registered (Zenodo 10.5281/zenodo.20815110), version 0.99.2. Single contributor (Czech B, 2026). MIT license. Documentation site with worked examples at bczech.github.io/ggwas/.

Strong candidate for adoption in any GWAS analysis pipeline. The gene annotation feature (automatic nearest-gene mapping, arrow labels on peaks) and region highlighting (e.g., MHC) are particularly useful for manuscript figures.

## Mechanical details

- Install: `pak::pak("bczech/ggwas")`
- Read data: `read_gwas_table()` auto-detects, or format-specific readers
- All plot functions return ggplot objects — layer with `+`
- Journal presets: `+ theme_nature()`, `+ theme_science()`, etc.
- Gene annotation: `manhattan_genes(gwas, genes = gene_table)`
- Top hits: `top_hits(gwas, genes = gene_table, p_threshold = 5e-8)`

## Security

MIT license. Pure R visualization package with no network calls, no code execution beyond ggplot2 rendering. Standard CRAN-style dependencies. No security concerns.