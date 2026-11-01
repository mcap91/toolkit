---
name: bdh
title: BDH (Dragon Hatchling)
url: "https://github.com/pathwaycom/bdh"
category: framework
summary: "Post-transformer neural architecture from Pathway — biologically inspired sparse graph of neuron-like nodes with Hebbian working memory, scale-free topology, and GPU-friendly state-space formulation; matches GPT-2-scale transformers at 10M-1B parameters with interpretable activations; 97.4% on Sudoku Extreme (internal implementation) without chain-of-thought; runs on NVIDIA AI infrastructure and AWS"
tags: [neural-architecture, post-transformer, neuroscience, sparse-networks, hebbian-learning, interpretability, reasoning]
reviewed: 2026-07-01
acquired: 2026-07-01
license: unlicensed
security_flags: [no-stated-license]
overlaps: [nanogpt]
source: unknown
---

## What it does

BDH (Brain Dragon Hatchling) is a biologically inspired LLM architecture that replaces dense self-attention with a sparse graph of neuron-like nodes connected by weighted synapses. Developed by researchers at Pathway.

Computation proceeds through repeated cycles of local processing: active nodes propagate evidence to neighbors, synaptic connections strengthen through Hebbian learning, and only the strongest activations survive via competitive selection. Unlike transformers whose weights are fixed during inference, BDH continuously updates its synaptic state during processing — memory lives in the synapses, supporting theoretically unbounded context under linear-complexity constraints.

The modular structure of the neuron network emerges spontaneously during training rather than being engineered into blocks.

## Differentiators

- **Biologically grounded**: Scale-free network topology mimicking biological connectivity, excitatory/inhibitory neuron dynamics, Hebbian working memory with monosemantic activations resembling neocortex behavior
- **Interpretable by design**: Activations are sparse and positive — interpretability of state is an inherent architectural property, not a post-hoc analysis
- **Linear-time inference**: Bounded memory usage and linear-time inference vs quadratic attention; no external caches needed
- **Sudoku Extreme**: 97.4% accuracy on ~250,000 difficult puzzles without chain-of-thought, backtracking, or external tools (internal Pathway implementation — not reproducible from open-source repo); leading LLMs score ~0%
- **Transformer-compatible scaling**: Follows transformer-like scaling laws at 10M-1B parameter range, matching GPT-2 performance on language and translation tasks
- **Industry recognition**: Wall Street Journal named Pathway alongside LeCun, Sutskever, and Li for post-transformer architectures; runs on NVIDIA AI infrastructure and AWS

## Mechanical details

Install: `pip install -r requirements.txt`, train with `python train.py` on a toy dataset. Based on Karpathy's nanoGPT codebase and tiny Shakespeare dataset for demonstration. The open-source repo contains the baseline variant; the 97.4% Sudoku result is from Pathway's internal implementation.

Community ports: MLX (severian42/bdh), Burn (mosure/burn_dragon_hatchling), dynamic vocabulary (adamskrodzki/bdh).

Paper: "The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain" (arXiv 2509.26507). Featured on SuperDataScience podcast, Forbes, Semafor, Turing Post.

## Security

No stated SPDX license in the repository. Research code from Pathway (commercial company). Sudoku benchmark claims based on internal implementation, not public code. Small contributor base (Pathway research team).