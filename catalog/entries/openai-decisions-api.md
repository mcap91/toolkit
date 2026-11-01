---
name: openai-decisions-api
title: OpenAI Decisions API
url: https://developers.openai.com/api/docs/guides/decisions
category: framework
summary: Hosted decision-model endpoint (POST /v1/decisions, model fixed to gpt-6-luna) that returns typed answers instead of free text — predicate (probability), choice (value + probabilities + confidence), and score (weighted score + probabilities + confidence) — from text, images, input_json, or conversation history; 1-400 questions per request; $0.10/1M uncached input tokens, no output-token charge, prompt caching (1,024-token minimum prefix); announced at DevDay 2026 (2026-09-29) in limited preview, now generally available with GPT-Live voice integration and Private Link; OpenAI claims up to 10x faster than a standard Responses API call to GPT-6 Luna, with a Box Extract case study reporting ~5x faster document routing at matching accuracy; supports Zero Data Retention, HIPAA, and regional data residency (US, EEA, Switzerland); competes with TypeSafe's Jev and Cloudflare's Clef/Clef-flash in the typed-decision-model space
tags:
  - decision-models
  - openai
  - gpt-6-luna
  - classification
  - scoring
  - jev-competitor
  - vision
  - hosted-api
  - compliance
  - voice
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - jev
  - cloudflare-clef
license: ""
security_flags: []
source: instagram
source_url: https://www.instagram.com/reel/DeIV3Tam24w/
---

## What it does

OpenAI's Decisions API is a hosted endpoint (`POST /v1/decisions`) that returns typed answers instead of generated text, using a constrained version of GPT-6 Luna — `model` is fixed to `gpt-6-luna`, the only supported model. A request carries 1-400 questions, each one of three types:
- Predicate: a yes/no condition, returns a `probability` (0-1)
- Choice: pick from fixed options, returns the chosen value plus a `probabilities` array and a `confidence`
- Score: rate against ordered levels, returns a `score` (weighted average of level indices) plus `probabilities` and `confidence`

Input can be a plain text string, images (base64 data URLs or public HTTP/HTTPS URLs), structured JSON via an `input_json` content part, or full conversation history (messages, tool calls, tool outputs). The response is an `answers` array with one typed entry per question, or a `refusal` entry.

Announced at OpenAI's DevDay on 2026-09-29 in limited preview, the API moved to public beta and then general availability. GA added native GPT-Live voice integration (GPT-Live calls Decisions directly while a user is still speaking, instead of round-tripping through the developer's app), prompt caching, and the 400-question-per-request limit. OpenAI claims the API answers up to 10x faster than a standard Responses API call to GPT-6 Luna; a Box Extract case study reported about 5x faster document routing on certificate-of-insurance classification, at the same accuracy as the Responses API.

## Mechanical details

- Endpoint: `POST /v1/decisions`, Bearer token auth, model fixed to `gpt-6-luna`.
- Pricing: $0.10 per 1M uncached input tokens; no charge for output tokens; cached input gets a discount off standard gpt-6-luna rates (1,024-token minimum reusable prefix for caching).
- Organization usage is queryable via `GET /v1/organization/usage/decisions`.
- Compliance: Zero Data Retention (ZDR) and HIPAA eligibility, data residency in supported regions (US, EEA, Switzerland), and a Private Link option for sending requests over a private network connection.
- OpenAI names three primary use cases: content classification, request routing, and agent next-action selection.

## Security

Closed, hosted-only API — no open weights and no self-hosting option; all inference runs on OpenAI's infrastructure and requires an OpenAI API key. ZDR and HIPAA eligibility are available for qualifying customers, and Private Link avoids the public internet, but the underlying gpt-6-luna weights are never exposed to the caller. This differs from both competing decision models already cataloged here: Jev (TypeSafe) is also a closed hosted API, text-only; Cloudflare's Clef/Clef-flash ship open weights (Apache 2.0) with a genuine self-hosted path.
