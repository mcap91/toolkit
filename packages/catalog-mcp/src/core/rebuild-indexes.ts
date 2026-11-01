// packages/catalog-mcp/src/core/rebuild-indexes.ts
// The full "rebuild everything derived from catalog/entries/" step: index.md, the search index,
// and the semantic vectors (if the embedder venv exists). This was the `index` MCP tool's
// handler body; it is now the single shared implementation so the tool and the WK-0092 headless
// adapter (`adapter/run-processing.ts`, which calls it once after its per-item loop instead of
// through an LLM `index` call) can't drift apart.
import { existsSync } from 'node:fs';
import { generateAndWriteIndex, buildSearchIndex } from './index-gen.js';
import { runCatalogEmbedder, venvPythonPath, codeRoot } from './embedder-subprocess.js';

export interface RebuildCatalogIndexesOptions {
  dir: string;
  format?: 'full' | 'category';
}

export interface RebuildCatalogIndexesResult {
  path: string;
  searchIndexPath: string;
  entryCount: number;
  vectorResult: { status: string; reason?: string; stderr?: string };
}

export async function rebuildCatalogIndexes(
  opts: RebuildCatalogIndexesOptions,
): Promise<RebuildCatalogIndexesResult> {
  const { dir } = opts;
  const format = opts.format ?? 'full';

  const result = await generateAndWriteIndex({ dir, format });
  const searchResult = await buildSearchIndex(dir);

  // WK-0097 D2: the venv lives in the code checkout, not `dir` (the catalog data root, possibly
  // an isolated --root copy or an out-of-repo CATALOG_ROOT) — `--dir` below still targets `dir`.
  const venvPython = venvPythonPath(codeRoot());
  let vectorResult: { status: string; reason?: string; stderr?: string };
  if (existsSync(venvPython)) {
    const { stderr, code } = await runCatalogEmbedder(venvPython, ['build', '--dir', dir]);
    vectorResult = code === 0 ? { status: 'ok' } : { status: 'error', stderr };
  } else {
    vectorResult = { status: 'skipped', reason: 'venv not found' };
  }

  return {
    path: result.path,
    searchIndexPath: searchResult.path,
    entryCount: result.entryCount,
    vectorResult,
  };
}
