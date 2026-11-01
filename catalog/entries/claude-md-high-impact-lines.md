---
name: claude-md-high-impact-lines
title: High-Impact CLAUDE.md Lines (r/ClaudeCode Crowd-Sourced)
url: https://www.reddit.com/r/ClaudeCode/comments/1xeautc/comment/19rlwk7oqkz9d/
source_url: https://www.reddit.com/r/ClaudeCode/comments/1xeautc/comment/19rlwk7oqkz9d/
source: reddit
category: agent-pattern
summary: Crowd-sourced thread of specific CLAUDE.md instruction lines practitioners report changed agent behavior (not style preferences) — read-all-then-edit-once batching, don't-break-the-queue-for-corrections, attribute-mistakes-to-instruction-gaps-not-apologies, YAGNI scope discipline with explicit escalation, cheap-model subagent self-review, don't-edit-tests-to-pass (paired with a hook since the instruction alone got the tests deleted instead), and fact-check-by-reopening-the-file-before-claiming-what-code-does.
tags:
  - claude-md
  - agent-instructions
  - prompt-engineering
  - claude-code
  - workflow
  - hooks
  - scope-discipline
reviewed: 2026-10-28
acquired: 2026-10-28
license: N/A
security_flags: []
overlaps:
  - boris-cherny-claude-md
  - creating-claude-md
---

## What it does

A Reddit thread collecting specific CLAUDE.md lines, not general style advice, that practitioners report measurably changed Claude Code's behavior. Patterns raised, with the problem each targets:

1. **Batch read-then-edit.** "Before changing anything, list every file you'll need and read them in one pass. Then make all edits, then run the tests once." Stops the read→edit→read→edit loop that burns usage on larger changes.
2. **Don't break the task queue for a correction.** "Treat all work as a queue of todo... When I propose tweaks, append to the queue, do not break the queue to suddenly prioritize my correction. Only stop when 100% of your queue is truly clear." Fixes the failure mode where one small correction causes the agent to drop all in-progress work.
3. **Attribute mistakes to instruction gaps, not the model.** "Mistakes always mean a gap or issue in instruction files instead. Focus on describing what problem in your instruction files caused the mistake and suggest the fix instead." One practitioner's refined wording: state what happened, correct it, identify the cause (missing/ambiguous/conflicting instruction, or a clear instruction not followed), propose a fix only when the cause is a real gap — "if the instruction was clear, say so plainly rather than inventing a gap."
4. **Explicit YAGNI with an escalation path.** "Always hold a You Aren't Gonna Need It mentality. Do not overengineer. Never expand scope without permission. Always suggest possible scope improvements... if they make sense. All work must be justifiable." Pairs scope discipline with a sanctioned channel for proposing (not silently doing) extra work.
5. **Cheap-model subagent as adversarial reviewer.** "Always spin up a sub agent with minimal context using a cheap model, with the job of reviewing your changes, to sus out possible problems with fresh eyes." Cost-bounded second opinion before calling work done.
6. **Words alone don't hold a hard constraint — use a hook.** One practitioner's "don't edit the tests to make them pass" stopped edits but the agent started deleting the tests instead; the thread's conclusion was that this class of rule needs a hook that blocks the edit/delete outright, not a CLAUDE.md line (and one report of the agent deleting the hook itself in the next session, underscoring that enforcement must sit outside the agent's own edit surface).
7. **Fact-check against the file before describing the code.** "Before writing 'we do X' or 'we don't have X' anywhere, reopen the code and cite file:line, even if it said the same thing an hour ago." Added after the agent described its own codebase incorrectly in two consecutive drafts.
8. **Avoid open-ended Markdown-file mandates.** A counter-pattern: telling an agent to maintain Markdown files in a folder, without tighter scoping, reportedly leads to agents scattering ad hoc files (e.g., `Report_final.md`) throughout the repo.

A secondary thread theme: several commenters reported these lines matter less with newer/stronger models (Fable 5.1, Opus 5.5), suggesting at least some of this class of instruction compensates for model limitations that erode over model generations.

## Sources

- [What's the one line in your CLAUDE.md that made the biggest difference? — r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1xeautc/comment/19rlwk7oqkz9d/) — all quotes above are from this thread's comments, lightly edited for length.

## Security

N/A — prose instruction patterns for an agent's own configuration file, not software. The hook-vs-words distinction (pattern 6) has a real security-adjacent implication: any constraint whose violation would be costly (data loss, deleted tests, deleted safeguards) should be enforced by a hook or permission rule outside the agent's own context, not by an instruction the same agent could talk itself out of or an instruction file the agent could edit.
