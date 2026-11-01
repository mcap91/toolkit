---
name: paperbanana
title: PaperBanana
url: "https://github.com/dwzhu-pku/PaperBanana"
category: framework
summary: "Reference-driven multi-agent framework for automated academic illustration — five specialized agents (Retriever, Planner, Stylist, Visualizer, Critic) transform method descriptions and figure captions into publication-quality diagrams and plots via in-context learning, style guidelines, and iterative critic refinement; Gradio/Streamlit UIs, CLI, ClawHub skill; Google Research origin, Apache-2.0 (Google patents on core workflows restrict commercial use)"
tags: [academic-illustration, multi-agent, image-generation, vlm, scientific-figures, in-context-learning, gradio, streamlit, research-tools]
reviewed: 2026-09-03
acquired: 2026-09-03
license: Apache-2.0
security_flags: [patent-restricted-commercial]
overlaps: []
source: unknown
---

## What it does

PaperBanana automates the generation of academic illustrations (conceptual diagrams and data plots) from scientific text. Given a method section and figure caption, it produces publication-quality diagrams through a five-agent pipeline:

1. **Retriever Agent**: finds the most relevant reference diagrams from a curated collection to guide downstream agents via in-context learning
2. **Planner Agent**: translates method content and communicative intent into comprehensive textual descriptions using retrieved examples
3. **Stylist Agent**: refines descriptions to adhere to academic aesthetic standards using automatically synthesized style guidelines
4. **Visualizer Agent**: transforms textual descriptions into visual outputs using image generation models (Gemini, OpenRouter, OpenAI)
5. **Critic Agent**: forms a closed-loop refinement mechanism with the Visualizer through multi-round iterative improvements

Multiple experiment modes available: vanilla (direct generation), dev_planner, dev_planner_stylist, dev_planner_critic, dev_full (all agents). Supports parallel candidate generation (up to 20 simultaneously) with batch export.

## Differentiators

- Reference-driven approach — retrieves similar published diagrams to guide generation rather than generating from scratch
- Five-agent pipeline with iterative Critic-Visualizer refinement loop
- Automatically synthesized style guidelines for academic aesthetic consistency
- Hosted on Hugging Face Spaces for zero-setup use
- Available as a ClawHub skill (`clawhub install paperbanana`)
- Supports multiple VLM backends via OpenRouter (OpenAI, Anthropic, Google) and direct Gemini API
- PaperBananaBench benchmark dataset included for evaluation
- Active community with Chinese-enhanced fork (PaperBanana-Pro) and related tools (AutoFigure-Edit, Paper2Any, Edit-Banana)

## Mechanical details

- Language: Python 3.12, managed with uv
- APIs: Google Gemini (generation + image), OpenRouter (multi-provider), OpenAI (image generation)
- UIs: Gradio web app (`app.py`), Streamlit interactive demo (`demo.py`), CLI (`main.py`)
- Configuration: YAML config file (`configs/model_config.yaml`) for API keys, model selection, defaults
- Dataset: PaperBananaBench with diagram and plot tasks, reference images, and evaluation ground truth
- Image resolution: maps figure size to 1K/2K/4K for Gemini/OpenRouter; OpenAI uses fixed-size API
- Evaluation: built-in evaluation framework with multiple metrics against ground truth
- Originally open-sourced under Google Research as PaperVizAgent; forked and maintained independently

## Security

- Apache-2.0 license, but Google patents cover the core workflows — restricts third-party commercial applications
- API keys stored in gitignored YAML config file
- No eval() or shell injection patterns observed
- Not an officially supported Google product; not eligible for Google OSSVR Program
- Research-oriented; single primary maintainer with community contributors