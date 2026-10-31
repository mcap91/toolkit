"""Tests for `pricing.py` (WK-0100: no implicit default into another
checkout): the CLI-value > env-var > error precedence `resolve_prices_path`
implements, and `price_usage`'s "a missing table or an unknown model id
yields `(None, reason)`, never a substitute rate" contract (OR-1.4).

The "real row prices tokens with the kb formula" test does not invent a row
shape: it reads the real, vendored kb LiteLLM table at
`REAL_LITELLM_PRICES_PATH` (the kb checkout's pinned table, a read-only data
mount in this environment — not a pricing.py default) and copies one real
row (every field, verbatim) that happens to carry all four token-cost
fields `price_usage` reads, into a tiny table file under `tmp_path`. If that
real file is absent on this machine, the test is skipped rather than faking
a row — report this if it happens, don't invent field names.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from catalog_capture import pricing

REQUIRED_FIELDS = (
    "input_cost_per_token",
    "output_cost_per_token",
    "cache_creation_input_token_cost",
    "cache_read_input_token_cost",
)

# The real kb-vendored LiteLLM table (WK-0094 Phase B's documented default, before WK-0100
# removed it as a pricing.py fallback). Test-only: these tests still need a real row shape to
# avoid inventing field names; pricing.py itself never references this path.
REAL_LITELLM_PRICES_PATH = Path("/home/mcap91/projects/kb/packages/wiki-core/src/pricing/litellm-prices.json")


def _find_real_row() -> tuple[str, dict] | None:
    """Returns (model_id, row) for the first real table entry that carries
    all four fields `price_usage` reads, or None if the real table is
    missing/unreadable/has no such row."""
    try:
        table = json.loads(REAL_LITELLM_PRICES_PATH.read_text())
    except OSError:
        return None
    for model_id, row in table.items():
        if isinstance(row, dict) and all(f in row for f in REQUIRED_FIELDS):
            return model_id, row
    return None


# --------------------------------------------------------------------------
# resolve_prices_path: CLI value > env var > error (WK-0100: no implicit
# default into another checkout).
# --------------------------------------------------------------------------


def test_resolve_prices_path_cli_value_beats_env_var(monkeypatch):
    monkeypatch.setenv(pricing.ENV_VAR, "/env/table.json")
    assert pricing.resolve_prices_path("/cli/table.json") == Path("/cli/table.json")


def test_resolve_prices_path_env_var_beats_cli_absence(monkeypatch):
    monkeypatch.setenv(pricing.ENV_VAR, "/env/table.json")
    assert pricing.resolve_prices_path(None) == Path("/env/table.json")


def test_resolve_prices_path_raises_when_neither_cli_value_nor_env_var_set(monkeypatch):
    """No implicit default into another checkout (WK-0100): the error names both
    configuration routes (the env var and the CLI flag) so an operator knows how to fix it."""
    monkeypatch.delenv(pricing.ENV_VAR, raising=False)
    with pytest.raises(ValueError) as exc_info:
        pricing.resolve_prices_path(None)
    assert pricing.ENV_VAR in str(exc_info.value)
    assert "--prices-path" in str(exc_info.value)


def test_resolve_prices_path_empty_cli_value_does_not_win(monkeypatch):
    """`cli_value` is falsy-checked (`if cli_value:`), so an empty string
    (argparse's "flag not passed" default) falls through to the env var,
    same as None — not a change in behavior, pinned here so a future edit
    to the truthiness check is deliberate."""
    monkeypatch.setenv(pricing.ENV_VAR, "/env/table.json")
    assert pricing.resolve_prices_path("") == Path("/env/table.json")


# --------------------------------------------------------------------------
# price_usage: missing table / unknown model id -> (None, reason), never a
# substitute rate.
# --------------------------------------------------------------------------


def test_price_usage_missing_table_file_returns_none_and_reason(tmp_path: Path):
    missing_path = tmp_path / "does-not-exist.json"
    usd, reason = pricing.price_usage(
        {"model": "any-model", "input_tokens": 100, "output_tokens": 50},
        prices_path=missing_path,
    )
    assert usd is None
    assert reason is not None
    assert "any-model" in reason


def test_price_usage_model_with_no_row_returns_none_and_reason(tmp_path: Path):
    table_path = tmp_path / "prices.json"
    table_path.write_text(json.dumps({"some-other-model": {"input_cost_per_token": 1.0}}), encoding="utf-8")
    usd, reason = pricing.price_usage(
        {"model": "not-in-table", "input_tokens": 100, "output_tokens": 50},
        prices_path=table_path,
    )
    assert usd is None
    assert reason is not None
    assert "not-in-table" in reason


def test_price_usage_no_model_id_returns_none_and_reason(tmp_path: Path):
    usd, reason = pricing.price_usage({"input_tokens": 100}, prices_path=tmp_path / "unused.json")
    assert usd is None
    assert reason is not None


def test_price_usage_real_row_prices_tokens_with_kb_formula(tmp_path: Path):
    found = _find_real_row()
    if found is None:
        pytest.skip(
            f"real kb LiteLLM table not found/usable at {REAL_LITELLM_PRICES_PATH} "
            "(or it has no row with all of input/output/cache_creation/cache_read cost fields) "
            "— cannot build a non-invented row shape on this machine"
        )
    model_id, real_row = found

    table_path = tmp_path / "prices.json"
    table_path.write_text(json.dumps({model_id: real_row}), encoding="utf-8")

    usage = {
        "model": model_id,
        "input_tokens": 1000,
        "output_tokens": 200,
        "cache_creation_tokens": 50,
        "cache_read_tokens": 25,
    }
    usd, reason = pricing.price_usage(usage, prices_path=table_path)

    assert reason is None
    expected = (
        usage["input_tokens"] * real_row["input_cost_per_token"]
        + usage["output_tokens"] * real_row["output_cost_per_token"]
        + usage["cache_creation_tokens"] * real_row["cache_creation_input_token_cost"]
        + usage["cache_read_tokens"] * real_row["cache_read_input_token_cost"]
    )
    assert usd == expected


def test_price_usage_missing_token_counts_default_to_zero(tmp_path: Path):
    found = _find_real_row()
    if found is None:
        pytest.skip(
            f"real kb LiteLLM table not found/usable at {REAL_LITELLM_PRICES_PATH} "
            "— cannot build a non-invented row shape on this machine"
        )
    model_id, real_row = found

    table_path = tmp_path / "prices.json"
    table_path.write_text(json.dumps({model_id: real_row}), encoding="utf-8")

    usd, reason = pricing.price_usage({"model": model_id}, prices_path=table_path)

    assert reason is None
    assert usd == 0


# --------------------------------------------------------------------------
# WK-0087 pricing fix: cache-creation tokens split by TTL (1-hour vs the
# generic/5-minute rate), each priced at its own rate. "claude-sonnet-5" is
# the exact model id the real captures report (`modelUsage` key) and is the
# one real row inspected for `pricing.CACHE_CREATION_1H_FIELD` — not an
# invented field name (WK-0087 build step 8).
# --------------------------------------------------------------------------


def _find_claude_sonnet_5_row() -> dict | None:
    try:
        table = json.loads(REAL_LITELLM_PRICES_PATH.read_text())
    except OSError:
        return None
    return table.get("claude-sonnet-5")


def test_price_usage_prices_1h_and_5m_cache_creation_at_their_own_rate(tmp_path: Path):
    real_row = _find_claude_sonnet_5_row()
    if real_row is None or pricing.CACHE_CREATION_1H_FIELD not in real_row:
        pytest.skip(
            f"real kb LiteLLM table not found/usable at {REAL_LITELLM_PRICES_PATH}, or its "
            f'"claude-sonnet-5" row has no "{pricing.CACHE_CREATION_1H_FIELD}" field — cannot build a '
            "non-invented row shape on this machine"
        )
    table_path = tmp_path / "prices.json"
    table_path.write_text(json.dumps({"claude-sonnet-5": real_row}), encoding="utf-8")

    usage = {
        "model": "claude-sonnet-5",
        "input_tokens": 2,
        "output_tokens": 100,
        "cache_read_tokens": 10,
        "cache_creation_1h_tokens": 1000,
        "cache_creation_5m_tokens": 500,
    }
    usd, reason = pricing.price_usage(usage, prices_path=table_path)

    assert reason is None
    expected = (
        usage["input_tokens"] * real_row["input_cost_per_token"]
        + usage["output_tokens"] * real_row["output_cost_per_token"]
        + usage["cache_read_tokens"] * real_row["cache_read_input_token_cost"]
        + usage["cache_creation_1h_tokens"] * real_row[pricing.CACHE_CREATION_1H_FIELD]
        + usage["cache_creation_5m_tokens"] * real_row["cache_creation_input_token_cost"]
    )
    assert usd == pytest.approx(expected)
    # Sanity: the 1-hour rate really is higher than the generic/5-minute one
    # — otherwise this test could pass by coincidence even with the two
    # buckets swapped.
    assert real_row[pricing.CACHE_CREATION_1H_FIELD] > real_row["cache_creation_input_token_cost"]


def test_price_usage_reports_reason_when_1h_tokens_present_but_table_row_lacks_the_field(tmp_path: Path):
    table_path = tmp_path / "prices.json"
    table_path.write_text(
        json.dumps({"some-model": {"input_cost_per_token": 1.0, "cache_creation_input_token_cost": 1.0}}),
        encoding="utf-8",
    )
    usd, reason = pricing.price_usage(
        {"model": "some-model", "cache_creation_1h_tokens": 100, "cache_creation_5m_tokens": 0},
        prices_path=table_path,
    )
    assert usd is None
    assert reason is not None
    assert pricing.CACHE_CREATION_1H_FIELD in reason


def test_price_usage_zero_1h_tokens_does_not_require_the_1h_field(tmp_path: Path):
    """A model whose row genuinely has no 1-hour cache tier still prices
    fine as long as the usage's 1-hour bucket is actually zero — only a
    *non-zero* 1-hour bucket with no row field is reported as unpriceable."""
    table_path = tmp_path / "prices.json"
    table_path.write_text(
        json.dumps({"some-model": {"input_cost_per_token": 1.0, "cache_creation_input_token_cost": 2.0}}),
        encoding="utf-8",
    )
    usd, reason = pricing.price_usage(
        {"model": "some-model", "input_tokens": 10, "cache_creation_1h_tokens": 0, "cache_creation_5m_tokens": 5},
        prices_path=table_path,
    )
    assert reason is None
    assert usd == 10 * 1.0 + 5 * 2.0


# --------------------------------------------------------------------------
# Golden test (WK-0087 build step 8): price_usage on both real carousel
# captures equals the CLI's own modelUsage.*.costUSD within $0.0001 — proof
# the 1h/5m split fix reproduces real billing, not just a plausible formula.
# --------------------------------------------------------------------------

CAROUSEL_FIXTURES_DIR = Path(__file__).parent / "fixtures" / "instagram" / "carousel"

# (shortcode, raw_stdout filename, real CLI modelUsage.*.costUSD from the
# WK-0087 "Steps 1-2 result" table / the raw captures themselves)
GOLDEN_CAROUSEL_CASES = [
    ("De9SalRGOhy", 0.4215258),
    ("DeCKnW0DAGc", 0.1524238),
]


@pytest.mark.parametrize("shortcode,expected_cost_usd", GOLDEN_CAROUSEL_CASES)
def test_price_usage_matches_real_cli_costusd_for_the_carousel_goldens(shortcode: str, expected_cost_usd: float):
    from catalog_capture.stages.read import parse_claude_stream_result

    if not REAL_LITELLM_PRICES_PATH.exists():
        pytest.skip(f"real kb LiteLLM table not found at {REAL_LITELLM_PRICES_PATH}")

    raw_stdout = (CAROUSEL_FIXTURES_DIR / shortcode / "read" / "raw_stdout.jsonl").read_text(encoding="utf-8")
    parsed = parse_claude_stream_result(raw_stdout)
    usage = {
        "model": parsed["model"],
        "input_tokens": parsed["input_tokens"],
        "output_tokens": parsed["output_tokens"],
        "cache_read_tokens": parsed["cache_read_tokens"],
        "cache_creation_1h_tokens": parsed["cache_creation_1h_tokens"],
        "cache_creation_5m_tokens": parsed["cache_creation_5m_tokens"],
    }
    usd, reason = pricing.price_usage(usage, prices_path=REAL_LITELLM_PRICES_PATH)

    assert reason is None
    assert usd == pytest.approx(expected_cost_usd, abs=0.0001)
