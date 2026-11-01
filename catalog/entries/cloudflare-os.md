---
name: cloudflare-os
title: Cloudflare OS
url: "https://github.com/cloudflare/cloudflare-os"
category: framework
summary: "Cloudflare's open-sourced internal 'agent workspace' platform on Workers/Durable Objects — sandboxed per-user 'Gadgets' (AI-built mini-apps) governed by capability-based 'Gatekeeper' services that mediate external-API access and support async human-in-the-loop approval"
tags: [cloudflare-workers, durable-objects, agent-workspace, sandboxing, capability-based-security, gadgets, mcp-alternative, apache-2.0]
reviewed: 2026-08-09
acquired: 2026-08-09
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Cloudflare OS is an "AI productivity environment" that Cloudflare built and used internally, now released as open source (v2, a full rewrite of an internal v1) so other organizations can fork it into "Your Company OS." It provides three parts: an agent chat UI preloaded with company context, sandboxed application development where agents build small personal apps called "Gadgets," and a capability-based security layer called "Gatekeepers" that mediates every connection between an agent/Gadget and an external service.

**Gadgets**: instead of a shared multi-tenant SaaS app, each user gets their own private, sandboxed instance of whatever app they ask an agent to build (e.g., a slide-deck tool, a whiteboard, a game). The server half runs in a Cloudflare Dynamic Worker Facet with no default internet access; the client half runs in a sandboxed iframe that can only talk to its own server via Cap'n Web RPC over `postMessage`. Because client and server communicate over Cap'n Web, every Gadget automatically exposes an agent-callable API with no separate MCP server needed. Gadgets support real-time multiplayer (each is backed by a Durable Object) and can be shared as "Blueprints" — copyable source templates, not shared hosted instances, so a recipient gets their own independently modifiable copy.

**Gatekeepers**: a per-external-service Worker that wraps that service's native API in a Cap'n Web interface, handles OAuth, restricts access to only the specific resource introduced to an agent, logs every action, and supports side-effecting actions. For actions requiring approval, a Gatekeeper simulates the outcome locally so the agent can keep working immediately; the human reviews and approves/rejects the queued real actions later (individually or in bulk), instead of the agent blocking synchronously on each approval. Shipped Gatekeepers in the repo cover GitHub, Google, Cloudflare, Supabase, Notion, Confluence, email, Home Assistant, Slack, Spotify, and ZoomInfo APIs.

Access is capability-based and zero-by-default: neither an agent nor a Gadget has access to any external resource until a human (or the agent, pending human approval) explicitly introduces that specific resource — a contrast to MCP setups where configured servers are ambiently available in every chat.

## Differentiators

- Every Gadget is its own sandboxed instance per user (analogous to a desktop/mobile app model) rather than a shared hosted service, which the README argues removes an entire class of cross-tenant data-leak bugs by construction.
- Gatekeepers' asynchronous "simulate now, approve later" pattern is presented as an alternative to synchronous human-in-the-loop approval (and to blanket `--dangerously-skip-permissions`-style auto-approval).
- Built directly by the Cloudflare Workers runtime team, using and co-developing Workers primitives (Dynamic Workers, Facets) specifically to support this project; every workspace is a Durable Object.
- The coding agent is a general-purpose "Code Mode" agent (writes and executes code snippets) that can act with or without producing a Gadget.

## Mechanical details

- Quick local run: install `pnpm`, then `pnpm run-local`; visits `http://localhost:8787`; runs the full stack on `wrangler`/`workerd` (not intended for production; data lands in a local `.wrangler` directory).
- Production deploy: hosted flow at `os.cloudflare.app/deploy` to deploy to a user's own Cloudflare account, or a separate `cloudflare/cloudflare-os-starter` repo for a customized deployment with one's own Gatekeepers.
- Development mode runs frontend and backend as separate processes (`pnpm dev-server`, `pnpm dev-client`), served at `http://localhost:3000`.
- Each Gatekeeper package documents its own OAuth client-credential setup steps for the third-party service it wraps.
- Status: "Early access" — described in the README as v2, a complete rewrite of v1, with "many rough edges." The project is not currently accepting outside code contributions beyond small (~dozen-line) fixes; larger ideas are directed to a GitHub Discussion instead.
- Notable dependencies credited in the README: `pi-agent-core` (multi-LLM-provider support), Monaco editor, Yjs (client/agent sync), Vite.

## Security

Apache-2.0 licensed (confirmed via the npm/GitHub license field as of the August 2026 open-source release; the README itself does not state the license inline). Built on Cloudflare Workers/Durable Objects/Dynamic Workers — a sandboxed multi-tenant serverless runtime rather than a general-purpose VM, which is the basis for the project's sandboxing claims (Gadget servers have no default internet access; Gadget clients run in a `Content-Security-Policy`- and `sandbox`-restricted iframe). Capability-based access control is zero-by-default for both agents and Gadgets. The project self-describes as "early access" with "heavy development" and "many rough edges," and third-party coverage from its August 2026 launch reported roughly 5,100+ stars and 387 forks within a day of announcement — a young public codebase by a well-resourced vendor, not yet independently security-audited per the fetched material. External code contributions are explicitly discouraged beyond trivial fixes, which limits community security review via pull request at this stage.