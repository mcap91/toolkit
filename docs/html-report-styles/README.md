# HTML report styles

Self-contained HTML reference pages, one per kind of output. Open a page to see the style: its colors, boxes,
arrows, charts, and rules. To use a style, copy the page's CSS (everything above the `SPECIMEN-ONLY` marker),
keep the class names, and replace the content. Each page also carries its rules at the bottom.

| Page | Use it for | Status |
|---|---|---|
| [chain.html](chain.html) | One initiative and its next work items, in build order, as a top-to-bottom flow | reference; kb generates it from records (kb WK-0228) |
| [science-report.html](science-report.html) | A results page: experiment, eval, benchmark. Flow, compared setups, bars, tables, takeaways | reference |
| [text-report.html](text-report.html) | A prose page with no charts: status, investigation, proposal, postmortem | reference |
| [concept.html](concept.html) | A boundary: two owners, what crosses between them, allowed and never rules | reference |
| [architecture.html](architecture.html) | System diagrams. A pointer: render them with archify, not by hand | pointer |
| job board, shop board | kb-autoshop launch and run views | not yet: designed with kb WK-0233 and WK-0224 |

These are visual styles. `docs/output-styles/` is a different thing: the voice rules for an agent's chat replies.

## Rules for every page

1. Self-contained: one HTML file, no external CSS, fonts, or scripts. It opens offline.
2. Light and dark themes via `data-theme` on `<html>`, with a toggle. Test both.
3. Prose follows the write-plain rules.
4. No work or project content in a reference page. Use placeholders (WK-0001, owner A, setup_a).
5. Add a rule to a page with a date. Do not remove a rule without a note.

## Sources

Each page was taken from a page that worked, then stripped to placeholders (2026-11-02):

- chain.html: kb `wiki/dashboard/IN-0011-chain.html`, plus the theme toggle, next-actions callout, and gate box from an earlier chain view.
  The light palette is new.
- science-report.html: an internal experiment report, via the first report-style template and guide.
- text-report.html: the science-report shell with the charts removed, and the `direct` output style's reply order.
- concept.html: section 1 of kb `wiki/dashboard/kb-exchange-concept.html`.
- architecture.html: kb `wiki/dashboard/kb-dispatch-v2.html`, rendered by archify.
