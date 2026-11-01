---
name: model-workspace-protocol
title: Model Workspace Protocol (MWP)
url: "https://arxiv.org/abs/2603.16021"
category: reference
summary: Research paper proposing filesystem structure as agent orchestration; numbered folders + markdown prompts replace multi-agent frameworks for sequential workflows
tags: [research, orchestration, filesystem, agent-architecture, unix-philosophy, markdown]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: []
overlaps: [claude-meta-skill]
source: unknown
---

## What it does

A research paper (arXiv:2603.16021) presenting Model Workspace Protocol (MWP) — a method that replaces framework-level agent orchestration with filesystem structure. Instead of multi-agent frameworks managing context passing, memory, error handling, and step coordination through code, MWP uses: numbered folders representing stages, plain Markdown files carrying prompts and context for each step, and local scripts for mechanical (non-AI) work. A single agent reads the right files at the right moment, doing work that would otherwise require a multi-agent framework.

The approach draws from Unix pipeline design, modular decomposition, multi-pass compilation, and literate programming. Designed for sequential workflows where a human reviews output at each step. MIT licensed, open source.

## Assessment

The idea is elegant in its simplicity — filesystem structure as the orchestration layer is maximally transparent and debuggable. For sequential, human-in-the-loop workflows (which describes much of our catalog processing and research work), it could reduce complexity compared to framework-level orchestration. The Unix philosophy alignment (each stage does one thing, plain text interfaces) resonates. However, note rather than pilot because: (1) it explicitly targets sequential workflows with human review, not concurrent or autonomous operation, (2) our existing recipe-based approach (catalog/recipe.md driving a headless loop) already captures a similar pattern informally, (3) the paper is the contribution — the protocol itself is a convention, not tooling, and (4) the numbered-folders approach may not scale well to dynamic or branching workflows.

## Mechanical details

- Paper: 28 pages, 5 figures, 2 tables, 54 references
- Stages represented as numbered folders (e.g., `01-research/`, `02-analyze/`, `03-synthesize/`)
- Each folder contains Markdown files with prompts and context
- Local scripts handle mechanical work (file operations, formatting, etc.)
- Single agent reads folder contents at each stage
- Human reviews output between stages
- Protocol is a convention — no required tooling, SDK, or framework
- Published March 2026, v2

## Security

- **License**: MIT (protocol is open source)
- **Dependency health**: N/A — it's a convention/protocol, not software
- **Code quality signals**: Peer-submitted research paper with 54 references; formal methodology
- **Supply chain**: Academic paper by Jake Van Clief
- **Dangerous patterns**: None — the protocol is a set of filesystem conventions
- **Maintenance**: Research paper; the protocol is stable by nature (conventions don't need updates)

## Usage notes

- Cited in an Instagram reel (under the name "ICM," attributed to Jake van Cleef) as part of a blind benchmark (uncredited methodology) comparing three LLM-wiki implementations ([[nashsu-llm-wiki]], [[nvk-llm-wiki]], and an uncorroborated "Lukastorian" agent) against plain Claude Code structured with this protocol's organized-folders approach; the reel reports the folder-structured plain-Claude-Code baseline matched the best-performing wiki tool's answer accuracy at about half the per-answer cost (source: https://www.instagram.com/reel/DfFSZDvN6oV/)
