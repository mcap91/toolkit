---
name: unusual-whales-mcp
title: Unusual Whales MCP
url: "https://github.com/unusual-whales/unusual-whales-official-mcp"
category: mcp-server
summary: "Official Unusual Whales MCP server — 100+ market data endpoints covering options flow, dark pool, congressional trading, Greek exposure, volatility, earnings, ETFs, shorts, fundamentals, and technicals; 30+ analysis prompts; remote or local mode; MIT"
tags: [mcp-server, finance, options, market-data, dark-pool, congressional-trading]
reviewed: 2026-06-23
acquired: 2026-06-23
license: MIT
security_flags: [api-key-required, cloud-hosted]
overlaps: []
source: unknown
---

## What it does

The official MCP server for Unusual Whales market data. Exposes 100+ tools across 15 data categories that MCP clients call automatically based on natural language queries.

**Data categories:**
- **Stock**: Options chains, Greeks, IV rank, OHLC candles, max pain, OI, volatility
- **Options**: Contract flow, historic prices, intraday data, volume profiles
- **Flow**: Options flow alerts, full tape, net flow by expiry, sector flow
- **Dark Pool**: Transactions with NBBO context, price level filtering
- **Congress**: Congressional trades, late filings, individual member activity
- **Politicians** (Premium): Portfolios, recent trades, holdings by ticker
- **Insider**: Insider transactions, sector/ticker flow
- **Institutions**: 13F filings, holdings, sector exposure, ownership changes
- **Market**: Market tide, sector tide, economic calendar, FDA calendar, correlations
- **Earnings**: Pre/aftermarket schedules, historical earnings
- **ETF**: Holdings, exposure, inflows/outflows, sector weights
- **Shorts**: Short interest, FTDs, short volume ratio, borrow rates
- **Seasonality**: Monthly performers, yearly patterns
- **Screener**: Stock screener, options screener, analyst ratings
- **News**: Market news headlines
- **Fundamentals/Technicals**: Income statements, balance sheets, cash flows, earnings history, 14 technical indicators (SMA, EMA, RSI, MACD, BBANDS, etc.)

**30+ analysis prompts** built in: daily-summary, morning-briefing, ticker-analysis, unusual-flow, dark-pool-scanner, congress-tracker, bullish/bearish-confluence, and more. Prompts can be chained.

**Connection modes:**
- **Remote** (recommended): Connect to `https://api.unusualwhales.com/api/mcp` — no install needed
- **Local**: `npx -y @unusualwhales/mcp` with `UW_API_KEY` env var

## Assessment

Well-built MCP server with unusually broad data coverage — 15 categories and 100+ endpoints is exceptional for a single MCP server. The built-in analysis prompts (30+) are a thoughtful touch that reduces prompt engineering for common queries. Congressional trading and dark pool data are genuinely unique data sources not available through standard market APIs.

Not directly relevant to bioinformatics workflows, but valuable for anyone doing financial analysis or building trading-adjacent AI tools. The remote mode (no install, just add the URL) makes it trivially easy to try.

Requires a paid Unusual Whales API key. Rate limiting (default 120 req/min) and circuit breaker (5 failures) are built in.

## Mechanical details

```bash
# Claude Code (remote — recommended)
claude mcp add --transport http unusualwhales \
  https://api.unusualwhales.com/api/mcp \
  --header "Authorization: Bearer YOUR_KEY"

# Claude Code (local)
claude mcp add unusualwhales -e UW_API_KEY=YOUR_KEY -- npx -y @unusualwhales/mcp
```

Also supports Cursor, VS Code, Windsurf, and Claude Desktop via JSON config.

## Security

- **License**: MIT — fully permissive
- **API key**: Required, passed via Authorization header (remote) or env var (local)
- **Data flow**: Remote mode sends queries to Unusual Whales API; local mode runs Node.js process locally but still calls the API
- **Rate limiting**: Configurable (default 120/min) with circuit breaker
- **Supply chain**: Official first-party server from Unusual Whales; builds on community work by Erik Maday