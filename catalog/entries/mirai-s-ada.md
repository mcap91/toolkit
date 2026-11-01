---
name: mirai-s-ada
title: mirai-s-ada (Mirai S 27B on 12GB + agent layer)
url: https://github.com/professorpalmer/mirai-s-ada
category: framework
summary: Serving recipe and launcher for Mirai Labs' Mirai S (Qwen3.8-27B-S, ~2.4-bit trellis GGUF) on a 12GB RTX 4070 — custom llama.cpp fork with 262K context, tiered q8_0 KV cache, and MTP speculative drafting at every depth (author-measured decode 70 / 61 / 20 / 10 tok/s at 4K / 64K / 128K / 200K context) — plus an optional OpenAI-chat-schema proxy 'layer' that adds a WASI-sandboxed `run_python` tool loop, auto-generated API cards for Python modules appended to the first user message, and an API check that flags nonexistent names/kwargs in earlier tool code; OpenAI-compatible API with bearer key; MIT
tags:
  - local-inference
  - llama-cpp
  - qwen
  - quantization
  - speculative-decoding
  - mtp
  - long-context
  - kv-cache
  - openai-compatible
  - proxy
  - code-interpreter
  - wasi-sandbox
  - consumer-gpu
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - qwen38-27b-200k-on-16gb
  - llama-cpp-adaptive-kv-streaming
  - strata
license: MIT
security_flags:
  - custom-llama-cpp-fork
  - single-maintainer
  - new-project
source: unknown
---

## What it does

Two pieces for running a 27B model as a long-context local coding/agent backend on a 12GB GPU:

1. **Serving recipe.** Runs Mirai S (Mirai Labs' Qwen3.8-27B-S experimental, from `huggingface.co/trymirai/Qwen3.8-27B-S-experimental`, via alesha-pro's GGUF conversion with weights unchanged) on a custom llama.cpp fork pinned as a submodule. Features: full 262,144-token context, q8_0 K/V cache tiered between VRAM and host RAM, multi-token-prediction (MTP) drafting at every depth, and "harness-proofing" for clients that send `effort: "high"` or very small output caps. The launcher computes the VRAM split from measured fixed costs; 16GB+ cards keep all positions in VRAM.
2. **Agent "layer" (optional, `MIRAI_LAYER=1` default).** A small proxy started in front of `llama-server` on the same port, using only the OpenAI chat schema so it works with any server that has a tool-calling template:
   - **Code tool:** for requests that bring no tools, appends a `run_python(code, stdin)` function; tool calls execute in CPython 3.12 on WASI under wasmtime (no host files, no network, no processes, 128MB, 10s), results are fed back, looping up to 12 rounds; the client sees a single response (streaming supported, tool-call deltas withheld). The user's prompt text is exposed to the program as `input.txt`.
   - **API cards:** for coding requests, introspects the mentioned modules in the same runtime (signatures, docstrings, constants, methods) and appends them to the end of the first user message plus a sentence telling the model to use library functions; the author reports placement in the system message had no effect.
   - **API check:** parses code from earlier tool calls and notes nonexistent names/kwargs on the tool result.
   - **Pass-through rules:** requests with client tools get cards only; conversations already carrying fenced code are forwarded untouched. Per-request switches: `code_interpreter`, `api_cards`, `api_lint`, `input_file`.

## Mechanical details

- Run: Windows release zip/launcher or `start-server.ps1`; Linux `start-server.sh`. Optional `layer\fetch_runtime.ps1` downloads the checksummed WASI CPython runtime and runs isolation canaries; without it the plain server starts.
- API: OpenAI-compatible at `http://<host>:8080/v1`, bearer key in `artifacts/api_key.txt` (generated on first run).
- Author-reported results (RTX 4070 12GB): decode 70.1 / 60.9 / 20.3 / 10.3 tok/s at 4K / 64K / 128K / 200K context; prompt read ~1,090 tok/s (16.8K tokens); HumanEval 161/164; AppWorld test_normal 88.7%; a 37-task exact-work suite scored 18 without the layer vs 28 with it.
- Layer and test suite derive from the same author's `bonsai-ada-surgery` (Ternary Bonsai 2 27B on 12GB).

## Usage notes

- Reddit thread: the weights are ~2.4-bit; commenters asked for perplexity and baseline comparisons. One user reported 50–70 tok/s in synthetic tests but ~15 tok/s in real agentic coding at high context on a 12GB 4070 with DDR4 (the repo's own table shows the same decline with context); the author points to subsequent updates.

- A skeptical commenter (mike4080s) couldn't find the author's claimed "98%" figure in either linked page, and pointed out the repo's own table shows 72.6 tok/s at 16K context dropping to 11 tok/s at 180K context. (source: https://www.reddit.com/r/LocalLLM/comments/1x1rv5k/comment/pew7oqh/)
- Asked what harness produced the agentic-task numbers, the author named an unpublished personal harness, "Marionette" — no repo link given. (source: https://www.reddit.com/r/LocalLLM/comments/1x1rv5k/comment/pew7oqh/)

## Security

MIT. Code execution from the layer runs inside a WASI sandbox (no host filesystem, network, or subprocesses; memory/time limits) with canary tests checked at runtime fetch. The server binds an HTTP API protected by a generated bearer key. Depends on a custom llama.cpp fork and third-party GGUF conversions; single maintainer, created Oct 2026.
