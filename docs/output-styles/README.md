# direct-output-style

A Claude Code [output style](https://code.claude.com/docs/en/output-styles.md) in one Markdown file. It sets the voice and shape of every reply: answer first, short turns, plain words (ASD-STE100 as a guide), a fixed reply order (action items, decisions, recommendations, explanation), no `path:line` citations, and one closing question. It also carries the coding-discipline and evidence rules. One hook ships with it: `hooks/reply-length.py`, a Stop hook that logs the word count of every reply.

## Install (symlink)

Symlink the style from this repo, so a `git pull` updates it. Do not copy it; a copy goes stale.

```bash
mkdir -p ~/.claude/output-styles
ln -sfn ~/projects/toolkit/docs/output-styles/direct.md ~/.claude/output-styles/direct.md
```

Activate it for all projects in `~/.claude/settings.json`:

```json
{
  "outputStyle": "direct"
}
```

Or run `/output-style direct` in a session. Note: `/output-style` and `/config` save the choice to the current project's `.claude/settings.local.json`, not to the global file.

## Install the reply-length hook (symlink)

The style asks for 200-300 word replies. The hook measures what you actually get. It only logs; it never blocks.

```bash
mkdir -p ~/.claude/hooks
ln -sfn ~/projects/toolkit/docs/output-styles/hooks/reply-length.py ~/.claude/hooks/reply-length.py
```

Add it to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python3 ~/.claude/hooks/reply-length.py" } ] }
    ]
  }
}
```

Output goes to `~/.claude/reply-length/`: `log.jsonl` (one line per reply), `capture-stop-input.json` (the first raw hook input, kept as evidence of its shape), and `errors.log`. After about a week, read the log and decide whether a blocking ceiling is worth its cost. A blocking Stop hook makes Claude rewrite the whole reply, which costs a full turn.

`agent-lockdown checkup` verifies that the style and the hook are symlinks into this repo.

## Things to know

- **The name is case-sensitive in settings.** `"outputStyle": "direct"` must match the `name` field in the frontmatter. A value that does not match gives you the Default style, with no error.
- **Project settings win.** A project's `.claude/settings.json` or `.claude/settings.local.json` that sets `outputStyle` overrides the global value. Check there first if the style does not apply.
- **Restart after a change.** Claude Code reads style files at startup. After you edit the file or `git pull`, restart Claude Code.
- **Verify the install.** Run `/output-style` with no argument. The list must show `direct` and mark it as current.
- **Subagents do not get the style.** It applies to the main conversation and to forks only.
- **It is an instruction, not a guarantee.** Claude follows it most of the time. For something that must happen every time, use a hook.
- **`keep-coding-instructions: true`** keeps Claude Code's built-in software-engineering instructions next to this style.

## Install the toolkit skills the same way

Skills support symlinked folders. Symlink each skill folder so the frontmatter stays current:

```bash
ln -sfn ~/projects/toolkit/skills/explain-me-this ~/.claude/skills/explain-me-this
```

If `~/.claude/skills/explain-me-this` is already a real folder (an old copy), delete it first. `ln -sfn` does not replace a real folder; it puts the link inside it.

The frontmatter in `skills/explain-me-this/SKILL.md` controls the behavior:

- `disable-model-invocation: true` — only you can start the skill, with `/explain-me-this`. Claude cannot load it on its own.
- `disallowed-tools: Edit Write` — removes the file-editing tools while the skill is active. The restriction clears when you send your next message.

A stale copy without these fields lets Claude start the skill on its own and edit files.

## Clean up the old installation

If `setup-behavioral-baseline.sh` was installed before, remove its parts:

```bash
# Remove hook scripts
rm -f ~/.claude/fable-mode/reinject.sh ~/.claude/fable-mode/leak_test.py
rmdir ~/.claude/fable-mode 2>/dev/null || true

# Remove the hooks.UserPromptSubmit block from ~/.claude/settings.json
# (delete the "hooks" key or just its "UserPromptSubmit" entry)

# Remove the behavioral-baseline markers from ~/.claude/CLAUDE.md
# (delete the block between <!-- BEGIN behavioral-baseline --> and <!-- END behavioral-baseline -->)
```

The output style sends the same rules with every request, so the re-injection hook is not needed.
