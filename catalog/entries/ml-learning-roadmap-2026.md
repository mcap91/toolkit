---
name: ml-learning-roadmap-2026
title: Machine Learning Learning Roadmap (2026)
category: reference
summary: "Comprehensive practitioner/professor-authored learning path for ML — 5 stages totaling ~25-35 weeks at 8-10 hrs/week: Python (3-5w), math (6-10w, 6 sub-tracks from linear algebra to information theory), PyTorch (2w), ML foundations (10-14w, 5 units from perceptrons to evaluation), then specialization (NLP/CV/RL); emphasizes concept ordering as the primary blocker, spaced repetition for retention, and exercises over passive consumption"
tags: [learning, education, machine-learning, roadmap, python, pytorch, linear-algebra, probability, deep-learning, curriculum]
reviewed: 2026-09-25
acquired: 2026-09-25
license: N/A
security_flags: []
overlaps: []
source: unknown
---

## What it does

Structured ML curriculum authored by a visiting NLP professor (r/learnmachinelearning, Sep 2026). ~350 concepts across 5 stages, ordered to prevent the "hit a concept that assumed three others you skipped" stall.

**Stage 1: Python (3-5 weeks)** — ML-relevant slice: environments, data structures, comprehensions/generators, classes (nn.Module), type hints, file I/O, debugging.

**Stage 2: Math (6-10 weeks)** — 6 sub-tracks: mathematical toolkit/notation (1w), linear algebra (3w, 5 units through SVD/tensors), calculus and optimization (2w, through backprop and saddle points), probability and statistics (3w, 6 units through MCMC and bootstrap), information theory (3d), numerical computation (2d, floating-point, log-sum-exp, EMA).

**Stage 3: PyTorch (2 weeks)** — Tensor library before models. Autograd, broadcasting, devices, reproducibility.

**Stage 4: ML Foundations (10-14 weeks)** — 5 units: single neuron to classifier, deep neural networks, training that works (optimizers, scheduling, checkpointing), generalization (regularization, double descent), evaluation and diagnostics.

**Stage 5: Specialization** — NLP (tokenization → transformers), CV (convolutions → detection), RL, etc.

**Key pedagogical claims:** Concept ordering is the primary blocker; spaced repetition is the retention mechanism; writing code from scratch (not just reading) is required for concepts used weekly.

## Assessment

Useful as a background-knowledge reference when assessing catalog tools that target ML practitioners at different levels. The concept inventory maps well to prerequisite knowledge for tools in the catalog (e.g., quantization tools assume Stage 2 Unit 4 linear algebra, fine-tuning tools assume Stage 4).