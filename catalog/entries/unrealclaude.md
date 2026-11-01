---
name: unrealclaude
title: UnrealClaude
url: https://github.com/Natfii/UnrealClaude
source_url: https://www.instagram.com/reel/De369jptIw-/
source: instagram
category: plugin
summary: Unreal Engine 5.7 editor plugin that docks a Claude Code chat panel in the editor and shells out to the local `claude` CLI (no separate API key) for in-editor assistance, plus a bundled Node.js MCP bridge exposing 20+ tools for actor manipulation, Blueprint/Animation-Blueprint editing, level management, materials, and Enhanced Input; by default the plugin invokes `claude -p --skip-permissions` for every prompt, removing Claude Code's human-in-the-loop approval step unless the integrator changes AllowedTools in C++; a separate 'Auto-approve script execution' project setting (default OFF) controls whether Python/C++/console scripts triggered through the bridge or chat run without a per-script permission dialog; hidden MCP tools (execute_script, run_console_command) can reach the Python interpreter if un-hidden by editing source; Windows/Linux/macOS (Apple Silicon); MIT; built from source, no prebuilt binaries.
tags:
  - unreal-engine
  - claude-code
  - mcp-server
  - editor-plugin
  - blueprints
  - game-development
  - cpp
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags:
  - skip-permissions-by-default
  - unsandboxed-script-execution-available
overlaps: []
---

## What it does

UnrealClaude integrates the Claude Code CLI directly into the Unreal Engine 5.7 Editor: a docked chat panel (Tools → Claude Assistant) streams responses, groups tool calls, and renders code blocks, using the user's existing Claude Code authentication (Claude Pro/Max subscription or API access) rather than a separate API key. The plugin automatically gathers project context (source modules, enabled plugins, project settings, recent assets, a custom `CLAUDE.md`) and a dynamic UE 5.7 API-context loader (`unreal_get_ue_context`) feeds accurate engine documentation to Claude on demand, queryable by category (animation, blueprint, slate, actor, assets, replication) or keyword search.

A bundled Node.js MCP bridge (a separate repo, included as a submodule) runs an MCP server on port 3000 that starts automatically with the editor, exposing 20+ tools across actor manipulation (spawn/move/delete/inspect/set-properties), level management (open/create/list templates), Blueprint and Animation-Blueprint editing (variables, functions, nodes, pins, full state-machine editing including batch operations), asset search with dependency/referencer queries, character and material tools, Enhanced Input action/mapping management, and utility tools (console commands, output log, viewport capture, script execution) — plus an async task queue so long-running operations don't time out. Claude can write, compile via Live Coding, and run Python/Console/Editor-Utility scripts, each gated by a per-script permission dialog unless auto-approval is turned on. Conversation history persists per-project (`Saved/UnrealClaude/`) across editor sessions.

## Mechanical details

- **Build**: no prebuilt binaries — clone with `git clone --recurse-submodules`, build via `RunUAT.bat/.sh BuildPlugin` for the target platform (Win64/Linux/macOS), then copy the build output into the project's or engine's `Plugins/` directory and run `npm install` inside the bundled `mcp-bridge` folder.
- **Default execution path**: per the README's "How It Works" and "Command Line Equivalent" sections, every chat-panel prompt is sent via `claude -p --skip-permissions --allowedTools "Read,Write,Edit,Grep,Glob,Bash" --append-system-prompt "..." "your prompt"` — i.e. permission prompts for Claude Code's own tool calls are skipped by default for every prompt sent through the panel; the allowed-tool set is editable only by changing `Config.AllowedTools` in `ClaudeSubsystem.cpp` and rebuilding.
- **Script execution gating**: "Auto-approve script execution" (Project Settings → Plugins → Unreal Claude, default OFF) governs whether Python/C++/Console/Editor-Utility scripts run immediately or show a confirmation dialog; auto-approved runs still log to `LogUnrealClaude`. The MCP bridge deliberately hides `execute_script`, `run_console_command`, `cleanup_scripts`, and `get_script_history` from the model's tool list by default (`HIDDEN_TOOL_NAMES` in `tool-router.js`) — the README's own warning states that un-hiding `run_console_command` "can reach the Python interpreter... treat un-hiding it as enabling arbitrary code execution; keep it to trusted setups only." Hidden tools remain callable by exact name and still pass through the C++ permission dialog.
- **Platforms**: Windows (Win64), Linux (Rocky/Fedora package list given), macOS (Apple Silicon) — each with its own install doc (`INSTALL_MAC.md`, `INSTALL_LINUX.md`).
- Credits list community contributors for Linux and Mac support; MCP bridge ships its own Vitest test suite, runnable standalone without a running Unreal Editor.

## Security

Two separate security-relevant defaults: (1) the chat panel's default invocation skips Claude Code's own permission prompts for every prompt sent through it (`--skip-permissions`), unlike a stock Claude Code session; (2) script execution (Python/C++/console) is gated by a per-script dialog that defaults to ON (i.e., scripts require confirmation) unless the integrator flips "Auto-approve script execution" to always-run — the README explicitly calls un-hiding `run_console_command` an arbitrary-code-execution path and recommends trusted setups only. No prebuilt binaries are distributed — users build from source, reducing supply-chain risk relative to a signed release. MIT licensed.

## Sources

- [GitHub: Natfii/UnrealClaude](https://github.com/Natfii/UnrealClaude) — README: features, install, default CLI invocation, hidden-tool warning, license
- [Instagram reel](https://www.instagram.com/reel/De369jptIw-/) — named the tool ("Unreal Claude") as one of five repos that "turn Claude into an entire game studio" (catalog source; no link given in the reel itself)