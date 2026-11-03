# html-report

A Claude Code skill and a set of self-contained HTML reference pages, one per kind of output. Agents use them as
visual examples, so the HTML reports and views they build look like one family. People open a page to see its colors,
boxes, arrows, charts, and rules.

## Install

```
cp -r skills/html-report <your-project>/.claude/skills/html-report
```

or into `~/.claude/skills/` for every project. The style pages travel with the skill, so a copied skill works with no
access to this repo.

## The styles

| Page | Use it for |
|---|---|
| [styles/chain.html](styles/chain.html) | One initiative and its next work items, in build order, as a top-to-bottom flow |
| [styles/science-report.html](styles/science-report.html) | A results page: experiment, eval, benchmark. Flow, compared setups, bars, tables, takeaways |
| [styles/text-report.html](styles/text-report.html) | A prose page with no charts: status, investigation, proposal, postmortem |
| [styles/concept.html](styles/concept.html) | A boundary: two owners, what crosses between them, allowed and never rules |
| [styles/architecture.html](styles/architecture.html) | System diagrams. A pointer: render them with archify, not by hand |

Not yet: job board and shop board styles (kb-autoshop). Tracked in toolkit WK-0109.

These are visual styles. `docs/output-styles/` is a different thing: the voice rules for an agent's chat replies.

## Use

The pages are visual references, not templates. A new page should look like it belongs to the family (palette, type,
cards, stripes, chips, arrows, charts, restraint), but its layout and sections follow its own content. Mixing parts
from several references is fine; leaving out what the content does not need is expected.

Ask the agent for a page, or run `/html-report`. `SKILL.md` tells the agent what carries over and what does not.
By hand: open the nearest reference, take the CSS variables and components that fit (reusable CSS sits above the
`SPECIMEN-ONLY` marker), and build the page around your content.

## Rules for every page

These bind the reference pages themselves. Pages built from them share 1 to 3.

1. Self-contained: one HTML file, no external CSS, fonts, or scripts. It opens offline.
2. Light and dark themes via `data-theme` on `<html>`, with a toggle. Test both.
3. Prose follows the write-plain rules.
4. No work or project content in a reference page. Use placeholders (WK-0001, owner A, setup_a).
5. Add a rule to a page with a date. Do not remove a rule without a note.

## Update a style

1. Edit the page in `styles/` in place. Keep class names and CSS variable names stable. Pages already built from a
   style, and kb's chain generator (kb WK-0228), depend on them. If a rename is needed, note it under Changes below.
2. Keep the split: reusable CSS above the `SPECIMEN-ONLY` marker, specimen-only CSS and the Rules section below it.
3. Add or change a rule in the page's Rules section, with the date.
4. Render both themes and look at them:

   ```
   B=$(find ~/.cache/ms-playwright -name chrome-headless-shell -type f | head -1)
   "$B" --no-sandbox --hide-scrollbars --window-size=1280,1600 --screenshot=/tmp/light.png "file://$PWD/styles/<page>.html"
   "$B" --no-sandbox --hide-scrollbars --window-size=1280,1600 --blink-settings=preferredColorScheme=0 \
     --screenshot=/tmp/dark.png "file://$PWD/styles/<page>.html"
   ```

   The page picks the theme from the system preference on first load; the flag forces dark.
5. Check for leaks and prose tells, outside code and CSS:

   ```
   grep -nPi '[\x{2013}\x{2014}]|\b(leverag|utiliz|robust|seamless)' styles/<page>.html
   ```

   Also read the page for real names, record ids, or project vocabulary. Placeholders only.
6. Add a line under Changes. If `chain.html` changed, tell the kb chain generator to re-copy its CSS.

To add a new style: start from the closest page, keep the shared neutrals and the theme toggle, add a row to the table
above, and add the style to the picking table in `SKILL.md`.

## Sources

Each page was taken from a page that worked, then stripped to placeholders (2026-11-02):

- chain.html: kb's hand-built IN-0011 chain view, plus the theme toggle, next-actions callout, and gate box from an
  earlier chain view. The light palette is new.
- science-report.html: an internal experiment report, via the first report-style template and guide.
- text-report.html: the science-report shell with the charts removed, and the `direct` output style's reply order.
- concept.html: section 1 of kb's kb-exchange concept page.
- architecture.html: kb's archify-rendered dispatch diagram.

## Changes

- 2026-11-02: SKILL.md rewritten: the pages are visual references, not templates (operator).
- 2026-11-02: first set of five pages. Moved from `docs/html-report-styles/` into this skill so a copied skill carries
  its pages.
