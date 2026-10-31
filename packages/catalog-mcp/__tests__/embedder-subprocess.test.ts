// packages/catalog-mcp/__tests__/embedder-subprocess.test.ts
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { mkdtemp, mkdir, writeFile, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { codeRoot, venvPythonPath } from '../src/core/embedder-subprocess.js';

// Independently computed, the same way other tests in this package locate the real repo root
// (e.g. __tests__/index-gen.test.ts): three dirname-ups from __tests__.
const REAL_REPO_ROOT = path.resolve(import.meta.dirname, '..', '..', '..');

// rebuildCatalogIndexes' index.md/search-index steps are exercised elsewhere
// (index-gen.test.ts); mocked here so this file can isolate the one thing WK-0097
// D2 changed: which root the vector-build step looks up its venv under. `codeRoot` defaults to
// delegating to the real implementation (vi.mock is file-hoisted, so it also wraps the plain
// `codeRoot` import above) — only the `rebuildCatalogIndexes` describe below overrides its
// return value, so the `codeRoot` describe above still exercises the real self-resolve logic.
vi.mock('../src/core/index-gen.js', () => ({
  generateAndWriteIndex: vi.fn().mockResolvedValue({ path: '/idx', entryCount: 0, decisionStatusCounts: {} }),
  buildSearchIndex: vi.fn().mockResolvedValue({ path: '/search-idx', count: 0 }),
}));
vi.mock('../src/core/embedder-subprocess.js', async () => {
  const actual = await vi.importActual<typeof import('../src/core/embedder-subprocess.js')>(
    '../src/core/embedder-subprocess.js',
  );
  return { ...actual, runCatalogEmbedder: vi.fn(), codeRoot: vi.fn(actual.codeRoot) };
});

describe('codeRoot (WK-0097 D2)', () => {
  it('self-resolves to the real repo checkout from this module\'s own location, regardless of cwd or CATALOG_ROOT — the embedder venv belongs to the code, not to whatever catalog data directory a caller is pointed at', () => {
    expect(codeRoot()).toBe(REAL_REPO_ROOT);
  });

  it('is unaffected by CATALOG_ROOT pointing somewhere else entirely — otherwise an out-of-repo pilot catalog would look for (and never find) its own venv instead of the code checkout\'s', () => {
    const prev = process.env.CATALOG_ROOT;
    process.env.CATALOG_ROOT = '/some/outside/catalog/copy';
    try {
      expect(codeRoot()).toBe(REAL_REPO_ROOT);
    } finally {
      if (prev === undefined) delete process.env.CATALOG_ROOT;
      else process.env.CATALOG_ROOT = prev;
    }
  });

  it('venvPythonPath(codeRoot()) still joins packages/catalog-embedder/.venv/bin/python under the code root', () => {
    expect(venvPythonPath(codeRoot())).toBe(
      path.join(REAL_REPO_ROOT, 'packages', 'catalog-embedder', '.venv', 'bin', 'python'),
    );
  });
});

describe('rebuildCatalogIndexes (WK-0097 D2)', () => {
  let fakeCodeRoot: string; // a fake checkout with its own .venv, distinct from the catalog root
  let venvPython: string;

  beforeEach(async () => {
    fakeCodeRoot = await mkdtemp(path.join(os.tmpdir(), 'catalog-code-root-'));
    const venvBin = path.join(fakeCodeRoot, 'packages', 'catalog-embedder', '.venv', 'bin');
    await mkdir(venvBin, { recursive: true });
    venvPython = path.join(venvBin, 'python');
    await writeFile(venvPython, '', 'utf-8');

    const { runCatalogEmbedder, codeRoot: mockedCodeRoot } = await import('../src/core/embedder-subprocess.js');
    vi.mocked(runCatalogEmbedder).mockReset().mockResolvedValue({ stdout: '', stderr: '', code: 0 });
    vi.mocked(mockedCodeRoot).mockReset().mockReturnValue(fakeCodeRoot);
  });

  afterEach(async () => {
    await rm(fakeCodeRoot, { recursive: true, force: true });
  });

  it('on an outside catalog root, looks up the venv under the code root (not the catalog dir) and still rebuilds vectors for that catalog\'s own entries via --dir', async () => {
    const { rebuildCatalogIndexes } = await import('../src/core/rebuild-indexes.js');
    const { runCatalogEmbedder, codeRoot: mockedCodeRoot } = await import('../src/core/embedder-subprocess.js');
    const outsideCatalogRoot = '/outside/pilot-catalog';

    const result = await rebuildCatalogIndexes({ dir: outsideCatalogRoot });

    expect(mockedCodeRoot).toHaveBeenCalled();
    expect(vi.mocked(runCatalogEmbedder)).toHaveBeenCalledWith(venvPython, ['build', '--dir', outsideCatalogRoot]);
    expect(result.vectorResult.status).toBe('ok');
  });

  it('skips the vector rebuild when the code root has no venv installed, even though the catalog root is reachable', async () => {
    const { rebuildCatalogIndexes } = await import('../src/core/rebuild-indexes.js');
    const { runCatalogEmbedder, codeRoot: mockedCodeRoot } = await import('../src/core/embedder-subprocess.js');
    vi.mocked(mockedCodeRoot).mockReturnValue('/no/venv/here');

    const result = await rebuildCatalogIndexes({ dir: '/outside/pilot-catalog' });

    expect(vi.mocked(runCatalogEmbedder)).not.toHaveBeenCalled();
    expect(result.vectorResult).toEqual({ status: 'skipped', reason: 'venv not found' });
  });
});
