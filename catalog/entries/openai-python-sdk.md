---
name: openai-python-sdk
title: OpenAI Python SDK
url: "https://github.com/openai/openai-python"
category: framework
summary: "Official Python client for the OpenAI API — GPT, o-series, Codex, DALL-E, Whisper, embeddings; typed Pydantic models, async support, streaming, function calling; MIT, PyPI"
tags: [openai, python, sdk, llm, api-client]
reviewed: 2026-06-22
acquired: 2026-06-22
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Official Python client library for the OpenAI API. Covers all API endpoints: chat completions (GPT-5.4-mini, GPT-5, o-series), embeddings, images (DALL-E), audio (Whisper/TTS), assistants, fine-tuning, batch, and files. Typed with Pydantic models, supports sync and async, streaming, and function/tool calling.

Basic conversation loop with memory:
```python
from openai import OpenAI
client = OpenAI()
messages = [{"role": "system", "content": "You are helpful."}]
while True:
    messages.append({"role": "user", "content": input("> ")})
    resp = client.chat.completions.create(model="gpt-5.4-mini", messages=messages)
    messages.append(resp.choices[0].message)
    print(resp.choices[0].message.content)
```

## Assessment

Standard SDK for OpenAI API access. Relevant as infrastructure when building multi-provider agent pipelines or when a task specifically requires OpenAI models (e.g., Whisper for transcription, DALL-E for images). Not directly needed when working natively with Claude, but worth having cataloged as the canonical OpenAI client.

## Mechanical details

- Install: `pip install openai`
- Auth: `OPENAI_API_KEY` env var or `OpenAI(api_key=...)`
- Async: `from openai import AsyncOpenAI`
- Streaming: `client.chat.completions.create(..., stream=True)`

## Security

- **License**: Apache-2.0
- **Maintenance**: official OpenAI repository, actively maintained
- **API key handling**: reads from env var by default — standard pattern