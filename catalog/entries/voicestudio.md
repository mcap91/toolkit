---
name: voicestudio
title: VoiceStudio
url: "https://github.com/debpalash/VoiceStudio"
category: framework
summary: "Open-source local-first ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription, and audiobook creation in 646 languages; Electron desktop app with local API and MCP server for agent integration; NVIDIA CUDA and Apple Metal acceleration; AGPL-3.0"
tags: [voice-cloning, tts, dubbing, transcription, dictation, audiobook, local-first, electron, mcp, agent-skill]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: AGPL-3.0
security_flags: []
source: unknown
---

## What it does

VoiceStudio is a fully-local voice toolkit covering cloning, design, video dubbing, dictation, transcription, and audiobook creation across 646 languages. Default engine is k2-fsa/OmniVoice.

Workspaces:
- **Clone**: clone a voice from a clean reference recording
- **Design**: create custom voices
- **Dub**: video dubbing with timed speech
- **Dictate**: floating widget for dictation
- **Produce**: stories, audiobooks, batch jobs
- **Connect**: local API and MCP server for agent integration

Hardware support: NVIDIA GPU (CUDA), Apple Silicon (Metal), CPU-only fallback (slower), experimental Windows on ARM.

## Mechanical details

Install: `curl -fsSL https://voicestudio.sh/install | sh` (macOS/Linux), `irm https://voicestudio.sh/install | iex` (Windows PowerShell). Also available as .dmg, .exe, .AppImage, .deb from releases. Docker supported.

Agent integration: `npx skills add debpalash/VoiceStudio` for coding agents (Claude Code, Codex, Cursor). Local API and MCP server for programmatic access. Optional remote workers.

Build from source: `git clone && cd VoiceStudio && bun install && bun run setup:api && bun run dev`.

## Security

AGPL-3.0 licensed. Local workflows run entirely on your hardware. Remote services are optional. Usage analytics requires consent. Models have their own licenses — review before commercial use. Clone voices only with permission.

## Usage notes

- Install flow runs a hardware compatibility check on first launch and lets the user pick output quality (e.g. max); voice cloning worked from a 15-second reference clip in a live demo (source: https://www.instagram.com/reel/De1zlGniBQp/)
