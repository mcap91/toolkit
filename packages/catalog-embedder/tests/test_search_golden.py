"""WK-0098 golden test: semantic=False lexical output must match the pre-change capture
exactly. Fixtures in tests/fixtures/search-golden-2026-10-31/ are the unedited output of
`python -m catalog_embedder search` (semantic ON) at commit 642ab54, 738 entries, captured
2026-10-31 — see that directory's README.md and commands.txt for provenance.

The underlying query/terms/semantic_n/category per capture are hardcoded below rather than
parsed from commands.txt: that file's command lines are a human-readable summary (multi-word
--query and --term values appear unquoted, so they are not unambiguously machine-parseable),
not a shell-escaped transcript. Each tuple here was cross-checked against the capture's own
`swept_terms` (the authoritative, machine-checkable record of what was actually swept) and
against commands.txt's prose rendering of the same call — see the comment per case.
"""

import json
from pathlib import Path

import pytest

from catalog_embedder.search import run_search

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "search-golden-2026-10-31"
# tests/ -> catalog-embedder/ -> packages/ -> repo root
REPO_ROOT = Path(__file__).parent.parent.parent.parent
ENTRIES_DIR = REPO_ROOT / "catalog" / "entries"

# (capture file stem, query, terms, semantic_n, category) — order matches commands.txt.
CASES = [
    # catalog_embedder search --dir <toolkit> --query ocr
    ("q01-query-only", "ocr", None, 10, None),
    # catalog_embedder search --dir <toolkit> --query ocr document to markdown
    #   --term ocr --term "text extraction" --term "document to markdown"
    #   --term "handwriting recognition"
    ("q02-terms-expanded", "ocr document to markdown",
     ["ocr", "text extraction", "document to markdown", "handwriting recognition"], 10, None),
    # catalog_embedder search --dir <toolkit> --query zqxv nonexistent term
    ("q04-miss", "zqxv nonexistent term", None, 10, None),
    # catalog_embedder search --dir <toolkit> --query agent memory
    ("q05-multiword-query", "agent memory", None, 10, None),
    # catalog_embedder search --dir <toolkit> --query retrieval augmented generation
    #   --term rag --term retrieval --semantic-n 1
    ("q06-semantic-n-1", "retrieval augmented generation", ["rag", "retrieval"], 1, None),
    # catalog_embedder search --dir <toolkit> --query ocr  (repeat of q01, determinism check)
    ("q01-repeat", "ocr", None, 10, None),
    # catalog_embedder search --dir <toolkit> --query 'vector database'
    #   --term 'vector database' --term embeddings --category framework
    ("q03-category", "vector database", ["vector database", "embeddings"], 10, "framework"),
]

if not ENTRIES_DIR.is_dir():
    pytest.skip(
        f"catalog/entries not found at {ENTRIES_DIR} — golden test needs the live catalog "
        "(738 entries) checked out at the repo root; skipping.",
        allow_module_level=True,
    )


def _load_capture(stem: str) -> dict:
    return json.loads((FIXTURES_DIR / f"{stem}.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("stem,query,terms,semantic_n,category", CASES)
def test_golden_lexical_matches_pre_change_capture(stem, query, terms, semantic_n, category):
    capture = _load_capture(stem)
    capture_lexical = [r for r in capture["results"] if r["match"]["type"] == "lexical"]

    response = run_search(
        REPO_ROOT, query, terms=terms, semantic_n=semantic_n, category=category, semantic=False,
    )

    lexical_results = [r for r in response["results"] if r["match"]["type"] == "lexical"]
    assert lexical_results == capture_lexical
    assert response["swept_terms"] == capture["swept_terms"]
    assert response["lexical_total"] == capture["lexical_total"]
    assert response["total"] == response["lexical_total"]
    assert all(r["match"]["type"] != "semantic" for r in response["results"])


def test_q04_miss_returns_total_zero():
    response = run_search(REPO_ROOT, "zqxv nonexistent term", semantic_n=10, semantic=False)
    assert response["total"] == 0
    assert response["lexical_total"] == 0
    assert response["results"] == []
