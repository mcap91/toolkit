---
name: html-report
description: House visual style for HTML reports and views. Five reference pages ship with this skill as visual examples (chain view of an initiative, science report with charts, text report, concept/boundary page, architecture via archify). Use when building any HTML report, results page, write-up, dashboard page, chain view, concept page, or diagram, or when the user says "/html-report" or "make this a page".
---

# html-report

The pages in `styles/` are visual references, not templates. They show what the house style looks like: the palette,
the type, the cards, stripes, chips, arrows, charts, and the restraint. Your page should look like it belongs to the
same family. Its layout, sections, and components follow its own content, not the reference.

## The references

| Reference | Shows the look of |
|---|---|
| `styles/chain.html` | a flow of work items: status stripes, chips, arrows, a fork and merge, a gate |
| `styles/science-report.html` | results: box-and-arrow flow, compared setups, bars with a reference line, tables, takeaway cards, a dot rail |
| `styles/text-report.html` | prose: answer box, callouts, numbered steps, quoted captures |
| `styles/concept.html` | a boundary: owner boxes, a bridge, allowed and never rows |
| `styles/architecture.html` | system diagrams are rendered with archify, not hand-written |

Look at the one or two nearest to what you are building. Mixing parts from several is fine.

## What carries over

- **The family look:** the neutrals and accent colors, the fonts, the card and border treatment, the spacing. Reuse
  the CSS variables and components that fit; write new components in the same spirit when none fits.
- **Color means something:** one color per meaning, kept the same across the page. Status colors for status, series
  colors for series, verdict colors (good/bad) only for verdicts.
- **Self-contained:** one HTML file, no external CSS, fonts, or scripts. It opens offline.
- **Light and dark themes**, with a toggle.
- **Plain prose:** the write-plain rules. Lead with the answer or the question the page answers.
- **Numbers trace to sources**, linked at the end. Label estimates as estimates.

The Rules section at the bottom of each reference records what worked for that kind of page. Treat it as guidance,
not as a checklist to satisfy.

## What does not carry over

- The section order, the number of sections, or any placeholder text.
- The `SPECIMEN-ONLY` parts: class-name labels, palette swatches, the Rules section.
- Components the content does not need. Leave out anything that is there only because a reference had it.

## Before you reply

If a headless browser is available, render the page in both themes and look at it:

```
B=$(find ~/.cache/ms-playwright -name chrome-headless-shell -type f | head -1)
"$B" --no-sandbox --hide-scrollbars --window-size=1280,1600 --screenshot=/tmp/light.png "file://<abs path>"
"$B" --no-sandbox --hide-scrollbars --window-size=1280,1600 --blink-settings=preferredColorScheme=0 --screenshot=/tmp/dark.png "file://<abs path>"
```

If not, say the page was not rendered. Do not edit the reference pages while building a report; changing a reference
follows `README.md`.
