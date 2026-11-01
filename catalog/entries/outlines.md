---
name: outlines
title: Outlines
url: "https://github.com/dottxt-ai/outlines"
category: framework
summary: "Structured generation library by .txt — guarantees LLM outputs conform to JSON Schema, Pydantic models, regex, grammars, or Python types via constrained decoding (FSM-based token masking); works with transformers, llama.cpp, vLLM, Ollama, OpenAI, Gemini; Jinja prompt templates, function calling inference, batch generation; Rust core (outlines-core) for performance; 65M+ downloads; trusted by NVIDIA, Cohere, HuggingFace, vLLM; Apache-2.0"
tags: [structured-generation, constrained-decoding, json-schema, pydantic, regex, grammar, llm, python, rust, vllm, ollama]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [dspy]
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

Outlines is a Python library that guarantees LLM outputs match a specified structure during generation — not after. It uses finite-state machine (FSM) based constrained decoding to mask invalid tokens at each generation step, making it impossible for the model to produce invalid output.

Key capabilities:

- **Type-driven interface**: Specify the desired output type and Outlines enforces it. `model(prompt, int)` returns an integer. `model(prompt, MyPydanticModel)` returns valid JSON matching the schema. `model(prompt, Literal["Yes", "No"])` returns exactly one of those strings.
- **Multiple constraint types**: JSON Schema / Pydantic models, Python `Literal` types, `int`/`float`/`bool`, regular expressions, context-free grammars, and function signatures (infers structure from typed function parameters).
- **Provider-agnostic**: Same code runs across local models (transformers, llama.cpp), inference servers (vLLM, Ollama), and APIs (OpenAI, Gemini, Dottxt). Switch models without changing generation code.
- **Prompt templates**: Jinja-based `outlines.Template` for separating prompt logic from code, supporting few-shot examples and dynamic content.
- **Batch generation**: Pass a list of prompts for batch inference.
- **Union types**: `Union[EventInfo, Literal["I don't know"]]` lets the model return structured data or a fallback, handling incomplete information gracefully.

**How it works:** Outlines compiles the output specification (JSON Schema, regex, grammar) into a finite-state automaton, then at each decoding step masks tokens that would lead to an invalid state. The result is always valid — no parsing, retrying, or defensive code needed.

## Mechanical details

Install via `pip install outlines`. Core FSM algorithms extracted to `outlines-core` (Rust via PyO3, co-developed with Hugging Face) for performance. Negligible latency overhead vs unconstrained generation. Research paper: arXiv:2307.09702 ("Efficient Guided Generation for Large Language Models"). The commercial arm (.txt / Dottxt) offers a hosted API and enterprise self-hosted solutions.

## Security

Apache-2.0 licensed. 65M+ PyPI downloads. Backed by .txt company. Used in production by NVIDIA, Cohere, HuggingFace, vLLM. Pure computation library — no network access or side effects beyond what the underlying model provider requires. Rust core has no unsafe code concerns documented.

## How to use it

pip install outlines
