"""WK-0098: with semantic=False, run_search must never touch the vector file or the model."""

from pathlib import Path

from catalog_embedder import embeddings, search
from catalog_embedder.search import run_search
from conftest import write_entry


def _raise(*args, **kwargs):
    raise AssertionError("semantic=False must not call this")


def test_semantic_off_never_loads_vectors_or_model(catalog_dir: Path, monkeypatch):
    entries_dir = catalog_dir / "catalog" / "entries"
    write_entry(entries_dir, "pdf-tool", "PDF Tool", "cli-tool", "parses pdf files", ["pdf", "ocr"], "pdf body")

    # If semantic=False lets any of these run, the test fails loudly instead of quietly
    # exercising a path a real sandbox (no model cache, no vector file) can't support.
    monkeypatch.setattr(search, "read_vectors", _raise)
    monkeypatch.setattr(search, "run_build", _raise)
    monkeypatch.setattr(embeddings, "embed_texts", _raise)

    response = run_search(catalog_dir, "pdf", semantic=False)

    assert response["lexical_total"] == 1
    assert response["total"] == response["lexical_total"]
    assert all(r["match"]["type"] != "semantic" for r in response["results"])
