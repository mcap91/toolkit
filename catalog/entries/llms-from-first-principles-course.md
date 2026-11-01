---
name: llms-from-first-principles-course
title: LLMs from First Principles (Doug Does) + AI-engineer fine-tuning AMA
url: https://dougdoes.ai/courses/llms-from-first-principles/start/?flow=outcome&course=build&step=goals
category: reference
summary: "Free, account-less interactive course site by a senior AI engineer (ex full-stack) — three project-based courses: train a character-level transformer on Shakespeare, fine-tune a model for SQL question answering, and ML fundamentals (prediction and error analysis), with in-browser exercises and downloadable Python labs; posted alongside an r/learnmachinelearning AMA whose practitioner heuristics include: fine-tuning is usually not worth it given cheap frontier APIs unless the task is simple or data is massive, then distill a teacher via SFT → DPO → RLVR on expert/user data; most AI-engineering work is backend software engineering and data cleaning; segment production inputs to track training-data bias"
tags:
  - course
  - llm-fundamentals
  - transformers
  - fine-tuning
  - sft
  - dpo
  - rlvr
  - distillation
  - ai-engineering
  - career
  - learning
  - python
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - six-ai-engineer-projects
  - huggingface-agents-course
  - production-ai-portfolio-checklist
license: N/A
security_flags: []
source: unknown
---

## What it does

**Course site.** dougdoes.ai hosts free interactive courses (no account required) built with Codex and, per the author, walked through personally:

1. Language-model training — build and train a character-level transformer on Shakespeare (prereq: basic Python).
2. Fine-tuning — adapt a model for SQL question answering (prereq: Python + model basics).
3. ML fundamentals — prediction and error analysis (prereq: basic algebra).

Each course ends in a concrete artifact (a trained model, a measured comparison, or modified worked examples); Python projects are downloadable.

**AMA heuristics (r/learnmachinelearning, Oct 2026)** from the course author, a senior AI engineer (CS/CE undergrad, 3 years full-stack, AI master's, seizure-prediction research lab, eval-framework and agent-loop work at WHOOP, now fine-tuning):

- **When fine-tuning pays off:** usually it doesn't — frontier API price cuts make it hard to beat on cost while matching quality and latency. It wins when the use case is simple or you have a massive amount of data, letting a small base model become best-in-class on quality, latency, and cost at once, at the price of engineering effort.
- **Recipe:** reach a baseline by distilling a teacher model via SFT, raise it with DPO, then improve steadily with RLVR using subject-matter-expert and real-user signal.
- **Evaluating models/bias:** segment production inputs, then compare training-data coverage and output scores per segment to catch issues before rollout.
- **Role reality:** most AI-engineering work is backend engineering and data cleaning; "calling model.fit() isn't super complicated." Model ability tracks task verifiability (GRPO/RLVR), so human value concentrates on architecture, long-horizon and less-verifiable judgment, and telling agents to simplify over-engineered code.
- **Career transition:** teach your old-role skills to teammates so you stop being the only one who can do them, and take lower-status tasks in the new area to grow into it. Recommended intro: Latent Space's "The Rise of the AI Engineer."

## Security

Educational content; no installable code beyond optional downloaded course labs.
