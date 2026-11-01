---
name: applied-ml
title: Applied ML
url: "https://github.com/eugeneyan/applied-ml"
category: reference
summary: "Curated collection of ~400+ papers and engineering blog posts on data science & ML in production, maintained by Eugene Yan — organized by company (Airbnb, Uber, Netflix, Amazon, LinkedIn, etc.) and by application area (recommendation, search & ranking, feature stores, MLOps platforms, A/B testing, NLP, computer vision, and more)"
tags: [ml-in-production, curated-list, engineering-blogs, papers, mlops, case-studies, recommendation-systems, search-ranking]
reviewed: 2026-09-25
acquired: 2026-09-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Curated list of papers, articles, and engineering blog posts describing how companies design and operate machine learning systems in production, maintained by Eugene Yan (who also runs ApplyingML.com and the applyingml/ml-surveys repos). The stated purpose is to help practitioners see how other organizations framed a problem, what ML techniques worked (and what didn't), the reasoning/research behind the approach, and the real-world results achieved.

Content is organized into two overlapping structures:

- **By company**: Airbnb, Uber, Netflix, Google, Amazon, LinkedIn, Spotify, DoorDash, Alibaba, Meta/Facebook, Pinterest, Twitter, Shopify, Lyft, Stitch Fix, Gojek, and dozens more.
- **By application area** (table of contents, ~30 sections): Data Quality, Data Engineering, Data Discovery, Feature Stores, Classification, Regression, Forecasting, Recommendation, Search & Ranking, Embeddings, Natural Language Processing, Sequence Modelling, Computer Vision, Reinforcement Learning, Anomaly Detection, Graph, Optimization, Information Extraction, Weak Supervision, Generation, Audio, Privacy-Preserving ML, Validation and A/B Testing, Model Management, Efficiency, Ethics, Infra, MLOps Platforms, Practices, Team Structure, and Fails (post-mortems of ML failures, e.g., Google Photos gorilla-tagging incident, COMPAS-style criminality prediction).

Each list item is a link (paper and/or blog post, sometimes with linked code) tagged with the originating company and year, e.g. "Deep Neural Networks for YouTube Recommendations · YouTube · 2016" or "Applying Deep Learning To Airbnb Search (Paper) · Airbnb · 2018". No summaries or commentary are included in the repo itself — it is purely a link index.

~30k GitHub stars, ~4k forks, 53 contributors, created July 2020. Community-contributed via pull requests following a CONTRIBUTING.md template. Companion resources by the same author: `ml-surveys` (survey papers summarizing ML sub-field advancements) and `applyingml` (guides and mentor interviews on applying ML).

## Assessment

Reference-only resource — not a tool, but a high-signal discovery index for how production ML systems are actually built, with heavy representation of recommendation, search/ranking, and MLOps-platform case studies from large-scale consumer tech companies. Useful when designing agent workflows that touch classic ML system concerns (feature stores, A/B testing infrastructure, model monitoring, ranking) since it points to primary sources (papers and engineering blogs) rather than secondary summaries. Least relevant to bioinformatics-specific work directly, but the MLOps Platforms, Model Management, and Practices sections have general applicability to any ML system design, including ML components in bioinformatics pipelines (e.g., variant classifiers, genomic embedding models).

## Mechanical details

- **Format**: Single README.md, markdown link list grouped under H2 section headers, with a table of contents at the top
- **Scope**: ~400+ individual paper/blog links spanning 2003–2024 publication dates
- **Contribution model**: PRs following `[Title](url) \`Organization\`` format per CONTRIBUTING.md
- **Related repos by same maintainer**: `eugeneyan/ml-surveys`, `eugeneyan/applyingml`

## Security

- **License**: MIT
- **No code to audit** — static markdown link list, no executable content
- **Supply chain**: Standard GitHub PR contribution model; no CI/build pipeline needed since it's documentation-only
- **Maintenance**: Actively maintained, 53 contributors, ongoing additions through 2024
