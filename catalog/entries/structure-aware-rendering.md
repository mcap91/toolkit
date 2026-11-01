---
name: structure-aware-rendering
title: Structure-Aware Rendering (Eye-Tracking Study)
url: "https://arxiv.org/abs/2609.24616"
category: reference
summary: "Eye-tracking study (n=53) comparing how code rendering strategies (static, token-by-token, AST-based structured) affect programmer visual attention — structured rendering reveals code in syntactic chunks (outer blocks before inner details), inducing deeper processing and better structural awareness than character-based streaming; argues rendering is a first-class interaction primitive for AI coding tools"
tags: [eye-tracking, cognitive-load, code-rendering, ast, vibe-coding, hci, ai-assisted-coding, user-study]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: ""
security_flags: []
source: unknown
---

## What it says

Paper by Su et al. (arXiv 2609.24616, September 2026) arguing that how AI-generated code is rendered to the programmer matters as much as what is generated. Standard approaches — static block reveal or token-by-token streaming — reflect model generation order, not how programmers actually read code (selectively, non-linearly, structure-guided).

They introduce **structured rendering**: code revealed in semantically meaningful chunks derived from the AST hierarchy, exposing high-level structure (function signatures, control flow) before low-level details (loop bodies, expressions). Vertical rails mark nesting depth.

Eye-tracking study with 53 participants comparing three modes:

- **Static**: all code appears at once. Enables expert-like scanning with user control.
- **Character-based (token streaming)**: standard LLM output. Forces sequential attention, induces fewer but longer fixations.
- **Structured**: AST-based chunked reveal. Guides attention toward semantically meaningful units, supports high-level understanding, favored over character-based by participants.

Key finding: quiz-based assessments miss the differences — eye-tracking reveals distinct cognitive effort patterns invisible to outcome-only measures. Dynamic rendering provides attentional guidance that helps manage cognitive load, but structured rendering further improves structural awareness.

Dataset and interactive demo: codegaze.vercel.app.

## Security

Reference entry — no installable artifact. Anonymized dataset released publicly.