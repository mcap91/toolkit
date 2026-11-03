---
name: html-report
description: Build an HTML report or view in the house style. Five self-contained style pages ship with this skill (chain view of an initiative and its next work items, science report with charts, text report, concept/boundary page, architecture via archify). Use when the user asks for an HTML report, results page, write-up, dashboard page, chain view, concept page, or diagram, or says "/html-report", "make this a page", or "write this up as a report".
---

# html-report

Build one self-contained HTML page by copying the matching style page in `styles/` (next to this file). Copy its CSS
and markup, replace the content, follow its rules, run the checks. Do not invent a new look.

## 1. Pick the style

| The page is... | Style |
|---|---|
| one initiative and its next work items, in build order | `styles/chain.html` |
| results with numbers: experiment, eval, benchmark, comparison | `styles/science-report.html` |
| prose with no charts: status, investigation, proposal, postmortem | `styles/text-report.html` |
| a boundary: two owners, what crosses, who may write what | `styles/concept.html` |
| a system diagram: components, flows, sequences, states | `styles/architecture.html` (use archify; do not hand-write) |

If two fit, pick the one with fewer components that still carries the content. If none fits, use `text-report.html`
and say so in your reply. If the repo already has a generator for this view (for example a chain-view command), run
the generator instead of writing the page by hand.

## 2. Read the style page in full

Read the chosen page end to end before writing: its CSS, its markup, and its Rules section at the bottom. The rules
are binding for the page you build.

## 3. Build the page

1. Start a new file. Copy the `<head>` from the style page: the theme script and every CSS line **above** the
   `SPECIMEN-ONLY` marker. Do not copy CSS below the marker.
2. Copy the markup of the components you need. Keep the class names and CSS variable names as they are.
3. Replace every placeholder with real content. Remove every `<span class="cls">` label and the specimen sections
   (Palette, Rules).
4. Keep the theme toggle button and its script.
5. Add nothing external: no CDN links, web fonts, or scripts. One file that opens offline.
6. Write the prose with the write-plain rules (active voice, short sentences, plain words, no em dashes).
7. Every number traces to a source. Link the sources in the footer.

Save where the user says. If they did not say, follow the repo's convention for generated pages, or ask once.

## 4. Check before you reply

- Render the page in both themes if a headless browser is available, and look at the screenshots:

  ```
  B=$(find ~/.cache/ms-playwright -name chrome-headless-shell -type f | head -1)
  "$B" --no-sandbox --hide-scrollbars --window-size=1280,1600 --screenshot=/tmp/light.png "file://<abs path>"
  "$B" --no-sandbox --hide-scrollbars --window-size=1280,1600 --blink-settings=preferredColorScheme=0 --screenshot=/tmp/dark.png "file://<abs path>"
  ```

  If no browser is available, say the page was not rendered.
- Run the style page's own checklist (science-report and text-report have one).
- `grep -nPi '[\x{2013}\x{2014}]|\b(leverag|utiliz|robust|seamless)' <file>` is clean outside code and CSS.
- If the page is for readers outside the project, it carries no internal vocabulary (record ids, tool names, code
  names) outside the footer.

In your reply, give the file path, the style used, and whether both themes were rendered.

## Do not

- Do not edit the style pages in `styles/` while building a report. Changing a style follows `README.md`.
- Do not mix two styles in one page.
- Do not add colors outside the style's palette, or charts to a text report.
