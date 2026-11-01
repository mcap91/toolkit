---
name: huggingface-inference-providers
title: Hugging Face Inference Providers
url: "https://huggingface.co/docs/inference-providers/index"
category: framework
summary: "Unified API gateway routing inference to 15+ backend providers (Groq, Together AI, Cerebras, Replicate, etc.) via a single HF token; OpenAI-compatible, multi-task (LLM, VLM, image gen, embeddings, speech), with provider selection policies (:fastest, :cheapest, :preferred)"
tags: [huggingface, inference, model-api, gateway, openai-compatible, multi-provider, serverless]
reviewed: 2026-06-19
acquired: 2026-06-19
license: Apache-2.0
security_flags: []
overlaps: [openrouter, nvidia-build]
source: unknown
---

## What it does

Hugging Face Inference Providers is a unified API layer that sits between your application and 15+ AI inference backends — Cerebras, Groq, Together AI, Replicate, Fal AI, SambaNova, DeepInfra, Fireworks, Novita, Scaleway, and others. You authenticate once with an HF token and route requests to any supported provider through a single interface. The system auto-selects the fastest available provider by default, or you append `:cheapest` or `:preferred` to the model ID to control routing.

Three tiers exist under the "Inference" umbrella: (1) **Serverless Inference API** — free-tier, rate-limited, HF's own backend, good for prototyping and CPU-bound tasks like embeddings/classification; (2) **Inference Endpoints** — dedicated GPU instances you provision per-model ($0.50/hr+, scale-to-zero); (3) **Inference Providers** — the multi-provider gateway described above, pay-as-you-go at provider rates with no HF markup.

Tasks span chat completion (LLM and VLM), text-to-image, text-to-video, speech-to-text, feature extraction/embeddings, NER, summarization, and classification. The chat completions endpoint is an OpenAI API drop-in replacement (`https://router.huggingface.co/v1`).

## Assessment

Cataloged because: (1) the OpenAI-compatible gateway with provider selection policies (:fastest, :cheapest) makes this a practical multi-model routing layer for agentic workflows — same niche as OpenRouter but with tighter integration into the HF model ecosystem; (2) has an explicit Claude Code integration guide, suggesting designed-for-agent use; (3) no markup on provider rates and a free tier with monthly credits lowers the barrier for experimentation; (4) the embeddings and feature-extraction tasks are directly useful for RAG pipelines and semantic search in bioinformatics workflows. Overlaps with OpenRouter (multi-provider model gateway) and NVIDIA Build (model API catalog), but distinguished by the breadth of providers and the HF Hub integration (model cards, datasets, Spaces).

## Mechanical details

- Router endpoint: `https://router.huggingface.co/v1` (OpenAI-compatible)
- Python SDK: `huggingface_hub` (`InferenceClient`)
- JS SDK: `@huggingface/inference` (`InferenceClient`)
- Auth: HF fine-grained token with "Make calls to Inference Providers" permission
- Provider selection: append `:fastest` (default), `:cheapest`, or `:preferred` to model ID, or specify provider explicitly (`provider: "sambanova"`)
- Free tier: monthly inference credits included for all accounts
- PRO ($9/mo): raised rate limits, 2M monthly inference credits, 25 min/day H200 ZeroGPU
- No HF markup on provider rates — you pay the provider's published price

## Security

- License: Apache-2.0 (HF client libraries); individual models carry their own licenses
- Dependency health: HF-maintained SDKs with active development; providers are established companies (Groq, Together AI, Cerebras, etc.)
- Code quality signals: Major platform (~1M+ users); well-documented API; official SDKs in Python and JS
- Supply chain: Hugging Face is a well-funded, widely-used ML platform; requests proxy through HF infrastructure
- Dangerous patterns: Standard API proxy risks — your data transits HF servers and the selected provider; review provider privacy policies for sensitive workloads
- Maintenance: Actively maintained; new providers added regularly

## Usage notes

- Claude Code proxy technique (same pattern as nvidia-build): set `ANTHROPIC_BASE_URL=https://router.huggingface.co/v1`, provide `HF_TOKEN`, and route to open models through the HF gateway. Same caveats apply — verify Anthropic ToS compliance; intent is supplementing with open-source models for specific tasks.
- For model discovery, use the HF Hub model cards and the Inference Playground (`huggingface.co/playground`) to test models before committing to a provider.
- Provider selection tip: use `:cheapest` for batch/background workloads where latency doesn't matter; `:fastest` for interactive/agentic use.

- HF Pro plan ($9/month) with serverless inference can supplement agent building as a cheaper alternative to calling `claude -p` or Codex headless for open-source model workloads