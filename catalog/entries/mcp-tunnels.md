---
name: mcp-tunnels
title: MCP Tunnels (Anthropic)
url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview"
category: reference
summary: "Anthropic research-preview feature connecting Claude to MCP servers inside private networks — outbound-only tunnel via cloudflared + Anthropic proxy, no inbound firewall rules or public endpoints needed; completes the enterprise security story for Claude Managed Agents alongside self-hosted sandboxes"
tags: [mcp, anthropic, tunnels, enterprise, private-network, firewall, cloudflare, managed-agents, security]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [a2a-protocol, bedrock-agentcore-gateway]
license: proprietary
security_flags: []
source: unknown
---

## What it does

MCP Tunnels is an Anthropic research-preview feature that connects Claude to MCP servers running inside private networks without exposing them to the public internet. It reverses the connection direction: instead of Claude reaching into a private network, a small connector inside the network reaches out and holds the line open.

The tunnel stack has two components running inside the customer's network:

1. **cloudflared**: Cloudflare's open-source tunnel connector. Initiates outbound-only connections to the tunnel edge and carries encrypted traffic from Anthropic to the proxy.
2. **Proxy**: Anthropic's routing component. Receives traffic from the tunnel, terminates a second layer of encryption, and routes each request to the correct internal MCP server based on hostname.

This eliminates the need for inbound firewall rules, public endpoints, or IP allowlisting. Enterprise teams can connect internal databases, private APIs, and on-prem knowledge bases to Claude without exposing those systems publicly.

The feature is part of Anthropic's broader MCP Connector infrastructure, which also includes embedded UI, enterprise-managed auth, and observability. Together with self-hosted sandboxes, MCP Tunnels addresses the two blockers that made MCP impractical for regulated environments: inbound network exposure and per-developer credential sprawl.

## Assessment

Reference documentation for an Anthropic platform feature. Relevant context when evaluating whether MCP-based tools can be deployed in enterprise/private-network environments. The feature depends on Cloudflare's network (third-party dependency with no availability commitment for the underlying transport). Research preview status means no uptime, support, or continuity guarantees — Anthropic may modify or discontinue at any time.

## Security

Proprietary Anthropic service. Outbound-only connections (no inbound firewall exposure). Double-encrypted: cloudflared tunnel encryption + Anthropic proxy layer. Depends on Cloudflare infrastructure as third-party transport. Research preview — no SLA.