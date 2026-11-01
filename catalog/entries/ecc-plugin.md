---
name: ecc-plugin
title: Everything Claude Code (ECC)
url: "https://www.claudepluginhub.com/plugins/affaan-m-everything-claude-code"
category: plugin
summary: rate-limited (429 errors); trial when accessible
tags: [plugin, hub, all-in-one]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: [unverified-content, bundled-install, npx-remote-exec]
overlaps: []
source: unknown
---

## What it does

An all-in-one plugin package distributed through the Claude Plugin Hub. Bundles multiple capabilities into a single install command. Encountered 429 rate limit errors across three attempts in two separate sessions during the review period, preventing content verification.

## Assessment

Cannot fully evaluate without access. The bundled approach may introduce conflicts with the existing superpowers stack similar to the concerns with claude-spellbook. Rate limiting suggests high demand but also infrastructure instability. Low priority — trial when the plugin hub rate limit clears and the content can be verified.

## Mechanical details

Install: `npx claudepluginhub affaan-m/ecc --plugin ecc`. If the rate limit has cleared, trial in an isolated project before adding to the main stack. Evaluate for overlap with superpowers and existing skills before enabling broadly.

## Security

License is unknown — the plugin hub page was unreachable during review (429 errors), so no license, source code, or publisher verification was possible. The install mechanism (`npx claudepluginhub`) executes remote code directly without a pinned version, which is a supply-chain risk common to the npx-remote-exec pattern. The bundled all-in-one nature means the attack surface is wider than a single-purpose plugin; if any bundled component is malicious or compromised, the entire install is affected. Trial only in an isolated project with no access to production credentials or sensitive directories until the content can be verified and the publisher's identity confirmed.

## How to use it

npx claudepluginhub affaan-m/ecc --plugin ecc
