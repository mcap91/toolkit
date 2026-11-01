"""`search` command: semantic scoring with BM25 keyword rescue over catalog entries."""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path
from typing import Any

from . import embeddings
from .build import run_build
from .frontmatter import read_all_entries
from .vectors import cosine_similarity, is_valid, read_vectors

BM25_K1 = 1.2
BM25_B = 0.75
BM25_TOKENIZE_RE = re.compile(r"[^a-z0-9]+")

DEFAULT_SEMANTIC_N = 10
MAX_TERMS = 50
MAX_TERM_CHARS = 200
MAX_QUERY_CHARS = 2000


def _bm25_tokenize(text: str) -> list[str]:
    return [t for t in BM25_TOKENIZE_RE.split(text.lower()) if t]


def _entry_text(frontmatter: dict, body: str) -> str:
    """Concatenate all searchable fields into one document string."""
    parts = [
        str(frontmatter.get("title") or ""),
        str(frontmatter.get("name") or ""),
        str(frontmatter.get("summary") or ""),
        body,
        " ".join(str(t) for t in (frontmatter.get("tags") or [])),
    ]
    return " ".join(parts)


def bm25_score_all(
    entries: list[tuple[str, dict, str]],  # [(name, frontmatter, body), ...]
    query_terms: list[str],
) -> dict[str, float]:
    """Compute BM25 scores for all entries against query terms. Returns {name: score}."""
    # Tokenize all documents
    docs: dict[str, list[str]] = {}
    for name, fm, body in entries:
        docs[name] = _bm25_tokenize(_entry_text(fm, body))

    N = len(docs)
    if N == 0:
        return {}

    avgdl = sum(len(d) for d in docs.values()) / N

    # Document frequency per query term
    df: dict[str, int] = {}
    for term in query_terms:
        df[term] = sum(1 for d in docs.values() if term in d)

    # Score each document
    scores: dict[str, float] = {}
    for name, tokens in docs.items():
        score = 0.0
        dl = len(tokens)
        for term in query_terms:
            tf = tokens.count(term)
            if tf == 0:
                continue
            idf = math.log((N - df[term] + 0.5) / (df[term] + 0.5) + 1)
            numerator = tf * (BM25_K1 + 1)
            denominator = tf + BM25_K1 * (1 - BM25_B + BM25_B * dl / avgdl)
            score += idf * numerator / denominator
        scores[name] = score
    return scores


def _term_regexes(term: str) -> list[re.Pattern[str]]:
    """One boundary regex per whitespace token; a term matches iff ALL match (AND).

    (?<!\\w) instead of \\b: identical for word-leading tokens, correct for
    punctuation-leading ones (".net" matches " .net" but not "asp.net").
    """
    return [re.compile(r"(?<!\w)" + re.escape(tok)) for tok in term.lower().split()]


def resolve_terms(terms: list[str] | None, query: str) -> list[str]:
    """Normalize agent-supplied terms; fall back to the whole query as ONE AND term.

    Explicit terms: strip, lowercase, drop empties, dedupe preserving order (count and
    length bounds are raised by run_search, not silently truncated here).
    Fallback: deduped query tokens joined into a single multi-token AND term.
    Returns [] only when there is nothing to search lexically.
    """
    cleaned = [t.strip().lower() for t in (terms or []) if t and t.strip()]
    seen: set[str] = set()
    deduped = [t for t in cleaned if not (t in seen or seen.add(t))]
    if deduped:
        return deduped
    tokens = list(dict.fromkeys(_bm25_tokenize(query)))
    return [" ".join(tokens)] if tokens else []


def lexical_members(
    entries_dir: Path, names: list[str], terms: list[str]
) -> tuple[dict[str, list[str]], dict[str, int]]:
    """({name: [matched terms]}, {term: hit count}) over raw lowercased file text."""
    raw = {n: (entries_dir / f"{n}.md").read_text(encoding="utf-8").lower() for n in names}
    members: dict[str, list[str]] = {}
    hits: dict[str, int] = {}
    for term in terms:
        regexes = _term_regexes(term)
        if not regexes:
            hits[term] = 0
            continue
        count = 0
        for name, text in raw.items():
            if all(r.search(text) for r in regexes):
                members.setdefault(name, []).append(term)
                count += 1
        hits[term] = count
    return members, hits


_EVIDENCE_FIELDS = ("title", "name", "summary", "tags", "body")


def _match_fields(matched_terms: list[str], frontmatter: dict, body: str) -> list[str]:
    """Which named fields any matched term hits; ["frontmatter"] when none do."""
    texts = {
        "title": str(frontmatter.get("title") or "").lower(),
        "name": str(frontmatter.get("name") or "").lower(),
        "summary": str(frontmatter.get("summary") or "").lower(),
        "tags": " ".join(str(t) for t in (frontmatter.get("tags") or [])).lower(),
        "body": body.lower(),
    }
    out: list[str] = []
    for field in _EVIDENCE_FIELDS:
        for term in matched_terms:
            if all(r.search(texts[field]) for r in _term_regexes(term)):
                out.append(field)
                break
    return out or ["frontmatter"]


def run_search(
    dir: Path,
    query: str,
    terms: list[str] | None = None,
    semantic_n: int = DEFAULT_SEMANTIC_N,
    decision_status: str | None = None,
    category: str | None = None,
    semantic: bool = True,
) -> dict[str, Any]:
    # Input bounds — enforced here too, not only at CLI/Zod
    if not 1 <= semantic_n <= 50:
        raise ValueError("semantic_n must be between 1 and 50")
    if len(query) > MAX_QUERY_CHARS:
        raise ValueError(f"query exceeds {MAX_QUERY_CHARS} characters")
    raw_terms = terms or []
    if len(raw_terms) > MAX_TERMS:
        raise ValueError(f"too many terms (max {MAX_TERMS})")
    if any(len(t) > MAX_TERM_CHARS for t in raw_terms):
        raise ValueError(f"term exceeds {MAX_TERM_CHARS} characters")

    entry_vectors: dict[str, list[float]] = {}
    query_vector: list[float] | None = None
    # WK-0098 (DEC-0004 amendment): semantic off means no vector read/build and no query
    # embedding — the model and the vector file are never touched.
    if semantic:
        vector_data = read_vectors(dir)
        if not is_valid(vector_data):
            print(
                "catalog-embedder: vector file missing or model mismatch — running build",
                file=sys.stderr,
            )
            run_build(dir)
            vector_data = read_vectors(dir)
        entry_vectors = (vector_data or {}).get("entries", {})

        if query.strip():
            [query_vector] = embeddings.embed_texts([query])

    raw = read_all_entries(dir / "catalog" / "entries")

    candidates: list[dict[str, Any]] = []
    for name, (frontmatter, body) in raw.items():
        status = frontmatter.get("decision_status") or "open"
        if decision_status and status != decision_status:
            continue
        if category and frontmatter.get("category") != category:
            continue

        cosine = 0.0
        if query_vector is not None and name in entry_vectors:
            cosine = max(0.0, min(1.0, cosine_similarity(query_vector, entry_vectors[name])))

        candidates.append(
            {
                "name": name,
                "frontmatter": frontmatter,
                "status": status,
                "body": body,
                "cosine": cosine,
            }
        )

    def _build_result(c: dict[str, Any], match: dict[str, Any]) -> dict[str, Any]:
        fm = c["frontmatter"]
        result: dict[str, Any] = {
            "name": c["name"],
            "title": fm.get("title"),
        }
        if fm.get("url"):
            result["url"] = fm["url"]
        result["category"] = fm.get("category")
        result["decision_status"] = c["status"]
        result["summary"] = fm.get("summary")
        result["tags"] = fm.get("tags") or []
        result["match"] = match
        return result

    entries_dir = dir / "catalog" / "entries"
    term_list = resolve_terms(terms, query)

    if not term_list and not query.strip():  # listing mode: empty query, no terms
        results = [_build_result(c, {"type": "listing"}) for c in candidates]
        results.sort(key=lambda r: ((r["title"] or "").lower(), (r["name"] or "").lower()))
        return {"results": results, "swept_terms": [], "lexical_total": 0, "total": len(results)}

    if term_list:
        members, hits = lexical_members(entries_dir, [c["name"] for c in candidates], term_list)
        swept = [{"term": t, "hits": hits[t]} for t in term_list]
    else:
        # Non-empty query that tokenized to nothing: zero-hit sweep, but semantic
        # selection below STILL RUNS on the embedded query.
        members = {}
        swept = [{"term": query.strip().lower(), "hits": 0}]

    bm25_tokens = [tok for t in term_list for tok in _bm25_tokenize(t)]
    lex_candidates = [c for c in candidates if c["name"] in members]
    bm25 = bm25_score_all(
        [(c["name"], c["frontmatter"], c["body"]) for c in lex_candidates], bm25_tokens
    )
    lex_candidates.sort(key=lambda c: (
        -bm25.get(c["name"], 0.0),
        str(c["frontmatter"].get("title") or "").lower(),
        c["name"],
    ))
    lexical_results = [
        _build_result(c, {
            "type": "lexical",
            "terms": members[c["name"]],
            "fields": _match_fields(members[c["name"]], c["frontmatter"], c["body"]),
        })
        for c in lex_candidates
    ]

    sem_candidates = [c for c in candidates if c["name"] not in members and c["cosine"] > 0.0]
    sem_candidates.sort(key=lambda c: (
        -c["cosine"],
        str(c["frontmatter"].get("title") or "").lower(),
        c["name"],
    ))
    semantic_results = [
        _build_result(c, {"type": "semantic", "rank": i + 1})
        for i, c in enumerate(sem_candidates[:semantic_n])
    ]

    results = lexical_results + semantic_results
    return {
        "results": results,
        "swept_terms": swept,
        "lexical_total": len(lexical_results),
        "total": len(results),
    }
