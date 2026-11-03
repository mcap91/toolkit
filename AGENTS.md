# Agent Operating Guide

<!-- BEGIN kb-managed -->
Managed by kb — edits inside this block are overwritten by `kb bootstrap` / `kb sync-contract`; edit outside the markers.

## kb — wiki

This repository uses the kb toolkit. The installed kb MCP servers are registered in this repo's `.mcp.json`
and run from the kb checkout; every kb tool call targets this repository via `dir`.

### Retrieval — do this before substantive work

Repository-context retrieval is a wiki/docs retrieval problem first, not a filesystem-search problem first.

1. Search the wiki with the kb wiki MCP `search` tool. This is the first retrieval step.
2. If you need a structured overview, regenerate views with the MCP `generate` tool and read them
   (`catalog`, `now`, `inbox`, `backlog`, `archive`).
3. Then read the relevant durable `docs/` pages.
4. Then check related `wiki/decisions/`, `wiki/issues/`, `wiki/initiatives/`, `wiki/areas/`, `wiki/sources/`.
5. Only then inspect implementation files.

If the kb wiki MCP server is not available this session, run the same steps via the kb CLI from the kb
checkout (`npm run wiki -- search --dir <this repo>`, `npm run wiki -- generate --dir <this repo>`). Do
not use raw `rg`, file globbing, or direct file reads as the first retrieval step. Do not parallelize
implementation search with the initial retrieval pass.

### Wiki rules

- Prefer the `kb-wiki` MCP tools (`search`, `generate`, `lint`, `create`, `allocate-id`,
  `build-search-index`, `sync-contract`, `bootstrap`); CLI fallback `npm run wiki -- … --dir <this repo>`.
- `allocate-id` is an idempotent **peek/reserve**, not a counter: repeat calls return the same id until
  `create` writes the record that claims it. Call `create` to claim an id; repeated identical ids are
  correct, not a bug.
- Always pass `dir` pointing at this repository; run kb from its own checkout, not this repo root.
- If wiki records and code/tests disagree, report the mismatch rather than trusting a grep-first conclusion.
- Graph: `npm run graph -- --dir <this repo>` extracts the deterministic import graph with the wiki-record overlay.

## kb — dispatch

- Dispatch is the multi-agent handoff protocol: author HOs (`create-handoff`), dispatch workers in the bwrap
  jail, capture results, review, merge. The dispatch MCP server instructions carry the full orchestration
  recipe. Prefer `kb-dispatch` MCP tools; CLI fallback `npm run dispatch -- …`.
- For pipeline work, delegate via kb-dispatch; do not spawn coding-agent subagents or workflows unless the
  operator explicitly approves.
- `HO-*` handoffs are dispatch-owned (`wiki/handoffs/`, excluded from wiki scans); never create them via
  `wiki create`.
- Merges go through `merge-delivery` only — never by hand. After a merge, run this repo's validation command
  on the host and record the result in the WK.

## Engineering guidelines

Every build here is judged by: organization, cleanliness, configurability, reproducibility, extensibility,
deployability, interpretability, easy to debug, simple and not overengineered. The codebase and directory tree do
not balloon. No quick fixes — root cause, connected to the bigger picture, with blast radius considered. Clean,
intuitive docs for end users. A limit that matters lives outside the model, where the model cannot argue with it.
The question behind all of it: how can I improve this so that a future agent does not make the same mistake?

### Before you build

1. **Spec before build.** Write the spec before you build. Accept-all vibe coding is for throwaway work, never production.
2. **Success criteria, not step-by-step.** Define what done looks like, loop until it is verified, and checkpoint after each stage.
3. **Specify behavior, not mechanism.** The spec says what must be true; the how stays open unless the operator asked for one.
4. **Think before coding.** State assumptions, flag inconsistencies, present tradeoffs, and push back when a simpler approach exists. When patterns conflict, pick one, explain the choice, and flag the other for cleanup. Never proceed uncertainly — and never ask what the repo's rules, records, and code can answer; exhaust those first.
5. **The context window is scarce working memory.** Start a new session per topic; load only what the next step needs.
6. **Draw the runtime spine before slicing** (validate → acquire → transform → deliver → record); no spine, no slices. Skeleton first: the first increment runs the whole spine thin, takes the riskiest integration, and ends with something an owner can watch work. Each later increment widens one dimension and still runs end to end.
7. **Break false dependencies with named interims** — a hardcoded entry, an env passthrough, a hand-authored input. Each interim names the increment that retires it.
8. **Freeze late.** Schemas, contracts, and registries lock only after real runs have exercised them — never in increment one.
9. **Delete late.** A working system stays live with green tests until a cutover increment proves its replacement.
10. **Gates are live proofs an owner ratifies.** "Code complete" and component demos are not gates.
11. **Conserve scope.** Nothing enters or leaves scope silently; late-discovered work gets its own named task.
12. **Phases are a deliberate, written choice** — an external wait, no shared runtime spine, or slicing as ceremony — never the default.

### Code shape & reuse

13. **Climb the reuse ladder before writing anything new:** does it need to exist → this codebase → stdlib or platform → an installed dependency (never add one for a few lines) → an at-a-glance one-liner → only then minimum new code, with a stated reason. Logic lives in the library; scripts are thin entry points; atomic functions compose under a composite router; domain constants stay out of general modules.
14. **Settings are parameters, never names.** No task, experiment, model, or dataset names in code, file names, or registered names; no hardcoded shapes or counts the config already knows.
15. **Write the minimum code that solves the problem.** No speculative features or abstractions for single-use code; prefer dependency-light, hackable code over config objects and factories.
16. **Make surgical changes.** Touch only what the request requires; never change code or comments you do not understand, even orthogonal-looking ones.
17. **Read before you write:** the file's exports, its immediate caller, and the shared utilities.
18. **Cite, don't recall.** Every claim names the file and function read in this session.
19. **Reuse aggressively; generalize reluctantly.** Build new code at today's size — going generic needs a named second consumer (one adapter is a hypothetical seam, two is real).
20. **Name things for what they do now.** A name that encodes today's specifics drifts; rename when the job changes.
21. **Directory structure is discipline.** Read one sibling of the same kind before writing into a directory; use the existing structure; propose one when none exists; altering one is a reformat proposal, never ad hoc. Never mint an over-specific directory for one artifact.
22. **Fix the root cause only.** Diagnose first, grep every caller, fix once in shared code — no quick fixes, patches, or workarounds.
23. **Keep a "where code goes" map in the repo, outside the managed block:** one row per concern — its home, and the anti-pattern. Consult it before placing new code; update it in the same change that adds a new home.
24. **Never cut the floor.** Never cut validation at trust boundaries, error handling that prevents data loss, security, accessibility, or anything the user asked for. Never swallow an error — no bare catch or except-pass; an error stops the run or is handled and logged with its cause.

### Tests & evidence

25. **Never weaken a test to get green.** A test changes only on a diagnosed staleness, with evidence and a named replacement check.
26. **Agree test seams — public boundaries — before writing tests.** Tests verify intent: they encode why and fail when business logic changes. No implementation-coupled tests, no tautological tests, no horizontal slicing.
27. **Apply the deletion test.** Delete the module; if its complexity reappears across callers, it earned its keep.
28. **Prove a check bites.** Run it clean, plant a violation, confirm it fails, revert, confirm it passes.
29. **Debug with a repro loop, not theories.** Build the reproduction first; rank three to five falsifiable hypotheses before testing any.
30. **Evidence is observed, never claimed.** Counts, test status, and run facts come from commands and logs; your own claim is not evidence. Say plainly when you cannot be sure.
31. **A deterministic validator decides pass or fail** — at every task and every pipeline transition — never the model.
32. **Schema-valid is not semantically correct.** Passing validation says nothing about matching the request.
33. **Capture before code.** An external shape — an API response, CLI output, a file format — is an assumption until a real captured output proves it. Golden fixtures are real, unedited captures; never patch code to accept two shapes.
34. **Reviews check the rules as well as the spec.** Flag parallel copies, one-off scripts, hardcoded settings; judge in order — correct, safe, holds under load, tested, fast, lean; no finding without a concrete failing case.
35. **Keep diffs small and incremental.** The verification loop is the bottleneck; its speed bounds safe autonomy.
36. **Build evaluation loops.** A non-deterministic part ships with an eval path; a deterministic part ships with tests.

### Pipelines & runs

37. **Code orchestrates; the model works inside.** Deterministic code owns sequence, state, retries, routing, and delivery; call the model only where reasoning helps.
38. **A bounded model task returns a structured artifact** — a discovery record, never prose and never pipeline config. Code renders config from it; the model cannot hallucinate a threshold it never writes.
39. **Classify retries.** Code decides what the model may fix, feeds back the validator's error, and caps attempts; real failures stop the run.
40. **Make pipeline work idempotent, resumable, and provenanced.** Checkpoint completed units; regenerate artifacts to the same path, overwriting stale copies; content-hash inputs to skip finished work and prove identity; record input hash, code and config versions, and the run — or the artifact is scratch.
41. **Long-running work logs live.** Append, flush, timestamp; `tail -f` must show progress — an empty log during a run is a bug. A run that outlives the session is detached and reattachable; stop or hand off every background process before reporting done.
42. **Clean up what you open.** Close every handle, socket, and connection; bound and track concurrency; verify teardown before yielding.
43. **Write state atomically.** A state or checkpoint file writes to a temp path and renames into place; concurrent writers take a lock. A half-written state file is corruption, not progress.
44. **Record metrics per run for non-deterministic work** — wall time, tokens, tool calls, turns, cost, outcome — from logs, never self-reported. Code that calls LLMs uses OpenTelemetry GenAI conventions.
45. **Generated surfaces are never truth.** When a view disagrees with canon, canon wins and the view regenerates. Reports lead with the result, render deterministically from a structured spec, and stay rebuildable outputs.
46. **Keep model and provider behind one router interface, as config.** The test is the swap: change the model and everything else still works.
47. **Design the system around the agent.** Bounded tools, contracts at ambiguous decisions, validators at transitions, protected raw data, human approval at consequential boundaries — never agents sprinkled over scripts.

### Data & environments

48. **Data lives outside the codebase, with provenance.** Knowledge, run state, and artifacts are separate layers with different owners; none substitutes for another.
49. **End every session self-contained.** Objective, state, decisions, artifacts, evidence, and remaining work go to durable records — if the next session needs the transcript, the loop is incomplete.
50. **Keep an environment registry in AGENTS.md, outside the managed block:** each environment's name, manager, purpose, and freeze command — updated in the same change.
51. **Test against disposable databases.** Provision one for the task — never the connection string in the environment. Validate a migration by replaying full history plus the new one on a throwaway database, with the suite.
52. **Migrations are append-only.** Never edit an applied migration; destructive operations need explicit confirmation every time.
53. **In-scope is not safe.** A write scope or tool permission enforces boundaries, not prudence; "the tool let me" is never permission for a destructive step. Manage permissions, isolate work, and keep a human on diffs and specs.

### Dependencies & supply chain

54. **Verify before you install.** A package must exist on the registry — never trust a recalled name. Change lockfiles incrementally, never regenerate; audit after every dependency change; new versions get a cooldown window and a provenance check.
55. **Secrets never enter argv or logs.** Command lines and log streams are exfiltration surfaces, separate from source hardcoding.
56. **Never bypass a hook or gate.** On rejection, fix the named rule and retry. Stock linters are the first backstop — never hand-write a check a stock rule covers.

### Shipping & contracts

57. **Correctness wins over backward compatibility.** Internally, no silent shims, aliases, dual read/write, or fallback parsing — remove obsolete compatibility, or carry a decision naming the surface and removal condition. Once real consumers exist, a public or agent-facing contract changes only by explicit, time-boxed deprecation — replacement first, a deprecation mark with a removal date, one more cycle — and additive-looking changes count as breaking for typed or agent consumers.
58. **Decide shipping at planning time.** Name where the build ships and how — package, container, submodule — and when that choice is made; containers and submodules need a stated reason.
59. **Add a language boundary only for a clear capability,** behind a versioned, tested contract — never by drift.
60. **A UI needs a reason before it needs conventions.**
61. **Remove feature flags in fixed order:** pull the code check and deploy first; retire the flag in the flag system after.
62. **Declare the repo's AI-contribution policy** — refuse, disclose, verify, or hand off — separate from the license. Disclose contribution; never merge code no human understands.
63. **Every change names the parts of the repo it touches;** a core-surface change states why.
64. **Keep end-user docs current.** A shipped capability keeps clean, intuitive docs for its users; a behavior change updates the docs in the same change.
65. **Keep one source of truth per fact.** A second copy is derived and regenerated, never hand-maintained; where a copy must exist, fingerprint it against its source so drift is detected, not remembered. A hand-maintained duplicate is ad hoc only.
66. **Mark every shortcut.** Label it `shortcut: <the limit>, <when to upgrade>`; a shortcut with no upgrade trigger is rot.
67. **Every deferral carries a written re-open trigger,** checked at every gate.

Roles (`/planner`, `/orchestrator`, `/overseer`) install user-global via `install-roles` from the kb
checkout. This block is managed by kb and overwritten on sync; this repo's own rules, environment registry,
and where-code-goes map live below the end marker, where kb never writes.
<!-- END kb-managed -->

## What this repo is

Three layers, from DEC-0005.

**Catalog.** Public data: `catalog/entries/`, one template per entry, hand-curated by the operator. This
is the product — a personal library of tools, techniques, and references, each entry written deep enough
that an agent never has to re-fetch the source to answer a question about it.

**Reader.** Public code: an MCP server (a small background program that exposes callable tools to an
agent over the Model Context Protocol) running `search` and `index`, a lint CLI for contributors, and
`index.md` as a table of contents an agent can read straight off the raw GitHub URL.

**Workbench.** A private sibling repo, `../toolkit-workbench`: the pipeline that writes the catalog,
every project that uses the catalog to build or test something, raw runs, and third-party captures. It
has no wiki of its own — every record for both repos lives in this repo's `wiki/`.

No code in this repo writes a catalog entry. Intake — pulling links, curating the inbox, draining to the
queue, running the headless processing loop — runs from the workbench now.

## Working here

Work-tracking records (`WK`, `IN`, `DEC`, and the rest) live in `wiki/`, a private, gitignored repo nested
in this checkout. Start from `wiki/dashboard/chain.md`, the cross-initiative status surface the overseer
maintains.

Two settings carry the only paths that cross the repo boundary: `CATALOG_DIR` (default
`../toolkit/catalog`) and `WORKBENCH_DIR` (default `../toolkit-workbench`). No repo name, operator name,
or machine path goes into code or settings beyond these two.

Media and third-party captures never enter this repo. The `.gitignore` backstops that rule.

## Catalog entries

Every entry follows the same section order: What it is, How it works, How to use it, Evaluation and
limits, Context from the source, Related, Security.

Entries are factual. No verdicts, no adoption recommendations, no notes on whether the operator should
use the thing — those decisions happen outside the entry.

Three frontmatter fields carry provenance: `url` (the subject itself — a repo, a tool's site),
`source_url` (the link the item came in on, when different from `url`), and `source` (what that link
derives to: `instagram`, `reddit`, `x`, `web`, or `text`).

`catalog/recipe.md` is today's working description of the template. `catalog/template.md` (WK-0099) will
replace it as the formal contract.

## Reader MCP

The catalog MCP server lives in `packages/catalog-mcp`. Run it directly with:

```
npx tsx packages/catalog-mcp/src/server.ts
```

As of WK-0100 it registers 12 tools: `index`, `lint`, `search`, `config`, `queue`, `drain`, `ingest`,
`fetch-url`, `build-prompt`, `validate-entry`, `write-entry`, `annotate-entry`. The write tools move to
the workbench pipeline package under WK-0101, after which the public server exposes `search` and `index`
only.

## Workbench projects

- **ocr-bench** (IN-0002) — benchmark OCR and parser tools against a Sonnet agent on scientific PDFs; owes a
  results page.
- **semantic bench** (IN-0012) — embedding and reranking models for catalog search, measured on the sealed
  operator-brief eval; owes a benchmark page and, if it passes, a pinned model in the reader.
- **pipeline** (IN-0011) — intake (Gmail to inbox to queue), capture, one fresh session per queue item,
  `upsert-entry`, lint, index, and the commit back into this repo.
- **kb lab** (IN-0013) — wiki operations at scale and agent-rule experiments; results publish in the kb repo.

Graduation rule: a workbench project owes one public artifact under `docs/benchmarks/` — a results page,
a package, a recipe or template change, or a pinned-model change. The artifact moves into this repo; raw
runs and captures stay in the workbench.
