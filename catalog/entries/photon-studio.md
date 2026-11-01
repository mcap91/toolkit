---
name: photon-studio
title: Photon Studio
url: "https://tenzen.studio/photon/"
category: framework
summary: "Free proprietary desktop image editor (macOS/Windows 11/Linux) from Tenzen Studio positioned as a Photoshop alternative — layers, masks, smart objects, curves, liquify, local (on-device) background removal, and native PSD read/write; local-first with no upload or account required; reported by press as built largely via AI-assisted ('vibe-coded') development for roughly $2,000 in model tokens"
tags: [photo-editing, image-editor, photoshop-alternative, desktop-app, psd, vibe-coded, local-first, proprietary, closed-source]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Proprietary
security_flags: [closed-source, unverified-user-claims]
overlaps: []
source: unknown
---

## What it does

Photon Studio is a free desktop image editor and design tool from Tenzen Studio, distributed for macOS, Windows 11, and Linux. It combines photo editing with layer-based design work: groups, masks, adjustment layers, smart objects, layer effects (shadows, glows, strokes, overlays), editable text, vector shapes, pen paths, brushes, and gradients. Retouching tools include healing brush, clone stamp, content-aware fill, and Liquify; color/tone adjustments are handled via Curves and Levels with live preview. Subject selection and background removal run through an on-device model rather than a cloud API. The application reads and writes PSD files natively (the vendor notes some Photoshop-specific features may not transfer identically) and includes a command-search palette for finding tools/menu items by name, plus Photoshop-style customizable keyboard shortcuts.

All processing is local — no upload step, no processing queue, and no account required to open and edit a file. Distribution is via the vendor's site (tenzen.studio/photon), which gates the download behind an email address; there is no public source repository.

## Differentiators / Key takeaways

Photon Studio's origin was widely reported in tech press (Yahoo Tech, Gadget Review, and others) and on Reddit's r/vibecoding: the developer described spending approximately $2,000 in AI model tokens (primarily OpenAI's GPT-6 Astra, described as used for both planning and iterative bug-fixing) to build the application, framed as a personal project to replace their own Adobe Creative Cloud subscription. The vendor's own product page and blog post make no mention of this development methodology — the "vibe-coded" framing comes entirely from third-party press coverage and the developer's social-media posts, not from Tenzen Studio's official materials.

User-count claims vary by source and should be read as unverified: press coverage citing the developer's own r/vibecoding post and a follow-up X post reported roughly 170 downloads on launch day and 458 total downloads shortly after. A later post from the Tenzen Studio X account claimed the app "already has 20k users" and that images can be edited "through Codex or Claude Code" — neither the user-count jump nor the Codex/Claude Code integration claim is documented or verifiable on the vendor's product page.

Reviewers (e.g., Appmiao, cited in press roundups) place it alongside GIMP, Krita, and Photopea as a free Photoshop-adjacent option, but note it is not a full replacement for professional workflows that depend on plugins, color management, or print pipelines.

## Mechanical details / What to adopt

Download is gated behind providing an email address on tenzen.studio/photon; no account/login is required afterward. Supported OSes: macOS, Windows 11, Linux. All image processing, including AI-based subject selection/background removal, runs on-device rather than via a server API.

## Security

License: Proprietary/closed-source freeware — no SPDX identifier applies; no source code is published.

Security flags:
- `closed-source`: no source repository is available, so claims about local-only processing, the on-device background-removal model, and data handling cannot be independently verified.
- `unverified-user-claims`: the vendor's "20k users" and Codex/Claude Code image-editing integration claims (from an X/Twitter post) are not corroborated by the product page or by independent press, which instead reported download counts roughly two orders of magnitude lower (170–458).

The download flow collects an email address before granting access to the installer, which is a mild data-collection point beyond the tool's core "no account required" claim.