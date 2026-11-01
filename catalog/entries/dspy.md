---
name: dspy
title: DSPy
url: "https://dspy.ai/"
category: framework
summary: "Stanford NLP framework for programming (not prompting) LLMs via typed signatures, composable modules, and automatic prompt optimization; 35k stars, 433+ contributors, production use at scale — relevant for building optimized LLM pipelines"
tags: [llm, prompt-optimization, framework, python, signatures, modules, agents, rag, stanford]
reviewed: 2026-06-17
acquired: 2026-06-17
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

DSPy is a Python framework for building AI systems using structured signatures instead of hand-written prompts. Three core primitives:

1. **Signatures** — declare tasks as typed inputs/outputs (e.g., `"question -> answer"` or a class with `InputField`/`OutputField`). Portable across models.
2. **Modules** — control execution strategy without rewriting the task. Same signature can run as `dspy.Predict` (direct), `dspy.ChainOfThought` (step-by-step reasoning), or `dspy.ReAct` (tools + reasoning loop).
3. **Optimizers** — compile a program against a metric and training examples. GEPA (Reflective Prompt Evolution) automatically tunes prompts until quality converges (e.g., 62% → 89% accuracy on the same model).

Also supports multimodal inputs (images), agent pipelines, and composable multi-module programs (e.g., FactCheck = find claims → verify each).

## Assessment

DSPy represents a fundamentally different approach to LLM application development: treating prompts as compilable programs rather than hand-crafted text. The optimizer loop (give examples + metric → auto-tune prompts) is the key differentiator — it makes LLM pipelines reproducible and improvable without manual prompt engineering.

With 6.4M+ monthly downloads, 35k GitHub stars, 433+ contributors, and production use at companies like Databricks, this is a mature, well-maintained framework. The Stanford NLP research backing means new optimization algorithms land here first (GEPA, MIPROv2, BetterTogether).

For this project, DSPy is most relevant if we build structured LLM pipelines for bioinformatics tasks (e.g., extracting structured data from papers, classifying variants, building RAG systems). The signature pattern is cleaner than raw API calls for any multi-step LLM workflow. However, our current stack uses Claude Code's built-in agent patterns and the Anthropic API directly — DSPy adds a layer of abstraction that's most valuable when optimizing across models or when prompt quality needs to be systematically measured and improved.

## Mechanical details

- Install: `pip install dspy`
- Current version: 3.3.0b1
- Model support: OpenAI, Anthropic, and others via LM abstraction
- Key modules: `Predict`, `ChainOfThought`, `ReAct`, `ReActV2`
- Optimizer: `GEPA` (auto="light"|"medium"|"heavy")
- Programs save/load as JSON configs
- Research papers: DSPy (Oct 2023), MIPROv2 (Jun 2024), BetterTogether (Jul 2024), GEPA (Jul 2025), Recursive LMs (Dec 2025)

## Security

- **License**: MIT — no restrictions
- **Supply chain**: Stanford NLP origin, 433+ contributors, active development since Dec 2022. Major corporate production users
- **Maintenance**: Very active — 6.4M+ monthly npm/pip downloads, regular releases
- **Code quality**: Research-grade with production adoption. Well-documented API
- **Dangerous patterns**: `PythonInterpreter` module executes arbitrary code (used for calc tool) — standard for code execution tools, requires sandboxing in production

## Usage notes

- **Minimal program pattern:** `dspy.Predict("subject -> haiku")(subject="x")` — string signatures are parsed into typed input/output fields, auto-generate instructions, and return `Prediction` objects with named attributes. Variable names in the signature double as semantic hints to the model (changing "haiku" to "limerick" changes model behavior and output attribute name).
- **Adapter pipeline:** Signature + inputs → ChatAdapter renders messages (system instructions with field schema + user input) → LLM call (cached by default) → ChatAdapter parses response → Prediction object. Inspect with `dspy.inspect_history(n=1)`.
- **Getting started tutorial:** https://dspy.ai/getting-started/first-program/
