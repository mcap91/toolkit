---
name: cli-anything
title: CLI-Anything
url: "https://github.com/HKUDS/CLI-Anything"
category: skill-generator
summary: "Generates production-grade, agent-native CLI harnesses from any codebase via a 7-phase pipeline; directly integrates with Claude Code as a plugin and emits SKILL.md files for skill discovery."
tags: [cli-generation, agent-native, skill-generation, claude-code-plugin, python, bioinformatics-adjacent, meta-skill]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [runs-arbitrary-codegen, upstream-software-required]
overlaps: []
source: unknown
---
## What it does

CLI-Anything is a framework and Claude Code plugin that transforms any software codebase into an agent-native CLI harness through an automated 7-phase pipeline: analyze source, design command architecture, implement a Click CLI with REPL and `--json` output, plan and write tests, document, and publish via `pip install -e .`. The generated harness lands on PATH as `cli-anything-<software>` and ships a `SKILL.md` for agent skill discovery.

Two entry points exist: (1) **CLI-Hub** (`pip install cli-anything-hub`) — a package manager for 40+ pre-built harnesses covering creative tools, AI/ML platforms, scientific computing, office suites, and game engines; (2) the **Claude Code plugin** (`/plugin marketplace add HKUDS/CLI-Anything` + `/plugin install cli-anything`) — run `/cli-anything <path-or-repo>` to generate a fresh harness for any target. A meta-skill (`npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y`) lets agents autonomously discover and install the right CLI for a task.

Pre-built harnesses with bioinformatics relevance include UniMol Tools (molecular property prediction), QGIS (geospatial analysis), CloudAnalyzer (point cloud QA), and 3MF (mesh geometry for 3D printing). The project has 2,461 passing tests (100% pass rate) across unit and E2E layers, and publishes an arXiv technical report (2606.03854).

## Assessment

**Pilot** — the value proposition is high for bioinfo workflows: wrap any Python bioinformatics tool (ImageJ, RDKit, AlphaFold, DeepVariant, etc.) into a structured CLI that Claude Code can drive deterministically, without fragile UI automation. The SKILL.md output integrates directly with this project's skill infrastructure. The repo is actively maintained (PR activity through 2026-05-30), has a real test suite, and the Apache-2.0 license is clean.

Caveats: generation requires a frontier-class model (Claude Sonnet/Opus 4.x) and typically needs one or more `/refine` passes to reach production quality. The pipeline runs code-generation over arbitrary target codebases, which means review of generated harnesses before adoption is essential. No bioinformatics-specific harnesses ship out of the box beyond UniMol — practitioners will need to run the generator for tools like GATK, Nextflow, or custom pipelines.

## Mechanical details

- **Install plugin**: `/plugin marketplace add HKUDS/CLI-Anything` then `/plugin install cli-anything`
- **Build a harness**: `/cli-anything <path-or-repo>` (all 7 phases automated)
- **Refine coverage**: `/cli-anything:refine <path> ["focus area"]` (gap analysis, incremental, non-destructive)
- **Install from Hub**: `pip install cli-anything-hub` then `cli-hub install <name>`
- **Meta-skill for agents**: `npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y`
- Generated CLI: `pip install -e . && cli-anything-<software> --help`; bare invocation enters REPL mode; `--json` flag on every command returns structured output
- SKILL.md written to `skills/cli-anything-<software>/SKILL.md` in the target repo; compatible copy at `cli_anything/<software>/skills/SKILL.md`
- Windows support requires Git for Windows (bash + cygpath); cygpath guards are in the codebase

## Security

License is Apache-2.0 — no restrictions. The primary risk surface is that **the plugin executes code-generation over arbitrary target codebases**: the generated harness is new code that must be reviewed before production use. The changelog shows active security hardening (path traversal fix in Sketch CLI #304, `defusedxml` adoption for XML/SVG/ODF parsing #296, DomShell URL validation #156, Zoom token permissions #325). No eval() or shell injection patterns are documented in the README; the framework invokes real software backends via subprocess with structured arguments. `security_flags` reflect that (a) the code-generation step produces untrusted output requiring review, and (b) many harnesses require upstream desktop software (Blender, GIMP, LibreOffice) that must be separately installed and trusted. Supply chain is healthy: frequent commits, visible contributor community, CI with real E2E tests.
