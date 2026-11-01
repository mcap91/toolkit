---
name: screenshot-to-code
title: Screenshot to Code
url: https://github.com/abi/screenshot-to-code
category: framework
summary: Converts screenshots, mockups, Figma designs, and screen recordings into HTML+Tailwind, HTML+CSS, React+Tailwind, Vue+Tailwind, Bootstrap, or Ionic+Tailwind code via multi-provider LLMs (OpenAI/Anthropic/Gemini); Gemini extracts real logos/images from the source rather than regenerating them, Replicate handles image generation/editing/background removal; React/Vite frontend + FastAPI backend, self-hostable or hosted at screenshottocode.com; MIT, 55k+ stars
tags:
  - screenshot-to-code
  - design-to-code
  - ui-generation
  - website-cloning
  - llm-vision
  - react
  - vue
  - tailwind
  - fastapi
  - self-hostable
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
source: instagram
source_url: https://www.instagram.com/reel/Dcd3eY1iOMA/
---

## What it does

Takes a screenshot, mockup, Figma export, or screen recording and generates working front-end code in a chosen stack: HTML+Tailwind, HTML+CSS, React+Tailwind, Vue+Tailwind, Bootstrap, or Ionic+Tailwind. A user can also enter a live URL instead of uploading an image. Backend is FastAPI, frontend is React/Vite; self-hostable via Poetry or Docker, or used hosted at screenshottocode.com.

## Model support

Supports OpenAI, Anthropic, and Google Gemini as code-generation providers (at least one API key required), plus Replicate for image generation, editing, and background removal. Default models as of the current README: Gemini 3 Flash Preview / 3.1 Pro Preview, GPT-5.5 / GPT-5.4 Mini, Claude Opus 4.6 / Opus 4.8. With multiple provider keys set, the app generates multiple variants per request so results can be compared side by side. Gemini additionally powers asset extraction — reusing the real logos/images found in the source screenshot instead of generating replacements — and is required for video-to-code mode. Running on local Ollama models is supported but documented by the maintainer as not recommended due to poor output quality.

## Differentiators

- **Asset extraction, not regeneration** — Gemini-based pipeline detects and reuses real logos/images from the screenshot rather than having the model hallucinate replacements
- **Screenshot preview loop** — optional headless-Chromium (Playwright) step renders the model's own generated output so the agent can visually check its work before returning it
- **Video-to-code mode** — accepts a screen recording of a live site and reproduces it as a functional prototype, not just a static screenshot
- **Multi-stack output** — one input can target six different HTML/CSS/JS stack combinations

## Mechanical details / What to adopt

- Self-host: `cd backend && poetry install && poetry run playwright install chromium && poetry run uvicorn main:app --reload --port 7001`, then `cd frontend && pnpm install && pnpm dev`, open `http://localhost:5173`
- Or Docker: `echo "OPENAI_API_KEY=sk-..." > .env && docker-compose up -d --build`
- API keys set via `backend/.env` or the frontend settings dialog (gear icon); `REPLICATE_API_KEY` must be set in `backend/.env`
- Reconfigurable backend/frontend ports via `VITE_HTTP_BACKEND_URL` / `VITE_WS_BACKEND_URL` in `frontend/.env.local`
- Also usable as the hosted product at screenshottocode.com with no local setup

## Security

MIT licensed. Self-hosted mode sends screenshots/recordings and prompts to whichever third-party LLM APIs are configured (OpenAI, Anthropic, Gemini) and to Replicate for image operations — no local-only mode without API keys. No sandboxing of generated code is documented; generated output should be reviewed before running or deploying. Hosted option (screenshottocode.com) is a third-party SaaS with its own data-handling terms, not evaluated here.