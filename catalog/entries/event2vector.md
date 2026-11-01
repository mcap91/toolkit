---
name: event2vector
title: Event2Vector (event2vec)
url: https://github.com/sulcantonin/event2vec_public
category: framework
summary: Python/PyTorch library for interpretable, composable embeddings of discrete event sequences — learns one vector per event type and represents a sequence as the composition (vector sum under the linear additive hypothesis) of its events, so trajectories support word2vec-style arithmetic; geometries include Euclidean, hyperbolic (Möbius addition), spherical, stereographic, rotation, Heisenberg, affine, and product; scikit-learn-style fit/transform/most_similar API; `pip install event2vector`; MIT; paper in PMLR vol. 282 (arXiv:2509.12188)
tags:
  - embeddings
  - event-sequences
  - representation-learning
  - pytorch
  - scikit-learn-api
  - hyperbolic-geometry
  - interpretability
  - clickstream
  - sequence-modeling
  - python
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps: []
license: MIT
security_flags:
  - single-maintainer
  - small-community
source: unknown
---

## What it does

Event2Vector learns embeddings for sequences of discrete events (clickstreams, shopping baskets, logs, user journeys, agent decision traces). Each event type gets a vector, and a whole sequence is represented by composing those vectors with a simple additive recurrent structure. The training objective — the paper's main contribution — makes representations compositionally sequential rather than only contextually similar, so sequence embeddings can be composed and decomposed with vector arithmetic (e.g. the author's shopping-data analogy: E(coffee) − E(instant_foods) + E(cereal) → seltzer/juice). The paper positions it as unifying order (as RNNs capture) and context (as word2vec captures) in a geometrically interpretable model.

## Mechanical details

- Install: `pip install event2vector` (Python 3.9+, PyTorch 1.13+).
- API mirrors scikit-learn: `Event2Vec(num_event_types=..., embedding_dim=..., geometry="euclidean", pad_sequences=True, num_epochs=..., random_state=...)` with `fit`, `fit_transform`, `transform`, and `most_similar(positive=..., topn=...)`, usable inside sklearn pipelines.
- Geometries: Euclidean (vector addition), hyperbolic (Möbius addition, for hierarchical data), stereographic, spherical, rotation, Heisenberg, affine (`x ↦ exp(M_e)x + v_e`, events act on the history — added in the 0.4.x line after Reddit feedback), and product geometries.
- Paper: A. Sulc, "Event2Vec: A Geometric Approach to Learning Composable Representations of Event Sequences," NeurIPS 2024/2025 Workshops on Symmetry and Geometry in Neural Representations, PMLR 282:492–512; preprint arXiv:2509.12188. Project site event2vec.com lists v0.6.0.
- Repo: pytest test suite and CI present; ~45 stars, ~49 commits.

## Usage notes

- r/learnmachinelearning thread (post since deleted by author): commenters proposed conditioning each event on accumulated history (`h_t = h_{t-1} + f(e_t, h_{t-1})`), which the author handled via the affine geometry to preserve linear compositionality; others planned to use it for mid-execution failure-probability estimation in agent task orchestration and next-best-action modeling. Critiques compared it to an RNN or graph embeddings; the author's distinction is the enforced linear composition of sequences.

## Security

MIT. Pure-Python/PyTorch library with tests and CI; single primary maintainer and small user base. No network or credential handling observed.
