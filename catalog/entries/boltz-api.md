---
name: boltz-api
title: Boltz API (BoltzMol-1 / BoltzProt-1)
url: "https://boltz.bio/boltzmol-boltzprot-api"
category: framework
summary: "Boltz's biomolecular design API — BoltzMol-1 (small-molecule hit discovery, 6/10 targets with <51 compounds each) and BoltzProt-1 (de novo nanobody design, 3x hit rate over BoltzGen); $0.025/prediction, Python/JS SDKs, first-party Claude Code integration"
tags: [drug-discovery, protein-design, structure-prediction, api, nanobody, small-molecule, bioinformatics]
reviewed: 2026-06-19
acquired: 2026-06-19
license: Proprietary
security_flags: [proprietary-saas, api-key-required]
overlaps: []
source: unknown
---

## What it does

Commercial API serving three Boltz models for biomolecular design:

- **BoltzMol-1**: small-molecule hit discovery pipeline — ranks buyable compounds or generates from 74B make-on-demand space; confirmed hits on 6/10 challenging targets testing only 28-51 compounds per target; includes ADME property models
- **BoltzProt-1**: protein design pipeline — de novo nanobody design with Boltz-PPI scoring model; nearly 3x hit rate over BoltzGen; 58% of binders pass stringent developability panel
- **Boltz-2**: biomolecular structure and affinity prediction (previously released)

API-first design with Python and JavaScript SDKs, plus first-party integrations for Claude Code, Codex, and Gemini CLI. Designed for agentic workflows — the Boltz team uses it from agents on laptops to orchestrate large compute experiments.

## Assessment

Frontier biomolecular AI with experimental validation that goes well beyond in-silico benchmarks. The hit-discovery results (6/10 targets, <51 compounds each, $10-15k per campaign vs millions for traditional HTS) represent a genuine capability shift for drug discovery.

The Claude Code integration makes this directly usable in agent-driven research pipelines. At $0.025/prediction, the API is priced below self-hosting the open-source models.

Key caveats: proprietary SaaS requiring API key and trust in data handling (they state IP ownership stays with user and inputs/outputs are not used for retraining). Launch credits ($2,000/company, $100/academic) available at launch. Partner integrations with Benchling, Phylo, Amazon Bio Discovery, Rowan, and others extend reach.

## Mechanical details

- **API**: `api.boltz.bio`
- **SDKs**: Python and JavaScript
- **Agent integrations**: Claude Code (first-party), Codex, Gemini CLI
- **Pricing**: from $0.025/prediction, scales to thousands of GPUs
- **IP terms**: user owns all inputs and outputs; no retraining on user data
- **Partners**: Benchling, Phylo, Amazon Bio Discovery, Rowan, Tamarind, Kiin Bio, Pauling.ai, Mirror Physics, Cultivarium

## Security

- **License**: Proprietary SaaS — commercial API
- **Dependencies**: SDK packages only (thin API clients)
- **Data handling**: claims no storage of inputs/outputs for retraining; user retains IP
- **Supply chain**: Boltz (VC-backed biotech company), NVIDIA partnership for inference kernels
- **Dangerous patterns**: none in SDK — standard API client pattern
- **Maintenance**: actively developed; backed by commercial entity with launch events and growing team