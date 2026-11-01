---
name: bmad-skill-forge
title: BMAD Skill Forge
url: "https://github.com/armelhbobdad/bmad-module-skill-forge"
category: skill-generator
summary: strong fit for bioinformatics tool skill generation; start with Brief tier on samtools
tags: [skill-generation, provenance, ast, cli-tools, meta-skill]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Transforms code repos and documentation into verified, version-pinned AI skill files. Uses AST parsing to extract real function signatures, so generated skills reference actual API shapes rather than guessed ones. Every claim traces back to source via a provenance-map.json (file:line at pinned commit for code, `[EXT:{url}]` citations for docs-only skills). Produces two outputs: a full `SKILL.md` with signatures, parameters, types, and inline provenance citations like `[AST:file.py:L27]`; and a `context-snippet.md` (80-120 token compressed index) for passive injection into CLAUDE.md. The workflow `@Ferris forge <library>` chains Brief → Create → Test → Export steps, each clearing context before the next.

**Three capability tiers**:
1. **Brief** — documentation/discourse analysis only, no AST. Immediately usable, no extra tooling.
2. **Forge** — adds AST extraction via `ast-grep`.
3. **Forge+/Deep** — adds semantic search (`cocoindex-code`) and hybrid indexing.

Lifecycle operations (Rename, Drop, Update, Export) are all transactional. Validation includes skill-check for agentskills.io format compliance and optional Snyk agent scan for prompt injection and data exposure.

## Assessment

For bioinformatics CLIs (samtools, bedtools, nextflow), hand-writing skill definitions risks hallucinated flag names and wrong parameter types. Skill Forge prevents this by grounding every claim in a parsed source. The provenance model is the key differentiator — no other skill generator in the current stack provides file:line:commit traceability. Brief tier requires only Node.js >= 22 and no AST setup, making it the lowest-friction entry point.

## Mechanical details

Requirements: Node.js >= 22, Python >= 3.10, `uv`. For Forge and above: `ast-grep`. Install via `npx bmad-module-skill-forge install`. Start with Brief tier on samtools — no AST setup needed, works from docs and man pages alone. The `.autoharness/` analog here is the provenance-map.json generated per skill file.

## Security

Licensed MIT. The tool runs locally — no cloud service, no data leaves the machine except for optional GitHub CLI calls to fetch repository content and any opt-in friction/bug-report submissions. The `npx`-based install pulls from the npm registry, so pin to a specific version in production use (`npx bmad-module-skill-forge@<version> install`) and verify the package hash against a known-good release. The optional Snyk agent scan and skill-check validation are outbound-only calls; neither receives private repo contents unless you point SKF at a private repository.

No prompt-injection surface exists in the generated skill files themselves — output is static Markdown and JSON with no executable content. The main operational risk is supply-chain: SKF chains several third-party tools (ast-grep, cocoindex-code, tessl, QMD) that are invoked at skill-generation time; review the installed versions and restrict network access if running against proprietary code. No `security_flags` are raised for normal usage against public repositories.

## How to use it

npx bmad-module-skill-forge install
