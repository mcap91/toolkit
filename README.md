# toolkit

A hand-curated catalog of tools, techniques, and references for building with coding agents. Each
entry is written so an agent can use it without re-fetching the source. The repo also ships a small,
read-only MCP server (a background program that exposes callable tools to an agent over the Model
Context Protocol) for searching the catalog, and a set of Claude Code skills.

## Use the catalog

Three ways to get at it:

1. **Browse it on GitHub.** Open [`catalog/index.md`](catalog/index.md).
2. **Point an agent at the raw file.** Fetch
   `https://raw.githubusercontent.com/mcap91/toolkit/main/catalog/index.md` — no server, no MCP
   registration required.
3. **Run the MCP server** and let an agent call `search` and `index` directly:

   ```bash
   npx tsx packages/catalog-mcp/src/server.ts
   ```

   Register it in your project's `.mcp.json`:

   ```json
   {
     "mcpServers": {
       "toolkit-catalog": {
         "type": "stdio",
         "command": "npx",
         "args": ["tsx", "PATH/TO/toolkit/packages/catalog-mcp/src/server.ts"],
         "env": {}
       }
     }
   }
   ```

   Replace `PATH/TO` with the path to your local clone.

## What an entry looks like

Every entry follows the same section order:

- **What it is** — what the thing is, in a few sentences.
- **How it works** — components, the core loop or algorithm, key data structures and config.
- **How to use it** — install, run, and integration points.
- **Evaluation and limits** — how it's measured, the numbers, failure modes, pushback.
- **Context from the source** — what the original link added: claims, use case, discussion.
- **Related** — other catalog entries and how they connect.
- **Security** — a factual security read, not a verdict.

[`catalog/recipe.md`](catalog/recipe.md) is today's working description of this template; a standalone
template file is being extracted from it.

## Skills

Copy any skill into a project:

```bash
cp -r skills/<name> <your-project>/.claude/skills/<name>
```

| Skill | Description |
|---|---|
| [agent-lockdown](skills/agent-lockdown/) | Pin an interactive coding agent CLI to a reproducible state — version pin, model pin, env config, file-read deny rules, model selector, and integrity checkup. Modes — lockdown (default), checkup (integrity audit), upgrade-check (diff CLI versions). |
| [blueprint](skills/blueprint/) | Create a portable, project-agnostic architecture reference document for a tool, module, or system. |
| [catalog-intake](skills/catalog-intake/) | Full catalog pipeline — Gmail pull, inbox curation, drain, and headless processing. |
| [explain-me-this](skills/explain-me-this/) | Discuss-and-explain mode — help me understand or decide, no building. Manual-only. |
| [html-report](skills/html-report/) | Build an HTML report or view in the house style. Five self-contained style pages ship with the skill: chain view, science report, text report, concept page, architecture (via archify). |
| [handoff](skills/handoff/) | Generate a self-contained prompt to hand off current work to a fresh CLI agent or a subagent. |
| [ntfy-bridge](skills/ntfy-bridge/) | Set up a phone bridge over ntfy.sh — one-way notifications for pipelines, or a two-way channel for an unattended Claude Code session to receive operator replies. |
| [plan-me-this](skills/plan-me-this/) | Package an approved spec into self-contained phase docs and a living readme_this_current_task.md. |
| resolve (moved to [kb](https://github.com/mcap91/kb) `contract/skills/resolve/`) | Before escalating a question to the operator, resolve it from evidence. Will ship to repos via kb `sync-contract` once its trials pass. |
| [scripts-reference](skills/scripts-reference/) | Generate a Markdown reference file listing production scripts in a project — name, namespace, brief description, and clickable absolute file path. |
| [spec-check](skills/spec-check/) | Read doc(s) and surface open design decisions that need operator input before the work can be handed off for autonomous execution. |
| [verticalizing-plans](skills/verticalizing-plans/) | Convert phase-shaped plans organized as sequential stages into thin vertical slices that prove the whole flow early. |
| [wrap-up](skills/wrap-up/) | End-of-session housekeeping. Runs available checks (typecheck, wiki lint/generate), detects dual-repo setup, commits and pushes safely. |
| [write-plain](skills/write-plain/) | House style for any prose an agent writes for a human reader — plain hyphens only, no AI tells, active voice, short sentences. |

[`statusline/`](statusline/) is a separate tool, not a skill: a status bar for the Claude Code CLI
that shows model name and context window usage.

## Benchmarks

- [Search eval](docs/benchmarks/search-eval.png) — catalog search quality across query styles.
- [Web capture benchmark](docs/benchmarks/web-capture.html) — three browser-capture engines compared on Reddit pages.

More benchmark pages are published here as workbench projects finish.

## Layout

```
catalog/                   The entries, the index, and the recipe
packages/catalog-mcp/      Read-only MCP server: search and index
packages/catalog-embedder/ Search backend: the lexical sweep, plus an optional semantic channel
packages/catalog-capture/  Capture adapters (moving to the private workbench)
skills/<name>/              Claude Code skills
statusline/                 Context window status bar tool
docs/                       Public documentation
```

## Status

738 entries as of 2026-10-31. Entries are being rewritten to a deeper template, and the public MCP
server is being narrowed to a read-only surface (`search` and `index` only); the write and intake
tools are moving to the private workbench.

## License

[MIT](LICENSE)
