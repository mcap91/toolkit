---
name: brag
title: /brag — Launch Video Generator
url: "https://github.com/latent-spaces/brag"
category: plugin
summary: "Claude Code skill/plugin that generates short shareable launch videos from any project — analyzes the codebase, creates a product story with music/motion/share copy, renders via Hyperframes; one command; works with Claude Code, Codex CLI, opencode, Gemini CLI, Cursor via skills CLI; optional AI voiceover via Kokoro; MIT"
tags: [claude-code-plugin, video, launch, marketing, hyperframes, skill, multi-platform]
reviewed: 2026-09-18
acquired: 2026-09-18
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

/brag is an agent skill that turns a software project into a short launch video. It analyzes the project, crafts a product narrative (angle, tone, key moments), then hands a focused brief to Hyperframes for video rendering with music, motion, and timing.

Usage: run /brag inside any project. Optional flags:
- --tone to steer the narrative style
- --voice to enable AI voiceover via Kokoro through Hyperframes (off by default)

Output: brag-output/ folder with the plan, composition brief, share copy, and rendered brag.mp4.

Installation:
- Claude Code: plugin marketplace add, then plugin install
- Other agents (Cursor, Codex, Copilot, Gemini CLI, opencode): npx skills add with the repo URL
- Manual: copy skills/brag/ to ~/.claude/skills/brag/

Cross-agent discovery via symlinks for Claude Code, Codex CLI, and opencode. Requirements: Node.js 22+, FFmpeg on PATH, Hyperframes CLI.

## Security

- License: MIT
- Dependencies: requires Hyperframes CLI and FFmpeg
- Music/SFX: bundled assets from ende.app and Kenney

## Usage notes

- One reported run against a real side project (a storage-cleaning app) took about 10 minutes and used 61,000 output tokens plus 600 input tokens, costing $6 (source: https://www.instagram.com/reel/Dezc4qeimex/)
