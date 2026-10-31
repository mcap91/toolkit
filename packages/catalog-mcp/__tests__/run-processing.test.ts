// packages/catalog-mcp/__tests__/run-processing.test.ts
// WK-0092: one fresh `claude --print` session per queue item, looped by code. `cross-spawn` is
// mocked throughout — these tests never launch a real `claude` process. The usage-parsing tests
// run against real, unedited captures (fixtures/wk-0092/*.json) per AGENTS evidence discipline
// (22-24): the shape is never hand-invented.
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { EventEmitter } from 'node:events';
import { mkdtemp, rm, mkdir, writeFile, readFile } from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';

vi.mock('cross-spawn', () => ({ default: vi.fn() }));
vi.mock('../src/core/rebuild-indexes.js', () => ({ rebuildCatalogIndexes: vi.fn().mockResolvedValue({}) }));

import spawn from 'cross-spawn';
import { rebuildCatalogIndexes } from '../src/core/rebuild-indexes.js';
import { removeFromQueue } from '../src/core/queue.js';
import {
  buildItemPrompt,
  buildClaudeArgs,
  parseSessionUsage,
  countToolCalls,
  processItem,
  runProcessing,
  parseStringFlag,
  parseItemTimeoutMs,
  resolveRootPath,
  assertCatalogRootExists,
  CATALOG_MCP_TOOLS,
  BUILTIN_TOOLS,
} from '../src/adapter/run-processing.js';
import type { QueueItem } from '../src/core/schema.js';
import { tools } from '../src/tools.js';

const mockSpawn = vi.mocked(spawn);
const mockRebuildCatalogIndexes = vi.mocked(rebuildCatalogIndexes);

const FIXTURES_DIR = path.join(path.dirname(fileURLToPath(import.meta.url)), 'fixtures', 'wk-0092');

async function readFixture(name: string): Promise<string> {
  return readFile(path.join(FIXTURES_DIR, name), 'utf-8');
}

// ---------------------------------------------------------------------------
// Fake `claude` child process. Keyed by the `key:` line in the prompt the
// production code writes to stdin (buildItemPrompt always emits that line),
// so each test can script per-item behavior without depending on call order.
// ---------------------------------------------------------------------------
interface ChildBehavior {
  removeFromQueue?: boolean; // simulate the session having removed this item (queue {action:remove})
  stdout?: string; // what the --output-format json session "printed"
  exitCode?: number | null;
  hang?: boolean; // never exits on its own — only resolves if the production code calls kill()
  delayMs?: number; // how long the session "runs" before exiting
}

function queueFilePath(dir: string): string {
  return path.join(dir, 'catalog', 'queue.json');
}

// Live sessions right now / the most seen at once — lets tests check the concurrency bound.
const inFlight = { now: 0, max: 0 };

function installFakeSpawn(dir: string, behaviors: Record<string, ChildBehavior>) {
  inFlight.now = 0;
  inFlight.max = 0;
  mockSpawn.mockImplementation(((_cmd: string, _args: string[], _opts: unknown) => {
    inFlight.now++;
    inFlight.max = Math.max(inFlight.max, inFlight.now);
    const child = new EventEmitter() as unknown as {
      stdout: EventEmitter;
      stderr: EventEmitter;
      stdin: { write: (d: string) => void; end: () => void };
      kill: (signal?: string) => void;
    } & EventEmitter;
    child.stdout = new EventEmitter();
    child.stderr = new EventEmitter();

    let promptBuf = '';
    child.stdin = {
      write: vi.fn((d: string) => { promptBuf += d; }),
      end: vi.fn(() => {
        const m = promptBuf.match(/^key: (.+)$/m);
        const key = m ? m[1] : '';
        const behavior = behaviors[key] ?? {};
        if (behavior.hang) return; // only resolves via kill() below
        setTimeout(async () => {
          // The real session removes its item through the catalog MCP server's locked queue code.
          if (behavior.removeFromQueue) await removeFromQueue(dir, [key]);
          inFlight.now--;
          if (behavior.stdout) child.stdout.emit('data', Buffer.from(behavior.stdout));
          child.emit('exit', behavior.exitCode ?? 0);
        }, behavior.delayMs ?? 0);
      }),
    } as unknown as typeof child.stdin;

    child.kill = vi.fn((_signal?: string) => {
      inFlight.now--;
      child.emit('exit', null); // SIGTERM makes the real process exit; the mock does too
    });

    return child;
  }) as unknown as typeof spawn);
}

async function writeQueueFile(dir: string, items: QueueItem[]): Promise<void> {
  await mkdir(path.join(dir, 'catalog'), { recursive: true });
  await writeFile(queueFilePath(dir), JSON.stringify({ items }), 'utf-8');
}

function item(key: string, extra: Partial<QueueItem> = {}): QueueItem {
  return { key, url: `https://example.com/${key}`, source: 'manual', added: new Date().toISOString(), ...extra } as QueueItem;
}

describe('buildItemPrompt', () => {
  const recipe = 'RECIPE TEXT\n\nStep 1. Do the thing.\n';

  it('embeds only the one given item (key, url, content) — the agent never sees another item or a queue{list} call', () => {
    const prompt = buildItemPrompt(recipe, item('k1', { url: 'https://x/k1', content: 'k1 body text' }));
    expect(prompt).toContain('key: k1');
    expect(prompt).toContain('url: https://x/k1');
    expect(prompt).toContain('k1 body text');
    // No other item's data, and no instruction to list the whole queue.
    expect(prompt).not.toContain('action:list');
    expect(prompt).not.toContain('action: list');
    expect(prompt).not.toContain('k2 body text');
  });

  it('marks the item data as untrusted, between fenced BEGIN/END markers', () => {
    const prompt = buildItemPrompt(recipe, item('k1'));
    expect(prompt).toContain('UNTRUSTED DATA');
    const begin = prompt.indexOf('===BEGIN ITEM DATA===');
    const end = prompt.indexOf('===END ITEM DATA===');
    expect(begin).toBeGreaterThan(-1);
    expect(end).toBeGreaterThan(begin);
  });

  it('renders "(none)" for a url-less or content-less item instead of the literal undefined', () => {
    const prompt = buildItemPrompt(recipe, item('k1', { url: undefined, content: 'only text' }));
    expect(prompt).toContain('url: (none)');
  });
});

describe('buildClaudeArgs', () => {
  it('always pins --model sonnet by default (WK-0092 OR-1: never the inherited default)', () => {
    const args = buildClaudeArgs('/tmp/mcp.json');
    const i = args.indexOf('--model');
    expect(i).toBeGreaterThan(-1);
    expect(args[i + 1]).toBe('sonnet');
  });

  it('WK-0097 --model: an explicit model is passed through --model instead of the sonnet default', () => {
    const args = buildClaudeArgs('/tmp/mcp.json', 'opus');
    const i = args.indexOf('--model');
    expect(i).toBeGreaterThan(-1);
    expect(args[i + 1]).toBe('opus');
  });

  it('always passes --strict-mcp-config, so only the catalog MCP server loads (no kb-wiki leak)', () => {
    expect(buildClaudeArgs('/tmp/mcp.json')).toContain('--strict-mcp-config');
  });

  it('restricts the built-in tool set to WebSearch, WebFetch, Read via --tools (removes Edit/Write/Bash/Task*)', () => {
    const args = buildClaudeArgs('/tmp/mcp.json');
    const i = args.indexOf('--tools');
    expect(i).toBeGreaterThan(-1);
    expect(args[i + 1]).toBe(BUILTIN_TOOLS.join(','));
    expect(args[i + 1]).toBe('WebSearch,WebFetch,Read');
  });

  it('pre-authorizes exactly the 3 built-ins plus the catalog MCP tools the single-item recipe calls, and nothing else', () => {
    const args = buildClaudeArgs('/tmp/mcp.json');
    const i = args.indexOf('--allowedTools');
    const j = args.indexOf('--disallowedTools'); // next flag after the variadic --allowedTools list
    const allowed = args.slice(i + 1, j);
    expect(allowed.sort()).toEqual([...BUILTIN_TOOLS, ...CATALOG_MCP_TOOLS].sort());
    // The recipe no longer calls `index` (code calls the index function directly, decision 6).
    expect(allowed).not.toContain('mcp__catalog__index');
  });

  it('denies every other catalog server tool, so the project settings allow list cannot reach index/lint/drain', () => {
    // WK-0092: --allowedTools alone let a session call a disallowed tool through .claude/settings.json.
    const args = buildClaudeArgs('/tmp/mcp.json');
    const i = args.indexOf('--disallowedTools');
    const j = args.indexOf('--output-format');
    const denied = args.slice(i + 1, j);
    const serverTools = tools.map((t) => `mcp__catalog__${t.name}`);
    // allowed + denied covers the whole server, with no overlap
    expect([...denied, ...CATALOG_MCP_TOOLS].sort()).toEqual(serverTools.sort());
    expect(denied.filter((d) => CATALOG_MCP_TOOLS.includes(d))).toEqual([]);
    for (const name of ['index', 'lint', 'drain', 'ingest', 'config']) {
      expect(denied).toContain(`mcp__catalog__${name}`);
    }
  });
});

describe('parseSessionUsage (golden capture)', () => {
  // Real, unedited `claude --print --model sonnet --tools "" --strict-mcp-config
  // --output-format json` captures (2026-10-28). See the module-level "Usage source" comment in
  // run-processing.ts for why the result object's usage, not the session JSONL, is parsed.
  it('parses the single-turn capture: a trivial 1-turn reply', async () => {
    const stdout = await readFixture('single-turn-result.json');
    const usage = parseSessionUsage(stdout);
    expect(usage).toEqual({
      sessionId: '27d70b74-c06f-40fc-b479-d0260abb15df',
      model: 'claude-sonnet-5',
      input: 2,
      cacheRead: 0,
      cacheWrite: 17014,
      output: 4,
      costUsd: 0.06810000000000001,
      numTurns: 1,
      durationApiMs: 1654,
      isError: false,
      subtype: 'success',
      permissionDenials: 0,
    });
  });

  it('parses the multi-turn capture: usage is cumulative across both turns, matching the session JSONL sum byte-for-byte (verified by hand against the transcript, cited in run-processing.ts)', async () => {
    const stdout = await readFixture('multi-turn-result.json');
    const usage = parseSessionUsage(stdout);
    expect(usage).toEqual({
      sessionId: '85446442-2755-4275-81a8-1b8732705236',
      model: 'claude-sonnet-5',
      input: 4,
      cacheRead: 18317,
      cacheWrite: 18477,
      output: 66,
      costUsd: 0.0782394,
      numTurns: 2,
      durationApiMs: 2755,
      isError: false,
      subtype: 'success',
      permissionDenials: 0,
    });
  });

  it('returns null for text that is not a parsable result object, instead of throwing (a crashed session prints nothing usable)', () => {
    expect(parseSessionUsage('not json')).toBeNull();
    expect(parseSessionUsage('{"type":"system"}')).toBeNull();
  });
});

describe('countToolCalls (golden capture)', () => {
  // Real transcript lines from one catalog:process item session (2026-10-29, the
  // thermo-nuclear-code-quality-review item, which searched, found an existing entry, and removed
  // itself from the queue). Only the assistant tool_use lines are kept, each unedited: run logs stay
  // out of this public repo. Evals rely on these counts to see what each session did.
  it('counts tool_use blocks by tool name across the whole session', async () => {
    const transcript = await readFixture('item-session-transcript.jsonl');
    expect(countToolCalls(transcript)).toEqual({
      Read: 1,
      'mcp__catalog__fetch-url': 2,
      mcp__catalog__queue: 1,
      mcp__catalog__search: 3,
    });
  });

  it('skips blank and unparsable lines instead of throwing', () => {
    expect(countToolCalls('\nnot json\n{"type":"user"}\n')).toEqual({});
  });
});

describe('processItem', () => {
  let dir: string;
  beforeEach(async () => {
    dir = await mkdtemp(path.join(os.tmpdir(), 'catalog-run-processing-'));
    mockSpawn.mockReset();
    // Point the transcript lookup at an empty store so tests never read ~/.claude.
    vi.stubEnv('CLAUDE_CONFIG_DIR', path.join(dir, 'claude-config'));
  });
  afterEach(async () => {
    vi.unstubAllEnvs();
    await rm(dir, { recursive: true, force: true });
  });

  it('status "done": the session removes the item from the queue, so the code-side check finds it gone', async () => {
    await writeQueueFile(dir, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, { k1: { removeFromQueue: true, stdout } });

    const outcome = await processItem(dir, item('k1'), 'RECIPE', '/tmp/mcp.json', { timeoutMs: 5000 });

    expect(outcome.status).toBe('done');
    expect(outcome.timedOut).toBe(false);
    expect(outcome.usage?.model).toBe('claude-sonnet-5');
  });

  it('status "failed": the item is still in the queue after its session exits 0 — outcome is decided by queue state, not exit code (design decision 4)', async () => {
    await writeQueueFile(dir, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, { k1: { removeFromQueue: false, stdout, exitCode: 0 } });

    const outcome = await processItem(dir, item('k1'), 'RECIPE', '/tmp/mcp.json', { timeoutMs: 5000 });

    expect(outcome.status).toBe('failed');
    expect(outcome.timedOut).toBe(false);
  });

  it('timeout path: a session that never exits is killed once the per-item timeout elapses, and is logged failed (item never left the queue)', async () => {
    await writeQueueFile(dir, [item('k1')]);
    installFakeSpawn(dir, { k1: { hang: true } });

    const outcome = await processItem(dir, item('k1'), 'RECIPE', '/tmp/mcp.json', { timeoutMs: 20 });

    expect(outcome.timedOut).toBe(true);
    expect(outcome.status).toBe('failed');
  });
});

describe('runProcessing', () => {
  let dir: string;
  beforeEach(async () => {
    dir = await mkdtemp(path.join(os.tmpdir(), 'catalog-run-processing-loop-'));
    await mkdir(path.join(dir, 'catalog'), { recursive: true });
    await writeFile(path.join(dir, 'catalog', 'recipe.md'), 'RECIPE TEXT', 'utf-8');
    mockSpawn.mockReset();
    mockRebuildCatalogIndexes.mockClear();
    vi.stubEnv('CLAUDE_CONFIG_DIR', path.join(dir, 'claude-config'));
  });
  afterEach(async () => {
    vi.unstubAllEnvs();
    await rm(dir, { recursive: true, force: true });
  });

  it('a failed item does not stop the loop: the next item is still processed and logged', async () => {
    await writeQueueFile(dir, [item('k1'), item('k2')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, {
      k1: { removeFromQueue: false, stdout }, // fails — left in queue
      k2: { removeFromQueue: true, stdout }, // succeeds
    });

    await runProcessing({ dir, timeoutMs: 5000 });

    expect(mockSpawn).toHaveBeenCalledTimes(2);
    const log = (await readFile(path.join(dir, 'catalog', 'process-log.jsonl'), 'utf-8'))
      .trim().split('\n').map((l) => JSON.parse(l));
    expect(log).toHaveLength(2);
    expect(log[0]).toMatchObject({ key: 'k1', status: 'failed' });
    expect(log[1]).toMatchObject({ key: 'k2', status: 'done' });
  });

  it('--limit processes only the first N items in stored queue order, leaving the rest untouched', async () => {
    await writeQueueFile(dir, [item('k1'), item('k2'), item('k3')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, {
      k1: { removeFromQueue: true, stdout },
      k2: { removeFromQueue: true, stdout },
      k3: { removeFromQueue: true, stdout },
    });

    await runProcessing({ dir, limit: 2, timeoutMs: 5000 });

    expect(mockSpawn).toHaveBeenCalledTimes(2);
    const remaining = JSON.parse(await readFile(queueFilePath(dir), 'utf-8'));
    expect(remaining.items.map((i: QueueItem) => i.key)).toEqual(['k3']); // never touched by this run
    const log = (await readFile(path.join(dir, 'catalog', 'process-log.jsonl'), 'utf-8'))
      .trim().split('\n').map((l) => JSON.parse(l));
    expect(log.map((r) => r.key)).toEqual(['k1', 'k2']);
  });

  it('calls the shared rebuildCatalogIndexes function exactly once after the loop, never per item, and with no LLM step — the same function the `index` MCP tool calls, so the search index/graph/vectors stay in sync too (not just index.md)', async () => {
    await writeQueueFile(dir, [item('k1'), item('k2')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, {
      k1: { removeFromQueue: true, stdout },
      k2: { removeFromQueue: true, stdout },
    });

    await runProcessing({ dir, timeoutMs: 5000 });

    expect(mockRebuildCatalogIndexes).toHaveBeenCalledTimes(1);
    expect(mockRebuildCatalogIndexes).toHaveBeenCalledWith({ dir, format: 'full' });
  });

  it('writes one cost-log JSON line per item with the designed fields, including dollar cost and turns for evals', async () => {
    await writeQueueFile(dir, [item('k1')]);
    const stdout = await readFixture('multi-turn-result.json');
    installFakeSpawn(dir, { k1: { removeFromQueue: true, stdout } });

    await runProcessing({ dir, timeoutMs: 5000 });

    const [record] = (await readFile(path.join(dir, 'catalog', 'process-log.jsonl'), 'utf-8'))
      .trim().split('\n').map((l) => JSON.parse(l));
    expect(Object.keys(record).sort()).toEqual(
      [
        'api_s', 'cache_read', 'cache_write', 'cost_usd', 'input', 'is_error', 'key', 'model', 'num_turns', 'output',
        'permission_denials', 'session_id', 'status', 'subtype', 'timed_out', 'tool_calls', 'transcript', 'ts', 'wall_s',
      ].sort(),
    );
    expect(record.cost_usd).toBe(0.0782394);
    expect(record.num_turns).toBe(2);
    expect(record.api_s).toBe(2.8);
    // No transcript in the (empty) store: logged as null, item outcome unaffected.
    expect(record.transcript).toBeNull();
    expect(record.tool_calls).toBeNull();
    expect(record.status).toBe('done');
    expect(record.model).toBe('claude-sonnet-5');
    expect(record.cache_read).toBe(18317);
    expect(record.cache_write).toBe(18477);
    expect(record.input).toBe(4);
    expect(record.output).toBe(66);
    expect(record.session_id).toBe('85446442-2755-4275-81a8-1b8732705236');
  });

  it('archives the session transcript into catalog/runs/<session_id>/ and logs its tool-call counts, so evals survive Claude Code transcript cleanup', async () => {
    const sessionId = '85446442-2755-4275-81a8-1b8732705236'; // from multi-turn-result.json
    const store = path.join(dir, 'claude-config', 'projects', '-some-project-slug');
    await mkdir(path.join(store, sessionId, 'tool-results'), { recursive: true });
    await writeFile(path.join(store, `${sessionId}.jsonl`), await readFixture('item-session-transcript.jsonl'), 'utf-8');
    await writeFile(path.join(store, sessionId, 'tool-results', 'big.txt'), 'oversized output', 'utf-8');
    await writeQueueFile(dir, [item('k1')]);
    installFakeSpawn(dir, { k1: { removeFromQueue: true, stdout: await readFixture('multi-turn-result.json') } });

    await runProcessing({ dir, timeoutMs: 5000 });

    const [record] = (await readFile(path.join(dir, 'catalog', 'process-log.jsonl'), 'utf-8'))
      .trim().split('\n').map((l) => JSON.parse(l));
    expect(record.transcript).toBe(path.join('catalog', 'runs', sessionId));
    expect(record.tool_calls).toEqual({
      Read: 1, 'mcp__catalog__fetch-url': 2, mcp__catalog__queue: 1, mcp__catalog__search: 3,
    });
    const runDir = path.join(dir, 'catalog', 'runs', sessionId);
    expect(await readFile(path.join(runDir, 'transcript.jsonl'), 'utf-8'))
      .toBe(await readFixture('item-session-transcript.jsonl'));
    expect(await readFile(path.join(runDir, 'sidecar', 'tool-results', 'big.txt'), 'utf-8')).toBe('oversized output');
  });

  it('--concurrency runs up to N sessions at once, never more, and still processes and logs every item', async () => {
    const keys = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7'];
    await writeQueueFile(dir, keys.map((k) => item(k)));
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, Object.fromEntries(keys.map((k) => [k, { removeFromQueue: true, stdout, delayMs: 20 }])));

    await runProcessing({ dir, timeoutMs: 5000, concurrency: 3 });

    expect(mockSpawn).toHaveBeenCalledTimes(7);
    expect(inFlight.max).toBe(3);
    const log = (await readFile(path.join(dir, 'catalog', 'process-log.jsonl'), 'utf-8'))
      .trim().split('\n').map((l) => JSON.parse(l));
    expect(log.map((r) => r.key).sort()).toEqual(keys);
    expect(log.every((r) => r.status === 'done')).toBe(true);
    expect(JSON.parse(await readFile(queueFilePath(dir), 'utf-8')).items).toEqual([]);
    expect(mockRebuildCatalogIndexes).toHaveBeenCalledTimes(1);
  });

  it('default concurrency is 1: sessions never overlap', async () => {
    await writeQueueFile(dir, [item('k1'), item('k2'), item('k3')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, {
      k1: { removeFromQueue: true, stdout, delayMs: 10 },
      k2: { removeFromQueue: true, stdout, delayMs: 10 },
      k3: { removeFromQueue: true, stdout, delayMs: 10 },
    });

    await runProcessing({ dir, timeoutMs: 5000 });

    expect(inFlight.max).toBe(1);
  });

  it('graceful stop: with catalog/.stop-processing present, no new session starts, items stay queued, the index is still rebuilt, and the stop file is cleared', async () => {
    await writeQueueFile(dir, [item('k1'), item('k2')]);
    await writeFile(path.join(dir, 'catalog', '.stop-processing'), '', 'utf-8');
    installFakeSpawn(dir, {});

    await runProcessing({ dir, timeoutMs: 5000, concurrency: 2 });

    expect(mockSpawn).not.toHaveBeenCalled();
    expect(JSON.parse(await readFile(queueFilePath(dir), 'utf-8')).items.map((i: QueueItem) => i.key)).toEqual(['k1', 'k2']);
    expect(mockRebuildCatalogIndexes).toHaveBeenCalledTimes(1);
    await expect(readFile(path.join(dir, 'catalog', '.stop-processing'))).rejects.toThrow();
  });

  it('--group keeps items that share a tool in one slot: they never run at the same time', async () => {
    const hint = 'Mentioned (unverified hints):\n- Docling: (no url)';
    await writeQueueFile(dir, [item('a', { content: hint }), item('b'), item('c', { content: hint })]);
    const stdout = await readFixture('single-turn-result.json');
    const running = new Set<string>();
    let overlapped = false;
    mockSpawn.mockReset();
    installFakeSpawn(dir, {
      a: { removeFromQueue: true, stdout, delayMs: 20 },
      b: { removeFromQueue: true, stdout, delayMs: 20 },
      c: { removeFromQueue: true, stdout, delayMs: 20 },
    });
    const fake = mockSpawn.getMockImplementation()!;
    mockSpawn.mockImplementation(((cmd: string, args: string[], o: unknown) => {
      const child = fake(cmd, args, o as never) as unknown as { stdin: { write: (d: string) => void }; on: (e: string, f: () => void) => void };
      const write = child.stdin.write;
      child.stdin.write = (d: string) => {
        const key = d.match(/^key: (.+)$/m)?.[1] ?? '';
        if ((key === 'a' && running.has('c')) || (key === 'c' && running.has('a'))) overlapped = true;
        running.add(key);
        child.on('exit', () => running.delete(key));
        write(d);
      };
      return child;
    }) as unknown as typeof spawn);

    await runProcessing({ dir, timeoutMs: 5000, concurrency: 3, group: true });

    expect(mockSpawn).toHaveBeenCalledTimes(3);
    expect(overlapped).toBe(false);
    expect(inFlight.max).toBe(2); // the a→c group in one slot, b in another
  });

  it('graceful stop inside a group: after the stop file appears, the slot starts none of its group\'s remaining items', async () => {
    const hint = 'Mentioned (unverified hints):\n- Docling: (no url)';
    await writeQueueFile(dir, [item('a', { content: hint }), item('b', { content: hint }), item('c', { content: hint })]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, {
      a: { removeFromQueue: true, stdout, delayMs: 10 },
      b: { removeFromQueue: true, stdout, delayMs: 10 },
      c: { removeFromQueue: true, stdout, delayMs: 10 },
    });
    // The operator touches the stop file while item `a` is running.
    const fake = mockSpawn.getMockImplementation()!;
    mockSpawn.mockImplementationOnce(((cmd: string, args: string[], o: unknown) => {
      void writeFile(path.join(dir, 'catalog', '.stop-processing'), '', 'utf-8');
      return fake(cmd, args, o as never);
    }) as unknown as typeof spawn);

    await runProcessing({ dir, timeoutMs: 5000, concurrency: 2, group: true });

    expect(mockSpawn).toHaveBeenCalledTimes(1);
    expect(JSON.parse(await readFile(queueFilePath(dir), 'utf-8')).items.map((i: QueueItem) => i.key)).toEqual(['b', 'c']);
  });
});

// WK-0097 pilot: `--root <dir>` runs against an isolated catalog copy (queue, entries, index,
// process log, transcript archive, the spawned session's CATALOG_ROOT) while `recipe.md` and the
// MCP server's own source keep coming from the code repo (`dir`), so the pilot exercises the real,
// in-progress recipe and code against throwaway data.
describe('runProcessing --root (catalogRoot)', () => {
  let dir: string; // code root: has catalog/recipe.md, nothing else under catalog/
  let catalogRoot: string; // isolated catalog data copy
  beforeEach(async () => {
    dir = await mkdtemp(path.join(os.tmpdir(), 'catalog-run-processing-coderoot-'));
    catalogRoot = await mkdtemp(path.join(os.tmpdir(), 'catalog-run-processing-dataroot-'));
    await mkdir(path.join(dir, 'catalog'), { recursive: true });
    await writeFile(path.join(dir, 'catalog', 'recipe.md'), 'RECIPE FROM CODE REPO', 'utf-8');
    mockSpawn.mockReset();
    mockRebuildCatalogIndexes.mockClear();
    vi.stubEnv('CLAUDE_CONFIG_DIR', path.join(catalogRoot, 'claude-config'));
  });
  afterEach(async () => {
    vi.unstubAllEnvs();
    await rm(dir, { recursive: true, force: true });
    await rm(catalogRoot, { recursive: true, force: true });
  });

  it('reads and writes the queue at <catalogRoot>/catalog/queue.json, never at <dir>', async () => {
    await writeQueueFile(catalogRoot, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(catalogRoot, { k1: { removeFromQueue: true, stdout } });

    await runProcessing({ dir, catalogRoot, timeoutMs: 5000 });

    expect(JSON.parse(await readFile(queueFilePath(catalogRoot), 'utf-8')).items).toEqual([]);
    await expect(readFile(queueFilePath(dir), 'utf-8')).rejects.toThrow();
  });

  it('writes process-log.jsonl under <catalogRoot>/catalog/, never at <dir>', async () => {
    await writeQueueFile(catalogRoot, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(catalogRoot, { k1: { removeFromQueue: true, stdout } });

    await runProcessing({ dir, catalogRoot, timeoutMs: 5000 });

    const log = (await readFile(path.join(catalogRoot, 'catalog', 'process-log.jsonl'), 'utf-8'))
      .trim().split('\n').map((l) => JSON.parse(l));
    expect(log).toHaveLength(1);
    expect(log[0]).toMatchObject({ key: 'k1', status: 'done' });
    await expect(readFile(path.join(dir, 'catalog', 'process-log.jsonl'), 'utf-8')).rejects.toThrow();
  });

  it('rebuilds indexes against catalogRoot, not dir', async () => {
    await writeQueueFile(catalogRoot, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(catalogRoot, { k1: { removeFromQueue: true, stdout } });

    await runProcessing({ dir, catalogRoot, timeoutMs: 5000 });

    expect(mockRebuildCatalogIndexes).toHaveBeenCalledWith({ dir: catalogRoot, format: 'full' });
  });

  it('archives the session transcript under <catalogRoot>/catalog/runs/, not <dir>', async () => {
    const sessionId = '85446442-2755-4275-81a8-1b8732705236'; // from multi-turn-result.json
    const store = path.join(catalogRoot, 'claude-config', 'projects', '-some-project-slug');
    await mkdir(path.join(store, sessionId, 'tool-results'), { recursive: true });
    await writeFile(path.join(store, `${sessionId}.jsonl`), await readFixture('item-session-transcript.jsonl'), 'utf-8');
    await writeQueueFile(catalogRoot, [item('k1')]);
    installFakeSpawn(catalogRoot, { k1: { removeFromQueue: true, stdout: await readFixture('multi-turn-result.json') } });

    await runProcessing({ dir, catalogRoot, timeoutMs: 5000 });

    const runDir = path.join(catalogRoot, 'catalog', 'runs', sessionId);
    expect(await readFile(path.join(runDir, 'transcript.jsonl'), 'utf-8'))
      .toBe(await readFixture('item-session-transcript.jsonl'));
  });

  it('still reads recipe.md from the code root (dir) — catalogRoot has no recipe.md at all', async () => {
    await writeQueueFile(catalogRoot, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(catalogRoot, { k1: { removeFromQueue: true, stdout } });

    // If the code tried to read recipe.md from catalogRoot instead, this would reject (ENOENT).
    await expect(runProcessing({ dir, catalogRoot, timeoutMs: 5000 })).resolves.not.toThrow();
  });

  it('points the generated MCP config\'s CATALOG_ROOT at catalogRoot, and the server command at the code root (dir)', async () => {
    await writeQueueFile(catalogRoot, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(catalogRoot, { k1: { removeFromQueue: true, stdout } });

    await runProcessing({ dir, catalogRoot, timeoutMs: 5000 });

    const mcpConfig = JSON.parse(await readFile(path.join(dir, '.catalog-mcp.run.json'), 'utf-8'));
    expect(mcpConfig.mcpServers.catalog.env.CATALOG_ROOT).toBe(catalogRoot);
    expect(mcpConfig.mcpServers.catalog.args).toContain(path.join(dir, 'packages', 'catalog-mcp', 'src', 'server.ts'));
  });

  it('defaults catalogRoot to dir when --root is not given (unchanged behavior)', async () => {
    await writeQueueFile(dir, [item('k1')]);
    const stdout = await readFixture('single-turn-result.json');
    installFakeSpawn(dir, { k1: { removeFromQueue: true, stdout } });

    await runProcessing({ dir, timeoutMs: 5000 });

    expect(mockRebuildCatalogIndexes).toHaveBeenCalledWith({ dir, format: 'full' });
  });
});

describe('parseItemTimeoutMs (CLI, backs --item-timeout, WK-0097 D3)', () => {
  it('converts whole minutes to milliseconds', () => {
    expect(parseItemTimeoutMs(['--item-timeout', '45'])).toBe(45 * 60 * 1000);
    expect(parseItemTimeoutMs(['--item-timeout', '45'])).toBe(2_700_000);
  });

  it('returns undefined when the flag is absent, so runProcessing falls back to the 15-minute default', () => {
    expect(parseItemTimeoutMs(['--limit', '2'])).toBeUndefined();
  });

  it('rejects 0, a negative value, a non-numeric value, and a missing value — same as --limit', () => {
    expect(() => parseItemTimeoutMs(['--item-timeout', '0'])).toThrow();
    expect(() => parseItemTimeoutMs(['--item-timeout', '-5'])).toThrow();
    expect(() => parseItemTimeoutMs(['--item-timeout', 'abc'])).toThrow();
    expect(() => parseItemTimeoutMs(['--item-timeout'])).toThrow();
  });
});

describe('parseStringFlag (CLI, backs --root and --model)', () => {
  it('reads the value following the flag', () => {
    expect(parseStringFlag(['--root', '/tmp/pilot'], '--root')).toBe('/tmp/pilot');
    expect(parseStringFlag(['--model', 'opus'], '--model')).toBe('opus');
  });

  it('returns undefined when the flag is absent, so callers can default', () => {
    expect(parseStringFlag(['--limit', '2'], '--root')).toBeUndefined();
  });

  it('rejects a missing or flag-shaped value instead of silently consuming the next flag', () => {
    expect(() => parseStringFlag(['--root'], '--root')).toThrow();
    expect(() => parseStringFlag(['--root', '--model'], '--root')).toThrow();
  });
});

describe('resolveRootPath (WK-0097 D1)', () => {
  afterEach(() => {
    vi.unstubAllEnvs();
  });

  it('resolves a relative --root against INIT_CWD, not process.cwd() — npm sets INIT_CWD to the directory the operator actually ran the command from, while process.cwd() for an npm run script is the package directory; without this, a pilot invoked from the repo root silently nests its catalog under packages/catalog-mcp/ instead of the repo root, and runs against an empty queue there', () => {
    vi.stubEnv('INIT_CWD', '/repo/root');
    expect(resolveRootPath('toolkit-workbench/x')).toBe(path.resolve('/repo/root', 'toolkit-workbench/x'));
  });

  it('falls back to process.cwd() when INIT_CWD is unset', () => {
    vi.stubEnv('INIT_CWD', '');
    delete process.env.INIT_CWD;
    expect(resolveRootPath('toolkit-workbench/x')).toBe(path.resolve(process.cwd(), 'toolkit-workbench/x'));
  });

  it('leaves an absolute --root unchanged, ignoring INIT_CWD', () => {
    vi.stubEnv('INIT_CWD', '/repo/root');
    expect(resolveRootPath('/abs/pilot')).toBe('/abs/pilot');
  });
});

describe('assertCatalogRootExists (WK-0097 D1, fail loud)', () => {
  let dir: string;
  beforeEach(async () => {
    dir = await mkdtemp(path.join(os.tmpdir(), 'catalog-assert-root-'));
  });
  afterEach(async () => {
    await rm(dir, { recursive: true, force: true });
  });

  it('throws naming the resolved path when <root>/catalog does not exist — otherwise a typo\'d or not-yet-copied --root falls through to readQueue\'s ENOENT->{items:[]} fallback and the pilot "succeeds" having silently processed 0 items', () => {
    const missing = path.join(dir, 'does-not-exist');
    expect(() => assertCatalogRootExists(missing)).toThrow(path.join(missing, 'catalog'));
  });

  it('does not throw when <root>/catalog exists', async () => {
    await mkdir(path.join(dir, 'catalog'), { recursive: true });
    expect(() => assertCatalogRootExists(dir)).not.toThrow();
  });

  it('runProcessing rejects before starting any session when --root points at a missing catalog dir', async () => {
    mockSpawn.mockReset();
    const missing = path.join(dir, 'pilot-not-copied-yet');
    installFakeSpawn(missing, {});

    await expect(runProcessing({ dir, catalogRoot: missing, timeoutMs: 5000 })).rejects.toThrow();
    expect(mockSpawn).not.toHaveBeenCalled();
  });
});

