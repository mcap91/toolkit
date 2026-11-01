---
name: bonsai-ada-surgery
title: bonsai-ada-surgery (Ternary Bonsai 2 27B on 8-12GB + agent layer)
url: https://github.com/professorpalmer/bonsai-ada-surgery
source_url: https://www.reddit.com/r/LocalLLM/comments/1x1rv5k/comment/pew7oqh/
category: framework
summary: Serving recipe and launcher for PrismML's Ternary Bonsai 2 27B (1.58-bit ternary GGUF, PTQ1_0 quant, 5.9GB) that runs the full 262,144-token trained context window on 8GB and 12GB NVIDIA cards — patched PrismML llama.cpp fork, a launcher that sizes the K/V cache per card (q4_0 on 12GB, q3_0 on 8GB), MTP speculative drafting, weights unchanged; fixes reported agent/coding regressions at the runtime layer (template-rejected effort words, output caps that cut off reasoning, a runaway "xhigh" reasoning default, tool calls returned as JSON) rather than the compression; optional agent "layer" (API cards, sandboxed Python) ported from the same author's mirai-s-ada; repo's own title claims 262k context on 12GB at 54-97 tok/s decode, 2x prefill, q8_0 KV recipe, grammar tool calls 9/9 (self-reported); OpenAI-compatible API; MIT for repo code, PrismML weights Apache-2.0.
tags:
  - local-inference
  - llama-cpp
  - ternary-quantization
  - long-context
  - kv-cache
  - speculative-decoding
  - mtp
  - openai-compatible
  - proxy
  - code-interpreter
  - consumer-gpu
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - mirai-s-ada
license: MIT
security_flags:
  - custom-llama-cpp-fork
  - single-maintainer
  - new-project
source: reddit
---

## What it does

Serving recipe and launcher for PrismML's Ternary Bonsai 2 27B (1.58-bit ternary GGUF, `PTQ1_0`
quant, 5.9GB) that runs the full 262,144-token trained-max context window on 8GB and 12GB NVIDIA
cards. Uses a patched PrismML llama.cpp fork; a launcher sizes the K/V cache precision per card
(`q4_0` on 12GB, `q3_0` on 8GB) and adds MTP (multi-token-prediction) speculative drafting. Model
weights are not changed — the repo's premise is that most of the coding/agent quality loss people
report on this model comes from the serving runtime, not the ternary compression, and fixes it at
that layer: effort words the chat template rejects, output caps that cut reasoning short, a
runaway `xhigh` reasoning-effort default, and tool calls returned as JSON instead of the expected
format. An optional agent "layer" (API cards for Python modules, sandboxed code execution) is
ported from the same author's `mirai-s-ada`.

## Mechanical details

- Quick start (Windows/NVIDIA): download `bonsai-bundle-win-x64.zip` from Releases, place
  `Ternary-Bonsai-2-27B-PTQ1_0.gguf` and the MTP head file in `models\`, run `.\start-server.ps1`;
  OpenAI-compatible API at `http://<host>:8080/v1`. Linux and build-from-source are documented
  separately in the repo.
- Repo's own GitHub description claims: 262k context (trained max) on 12GB, 54-97 tok/s decode,
  2x prefill, a q8_0 KV recipe, and grammar-constrained tool calls 9/9 — self-reported, not
  independently verified in this review.
- Docs tree covers per-card setup (`docs/12gb`, `docs/8gb`), quality fixes (`docs/quality`), the
  agent layer (`docs/agents-layer`), build/install (`docs/build`), speed (`docs/speed`), raw
  benchmark logs (`docs/receipts`), and benchmark methodology (`docs/research`, `docs/cards`).
- Repo code is MIT; model weights are PrismML's own release, Apache-2.0; repo states it is not
  affiliated with PrismML.
- Same author as `mirai-s-ada` (u/ProfessorPalmer on Reddit, Cary Palmer on GitHub); per the
  author's account this project predates mirai-s-ada ("I actually fixed Bonsai first!").

## Usage notes

- Reddit thread (r/LocalLLM, Oct 2026): the author reported "100 tok/s 262k on 12gb" for this
  patch. One reply (Anstellos) pushed back that base Bonsai was "always way dumber than original
  qwen 27b... so fast but stupid" and asked whether the patch actually fixed that; no benchmark
  was given in the visible reply thread to settle the question. (source:
  https://www.reddit.com/r/LocalLLM/comments/1x1rv5k/comment/pew7oqh/)

## Security

MIT for the repo's own code; model weights are PrismML's, Apache-2.0, and the repo explicitly
states it is not affiliated with PrismML. Same risk profile as `mirai-s-ada`: depends on a custom
llama.cpp fork, single maintainer, surfaced October 2026. The optional agent layer (ported from
mirai-s-ada) executes model-written code in a sandbox per that project's design — review before
enabling.