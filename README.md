# bioinfo-agent-toolkit

Reusable Claude Code skills, tools, and guides for bioinformatics workflows. Pick and choose what you need.

## Skills

Copy any skill into your project:

```bash
# From a clone of this repo
cp -r skills/<name> <your-project>/.claude/skills/<name>
```

| Skill | Description |
|---|---|
| [/blueprint](skills/blueprint/) | Create a portable architecture reference doc for reimplementation |
| [/handoff](skills/handoff/) | Generate a handoff prompt for a fresh CLI agent or subagent |
| [/plan-me-this](skills/plan-me-this/) | Package a spec into phase docs + readme_this_current_task.md |
| [/scripts-reference](skills/scripts-reference/) | Generate a clickable script reference doc |
| [/catalog-intake](skills/catalog-intake/) | Pull links from Gmail, curate, drain to queue, run headless processing |
| [/agent-lockdown](skills/agent-lockdown/) | Lock down a coding agent CLI — version pin, model pin, env hardening, secrets deny, integrity checkup |
| [/explain-me-this](skills/explain-me-this/) | Discuss-and-explain persona — explains, researches, and helps you decide; no code or plans. Manual-only. |
| [/verticalizing-plans](skills/verticalizing-plans/) | Convert phase-shaped plans into thin vertical slices that prove the whole flow early |
| [/spec-check](skills/spec-check/) | Surface open design decisions in a doc before handing work off for autonomous execution |
| [/resolve](skills/resolve/) | Re-orient an agent that asked a question evidence could answer: search, choose, cold-check, record, continue |
| [/write-plain](skills/write-plain/) | House style for all prose: no dashes, no AI tells, active voice, ASD-STE100 sentence limits |

## Output style

### [Direct](docs/output-styles/direct.md)

A Claude Code output style (not a skill) — action-first, terse, 23 rules across Voice, Shape, Coding Discipline, and Working constraints. Symlink `docs/output-styles/direct.md` into `~/.claude/output-styles/` (a copy goes stale) and set `"outputStyle": "direct"`. Ships with a reply-length Stop hook. Replaces the old `setup-behavioral-baseline.sh`. See [docs/output-styles/README.md](docs/output-styles/README.md).

## Tools

### [Status Line](statusline/)

Context window usage bar for the Claude Code CLI. See [statusline/README.md](statusline/README.md) for setup.

## Catalog

The `catalog/` directory tracks external skills, plugins, hooks, MCP servers, agent patterns, CLI tools, frameworks, and reference material — 171 assessed entries with summaries, security reviews, and tags.

### Using the catalog from another project

Register the catalog MCP server in your project's `.mcp.json` to give your agent access to search, graph traversal, and topic discovery across all catalog entries.

**Add to your project's `.mcp.json`:**

```json
{
  "mcpServers": {
    "bioinfo-catalog": {
      "type": "stdio",
      "command": "node",
      "args": [
        "--import",
        "file:///PATH/TO/bioinfo-agent-toolkit/node_modules/tsx/dist/loader.mjs",
        "PATH/TO/bioinfo-agent-toolkit/packages/catalog-mcp/src/server.ts"
      ],
      "env": {}
    }
  }
}
```

Replace `PATH/TO` with the absolute path to your local clone of this repo.

**Key tools for cross-repo use:**

| Tool | Purpose |
|---|---|
| `search` | Survey search: returns every entry lexically matching your terms (word-prefix, uncapped), plus flagged semantic suggestions for concepts phrased differently. No scores exposed. |
| `graph-query` | Knowledge graph traversal. `neighbors` mode: explore connections from a known entry (overlaps, shared tags, shared category). `topic` mode: discover entries by concept (substring match on tags/categories). |
| `graph-build` | Rebuild the knowledge graph on demand (normally auto-rebuilds via `index`). |

![This repo's catalog search vs. plain substring search, by query style](docs/benchmarks/search-eval.png)

**Search eval: this repo's search vs. plain substring search** ([method](docs/semantic-search.md#evaluation)). 40 test queries in four styles (10 each), run through three engines on the same frozen copy of the catalog: **substring** search (the baseline, the repo's original lookup), this repo's **lexical** search alone, and its full **lexical+semantic** search. Each cell is the share of relevant entries the engine surfaced, with the count: found / should have found, summed over the style's 10 queries. Relevance comes from an answer key labeled by Claude Opus 5.5 without seeing the queries; calibration entries repeated in every labeling batch got identical labels 88% of the time.

| query style | substring | lexical | lexical+semantic |
|---|---|---|---|
| exact name (e.g. "paddleocr") | 100% (10/10) | 100% (10/10) | 100% (10/10) |
| keyword (e.g. "document parsing") | 18% (50/284) | 56% (158/284) | 65% (184/284) |
| plain-language need | 0% (0/284) | 0% (0/284) | 14% (39/284) |
| keyword list (e.g. "local llm inference gpu quantization") | 0% (0/284) | 4% (10/284) | 26% (75/284) |

On exact-name queries the named tool was the first result 70% of the time for substring and 90% for lexical and lexical+semantic. Lexical search returned 48.6 entries per keyword query, 0.0 per plain-language query, and 1.3 per keyword-list query; on those last two styles, nearly all surfaced entries come from semantic suggestions (39 of 39 and 65 of 75). Semantic suggestions are limited to 10 per query by default, which caps how much of a large topic they can surface.

**Add retrieval instructions to your project's CLAUDE.md:**

```markdown
## External tool catalog

This project registers the bioinfo-agent-toolkit catalog MCP server as `bioinfo-catalog`.
Use it to find tools, skills, frameworks, or MCP servers:

- `search { query: "multi-agent orchestration" }` — keyword search
- `graph-query { mode: "topic", term: "orchestration" }` — find entries by concept
- `graph-query { mode: "neighbors", entry: "mycelium" }` — explore connections from a known entry
```

**Lightweight alternative (no MCP):** The catalog ships a search index at [`catalog/.search-index.json`](catalog/.search-index.json). Any agent can fetch it via raw GitHub URL and search in-context — no server, no MCP registration required.

**Index URL:**
```
https://raw.githubusercontent.com/mcap91/bioinfo-agent-toolkit/main/catalog/.search-index.json
```

**How to use it:**

1. **Fetch the index** — have your agent fetch the URL above. It returns a JSON array of all catalog entries (~193 entries) with searchable fields.
2. **Search in-context** — each entry includes `name`, `title`, `url`, `category`, `decision_status`, `summary`, `body_summary`, `tags`, `workflows`, `license`, `security_flags`, and `path`. Search by keyword in `summary`/`body_summary`, filter by `tags`, `category`, or `decision_status` (`adopted`/`rejected`/`open`).
3. **Read full entries** — the `path` field (e.g. `catalog/entries/faiss.md`) points to the full entry with security analysis and mechanical details. Fetch it at:
   ```
   https://raw.githubusercontent.com/mcap91/bioinfo-agent-toolkit/main/{path}
   ```

**Example agent prompt:**
> Fetch the bioinfo-agent-toolkit search index from `https://raw.githubusercontent.com/mcap91/bioinfo-agent-toolkit/main/catalog/.search-index.json`. Find entries tagged "vector-database" with decision_status "adopted". For each match, fetch the full entry via its `path` field and summarize the security analysis.

### Managing the catalog

The catalog is managed by an MCP tool server in [`packages/catalog-mcp/`](packages/catalog-mcp/) — 17 tools for intake, research support, validation, knowledge graph, and data management. The server never makes LLM calls; the calling agent does all reasoning.

| Group | Tools |
|---|---|
| Intake | `ingest`, `drain`, `fetch-url`, `reddit-extract`, `build-prompt` |
| Entries | `validate-entry`, `write-entry`, `annotate-entry`, `scaffold` |
| Data | `index`, `search`, `lint`, `queue`, `config`, `goals` |
| Graph | `graph-build`, `graph-query` |

Running `index` regenerates `catalog/index.md`, `catalog/.search-index.json`, and `catalog/.graph.json`.

### Prerequisites

Running the catalog MCP server requires:

- Node.js
- Python 3.10+
- [uv](https://astral.sh/uv) — manages the Python environment for semantic search; never base/system Python, never plain pip
- `fastembed`, installed via:
  ```bash
  cd packages/catalog-embedder && uv venv && uv pip install -r requirements.txt
  ```

The `search` tool runs a complete lexical sweep backstopped by flagged semantic
suggestions, and requires this Python environment to be set up. See
[docs/semantic-search.md](docs/semantic-search.md) for the full setup guide, matching
semantics, and auto-rebuild behavior.

Capturing Reddit links during intake (the capture step in
[`skills/catalog-intake/SKILL.md`](skills/catalog-intake/SKILL.md)) uses headless Chromium via
[`packages/catalog-capture/`](packages/catalog-capture/). One-time setup:

```bash
cd packages/catalog-capture && uv sync --extra dev && uv run playwright install chromium
```

## Structure

```
skills/<name>/         Skills (just a SKILL.md)
statusline/            Context window status bar tool
catalog/               External tool/skill catalog (data + derived artifacts)
packages/catalog-mcp/  Catalog MCP tool server (17 tools)
packages/catalog-capture/  Headless-browser capture for links a plain fetch cannot read (Reddit)
docs/                  Public documentation
docs/output-styles/    Claude Code output styles (e.g. direct.md)
```

## Maintainer Setup

This repo uses the `kb` toolkit for project tracking. The wiki lives in a separate private repo and is cloned into the gitignored `wiki/` directory.

```bash
# Clone the private wiki into this repo
git clone git@github.com:mcap91/bioinfo-agent-toolkit-wiki.git wiki

# Run kb commands from the kb checkout
cd ../kb
npm run wiki -- lint --dir ../bioinfo-agent-toolkit
npm run wiki -- generate --dir ../bioinfo-agent-toolkit
```

See `AGENTS.md` for the full kb workflow.

## License

[MIT](LICENSE)
