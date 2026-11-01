---
name: drevalpy
title: DrEvalPy
url: "https://github.com/daisybio/drevalpy"
category: framework
summary: "Python cancer cell line drug response prediction benchmark suite — maintained baseline model catalog, gold standard datasets (CTRPv2, GDSC1/2, CCLE, BeatAML2), application-driven evaluation splits (LPO/LCO/LDO/LTO), ablation studies, cross-study generalization, nf-core Nextflow pipeline; Nature Comms published, TUM/FU Berlin"
tags: [drug-response, cancer, benchmarking, nextflow, bioinformatics]
reviewed: 2026-06-22
acquired: 2026-06-22
license: GPL-3.0-only
security_flags: []
overlaps: []
source: unknown
---

## What it does

Standardized evaluation framework for cancer drug response prediction models. Handles the full experimental loop: dataset download, preprocessing, model training, cross-validation with biologically meaningful splits, ablation/permutation testing, cross-study generalization, and paper-ready HTML reports.

Key features:
- **Model catalog**: maintained baselines (NaivePredictor, ElasticNet, RandomForest, SimpleNeuralNetwork, GradientBoosting, SRMF, DIPK, SuperFELTR, MultiViewRandomForest/NeuralNetwork) — no need to reimplement literature models
- **Datasets**: CTRPv2, CTRPv1, CCLE, GDSC1, GDSC2, BeatAML2, PDX_Bruna, plus toy datasets
- **Splitting strategies**: Leave-Pair-Out (LPO), Leave-Cell-Line-Out (LCO), Leave-Drug-Out (LDO), Leave-Tissue-Out (LTO) — tests real prediction scenarios
- **Ablation**: permutation tests (SVRC/SVRD) and invariant ablation to verify feature contributions
- **Measures**: LN_IC50, pEC50, AUC
- **Pipeline**: nf-core/drugresponseeval Nextflow pipeline for HPC reproducibility
- **Hyperparameter tuning**: optional Ray Tune integration for parallel tuning
- **Reports**: `drevalpy-report` generates interactive HTML with comparison visualizations

## Assessment

Directly relevant to bioinformatics — this is the kind of benchmark framework an agent could use to evaluate drug response models rigorously. The nf-core Nextflow integration makes it HPC-ready. Published in Nature Communications gives strong credibility. The flexible model interface (`MODEL_FACTORY`) makes it straightforward to register new models and benchmark against maintained baselines.

The cross-study evaluation capability (train on CTRPv2, test on GDSC/BeatAML/PDX) is particularly valuable for assessing real-world generalization beyond the typical single-dataset leaderboard.

## Mechanical details

- Install: `pip install drevalpy` (or `drevalpy[multiprocessing]` for Ray Tune)
- Docker: `ghcr.io/daisybio/drevalpy:main`
- CLI: `drevalpy --run_id <id> --models <...> --dataset_name <...> --test_mode <...>`
- Python API: `drug_response_experiment()` for programmatic use
- Reports: `drevalpy-report --run_id <id> --dataset_name <...>` → `index.html`
- Nextflow: `nextflow run nf-core/drugresponseeval -profile docker --run_id <...>`
- Results stored in `results/<run_id>/<dataset>/<test_mode>/`
- Custom models: implement the model interface, register in `MODEL_FACTORY`

## Security

- **License**: GPL-3.0-only (copyleft — modifications must be distributed under GPL)
- **Academic provenance**: TUM + FU Berlin collaboration, Nature Communications publication
- **Dependencies**: standard scientific Python (numpy, pandas, scikit-learn, pytorch); Ray Tune optional
- **Data**: downloads public pharmacogenomics datasets to local `data/` directory
- **Docker**: official GHCR image available
- **Maintenance**: active development, nf-core pipeline integration indicates community review standards