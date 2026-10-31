"""USD pricing for a read call (OR-1.4), against kb's vendored, pinned
LiteLLM table (WK-0094 Phase B: the table path is now configurable — CLI
option and/or env var — with the current kb checkout path kept only as the
*documented default*, never a hardcoded sole path or a substitute rate)."""

from __future__ import annotations

import json
import os
from pathlib import Path

# Documented default (kb `pricing.ts:32`'s pin) — overridable via `--prices-path`
# (cli.py) or the env var below. A missing table at whichever path is resolved
# still yields `(None, reason)` from `price_usage`, never a substitute rate.
DEFAULT_LITELLM_PRICES_PATH = Path("/home/mcap91/projects/kb/packages/wiki-core/src/pricing/litellm-prices.json")
LITELLM_TABLE_PIN = "BerriAI/litellm@94a29e07085dd9d8f2269ee93e899ef0e374cdc7"  # pricing.ts:32
ENV_VAR = "CATALOG_CAPTURE_LITELLM_PRICES_PATH"


def resolve_prices_path(cli_value: str | os.PathLike | None = None) -> Path:
    """CLI option > env var > the documented kb-checkout default."""
    if cli_value:
        return Path(cli_value)
    env = os.environ.get(ENV_VAR)
    if env:
        return Path(env)
    return DEFAULT_LITELLM_PRICES_PATH


def load_pricing_table(path: Path) -> dict:
    try:
        return json.loads(Path(path).read_text())
    except (OSError, json.JSONDecodeError):
        return {}


#: The LiteLLM row field for the 1-hour cache-creation rate (WK-0087 pricing
#: fix). Found by inspecting the real, vendored table's "claude-sonnet-5" row
#: — not invented: it sits alongside the generic (5-minute)
#: `cache_creation_input_token_cost` field. Reproduces the real De9SalRGOhy
#: capture's CLI `costUSD` (0.4215258) exactly when the 1h/5m split is priced
#: at its own rate (WK-0087 golden pricing test).
CACHE_CREATION_1H_FIELD = "cache_creation_input_token_cost_above_1hr"


def price_usage(usage: dict, *, prices_path: Path | None = None) -> tuple[float | None, str | None]:
    """kb `pricing.ts` formula against the resolved LiteLLM table (OR-1.4):
    exact model-id key match only, else `(None, reason)` — never a substitute
    rate. `total_cost_usd` is never used.

    WK-0087 pricing fix: cache-creation tokens are not billed at one flat
    rate. The CLI reports them split by TTL (`usage.cache_creation`'s
    `ephemeral_1h_input_tokens` / `ephemeral_5m_input_tokens`) and bills the
    1-hour bucket higher than the generic/5-minute one. When `usage` carries
    that split (`cache_creation_1h_tokens` / `cache_creation_5m_tokens`,
    `stages.read.run_claude_read`'s shape), each bucket is priced at its own
    rate; a non-zero 1-hour bucket with no `CACHE_CREATION_1H_FIELD` row is
    reported as `(None, reason)`, never guessed at 0. Absent the split
    (callers that only ever pass the old merged `cache_creation_tokens`,
    e.g. existing tests), the generic rate applies to the whole amount,
    unchanged from before this fix."""
    model = usage.get("model")
    if not model:
        return None, "no model id resolved from modelUsage"
    path = prices_path if prices_path is not None else resolve_prices_path()
    table = load_pricing_table(path)
    entry = table.get(model)
    if entry is None:
        return None, f'no LiteLLM price row for model "{model}" ({LITELLM_TABLE_PIN}, table path {path})'

    cache_creation_1h = usage.get("cache_creation_1h_tokens")
    cache_creation_5m = usage.get("cache_creation_5m_tokens")
    if cache_creation_1h is not None or cache_creation_5m is not None:
        if cache_creation_1h and CACHE_CREATION_1H_FIELD not in entry:
            return None, (
                f'usage reports {cache_creation_1h} ephemeral 1-hour cache-creation token(s) but the '
                f'LiteLLM row for "{model}" has no "{CACHE_CREATION_1H_FIELD}" field '
                f"({LITELLM_TABLE_PIN}, table path {path})"
            )
        cache_creation_cost = (
            (cache_creation_1h or 0) * entry.get(CACHE_CREATION_1H_FIELD, 0)
            + (cache_creation_5m or 0) * entry.get("cache_creation_input_token_cost", 0)
        )
    else:
        cache_creation_cost = (usage.get("cache_creation_tokens") or 0) * entry.get("cache_creation_input_token_cost", 0)

    usd = (
        (usage.get("input_tokens") or 0) * entry.get("input_cost_per_token", 0)
        + (usage.get("output_tokens") or 0) * entry.get("output_cost_per_token", 0)
        + cache_creation_cost
        + (usage.get("cache_read_tokens") or 0) * entry.get("cache_read_input_token_cost", 0)
    )
    return usd, None
