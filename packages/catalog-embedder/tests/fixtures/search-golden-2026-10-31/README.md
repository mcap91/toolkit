# Pre-change search captures for WK-0098 (golden fixtures)

Real, unedited output of `python -m catalog_embedder search` on the live catalog, captured by the orchestrator
on 2026-10-31 at toolkit commit 642ab54 (738 entries, `catalog/.vectors.json` present and valid, semantic channel ON).
Purpose: WK-0098 acceptance "lexical results identical to today's lexical channel on a fixed query set".
The builder copies these into the embedder test fixtures and asserts that, with the semantic switch off, the
`type: "lexical"` results, `swept_terms` and `lexical_total` are byte-identical, and no `type: "semantic"` result appears.

Command per file: see commands.txt (one line per capture, same order). Python: packages/catalog-embedder/.venv.
Timings (wall clock, whole process incl. model load, semantic ON): q01 0.87 s, q02 0.91 s, q04 0.85 s, q05 0.84 s,
q06 0.88 s, q01-repeat 0.79 s. Use these as the "before" figures for the per-call timing acceptance criterion.

Files
- q01-query-only: query only, no terms (whole query as one lookup term). lexical 37, semantic 10.
- q02-terms-expanded: 4 expanded terms. lexical 92, semantic 10. 74 KB (audit F3 overflow class).
- q03-category: category filter (framework).
- q04-miss: honest miss. lexical 0, semantic 10 (today the response still carries 10 semantic rows).
- q05-multiword-query: multiword query, no terms. lexical 108.
- q06-semantic-n-1: --semantic-n 1. lexical 112, semantic 1.
- q01-repeat: same as q01, confirms determinism of the lexical channel.
