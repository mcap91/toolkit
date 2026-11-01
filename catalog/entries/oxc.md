---
name: oxc
title: Oxc (Oxidation Compiler)
url: "https://github.com/oxc-project/oxc"
category: cli-tool
summary: "Rust-based JavaScript/TypeScript toolchain from VoidZero (Evan You) providing a shared parser, linter (Oxlint), formatter (Oxfmt), transformer, minifier, and module resolver; Oxlint targets ESLint compatibility with 870+ built-in rules, claims 50-100x ESLint's speed, and offers type-aware linting via tsgo (the Go port of the TypeScript compiler). MIT."
license: MIT
tags: [javascript, typescript, rust, linter, formatter, parser, compiler-toolchain, eslint-alternative, voidzero, static-analysis]
reviewed: 2026-09-25
acquired: 2026-09-25
overlaps: []
security_flags: []
source: unknown
---

## What it does

Oxc (the Oxidation Compiler, pronounced "ox-ee-see") is a collection of high-performance JavaScript/TypeScript tools written in Rust, developed under VoidZero, the company founded by Vue.js/Vite creator Evan You. Rather than one tool, it is a shared toolchain: a parser, linter (Oxlint), formatter (Oxfmt), transformer, minifier, and module resolver, all built on common infrastructure so behavior stays consistent across the stack. The parser allocates its AST in a bumpalo memory arena and inlines short strings via CompactString to minimize heap allocations, and delegates scope binding, symbol resolution, and some syntax-error detection to a separate semantic analyzer rather than doing it inline. Oxc powers Rolldown (Vite's Rust-based bundler — used for parsing, transformation, and minification) and Nuxt (parsing); `oxc_resolver` is also used independently by Nova, swc-node, and knip.

The most mature and widely adopted component is Oxlint, a linter targeting ESLint compatibility. It ships 870+ built-in rules covering ESLint core, TypeScript (including type-aware rules), and popular plugins (React, Jest, Vitest, Import, Unicorn, jsx-a11y), and the docs claim 50-100x the speed of ESLint. Type-aware linting is powered by tsgo (the native Go port of the TypeScript compiler, aka "TypeScript 7") for TypeScript type-system compatibility — contrasted in Oxc's own docs with Biome, which implements its own type inference instead. Oxlint supports multi-file analysis (a project-wide module graph shared across rules, improving checks like `import/no-cycle`) and alpha-stage JS plugins for compatibility with the existing ESLint plugin ecosystem. It is used in production by elastic/kibana, getsentry/sentry, electron/electron, renovatebot/renovate, preactjs/preact, date-fns/date-fns, outline/outline, PostHog/posthog, actualbudget/actual, and cloudflare/agents.

Per Oxc's own docs, the parser and Oxlint are production-ready and widely used; the transformer and minifier are in active development approaching stability; Oxfmt (the Prettier-compatible formatter) is newer.

## Mechanical details

- **Install (linter):** `npm add -D oxlint`; run via `npx oxlint@latest`, or add `"lint": "oxlint"` / `"lint:fix": "oxlint --fix"` scripts
- **Install (formatter):** `npx oxfmt@latest`
- **Adoption paths:** replace ESLint outright (use `@oxlint/migrate` to convert an existing ESLint config automatically), or run Oxlint alongside ESLint incrementally, using `eslint-plugin-oxlint` to disable overlapping ESLint rules while both run
- **File support:** `.js`, `.mjs`, `.cjs`, `.ts`, `.mts`, `.cts`, `.jsx`, `.tsx`; framework files `.vue`, `.svelte`, `.astro` by linting only `<script>` blocks
- **Embeddable crates:** parser, transformer, minifier, and resolver (`oxc_resolver`) ship as separate Rust crates usable directly by other tooling (e.g. Rolldown)
- **Benchmark cited in docs:** parsing `typescript.js` on an M3 Max — Oxc ~26.3ms vs SWC ~84.1ms vs Biome ~130.1ms

## Security

MIT licensed. Oxlint and Oxfmt are static-analysis/formatting CLIs that run locally against source files, with no network calls in normal linting/formatting operation. Distributed via npm with no unusual install pattern.

## How to use it

npm add -D oxlint (linter); npx oxfmt@latest (formatter)
