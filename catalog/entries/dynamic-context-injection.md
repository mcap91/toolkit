---
name: dynamic-context-injection
title: Dynamic Context Injection in Claude Code Skills
url: "https://code.claude.com/docs/en/skills"
category: agent-pattern
summary: "Claude Code SKILL.md feature — `!`<command>`` (inline) or fenced ` ```! ` blocks (multi-line) run shell commands before the skill body reaches Claude, splicing stdout into the prompt; enables deterministic, non-LLM routing of which instructions get loaded instead of prose like 'if X, read file Y'"
tags: [claude-code, skills, skill-md, shell-injection, determinism, context-engineering, allowed-tools, prompt-construction]
reviewed: 2026-09-25
acquired: 2026-09-25
license: NOASSERTION
security_flags: []
overlaps: [agent-skills-spec]
source: unknown
---

## What it does

A Claude Code-specific extension to the SKILL.md format (Claude Code, not the cross-vendor Agent Skills spec body). Any line starting with `!`<command>`` — or a fenced code block opened with ` ```! ` for multiple commands — is executed as a shell command when the skill is loaded, and its stdout is substituted into the skill text before Claude ever sees it. Claude receives the rendered output, not the command syntax.

Two forms:
- **Inline**: `!`<command>``. Only recognized when `!` is at the start of a line or immediately follows whitespace; `!` glued to a preceding character (e.g. `KEY=!`cmd``) is left as literal text and nothing runs.
- **Multi-line**: a fenced block opened with ` ```! ` containing several commands.

Substitution is a single pass over the original file — command output is inserted as plain text and is not re-scanned, so an injected command cannot itself emit a new `!`<command>`` placeholder for further expansion.

The stated motivation: replace prose-level routing instructions ("If you are fixing a bug, read `./references/bugfix-instructions.md`") with a shell command that conditionally embeds the right reference file directly, e.g. `!`cat "${CLAUDE_SKILL_DIR}/references/$workType-instructions.md" || true``. This moves the routing decision out of LLM interpretation and into deterministic shell logic, and avoids the token cost of an intermediate "read about what to read" step.

## Mechanical details

- **Exit code handling (default Bash shell)**: a non-zero exit code from an injected command aborts the *entire* skill invocation, not just that one substitution. Carveout: exit code 1 from `find`, `grep`, `git diff`, or `diff` is treated as a normal "no match" result and its output is still injected; exit codes ≥2 still fail even for these four commands. The documented workaround for a command expected to fail is appending `|| true`.
- **PowerShell shell** (`shell: powershell`): a different carveout list applies — `grep` and `git diff` are exempted, but `find` and `diff` are not.
- **Failure surfacing**: a failed injected command renders `Shell command failed for pattern "..."` with the command's stderr attached, and aborts the skill invocation — Claude never sees that skill's content for the run.
- **Permission model**: injected commands are checked against permission rules before rendering. Commands not pre-approved via `allowed-tools` (e.g. `allowed-tools: Bash(gh *)`) can trigger a permission prompt that aborts skill loading; a command matching an explicit deny rule aborts with `Shell command permission check failed for pattern "..."`. In auto mode, unmatched commands instead load the skill with an instruction for Claude to run the command itself, subject to auto mode's normal checks. Forked skills with `agent` set still abort on unpermitted commands.
- **Kill switch**: `"disableSkillShellExecution": true` in settings disables the whole mechanism; each injection point is replaced with the literal string `[shell command execution disabled by policy]`. Applies to user/project/plugin/additional-directory skills; bundled and managed skills are unaffected. Intended for managed settings where users can't override it.
- **Synced-skill restriction (Claude Code v2.1.228+)**: skills synced from a claude.ai account never execute injected commands locally, regardless of local settings — in cloud sessions the body keeps normal (disabled) behavior, in desktop Cowork sessions each `!` line is replaced with the disabled-policy placeholder, and in other local sessions the commands reach Claude as literal text (or the placeholder, if `disableSkillShellExecution` is also on).

## Example (from docs)

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`
```

`gh pr diff`, `gh pr view --comments`, and `gh pr diff --name-only` run immediately on skill load; their output replaces the three placeholders before Claude sees the skill, and `allowed-tools: Bash(gh *)` pre-approves all three so none of them trigger a permission prompt.

## Security

Commands run locally with the invoking user's permissions — only stdout is sent to the model, not the command itself, but the command still executes with full local privileges, so an untrusted or unreviewed skill can run arbitrary shell as the user the moment it's loaded (not just when Claude decides to act). The built-in mitigations are the `allowed-tools` pre-approval gate, the global `disableSkillShellExecution` kill switch for managed environments, and the hard restriction that skills synced from claude.ai never execute injected commands locally. None of these are enabled by default beyond the permission-prompt-on-unapproved-command behavior, so a skill's `!`<command>`` lines deserve the same review as any other shell code before the skill is trusted.
