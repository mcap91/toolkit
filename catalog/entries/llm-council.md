---
name: llm-council
title: LLM Council
url: https://github.com/karpathy/llm-council
source_url: https://github.com/karpathy/llm-council
source: web
category: agent-pattern
summary: Andrej Karpathy's local web app (ChatGPT-like UI) that sends one query to multiple LLMs via OpenRouter, has each model anonymously rank the others' responses on accuracy/insight, then has a designated 'Chairman' model compile a final synthesized answer; three-stage pipeline (first opinions → anonymized cross-review/ranking → Chairman synthesis). FastAPI/Python backend, React/Vite frontend, uv + npm tooling. Explicitly described by the author as '99% vibe coded' as a weekend hack, unsupported and not intended to be improved further.
tags:
  - multi-model
  - llm-council
  - openrouter
  - ensemble
  - agent-pattern
  - fastapi
  - react
  - karpathy
  - vibe-coded
reviewed: 2026-10-28
acquired: 2026-10-28
license: NOASSERTION
security_flags:
  - unmaintained
  - no-support
overlaps:
  - agent-teams
  - local-model-adversarial-workflow
---

## What it does

A local web app that replaces a single-LLM query with a three-stage multi-model pipeline, run entirely through OpenRouter so any mix of provider models can participate:

1. **First opinions** — the user's query goes to every configured council model individually; each response is shown in its own tab so the user can inspect them side by side.
2. **Review** — each model is shown the other models' responses, with identities anonymized so a model can't favor itself or a known competitor, and is asked to rank them on accuracy and insight.
3. **Final response** — a separately designated "Chairman" model reads all individual responses (and implicitly the rankings) and compiles one final synthesized answer presented to the user.

**Default council** (editable in `backend/config.py`): GPT-5.1, Gemini 3 Pro Preview, Claude Sonnet 4.5, Grok 4, with Gemini 3 Pro Preview as Chairman — any OpenRouter-supported model can be substituted.

**Stack:** FastAPI (Python 3.10+) backend with async `httpx` calls to OpenRouter; React + Vite frontend with `react-markdown`; conversations persisted as JSON files in `data/conversations/`; `uv` for Python dependency management, `npm` for the frontend. Requires an `OPENROUTER_API_KEY` and purchased OpenRouter credits.

**Author's own framing:** built as a weekend hack ("99% vibe coded") to compare LLMs side by side while reading books with them; explicitly not supported or intended to be improved by the author going forward — offered as-is for inspiration, with an invitation to have one's own LLM modify it freely.

## Sources

- [karpathy/llm-council — GitHub README](https://github.com/karpathy/llm-council) — pipeline description, stack, setup, author's framing (fetched directly).

## Security

No license file/declaration found in the fetched README (NOASSERTION). Explicitly unmaintained by its author ("I'm not going to support it in any way... I don't intend to improve it") — anyone adopting it should expect no upstream fixes, including for any security issues, and should review the code themselves before use. Requires an OpenRouter API key with purchased credits; queries and model outputs transit OpenRouter and each underlying provider.
