---
name: claude-meta-skill
title: Claude Meta-Skill
url: "https://github.com/YYH211/Claude-meta-skill"
category: reference
summary: "Curated collection of 11 Claude Code skills; mostly Chinese-language or general-dev focused, with significant overlap to existing catalog entries"
tags: [claude-code, skills, collection, prompt-engineering, mcp, refactoring]
reviewed: 2026-06-16
acquired: 2026-06-16
license: Unlicense
security_flags: [no-tests, no-ci, no-license-file]
overlaps: [bmad-skill-forge, obsidian-skills-kepano, one-skill-to-rule-them-all, creating-claude-md]
source: unknown
---

## What it does

A curated GitHub repository containing 11 ready-to-use Claude Code skills packaged as SKILL.md files with YAML frontmatter. Skills cover: skill creation guidance (create-skill-file), prompt optimization, deep reading analysis using 10+ thinking frameworks (SCQA, 5W2H, First Principles, etc.), DRY refactoring, frontend design, MCP server building, daily AI news aggregation, FastGPT workflow JSON generation, Manus-style file-based planning (3-file pattern), local git diff review, and Chinese software copyright registration material preparation. Installation is copy-based (`cp -r skill-dir .claude/skills/`).

## Assessment

Several skills are Chinese-language only (prompt-optimize, dry-refactoring, frontend-design, local-diff-review, software-copyright-writer), limiting immediate utility. The general-development focus (frontend design, DRY refactoring) has no bioinformatics relevance. Key overlaps exist: create-skill-file duplicates our writing-skills workflow, planning-with-files duplicates our plan-me-this skill, and mcp-builder covers ground already in the catalog. The deep-reading-analyst skill (10+ thinking frameworks) and the 3-file planning pattern are the most novel ideas worth noting as reference material. No clear adoption path — cherry-picking individual skills is more practical than adopting the collection.

## Mechanical details

- Each skill is a directory with a `SKILL.md` plus optional templates/examples
- Skills use Claude Code's standard YAML frontmatter format (`name`, `description`)
- Some skills (fastgpt-workflow-generator, software-copyright-writer) require external dependencies: Python 3 with python-docx, Node.js with Playwright
- Trigger keywords listed per skill for activation
- The deep-reading-analyst skill references an external GitHub repo (ginobefun/deep-reading-analyst-skill)
- planning-with-files references OthmanAdi/planning-with-files as its source

## Security

- **License**: README states "Free to use for any purpose" but no LICENSE file in the repository — effectively unlicensed, which is legally ambiguous despite the permissive intent
- **Dependency health**: Core skills are pure Markdown with no dependencies; two skills (fastgpt-workflow-generator, software-copyright-writer) pull in Python/Node dependencies with unpinned versions
- **Code quality signals**: No tests, no CI, no linter configuration visible
- **Supply chain**: Appears single-contributor; no releases, no signing
- **Dangerous patterns**: The software-copyright-writer skill includes Playwright browser automation scripts and file-system writes — worth reviewing before use. No eval() or injection vectors in the Markdown skills themselves
- **Maintenance**: Active repository based on the breadth of skills; commit cadence and issue responsiveness unknown from fetched content