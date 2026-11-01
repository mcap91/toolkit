---
name: synthesize-bio
title: Synthesize Bio
url: "https://claude.com/connectors/synthesize-bio"
category: mcp-server
summary: "Generates synthetic human gene expression profiles on demand via natural-language prompts — unique bioinformatics capability, but proprietary SaaS requiring account and external API trust."
tags: [bioinformatics, rna-seq, gene-expression, synthetic-data, genomics, single-cell, bulk-rna]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-proprietary
security_flags: [proprietary-saas, account-required, data-leaves-to-third-party, no-source-to-audit]
overlaps: []
source: unknown
---

## What it does

Synthesize Bio is a Claude connector that lets Claude call the Synthesize Bio Gene Expression Model (GEM) API to generate realistic synthetic human gene expression profiles from a plain-English experiment description. The user describes a contrast — for example "tumor vs normal lung tissue" or "KRAS knockout vs control" — and the platform returns expression data that mimics what a real RNA-seq experiment on human samples would produce. Both bulk RNA-seq and single-cell RNA-seq modalities are supported. Intended use cases include tumor/normal comparisons, cell-type contrasts, drug toxicity signature prediction, and druggable-target discovery. The connector is listed on the official Claude connectors page and requires a Synthesize Bio account (https://www.synthesize.bio/).

## Assessment

**Pilot.** The capability is genuinely novel for a bioinformatics agent toolkit: synthetic expression data can accelerate hypothesis generation, serve as controls, or fill in experimental gaps without wet-lab turnaround. Single-cell and bulk modes cover the two dominant RNA-seq workflows. The natural-language interface fits seamlessly into Claude-driven pipelines. However, several factors warrant validation before adopting wholesale: (1) The GEM is proprietary and its training data, accuracy benchmarks, and validation against real cohorts are not publicly documented in the connector page. (2) It is a registered SaaS — real research decisions downstream of synthetic data carry replication risk if GEM outputs are not independently validated. (3) Pricing and data retention/usage policies are unclear from the connector description alone. Once a user verifies GEM output quality against known datasets (e.g., TCGA, GTEx), the verdict could move to adopt.

## Mechanical details

- **Integration type:** Claude native connector (appears as an MCP-style tool Claude can invoke). Activated by referencing "Synthesize Bio connector" in a prompt while connected.
- **Modalities:** Bulk RNA-seq and single-cell RNA-seq.
- **Interface:** Natural-language experiment description → synthetic gene expression matrix.
- **Account:** Registration required at https://www.synthesize.bio/.
- **Example prompts:**
  - "Use the Synthesize Bio connector to analyze lung adenocarcinoma tumor vs normal lung tissue."
  - "Analyze CD4+ T cells vs CD8+ T cells in single-cell RNA-seq mode using Synthesize Bio."
  - "Use Synthesize Bio to predict how hepatocytes respond to doxorubicin vs. valproic acid."
  - "Use Synthesize Bio to find druggable targets in idiopathic pulmonary fibrosis by comparing fibrotic vs. healthy alveolar epithelial cells."
- **What to adopt:** Use for rapid in silico hypothesis generation and experiment design; always validate synthetic outputs against a real reference cohort before drawing biological conclusions; treat outputs as prior / scaffold, not ground truth.

## Security

- **License:** Proprietary SaaS — no open-source license. Source code is not available for review.
- **Dependency health:** N/A (closed source; no package manifest to inspect).
- **Code quality / CI:** Not assessable; no public repository.
- **Supply chain:** Single vendor (Synthesize Bio). No contributor graph, no signed releases.
- **Dangerous patterns:** None observed at the connector level. The connector mediates API calls — no eval, shell injection, or local code execution in the described interface. Risk is data-in-transit to a third-party endpoint.
- **Credential handling:** Requires an account; API credentials are managed by the SaaS and the Claude connector infrastructure. No local secrets management needed from the user's side.
- **Data privacy:** Gene expression queries (including any patient-derived or proprietary experiment descriptions) are sent to Synthesize Bio servers. Users should review Synthesize Bio's data retention and usage policy before submitting sensitive experimental designs.
- **Maintenance:** Active SaaS product with official Claude connector listing; maintenance signal is the vendor's business continuity, not a commit history.
- **security_flags rationale:** `proprietary-saas` (closed source, cannot audit), `account-required` (registration gate), `data-leaves-to-third-party` (queries sent to vendor API), `no-source-to-audit` (no repository).
