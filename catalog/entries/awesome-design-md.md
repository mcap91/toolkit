---
name: awesome-design-md
title: awesome-design-md
url: "https://github.com/voltagent/awesome-design-md"
category: reference
summary: "Curated collection of 60+ DESIGN.md files — plain-text design-system documents (a Google Stitch concept) analyzed from real company websites — intended to be dropped into a project so AI coding/design agents generate UI consistent with that brand's visual language"
tags: [design-system, design-md, ui-generation, brand-design, google-stitch, curated-list, frontend]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: []
overlaps: [impeccable, ui-ux-pro-max-skill]
source: unknown
---

## What it says

DESIGN.md, per the README, is a concept introduced by Google Stitch: a plain-markdown design-system document, analogous to how AGENTS.md tells a coding agent how to build a project, except DESIGN.md tells a design-capable agent how the project should look. This repository is a curated collection of such files, each hand-extracted/analyzed from a real company's public website rather than generated speculatively. Every DESIGN.md follows a 9-section structure: visual theme/atmosphere, color palette with semantic role labels, typography hierarchy, component stylings (buttons/cards/inputs/nav with interaction states), layout/spacing principles, depth/elevation/shadow system, do's-and-don'ts guardrails, responsive behavior, and an agent prompt guide. Each site entry also ships `preview.html` and `preview-dark.html` visual catalogs showing color swatches, type scale, buttons, and cards.

60+ brand systems are covered across categories including AI/LLM platforms (Claude, Cohere, ElevenLabs, Mistral AI, Ollama, xAI, VoltAgent), developer tools (Cursor, Vercel, Raycast, Warp, Expo), backend/devops (MongoDB, Supabase, Sentry, ClickHouse, HashiCorp), productivity/SaaS (Linear, Notion, Airtable, Zapier, Cal.com), design tools (Figma, Framer, Webflow, Miro), fintech (Stripe, Coinbase, Binance, Wise), e-commerce/retail (Apple, Nike, Shopify, Starbucks), media (Spotify, Uber, SpaceX, WIRED), and automotive (Tesla, Ferrari, BMW, Lamborghini). A separate "Retro Web" series recreates 1990s/2000s-era sites (Dell 1996, Nintendo.com 2001) as period-accurate DESIGN.md files. The README states the repo is ranked roughly #150 globally on GitHub by stars.

## Key takeaways

- Usage pattern: copy a site's DESIGN.md into the project root and instruct an AI agent to build UI matching it — no additional tooling or schema required, since the file is plain Markdown.
- Each file explicitly separates semantic color roles (not just hex values) and captures do's/don'ts guardrails and an "agent prompt guide" section aimed specifically at LLM consumption, distinguishing it from a generic style guide.
- The README states design tokens represent publicly visible CSS values and explicitly disclaims ownership of any site's visual identity; files are described as analysis of public sites, not official brand assets from those companies.
- The README embeds sponsored/promotional listings for two unrelated third-party products (a social-scheduling tool and a starter-template product) within the collection page itself, alongside the DESIGN.md catalog entries.

## Security

MIT licensed. Content is entirely static Markdown and HTML preview files — no executable code, install step, or runtime component. The only integration surface is copying a file into a project and having an agent read it as design guidance, so there is no code-execution or dependency-supply-chain risk from the repository itself. The promotional third-party listings embedded in the README are unrelated to the DESIGN.md assets and do not appear inside the design files themselves.