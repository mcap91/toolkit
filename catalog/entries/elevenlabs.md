---
name: elevenlabs
title: ElevenLabs
url: https://elevenlabs.io/
source_url: https://www.reddit.com/r/vibecoding/comments/1wyxpef/look_what_i_built/
category: framework
summary: Commercial AI voice platform — text-to-speech (TTS), voice cloning, and voice-agent APIs; models adapt intonation/pacing/emotion to textual cues across up to 32 languages (marketing cites 90+ languages and 17,500+ voices for the broader product); voice library of 10,000+ community-shared voices plus professional and instant voice cloning and text-described voice design; core endpoint `POST /v1/text-to-speech/:voice_id` (model_id defaults to eleven_multilingual_v2, optional language_code); Eleven Realtime bundles ASR + VAD + turn-taking + LLM + TTS into one speech-to-speech voice agent; official JS (`@elevenlabs/elevenlabs-js`) and Python SDKs plus community integrations (Vercel AI SDK, LangChain-style wrappers); closed-source hosted SaaS, $5-$990+/mo tiers, ~$0.30/1k characters API metering; privacy policy retains voice-model data up to 3 years post-interaction with no published deletion guarantee for a trained voice-clone model, trains on consumer-tier data by default (opt-out available), and faces an active 2026 biometric-data class action and recurring deepfake/voice-cloning-misuse reports; Enterprise tier adds SOC 2 Type II, HIPAA, GDPR terms, EU residency, and a traffic-limited Zero Retention Mode
tags:
  - text-to-speech
  - voice-cloning
  - tts-api
  - voice-agents
  - speech-synthesis
  - commercial-api
  - saas
  - deepfake-risk
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - voicestudio
license: proprietary
security_flags:
  - closed-source
  - biometric-data-handling
source: reddit
---

## What it does

ElevenLabs is a commercial AI voice platform offering text-to-speech (TTS), voice cloning, and voice-agent APIs. Models adapt intonation, pacing, and emotional tone to textual cues across up to 32 languages (marketing copy cites 90+ languages and 17,500+ voices for the broader voice-generation product). The voice library ships 10,000+ community-shared voices alongside professional voice cloning (highest fidelity, from longer reference audio), instant voice cloning (from 1-2 minutes of reference audio), and text-described voice design.

Core API: `POST /v1/text-to-speech/:voice_id` converts text to audio for a chosen voice; optional parameters include `model_id` (defaults to `eleven_multilingual_v2`, queryable via `GET /v1/models`) and `language_code`. Eleven Realtime is a separate class of speech-to-speech models bundling ASR, voice-activity detection, turn-taking, an LLM, and TTS into one real-time voice agent. Official JS (`@elevenlabs/elevenlabs-js`) and Python SDKs exist, plus community integrations (Vercel AI SDK's `@ai-sdk/elevenlabs`, LangChain-style wrappers). Reported usage (r/vibecoding, Oct 2026): used for AI-generated music and voiceover in a Claude-Code-produced marketing video.

## Mechanical details

- Pricing: consumer tiers from $5-$11/mo (Starter/Creator, unlocks instant/professional voice cloning with commercial license) up to Pro ($99), Scale ($299), Business ($990); API metered at roughly $0.30 per 1,000 characters; 2 free regenerations per generation on identical content/params; voice library not available via API on the free tier.
- Enterprise tier adds SOC 2 Type II, HIPAA (with signed agreement), GDPR terms, EU data residency, and an optional Zero Retention Mode — limited to eligible API and per-agent traffic, not browser-UI traffic.
- Closed-source hosted SaaS; no self-hosted option.

## Security

Proprietary/closed-source. Per ElevenLabs' privacy policy, voice-model data is retained up to 3 years after the last interaction, with no published deletion guarantee specifically for a trained voice-clone model once created; raw recordings are deleted per policy, but voice characteristics absorbed into a trained model may persist. Consumer tiers are trained on by default (prospective opt-out available); Enterprise is excluded from training by default. Independent reviews report an active federal biometric-data class action (filed May 2026) and recurring real-world misuse (unauthorized deepfake audio, impersonation), despite ElevenLabs' consent-verification tooling and detection/takedown efforts; several US states carry deepfake-specific legal exposure for unauthorized commercial impersonation.