---
name: vscode-port-forwarding-devtunnels
title: VS Code Port Forwarding via Dev Tunnels (Public Localhost Sharing)
url: https://www.instagram.com/reel/DfCdgxvDwVG/
source_url: https://www.instagram.com/reel/DfCdgxvDwVG/
source: instagram
category: agent-pattern
summary: Technique for sharing a locally-running dev server with anyone over the internet using VS Code's built-in Ports panel — run the project, note the port, open the Ports view, use Forward a Port, then open the generated URL's context menu and set Port Visibility to Public so viewers reach it without GitHub sign-in. The underlying mechanism is Microsoft Dev Tunnels (URLs resolve to *.devtunnels.ms); forwarded ports default to Private (requires sign-in with the same GitHub account used to start forwarding) and must be explicitly switched to Public to work as a no-login share link. Works for any local server (the reel demonstrates a full-stack Vite/React PDF-tools clone) as long as the process keeps running on the local machine — the tunnel relays traffic, it does not host the app independently.
tags:
  - vscode
  - port-forwarding
  - dev-tunnels
  - localhost-sharing
  - web-dev
  - networking
  - remote-access
  - demo-sharing
reviewed: 2026-10-30
acquired: 2026-10-30
license: N/A
security_flags:
  - public-visibility-removes-auth
  - exposes-whatever-runs-on-port
overlaps: []
---

## What it does

VS Code ships built-in support for Microsoft Dev Tunnels, letting a developer expose a local dev server to anyone over the internet without a separate tunneling tool (e.g. ngrok): run the project locally, note its port, open the **Ports** view (bottom panel, next to Terminal, or via the **Ports: Focus on Ports View** command), click **Forward a Port**, and enter the port number. VS Code generates a URL of the form `https://<random-id>.devtunnels.ms` that proxies traffic to the local port.

By default the forwarded port's visibility is **Private**: anyone opening the URL must sign in with the same GitHub account used to start forwarding. To share it as a no-login link — the behavior the source reel shows — the user must right-click the port and set **Port Visibility → Public**; the reel's transcript does not mention this step or the Private default it bypasses. Once public, any URL holder reaches the service with no authentication of their own. The technique works for any locally-running full-stack process (the reel demos a Vite/React PDF-tools app); the one real condition is that the local process must keep running, since the tunnel only relays to it rather than hosting the app itself.

## Sources

- [Instagram reel, "Share Your Localhost LIVE With Anyone!"](https://www.instagram.com/reel/DfCdgxvDwVG/) — caption, transcript, and on-screen demo of the Ports-panel forwarding flow (catalog source).
- [GitHub Docs, "Forwarding ports in your codespace" (VS Code tab)](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace?tool=vscode) — documents the Private default, the GitHub sign-in requirement, and the Port Visibility → Public setting that removes it.

## Security

Switching a forwarded port's visibility to Public removes the GitHub sign-in gate entirely — the resulting `*.devtunnels.ms` URL grants any holder direct, unauthenticated access to whatever is running on that local port, for as long as the tunnel stays open. Because a typical local dev server has no auth of its own (debug endpoints, unpulled migrations, seeded test data, verbose error pages), making it Public is equivalent to deploying it to the open internet without the hardening a real deployment would have. Default-Private + GitHub sign-in is the safer mode for a known reviewer; Public should be scoped to the minimum needed time and closed (or re-forwarded) afterward.