"""CLI entry point: `python -m catalog_embedder build|search ...`"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .build import run_build
from .search import MAX_QUERY_CHARS, MAX_TERM_CHARS, MAX_TERMS, run_search


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m catalog_embedder")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="Embed all catalog entries and write the vector file")
    build_parser.add_argument("--dir", required=True, help="Path to the repo root")

    search_parser = subparsers.add_parser("search", help="Survey search: complete lexical sweep + flagged semantic rescue")
    search_parser.add_argument("--query", required=True)
    search_parser.add_argument("--dir", required=True, help="Path to the repo root")
    search_parser.add_argument("--term", dest="terms", action="append", default=[],
                                help="Expanded search term; repeatable (max 50)")
    search_parser.add_argument("--semantic-n", dest="semantic_n", type=int, default=10)
    search_parser.add_argument("--decision-status", dest="decision_status", default=None)
    search_parser.add_argument("--category", dest="category", default=None)
    # WK-0098 (DEC-0004 amendment): semantic rescue off by default at the caller (tools.ts); the
    # flag lets this CLI be driven directly without the channel.
    search_parser.add_argument("--no-semantic", dest="semantic", action="store_false", default=True)

    args = parser.parse_args(argv)

    if args.command == "build":
        run_build(Path(args.dir))
        return 0

    if args.command == "search":
        if len(args.terms) > MAX_TERMS:
            parser.error(f"too many --term flags (max {MAX_TERMS})")
        if any(len(t) > MAX_TERM_CHARS for t in args.terms):
            parser.error(f"term exceeds {MAX_TERM_CHARS} characters")
        if len(args.query) > MAX_QUERY_CHARS:
            parser.error(f"query exceeds {MAX_QUERY_CHARS} characters")
        if not 1 <= args.semantic_n <= 50:
            parser.error("--semantic-n must be between 1 and 50")
        response = run_search(
            Path(args.dir),
            args.query,
            terms=args.terms,
            semantic_n=args.semantic_n,
            decision_status=args.decision_status,
            category=args.category,
            semantic=args.semantic,
        )
        json.dump(response, sys.stdout)
        sys.stdout.write("\n")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
