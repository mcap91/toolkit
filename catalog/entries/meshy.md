---
name: meshy
title: Meshy
url: https://www.meshy.ai/
source_url: https://www.instagram.com/reel/DeuMK6FJhoc/
source: instagram
category: framework
summary: Commercial AI 3D-content platform — generates textured 3D models from text prompts ("Text to 3D") or images ("Image to 3D"/"Multi-Image to 3D"), plus AI texturing (PBR maps), auto-rigging, animation, remeshing/file conversion, and print-ready STL/3MF export; preview mesh in ~30s, textured model in under 2 minutes on the default Meshy 6 model, Meshy 7.1 branded for closer reference fidelity; bulk generation up to 50+ simultaneous tasks; access via web app, mobile app, REST API (official Python/Node.js SDKs), a Meshy MCP server, ComfyUI nodes, and Blender/Unity/Unreal plugins; for coding agents specifically, ships an open-source skill pack (`meshy-dev/meshy-3d-agent`, installed via `npx skills add meshy-dev/meshy-3d-agent`) with Claude Code/Cursor/OpenClaw skills that call the REST API directly, no MCP server required; closed-source hosted SaaS, Free (100 credits/mo, generated assets public) up to Pro $20/mo, Premium $40/mo, Ultra $100/mo, Studio from $60/mo, Enterprise custom; API-generated assets auto-delete after 3 days (non-Enterprise) per the API docs, though Meshy's own pricing page separately states 14 days for Studio — the two official pages disagree; SOC 2 Type 2, ISO 27001:2022, and GDPR compliance claimed.
tags:
  - text-to-3d
  - image-to-3d
  - 3d-model-generation
  - ai-texturing
  - rigging
  - animation
  - saas
  - mcp-server
  - claude-code-skill
  - game-development
reviewed: 2026-10-29
acquired: 2026-10-29
license: proprietary
security_flags:
  - closed-source
  - cloud-asset-storage
  - free-tier-public-assets
overlaps: []
---

## What it does

Meshy is a commercial AI platform for generating 3D content: text-to-3D and image-to-3D model generation, AI texturing (PBR diffuse/roughness/metallic/normal maps via text prompt), auto-rigging, animation, remeshing/file-format conversion, and print-ready STL/3MF export with printability checks. A preview mesh renders in roughly 30 seconds; a fully textured model completes in under 2 minutes on the current default model (Meshy 6), with the newer Meshy 7.1 marketed for closer fidelity to a reference image. Bulk generation supports 50+ simultaneous tasks for asset-pipeline use.

Access paths: the web app, a mobile app, a REST API with official Python and Node.js SDKs, a Meshy-hosted MCP server, ComfyUI custom nodes, and official plugins for Blender, Unity, and Unreal Engine. For AI coding agents specifically, Meshy publishes an open-source skill pack (`meshy-dev/meshy-3d-agent`, installed via `npx skills add meshy-dev/meshy-3d-agent`) providing ready-made Claude Code, Cursor, and OpenClaw skills that call the REST API directly to generate, texture, rig, and animate models and prepare 3D-printable files — no MCP server needed. A separate MCP server is offered for MCP-based clients (Claude Code, Cursor, Windsurf, Codex) that prefer that integration path instead.

## Mechanical details

- Pricing: Free (100 credits/month, generated assets public); Pro $20/mo (1,000 credits); Premium $40/mo (3,000); Ultra $100/mo (10,000); Studio from $60/mo or seat-based team pricing; Enterprise custom.
- Credit costs: Text to 3D 20 credits (10 on the "Lite" model); Image to 3D 20-30 credits depending on model/texture tier; AI texturing from 10 credits; auto-rigging 5 credits; animation 3 credits; remesh 5 credits; file conversion/resize 1 credit each. Failed generations are not charged; canceled tasks are refunded.
- API-generated assets auto-delete after 3 days on non-Enterprise plans per Meshy's API docs; Meshy's separate pricing page states 14 days of retention for Studio — the two official pages disagree on this figure. Enterprise plans get unlimited asset retention.
- Closed-source hosted SaaS, no self-hosted option; web app data stored on AWS in the US. Meshy's pricing FAQ states it will not use account data for training without consent. Compliance claims: SOC 2 Type 2, ISO 27001:2022, GDPR (per Meshy's published trust center).

## Security

- `closed-source` — proprietary SaaS; all generation runs on Meshy's infrastructure, no self-hosted option.
- `cloud-asset-storage` — uploaded prompts/images and generated models are stored on Meshy's AWS infrastructure; non-Enterprise API assets persist only 3-14 days (official pages disagree) before auto-deletion; Enterprise retention is unlimited.
- `free-tier-public-assets` — on the Free plan, generated models are publicly visible to other users; commercial use is permitted but requires crediting Meshy.
- The agent-skill install path (`meshy-3d-agent`) authenticates via a CLI-stored session (`meshy auth login`, or `--device` for headless/CI) shared across that OS user's skill installs — treat the stored session like any other long-lived API credential.

## Sources

- [Meshy — AI 3D Model Generator](https://www.meshy.ai/) — product site, pricing, features
- [Meshy Docs](https://docs.meshy.ai/en) — API/web-app documentation, retention policy
- [meshy-dev/meshy-3d-agent](https://github.com/meshy-dev/meshy-3d-agent) — official Claude Code/Cursor/OpenClaw skill pack
- [Instagram reel](https://www.instagram.com/reel/DeuMK6FJhoc/) — catalog source; creator describes Meshy as producing inconsistent, style-inconsistent "slop" results for AI-accelerated game development, and prefers writing custom procedural-generation code with a coding agent instead