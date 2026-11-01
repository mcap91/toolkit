---
name: askcos
title: ASKCOS
url: "https://github.com/ASKCOS/ASKCOS"
category: framework
summary: "ASKCOS is an integrated platform for computer-aided synthesis planning that combines ML models for retrosynthetic analysis, forward reaction prediction, reaction condition recommendation, synthetic complexity scoring, and fast reaction plausibility filtering; code is MPL-2.0, data/models are CC BY-NC-SA (noncommercial)"
tags: [synthesis-planning, retrosynthesis, forward-prediction, reaction-conditions, scscore, drug-discovery, cheminformatics, casp, docker]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [aizynthfinder]
license: MPL-2.0
security_flags: []
source: unknown
---

## What it does

ASKCOS (Automated Synthesis Knowledge for Chemical Operations and Synthesis) is an
integrated platform for computer-aided synthesis planning. It combines multiple ML models
for different aspects of synthetic route design:

- **Retrosynthetic analysis:** Template-based transformer that suggests single-step
  precursors with chirality consideration
- **Forward prediction:** Template-free model for predicting reaction outcomes
- **Reaction conditions:** Neural network model recommending reagents, solvents, temperature
- **Synthetic complexity (SCScore):** Learned metric for prioritizing precursors
- **Fast filter:** Binary classifier for quick reaction plausibility screening
- **Integrated CASP:** Tree search combining all modules for multi-step route planning

## Architecture

Docker-deployed web application with:
- Django web frontend
- Celery workers for async ML inference (scalable per queue)
- Database services seeded with buyables, reaction templates, and chemical data
- Recommended: 8–16 cores, 64–128 GB RAM

## Current Status

This repository (v0.4.1) is archived. Active development continues as ASKCOSv2 at
`gitlab.com/mlpds_mit/askcosv2/askcos2_core`, split into modular repositories.

## Deployment

```bash
git clone https://github.com/ASKCOS/ASKCOS
cd ASKCOS && git lfs pull
docker build -t askcos/askcos .
cd deploy && bash deploy.sh deploy
```

Individual modules (SCScore, retro transformer, forward predictor, fast filter) can also
run standalone via their `__main__` blocks.

## License

Code: MPL-2.0. Data and trained models: CC BY-NC-SA (noncommercial use only).