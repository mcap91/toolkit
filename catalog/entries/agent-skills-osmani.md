---
name: agent-skills-osmani
title: Agent Skills (Addy Osmani)
url: "https://github.com/addyosmani/agent-skills"
category: plugin
summary: "Production-grade 24-skill engineering pack for AI coding agents — full SDLC lifecycle (define/plan/build/verify/review/ship) with anti-rationalization tables, verification gates, and 8 slash commands; 65K+ stars, Claude Code marketplace-installable, multi-platform (Cursor/Gemini/Windsurf/Copilot/Kiro); MIT"
tags: [skills, sdlc, engineering-practices, claude-code, plugin, tdd, code-review, planning]
reviewed: 2026-06-25
acquired: 2026-06-25
license: MIT
security_flags: []
overlaps: [dotclaude, claude-spellbook]
source: unknown
---

## What it does

24 structured engineering skills covering the complete software development lifecycle, packaged as a Claude Code plugin (also works with Cursor, Gemini CLI, Windsurf, GitHub Copilot, Kiro, OpenCode, and Codex). Each skill is a SKILL.md with YAML frontmatter containing step-by-step workflows, verification gates, and anti-rationalization tables that prevent agents from skipping steps.

8 slash commands map to lifecycle phases: `/spec` (define), `/plan` (plan), `/build` (build — auto-generates plan and implements autonomously), `/test` (verify), `/review` (review), `/webperf` (audit), `/code-simplify` (simplify), `/ship` (deploy). 4 specialist agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor) and 5 reference checklists (definition-of-done, testing-patterns, security, performance, accessibility, observability).

Key skills: spec-driven-development, planning-and-task-breakdown, incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design, debugging-and-error-recovery, code-review-and-quality, code-simplification, security-and-hardening, performance-optimization, git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, observability-and-instrumentation, shipping-and-launch, interview-me, idea-refine, browser-testing-with-devtools.

Draws heavily from Google engineering culture: Hyrum's Law, Beyonce Rule, test pyramid, Chesterton's Fence, trunk-based development, Shift Left, change sizing (~100 lines).

## Assessment

The most popular agent skill pack by a wide margin (65K+ stars in 4 months, Feb–Jun 2026). By Addy Osmani, senior Google Chrome engineer and well-known engineering author. The anti-rationalization tables — explicit lists of excuses agents use to skip steps, with counter-arguments — are a distinctive and effective design pattern not seen in most other skill packs. Verification gates requiring evidence (test output, build output, runtime data) rather than "seems right" are another strength.

Significant overlap with our existing superpowers skill system, which already covers brainstorming, TDD, debugging, verification-before-completion, code review, and plan execution. The main value-add over superpowers is the breadth (24 skills vs ~15), the define phase (interview-me, idea-refine, spec-driven-development), the ship phase (CI/CD, deprecation, observability, launch), and the reference checklists. The doubt-driven-development skill (adversarial fresh-context review) is novel and relevant.

Multi-platform support (8 tools) makes it a strong recommendation for teams using mixed agent tooling. Marketplace-installable for Claude Code.

## Mechanical details

- Install: `claude plugin install agent-skills@addy-agent-skills` or clone and `claude --plugin-dir`
- Skills are plain Markdown — portable to any agent that reads instruction files
- Progressive disclosure: SKILL.md is the entry point, references load only when needed (token-efficient)
- Skills auto-activate based on task context (API work triggers api-and-interface-design, UI work triggers frontend-ui-engineering)
- `/build` combines plan generation and autonomous implementation in a single approved pass

## Security

MIT license, no dependencies (pure Markdown), no code execution, no credential handling. Clean supply chain — the skills are instruction files, not executable code. Large contributor base with active PR review. No security concerns for catalog or adoption.