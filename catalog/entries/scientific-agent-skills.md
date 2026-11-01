---
name: scientific-agent-skills
title: Scientific Agent Skills (K-Dense)
url: "https://github.com/K-Dense-AI/scientific-agent-skills"
category: plugin
summary: "Scientific Agent Skills is a library of 163 curated Agent Skills that turn AI coding agents into scientific research assistants, spanning bioinformatics/genomics, cheminformatics/drug discovery, clinical research, ML/AI, scientific databases, and lab automation, each scanned with the Cisco AI Defense Skill Scanner"
tags: [agent-skills, scientific-computing, bioinformatics, cheminformatics, drug-discovery, clinical-research, lab-automation, multi-domain, claude-code-plugin]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

Scientific Agent Skills is a comprehensive Agent Skills library that transforms AI coding
agents into scientific research assistants. It provides 163 curated skills across multiple
scientific domains, each with documentation, code examples, and best practices.

Key domains covered:

- **Bioinformatics & Genomics (27 skills):** Scanpy, BioPython, pysam, scvi-tools, scVelo,
  PyDESeq2, gget, population genomics (OneKGPd), pathogen surveillance
- **Cheminformatics & Drug Discovery (10 skills):** RDKit, Datamol, DeepChem, DiffDock,
  OpenMM/MDAnalysis, MedChem, PyTDC
- **Clinical Research (8 skills):** PK/PD modeling, DepMap, clinical reports, decision support
- **ML & AI (14 skills):** PyTorch Lightning, scikit-learn, SHAP, PyMC, TimesFM
- **Scientific Databases (11 skills, 100+ databases):** Unified database-lookup for PubChem,
  ChEMBL, UniProt, ClinVar, COSMIC, ClinicalTrials.gov, KEGG, Reactome, and 70+ more
- **Lab Automation (6 skills):** Opentrons, PyLabRobot, Benchling, Ginkgo Cloud Lab
- **Scientific Communication (27 skills):** Literature review, Paperclip, scientific writing

## Installation

```bash
# npx (cross-host)
npx skills add K-Dense-AI/scientific-agent-skills

# GitHub CLI
gh skill install K-Dense-AI/scientific-agent-skills

# Manual
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git ~/.claude/skills/scientific-agent-skills
```

Also installable as an Agent Plugins 1.0 package for Cursor, Codex, and other plugin clients.

## Security

All skills scanned with Cisco AI Defense Skill Scanner. Security report published to
`docs/security-report.md`. Per-skill licenses specified in each SKILL.md frontmatter —
review individually.