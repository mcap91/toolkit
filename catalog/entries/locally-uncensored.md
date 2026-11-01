---
name: locally-uncensored
title: Locally Uncensored
url: https://github.com/PurpleDoubleD/locally-uncensored
category: framework
summary: All-in-one free, open-source local AI desktop studio (Windows/Linux, AGPL-3.0-only) combining chat, image generation, video generation, and a coding agent — no Docker, terminal, or cloud required; coding agent shows the diff before applying changes; supports local image models (Juggernaut XL V9, DreamShaper XL Turbo V2, FLUX.1, FLUX 2 Klein 4B, Z-Image Turbo, Qwen-Image 2.1); beta features include on-device voice conversation and gated computer-control; optional remote access via passcode-gated encrypted Cloudflare tunnel; maintained by GitHub user PurpleDoubleD with near-weekly releases (~1,750 stars as of Sept 2026); Windows installers currently ship unsigned
tags:
  - desktop-app
  - local-inference
  - chat
  - image-generation
  - video-generation
  - coding-agent
  - windows
  - linux
  - open-source
  - privacy
reviewed: 2026-10-30
acquired: 2026-10-30
license: AGPL-3.0-only
security_flags:
  - agpl-copyleft
  - unsigned-installer
overlaps:
  - lm-studio
source_url: https://www.instagram.com/reel/De2LjyNNS4H/
source: instagram
---

## What it does

Locally Uncensored (LU) is a free, open-source, all-in-one local AI studio for the desktop: chat, image generation, video generation, and a coding agent in one app, running entirely on the user's machine with no Docker, no terminal, and no cloud required. It ships for Windows (NSIS installer or MSI) and Linux (AppImage, deb, or rpm); there is no macOS desktop build — Mac users are directed to a browser-based "LU Cloud" instead. The project markets itself against Open WebUI, LM Studio, Jan, and SillyTavern on the basis of including image-to-image, image-to-video, and a coding agent in one app. The coding agent shows the diff before applying a change; "agent mode" otherwise performs the work directly. In local mode, chat, agent runs, and image/video generation happen on-device with no telemetry or analytics.

Supported local image-generation models include Juggernaut XL V9 (photoreal SDXL), DreamShaper XL Turbo V2 (anime/stylized), FLUX.1, FLUX 2 Klein 4B, Z-Image Turbo, and Qwen-Image 2.1 (generate-and-edit-in-one-model, requiring ComfyUI 0.37.0 under a research/non-commercial license).

Beta features: an on-device spoken-conversation mode (speech recognition, voice, and turn-taking run locally, English only, fifteen voices), and a computer-control feature where a model views the screen and uses the mouse/keyboard in approved apps, asking before every action unless set to autonomous, and never touching terminals, password managers, or password fields. Remote access is off by default; when enabled it is passcode-gated — on a LAN nothing leaves the network, and off-LAN it uses an encrypted Cloudflare tunnel with no third-party AI server involved.

## Mechanical details

- Canonical source: github.com/PurpleDoubleD/locally-uncensored (the releases page is the only official download source); companion sites locallyuncensored.com and lu-labs.ai
- Maintainer: GitHub user PurpleDoubleD, near-weekly releases through 2026, ~1,750 stars as of September 2026
- Numerous same-named GitHub forks/mirrors exist under unrelated usernames (e.g. annihilatorrrr, ozMerv, sdfsws, vinberg88, NEXINSx, rssikong) — only the PurpleDoubleD repo and its releases page are confirmed official
- License: AGPL-3.0-only (per repo LICENSE file and badge)

## Security

AGPL-3.0-only — copyleft obligations apply to any derivative distribution. Windows installers currently ship unsigned; SignPath Foundation has accepted the project for free code-signing but the production certificate is not yet in place. The proliferation of same-named GitHub forks under unrelated accounts makes source verification important — confirm downloads come from the PurpleDoubleD repo's releases page, not a fork.
