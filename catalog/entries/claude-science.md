---
name: claude-science
title: Claude Science
url: "https://www.anthropic.com/news/claude-science-ai-workbench"
category: framework
summary: "Anthropic's AI workbench for scientists — generalist coordinating agent with 60+ curated skills for genomics/proteomics/structural-biology/cheminformatics, native 3D molecular rendering, HPC/GPU compute management via Modal, reviewer agent for citation/calculation checking, NVIDIA BioNeMo integration (Evo 2, Boltz-2, OpenFold3); runs on existing Claude models; Pro/Max/Team/Enterprise beta"
tags: [scientific-computing, genomics, proteomics, structural-biology, cheminformatics, single-cell, hpc, anthropic, claude, bioinformatics]
reviewed: 2026-07-01
acquired: 2026-07-01
license: Proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it does

Claude Science is an AI workbench from Anthropic launched June 30, 2026 that integrates scientific tools and packages into a single research environment. Runs on existing Claude models (including Opus 4.8) — not a new model, but a new application layer. A generalist coordinating agent with 60+ curated skills handles multi-step research across genomics, single-cell analysis, proteomics, structural biology, and cheminformatics. Available in beta for Pro, Max, Team, and Enterprise plans on macOS and Linux.

Scientists interact conversationally — the agent queries databases, executes analyses, generates figures, and drafts manuscripts. A separate reviewer agent checks citations and calculations, flagging and correcting errors. Competitive landscape includes OpenAI's GPT-Rosalind (fine-tuned for biological reasoning, April 2026) and Google DeepMind's Gemini for Science (May 2026).

## Differentiators

- **Native scientific rendering**: 3D protein structures, genome browser tracks, chemical structures, and publication-quality figures displayed directly; figures editable via plain-language instructions
- **Auditable artifacts**: Every generated figure includes exact code, environment, plain-language description, and full message history — designed for reproducibility validation months later
- **Compute management**: Handles job submission to local laptops, HPC clusters via SSH, or on-demand GPUs via Modal — scales from single GPU to hundreds; data stays on lab infrastructure
- **BioNeMo integration**: Connects to NVIDIA's BioNeMo Agent Toolkit for Evo 2, Boltz-2, and OpenFold3 models
- **Multi-agent architecture**: Coordinator spawns specialist agents; actor-critic pattern (content agent + reviewer agent) validates accuracy and citation fidelity
- **Session forking**: Fork at any point to compare approaches without losing the original thread
- **Database connectors**: Pre-configured for UniProt, PDB, Ensembl, Reactome, ClinVar, ChEMBL, GEO, journals, and preprint servers

## Mechanical details

Runs locally on macOS or Linux, or on remote machines via SSH/HPC login nodes. Datasets load once into a running session. Only per-step context is sent to Claude — large/sensitive datasets stay local. Custom pipelines saved as reusable skills; future sessions inherit them.

Grant program: up to 50 projects supported with $30K credits each + $2K Modal compute. Applications open through July 15, 2026; projects run September 1–December 1, 2026. Discounted Team plan seats for academic labs and nonprofit research organizations.

## Security

Proprietary Anthropic product. Data stays on local infrastructure — only per-step context sent to Claude. Requires Claude subscription. No open-source code to audit.