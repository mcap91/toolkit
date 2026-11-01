---
name: agent-plugins-vscode
title: Agent Plugins in VS Code (Agent Plugins 1.0)
url: "https://code.visualstudio.com/docs/agent-customization/agent-plugins"
category: reference
summary: "VS Code docs for Agent Plugins 1.0, an open vendor-neutral standard (Vercel, AWS, Cursor, GitHub, Microsoft, OpenAI) for packaging portable Agent Skills + MCP servers into one installable plugin folder, working across VS Code, GitHub Copilot, Cursor, ChatGPT/Codex, and Kiro; Claude Code is not a coalition member but plugins install into it via format translation"
tags: [agent-plugins, open-standard, mcp, skills, vs-code, github-copilot, plugin-marketplace, interoperability]
reviewed: 2026-08-09
acquired: 2026-08-09
license: unlicensed
security_flags: [implicit-trust-mcp-install, no-provenance-verification, spec-status-ambiguous]
overlaps: [agent-skills-spec]
source: unknown
---

## What it says

Agent Plugins 1.0 was announced August 6, 2026 by a coalition (Vercel, AWS, Cursor/Anysphere, GitHub, Microsoft, OpenAI) as an open standard for packaging AI agent extensions. A plugin is a directory with a `plugin.json` manifest, an optional `skills/` folder holding Agent Skills (the SKILL.md format), and an optional `mcp.json` configuring MCP servers — these two component types (skills, MCP servers) are the only ones defined as portable across clients. Custom agents, hooks, and slash commands are left as client-specific extensions under reverse-domain namespaces (e.g., Claude's `.claude-plugin/plugin.json`, `${CLAUDE_PLUGIN_ROOT}`).

VS Code auto-detects four plugin formats by manifest location/schema: Agent Plugins 1.0 (`plugin.json` with the canonical `$schema`), Copilot (`plugin.json` without that schema, the default fallback), Claude (`.claude-plugin/plugin.json`), and legacy OpenPlugin (`.plugin/plugin.json`). Plugins are discovered from configured marketplaces (Git repos; defaults are `copilot-plugins` and `awesome-copilot`) or installed directly from a Git URL. Workspace-level recommendations are configured via `.claude/settings.json` or `.github/copilot/settings.json` (`extraKnownMarketplaces`, `enabledPlugins`).

## Differentiators / Key takeaways

- Anthropic is not part of the launch coalition despite having authored the Agent Skills spec (SKILL.md) that Agent Plugins 1.0 packages, and Claude Code is not a launch client — but Anthropic's `.claude-plugin` format is still natively recognized by VS Code, and the plugins CLI translates the portable format into Claude Code's own plugin format for installation.
- The standard is intentionally narrow (skills + MCP servers only as portable types) — it does not attempt to standardize hooks, custom agents, or slash commands, which remain per-client.
- Governance is early-stage per external coverage: the spec page reportedly reads "Status: Working Draft" while the repo README calls 1.0.0 the current published release, with no corresponding git tag or GitHub Release; a "future considerations" doc reportedly names provenance verification as an unaddressed gap.
- Builds directly on the pre-existing Agent Skills open standard (see `agent-skills-spec` in this catalog) by making skill folders one of two portable payload types inside a larger installable-bundle format aimed at marketplace distribution, rather than defining a new skill format itself.

## Mechanical details / What to adopt

- Enable/inspect in VS Code via `chat.plugins.enabled` and `chat.plugins.marketplaces` settings; local unpublished plugins register via `chat.pluginLocations`.
- Plugin MCP servers start/stop automatically with plugin enable/disable and appear alongside workspace/user-level MCP servers in the same tool list.
- Hooks (when present, client-specific) use the same `hooks.json` shape as Claude Code hooks, including matcher syntax — though VS Code currently ignores matcher values and runs on every event of that type.
- Install from source via the `Chat: Install Plugin From Source` command with a Git repo URL; install from marketplace via the `@agentPlugins` filter in the Extensions view.

## Security

Documentation page carries no software license itself (informational/reference). The doc explicitly warns: "Plugins can include hooks and MCP servers that run code on your machine. Review the plugin contents and publisher before installing, especially for plugins from community marketplaces." Plugin MCP servers are implicitly trusted at install with no separate trust prompt (unlike workspace-level MCP servers, which do get one) — flagged in external coverage as an open provenance-verification gap in the standard as of its August 2026 1.0 launch. Treat third-party marketplace plugins as arbitrary-code-execution surface until the standard's provenance story matures.
