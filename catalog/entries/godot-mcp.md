---
name: godot-mcp
title: Godot MCP (Coding-Solo)
url: https://github.com/Coding-Solo/godot-mcp
source_url: https://www.instagram.com/reel/De369jptIw-/
source: instagram
category: mcp-server
summary: MCP server (npm package @coding-solo/godot-mcp) that lets an AI agent launch the Godot editor, run a project in debug mode, capture debug/error output, list projects in a directory, query the installed Godot version, and manage UIDs for Godot 4.4+; installs via `claude mcp add godot -- npx @coding-solo/godot-mcp`; the most-forked and most-cited server under the generic 'Godot MCP' name per third-party MCP-server directories, ahead of numerous same-named community forks and rewrites that add scene-tree editing, screenshot capture, and C# support; MIT.
tags:
  - godot
  - mcp-server
  - claude-code
  - game-development
  - debugging
  - typescript
  - npm
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

Godot MCP is a Model Context Protocol server that gives an AI coding agent a feedback loop into the Godot game engine: it can launch the Godot editor for a given project, run a project in debug mode and capture its debug output (including runtime errors), list Godot projects found under a directory, retrieve the installed Godot engine version, and manage resource UIDs introduced in Godot 4.4+. The project's own framing is that direct run/debug feedback — rather than just generating code blind — helps an agent tell what works from what doesn't and produce better fixes. A bundled script accepts an operation type and JSON parameters, so operations run without the server generating a temporary file per call.

## Mechanical details

- **Install**: `claude mcp add godot -- npx @coding-solo/godot-mcp`, or clone (`git clone https://github.com/Coding-Solo/godot-mcp.git`), `npm install`, `npm run build`. Published to npm as `@coding-solo/godot-mcp`.
- **Stack**: Node.js/TypeScript MCP server; not an official Godot Engine product — maintained by a single named author (Solomon Elias / Coding-Solo).
- Multiple other projects share the generic "Godot MCP" / "godot-mcp" name and build on or diverge from this one — e.g. forks adding scene-tree editing, live screenshot capture, and C#/.NET project support, and at least one unrelated GDScript-native rewrite avoiding Node.js entirely. This entry covers the Coding-Solo original specifically, identified by its npm package and GitHub path; a captured reel naming "Godot MCP" without a link cannot be matched to a specific fork with certainty.

## Security

Local developer tool — launches a local Godot editor/project process and reads its output; no network service, credential handling, or elevated-privilege pattern observed in the README. MIT licensed.

## Sources

- [GitHub: Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) — README: feature list, install command, license
- [Instagram reel](https://www.instagram.com/reel/De369jptIw-/) — named "Godot MCP" (no link) as one of five repos that "turn Claude into an entire game studio," describing it as building the scene, playing the game, and self-correcting on errors (catalog source)