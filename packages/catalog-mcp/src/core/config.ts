// packages/catalog-mcp/src/core/config.ts
import { readFile, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { configSchema, stateSchema, type CatalogConfig, type CatalogState } from './schema.js';

export function resolveDir(inputDir?: string): string {
  if (inputDir) return path.resolve(inputDir);

  const envDir = process.env['CATALOG_ROOT'];
  if (envDir) return path.resolve(envDir);

  // Self-resolve: walk up from this file to find catalog/ directory
  let current = path.dirname(fileURLToPath(import.meta.url));
  for (let i = 0; i < 10; i++) {
    if (existsSync(path.join(current, 'catalog'))) return current;
    const parent = path.dirname(current);
    if (parent === current) break;
    current = parent;
  }

  throw new Error(
    'Cannot resolve repo root. Pass dir explicitly or set CATALOG_ROOT env var.',
  );
}

export async function loadConfig(dir: string): Promise<CatalogConfig> {
  const configPath = path.join(dir, 'catalog', 'config.json');
  const raw = await readFile(configPath, 'utf-8');
  const parsed = JSON.parse(raw);
  return configSchema.parse(parsed);
}

export function catalogPaths(dir: string) {
  return {
    entries: path.join(dir, 'catalog', 'entries'),
    index: path.join(dir, 'catalog', 'index.md'),
    searchIndex: path.join(dir, 'catalog', '.search-index.json'),
    taxonomy: path.join(dir, 'catalog', 'taxonomy.json'),
    queue: path.join(dir, 'catalog', 'queue.json'),
    config: path.join(dir, 'catalog', 'config.json'),
    state: path.join(dir, 'catalog', 'state.json'),
    queueLock: path.join(dir, 'catalog', '.queue.lock'),
    entriesLock: path.join(dir, 'catalog', '.entries.lock'),
  };
}

export async function loadState(dir: string): Promise<CatalogState> {
  const statePath = catalogPaths(dir).state;
  try {
    const raw = await readFile(statePath, 'utf-8');
    return stateSchema.parse(JSON.parse(raw));
  } catch {
    return stateSchema.parse({});
  }
}

export async function saveState(dir: string, updates: Partial<CatalogState>): Promise<CatalogState> {
  const current = await loadState(dir);
  const merged = { ...current, ...updates };
  const validated = stateSchema.parse(merged);
  const statePath = catalogPaths(dir).state;
  await writeFile(statePath, JSON.stringify(validated, null, 2) + '\n', 'utf-8');
  return validated;
}
