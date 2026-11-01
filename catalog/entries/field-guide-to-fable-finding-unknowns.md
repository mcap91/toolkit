---
name: field-guide-to-fable-finding-unknowns
title: "A Field Guide to Fable: Finding Your Unknowns"
url: "https://x.com/trq212/status/2073100352921215386"
category: agent-pattern
summary: "Anthropic engineer Thariq Shihipar's framework for working with capable AI models — the bottleneck shifts from model ability to specification quality; five techniques (blind-spot pass, interviews, references, rough mockups, brainstorms) for surfacing assumptions before they compound into costly rework; 2M views in 3 days"
tags: [prompting, workflow, fable, claude-code, specification, unknowns, anthropic, agent-pattern]
reviewed: 2026-07-15
acquired: 2026-07-15
license: unlicensed
security_flags: []
overlaps: []
source: unknown
---

## What it says

Essay by Thariq Shihipar (Anthropic, Claude Code team) arguing that with sufficiently capable models, the quality bottleneck shifts from "can the model do the task" to "did you specify the task correctly." Central metaphor: the map (your prompts and context) vs the territory (the codebase and real constraints). The gap between them — unknowns — is where accumulated blind guesses derail complex tasks.

A weak model's failures are loud and local. A strong model's failures are quiet and compounding — it takes your map at face value and executes it thoroughly, making every unstated assumption expensive.

### Four types of unknowns (Rumsfeld framework)

1. **Known knowns** — what's in your prompt
2. **Known unknowns** — gaps you're aware of but haven't resolved
3. **Unknown knowns** — things so obvious you'd never write them down, but would recognize if wrong
4. **Unknown unknowns** — what you haven't considered at all

### Five techniques for surfacing unknowns

1. **Blind-spot pass:** Before starting unfamiliar work, tell the model what you don't understand and ask it to map the traps and questions you didn't know to ask
2. **Interviews:** Have the model interview you about ambiguities one question at a time, prioritizing questions where the answer would change the architecture
3. **References:** When you can't describe what you want, point the model at existing source code, diagrams, or documentation — source code is the strongest reference
4. **Rough mockups:** Have the model build wildly different rough mockups with fake data so you catch direction problems while they're cheap to change
5. **Brainstorms:** Use brainstorms to surface gaps between your mental model and reality

### Recommended workflow

Write a short spec (1–2 pages) → have the model interview you about implementation details, boundary conditions, trade-offs, and failure points → solidify the spec from the answers → then implement.

## Key takeaways

- "We used to verify that Claude did the work right. Now we verify that it's doing the right work"
- People winning with capable models aren't writing longer prompts — they're running a specific loop of discovery moves before, during, and after implementation
- The interview technique is particularly high-leverage: "Ask me one question at a time about anything ambiguous, prioritizing questions where my answer would alter the architecture"
- Published July 3, 2026; drew 2 million views in 3 days
- Community has produced installable SKILL.md implementations of the techniques (finding-unknowns-skills repos)

## Security

Essay and technique — no code to audit.