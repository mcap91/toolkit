---
name: godogen
title: godogen
url: "https://github.com/htdt/godogen"
category: cli-tool
summary: "Generator + agent-driven workflow for autonomous game development targeting Godot 4, Bevy, or Babylon.js — a publish.sh script renders a thin runtime layout (manifest, engine guide, asset-generation skill) into a fresh target repo for either Claude Code (CLAUDE.md + .claude/skills/) or Codex (AGENTS.md + .agents/skills/), then the chosen host agent builds the actual game by reading the engine guide and calling external asset-generation APIs (Gemini, xAI Grok, Tripo3D)"
tags: [game-development, godot, bevy, babylonjs, claude-code, claude-code-skill, codex, agent-workflow, asset-generation, generator, python]
reviewed: 2026-08-25
acquired: 2026-08-25
license: MIT
security_flags:
  - 'Requires third-party API keys with outbound network calls to external paid services during agent runs: GOOGLE_API_KEY (Gemini image generation), XAI_API_KEY (Grok image/video generation), TRIPO3D_API_KEY (image-to-3D and rigged animation) — these keys and generated content leave the local machine'
  - "Designed to run an AI coding agent (Claude Code or Codex) autonomously/unattended for extended periods ('a full generation run can take hours'); the README suggests running under tmux/screen on a remote server with the agent's remote-control interface, i.e. long unattended agent execution with real API credentials and code-execution ability"
  - 'No LICENSE file found at the repository''s raw content path checked (githubusercontent.com/htdt/godogen/main/LICENSE returned 404); license is asserted via the GitHub repository metadata API (license.spdx_id: MIT) rather than confirmed from an in-repo LICENSE file'
overlaps: []
source: unknown
---

## What it does

godogen is not itself a game — it is the source for a generator that produces game-development repos: `godogen -> game repo -> game`. Running `./publish.sh --engine <godot|bevy|babylon> --agent <claude|codex> --out <dir>` renders a deliberately thin runtime layout into a fresh target directory: a runtime manifest (`prompts/runtime.md`), a one-page per-engine guide (`engines/{babylon,godot,bevy}.md`), and a cross-engine asset-generation skill (`asset-gen/`), formatted for either Claude Code (`CLAUDE.md` + `.claude/skills/`) or Codex (`AGENTS.md` + `.agents/skills/`) depending on the `--agent` flag. The chosen host coding agent then runs inside that freshly published repo and reconstructs everything else (project scaffold, capture tooling) from the short engine guide, building an actual playable game: it describes a game from a prompt, and the agent scaffolds the project, generates art/asset assets via external generation APIs, runs the target engine, and produces proof of the result — either a live, steerable session (a Babylon.js URL to watch in-browser, or a Godot/Bevy project run locally) or a recorded 15–20 second video clip when run unattended.

Per-engine targets: Godot 4 (C#/.NET projects, build-time scene generation, runtime scripts, Jolt physics), Bevy (Rust/ECS, code-first scenes, offscreen capture), Babylon.js (TypeScript/Vite, served as a live browser URL). Asset generation is delegated to three external services: Google Gemini for precise image references/characters, xAI Grok for textures/simple objects plus Grok video for animated sprites (with loop detection and background removal), and Tripo3D for image-to-3D conversion and rigged biped animation.

## Differentiators / Key takeaways

- Treats "engine + host agent" as a publish-time rendering choice rather than maintaining separate source trees per combination — one generator, multiple output flavors.
- Explicitly designed around agent "proof over claims": the agent is expected to judge results from the running game (live URL or recorded clip) rather than from a clean compile, driving iteration off visible defects.
- Supports both a supervised mode (user watches/steers a live game) and an unattended mode (agent runs solo, produces a short proof video) — "the agent takes its cue from how you frame the task."
- Chains three different external generative-AI providers (Gemini, Grok, Tripo3D) for different asset types (2D references, textures/video, 3D+rigging) within a single pipeline.

## Mechanical details

- Repo layout: `prompts/runtime.md` (runtime manifest), `asset-gen/` (cross-engine asset skill), `engines/babylon.md` / `engines/godot.md` / `engines/bevy.md` (per-engine guides), `publish.sh` (renderer).
- Publish command: `./publish.sh --engine {godot|bevy|babylon} --agent {claude|codex} --out <dir>`; `--force` overwrites an existing target directory.
- Prerequisites: Godot 4 (.NET build) on PATH, Rust/Cargo, Node.js 22.12+ and npm, Chrome/Chromium with hardware WebGL2, Python 3 with pip, system packages per `setup.md` (vulkan-tools, xvfb, ffmpeg, imagemagick, plus platform-specific extras); tested on Ubuntu, Debian, macOS.
- Required environment variables for asset generation: `GOOGLE_API_KEY`, `XAI_API_KEY`, `TRIPO3D_API_KEY`.
- Long unattended runs are expected to be kept alive via `tmux`/`screen` over SSH, optionally combined with Claude Code's or Codex's official remote-control interface for checking in mid-run.
- GitHub repository metadata: primary language Python, MIT license (per GitHub API `license.spdx_id`), 6,090 stars, 545 forks, 8 open issues, created 2026-02-06, last pushed 2026-07-26, topics include `claude`, `claude-code`, `claude-code-skill`, `codex`, `codex-cli`, `codex-skill`, `game-development`, `godot`, `godot4`, `skills`. Author: htdt (`@alex_erm` on X/Twitter).

## Security

- **License**: MIT per GitHub's repository metadata API; a direct fetch of a raw `LICENSE` file at the default branch path returned HTTP 404 during this review, so the license was not independently confirmed by reading an in-repo LICENSE file.
- **Secrets/credentials**: Requires three separate paid third-party API keys (Google AI Studio, xAI, Tripo3D) exported as environment variables; asset-generation requests and generated content transit these external services.
- **Autonomous execution**: The tool is explicitly designed to run a coding agent (Claude Code or Codex) unattended for hours, with code-execution ability (project scaffolding, engine builds, running game engines) and network access (asset-generation API calls) — standard risks of long-running unattended agent sessions with live credentials apply.
- **Supply chain**: Individual-maintainer GitHub repo (not an org); no signed releases or reproducible-build attestation mentioned in the README.
- **Maintenance signal**: 6,090 stars / 545 forks with commits as recent as 2026-07-26 per repository metadata, indicating active use, but this reflects popularity rather than an audit of the generated skill/prompt content itself.
