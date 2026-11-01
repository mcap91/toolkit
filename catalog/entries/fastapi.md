---
name: fastapi
title: FastAPI
url: "https://github.com/fastapi/fastapi"
category: framework
summary: "High-performance async Python web framework built on Starlette + Pydantic — declares request/response contracts via standard Python type hints, generating validation, serialization, and OpenAPI/JSON Schema docs (Swagger UI, ReDoc) automatically; dependency-injection system, WebSockets, background tasks; MIT, ~102k stars, created 2018 by Sebastián Ramírez, actively maintained"
tags: [web-framework, python, async, rest-api, openapi, pydantic, starlette, type-hints, dependency-injection]
reviewed: 2026-09-10
acquired: 2026-09-10
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

FastAPI is a Python web framework for building HTTP APIs where the request/response contract is declared with standard Python type hints. Pydantic models drive validation, serialization, and automatic interactive documentation (OpenAPI/JSON Schema, served via Swagger UI and ReDoc); Starlette provides the async ASGI core (routing, WebSockets, middleware, background tasks). Endpoints are plain (async) functions with typed parameters; a hierarchical dependency-injection system handles auth, DB sessions, and shared resources.

## Differentiators

- Types-as-contract: one type annotation yields editor autocomplete, runtime validation, serialization, and docs simultaneously — the framework's core idea.
- Performance in the top tier of Python frameworks (on par with Node/Go-class ASGI throughput per TechEmpower, via Starlette/uvicorn).
- Ubiquity in the ML/agent-serving ecosystem: the default HTTP layer for model servers, MCP-adjacent services, and inference APIs (vLLM, many agent backends expose FastAPI apps).
- Ecosystem: `fastapi-cli` (`fastapi dev`), SQLModel (same author) for ORM integration, first-party full-stack template.

## Mechanical details

- Install/run: `pip install "fastapi[standard]"`; `fastapi dev main.py` for a dev server (uvicorn underneath); interactive docs at `/docs` and `/redoc`.
- Minimal app: `app = FastAPI()` + `@app.get("/items/{item_id}") def read(item_id: int, q: str | None = None): ...` — path/query/body parameters inferred from the signature.
- Python, MIT, ~102.2k stars, ~9.9k forks, only 81 open issues (triage is aggressive); created 2018-12 by Sebastián Ramírez (tiangolo); pushed Sep 2026, active org with 769 watchers; docs at fastapi.tiangolo.com.

## Security

- **License:** MIT.
- Mature, heavily audited project with a large contributor base, full test coverage policy, and an established security policy; no open flags.
- Security posture of an app depends on deployment choices (auth dependencies, CORS, TLS termination) — the framework provides OAuth2/JWT utilities but does not impose them.