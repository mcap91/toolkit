---
name: tiktoken
title: tiktoken
url: "https://github.com/openai/tiktoken"
category: cli-tool
summary: "OpenAI's fast BPE tokenizer library — 3-6x faster than HuggingFace tokenizers; supports all OpenAI model encodings (o200k_base, cl100k_base, etc.); Python API for encode/decode, model-to-encoding lookup, custom encoding extension via plugin mechanism; educational submodule for visualizing BPE procedure; MIT"
tags: [tokenizer, bpe, openai, python, nlp, token-counting, encoding]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

tiktoken is a fast Byte Pair Encoding (BPE) tokenizer library by OpenAI, used for tokenizing text into the token sequences that OpenAI's language models consume.

Key capabilities:

- **Model-specific encoding**: `tiktoken.encoding_for_model("gpt-4o")` returns the correct tokenizer for any OpenAI model. Built-in encodings include `o200k_base` (GPT-4o and later), `cl100k_base` (GPT-4/GPT-3.5-turbo), and older encodings.
- **Performance**: 3-6x faster than comparable open-source tokenizers (benchmarked against HuggingFace `tokenizers` on 1GB text).
- **Reversible and lossless**: `decode(encode(text)) == text` for all inputs.
- **Custom encodings**: Extend with custom special tokens or entirely new BPE vocabularies via direct `Encoding` construction or the `tiktoken_ext` plugin mechanism.
- **Educational module**: `tiktoken._educational` provides `SimpleBytePairEncoding` for visualizing BPE tokenization and `train_simple_encoding()` for training toy tokenizers.

Useful for token counting before API calls, understanding tokenization behavior, building token-aware text chunking for RAG pipelines, and debugging token-level model behavior.

## Mechanical details

Pure Python API with Rust core (via PyO3). Install from PyPI with `pip install tiktoken`. API documented in `tiktoken/core.py`. Supports Python 3.8+.

## Security

MIT licensed. Official OpenAI project with active maintenance. No known security concerns — pure computation library with no network access, file writes, or side effects beyond tokenization.

## How to use it

pip install tiktoken
