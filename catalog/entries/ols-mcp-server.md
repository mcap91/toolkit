---
name: ols-mcp-server
title: OLS MCP Server
url: "https://github.com/seandavi/ols-mcp-server"
category: mcp-server
summary: "MCP server for EBI Ontology Lookup Service — search terms, explore hierarchies, find similar terms across GO, HPO, MONDO, ChEBI, UBERON and all EBI-hosted ontologies; directly addresses LLM ontology hallucination problem"
tags: [mcp, ontology, bioinformatics, gene-ontology, hpo, ebi, ols]
reviewed: 2026-06-19
acquired: 2026-06-19
license: MIT
security_flags: [single-contributor]
overlaps: []
source: unknown
---

## What it does

MCP server wrapping the EBI Ontology Lookup Service (OLS4) API. Provides 6 tools:

- **Search Terms**: query across ontologies with flexible filtering
- **Search Ontologies**: discover available ontologies and metadata
- **Get Ontology Information**: detailed info about a specific ontology
- **Get Term Information**: comprehensive details for a specific term
- **Get Term Children / Ancestors**: navigate ontological hierarchies
- **Find Similar Terms**: semantic similarity via LLM embeddings

Covers all ontologies hosted by EBI OLS: Gene Ontology (GO), Human Phenotype Ontology (HP), MONDO, ChEBI, UBERON, EFO, and hundreds more.

Motivated by a real problem: LLMs hallucinate ontology terms and identifiers. This server provides grounded, API-backed lookups so agents can reference real terms.

## Assessment

Directly relevant to bioinformatics agent workflows. Ontology lookup is a core operation when annotating genes, phenotypes, diseases, or chemical entities — and LLM hallucination of term IDs is a documented failure mode this tool explicitly addresses.

The author (Sean Davis) is a well-known bioinformatics researcher (NCI, University of Colorado), which gives confidence in domain correctness. The server is a thin MCP wrapper over EBI's stable public API, so the attack surface and maintenance burden are low.

Single contributor is the main risk, but the tool is simple enough that forking/maintaining it would be trivial.

## Mechanical details

- **Runtime**: Python 3.12+, uv package manager, FastMCP framework
- **Install**: `uv sync` then configure in Claude Desktop or `.mcp.json`
- **Config**: `"command": "uv", "args": ["tool", "run", "ols-mcp-server"]`
- **API backend**: EBI OLS4 API v2 (public, no auth required)
- **Code quality tools**: ruff (format + lint), mypy, pytest
- **Windows**: supported (uv install via PowerShell, .venv activation)

## Security

- **License**: MIT (inferred from standard GitHub project; verify LICENSE file)
- **Dependencies**: FastMCP, httpx — minimal dependency tree
- **Code quality**: ruff formatting, mypy type checking, pytest tests, dev extras
- **Supply chain**: single contributor (Sean Davis, established bioinformatics researcher)
- **Dangerous patterns**: none — read-only API wrapper, no credential handling, no shell execution
- **Maintenance**: recently created, active development