// packages/catalog-mcp/src/tools.ts
import { z } from 'zod';
import { dirSchema } from './core/schema.js';
import { resolveDir, loadConfig, loadState, saveState } from './core/config.js';
import { rebuildCatalogIndexes } from './core/rebuild-indexes.js';
import { lint } from './core/lint.js';
import { readQueue, removeFromQueue, returnToInbox, clearQueue } from './core/queue.js';
import { ingest } from './core/ingest.js';
import { fetchUrl } from './core/fetch-url.js';
import { buildPrompt } from './core/prompt-builder.js';
import { validateEntry } from './core/validate-entry.js';
import { writeEntry } from './core/write-entry.js';
import { annotateEntry } from './core/annotate-entry.js';
import { drainInbox } from './core/drain.js';
import { existsSync } from 'node:fs';
import { runCatalogEmbedder, venvPythonPath, codeRoot } from './core/embedder-subprocess.js';

export interface ToolDef {
  name: string;
  description: string;
  inputSchema: z.ZodType;
  handler: (input: Record<string, unknown>) => Promise<unknown>;
}

export const tools: ToolDef[] = [
  {
    name: 'index',
    description: 'Regenerate catalog/index.md from all entry files',
    inputSchema: dirSchema.extend({
      format: z.enum(['full', 'category']).default('full'),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      return rebuildCatalogIndexes({
        dir,
        format: input.format as 'full' | 'category',
      });
    },
  },
  {
    name: 'lint',
    description: 'Validate entry frontmatter against the catalog schema',
    inputSchema: dirSchema.extend({
      files: z.array(z.string()).optional(),
      fix: z.boolean().default(false),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      const { results, taxonomy } = await lint({
        dir,
        files: input.files as string[] | undefined,
        fix: input.fix as boolean,
      });
      const hasErrors = results.some((r) => r.errors.length > 0);
      return { results, taxonomy, clean: !hasErrors };
    },
  },
  {
    name: 'search',
    description: 'Survey search over catalog entries. Returns EVERY entry lexically matching your terms (word-prefix match, uncapped), plus up to semantic_n flagged semantic suggestions for concepts phrased differently. Expand your query into synonyms and related terms (e.g. "ocr" -> ["ocr", "text extraction", "document to markdown", "handwriting recognition"]) and pass them as terms; omitting terms treats the whole query as one all-tokens-must-match lookup term. Response reports per-term hit counts (swept_terms) and lexical_total — lexical_total 0 means an honest miss. Filters: category.',
    inputSchema: dirSchema.extend({
      query: z.string().max(2000),
      terms: z.array(z.string().min(1).max(200)).max(50).optional(),
      semantic_n: z.number().int().min(1).max(50).default(10),
      category: z.string().optional(),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      // WK-0097 D2: the venv lives in the code checkout, not whatever catalog dir `dir` resolved
      // to (e.g. an out-of-repo CATALOG_ROOT) — `--dir` below still targets the catalog data.
      const venvPython = venvPythonPath(codeRoot());
      if (!existsSync(venvPython)) {
        return {
          error: 'Semantic search not available. Run: cd packages/catalog-embedder && uv venv && uv pip install -r requirements.txt',
        };
      }

      const query = input.query as string;
      const terms = (input.terms as string[] | undefined) ?? [];
      const semantic_n = input.semantic_n as number;
      const category = input.category as string | undefined;

      const { stdout, stderr, code } = await runCatalogEmbedder(venvPython, [
        'search',
        '--query', query,
        '--dir', dir,
        ...terms.flatMap((t) => ['--term', t]),
        '--semantic-n', String(semantic_n),
        ...(category ? ['--category', category] : []),
      ]);

      if (code !== 0) {
        return { error: 'Search failed', stderr };
      }

      try {
        return JSON.parse(stdout);
      } catch {
        return { error: 'Failed to parse search output', stdout: stdout.slice(0, 500) };
      }
    },
  },
  {
    name: 'config',
    description: 'View and update catalog configuration and persistent state (e.g. Gmail pull cursor)',
    inputSchema: dirSchema.extend({
      action: z.enum(['get', 'set', 'check', 'get-state', 'set-state']),
      key: z.string().optional(),
      value: z.union([z.string(), z.array(z.string()), z.null()]).optional(),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      const action = input.action as string;
      if (action === 'get') {
        const config = await loadConfig(dir);
        const redditId = process.env['REDDIT_CLIENT_ID'] ? 'set' : 'not set';
        const redditSecret = process.env['REDDIT_CLIENT_SECRET'] ? 'set' : 'not set';
        const redditUser = process.env['REDDIT_USERNAME'] ? 'set' : 'not set';
        return {
          config,
          credentials: {
            REDDIT_CLIENT_ID: redditId,
            REDDIT_CLIENT_SECRET: redditSecret,
            REDDIT_USERNAME: redditUser,
          },
        };
      }
      if (action === 'check') {
        const config = await loadConfig(dir);
        const missing: string[] = [];
        if (!process.env['REDDIT_CLIENT_ID']) missing.push('REDDIT_CLIENT_ID');
        if (!process.env['REDDIT_CLIENT_SECRET']) missing.push('REDDIT_CLIENT_SECRET');
        if (!process.env['REDDIT_USERNAME']) missing.push('REDDIT_USERNAME');
        return {
          configValid: true,
          config,
          missingCredentials: missing,
        };
      }
      if (action === 'get-state') {
        return { state: await loadState(dir) };
      }
      if (action === 'set-state') {
        if (!input.key) throw new Error('key is required for set-state action');
        const VALID_STATE_KEYS = new Set(['gmail_last_pull_iso']);
        if (!VALID_STATE_KEYS.has(input.key as string)) {
          throw new Error(
            `Unknown state key "${input.key}". Valid keys: ${[...VALID_STATE_KEYS].join(', ')}`,
          );
        }
        const state = await saveState(dir, { [input.key as string]: input.value ?? null });
        return { updated: input.key, state };
      }
      // action === 'set'
      if (!input.key) throw new Error('key is required for set action');
      const VALID_KEYS = new Set(['url_patterns']);
      if (!VALID_KEYS.has(input.key as string)) {
        throw new Error(`Unknown config key "${input.key}". Valid keys: ${[...VALID_KEYS].join(', ')}`);
      }
      const { readFile, writeFile } = await import('node:fs/promises');
      const { catalogPaths } = await import('./core/config.js');
      const paths = catalogPaths(dir);
      const raw = JSON.parse(await readFile(paths.config, 'utf-8'));
      raw[input.key as string] = input.value;
      await writeFile(paths.config, JSON.stringify(raw, null, 2) + '\n', 'utf-8');
      return { updated: input.key, value: input.value };
    },
  },
  {
    name: 'queue',
    description: 'Manage the catalog intake queue (list/remove/return/clear). Holds only pending work; return sends an item back to inbox.md marked ⚠ <reason>.',
    inputSchema: dirSchema.extend({
      action: z.enum(['list', 'remove', 'return', 'clear']),
      keys: z.array(z.string()).optional(),
      key: z.string().optional(),
      reason: z.string().optional(),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      const action = input.action as string;
      if (action === 'list') {
        const queue = await readQueue(dir);
        return { items: queue.items, count: queue.items.length };
      }
      if (action === 'remove') {
        const keys = input.keys as string[];
        if (!keys?.length) throw new Error('keys required for remove action');
        return { removed: await removeFromQueue(dir, keys) };
      }
      if (action === 'return') {
        const key = input.key as string;
        if (!key) throw new Error('key required for return action');
        if (!input.reason) throw new Error('reason required for return action');
        return { returned: await returnToInbox(dir, key, input.reason as string) };
      }
      await clearQueue(dir);
      return { cleared: true };
    },
  },
  {
    name: 'drain',
    description: 'Drain catalog/inbox.md into the queue: ingest ready items, keep+mark blocked items (⚠ needs-link)',
    inputSchema: dirSchema,
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      return drainInbox(dir);
    },
  },
  {
    name: 'ingest',
    description: 'Add URLs or free-form text items to the intake queue, with dedup',
    inputSchema: dirSchema.extend({
      items: z.array(z.object({
        url: z.string().url().optional(),
        content: z.string().optional(),
        source: z.enum(['manual', 'reddit', 'slack', 'email', 'other']).default('manual'),
        notes: z.string().optional(),
        context: z.record(z.string(), z.unknown()).optional(),
      })),
      deduplicate: z.boolean().default(true),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      return ingest({
        dir,
        items: input.items as Array<{ url?: string; content?: string; source?: 'manual' | 'reddit' | 'slack' | 'email' | 'other'; notes?: string; context?: Record<string, unknown> }>,
        deduplicate: input.deduplicate as boolean,
      });
    },
  },
  {
    name: 'fetch-url',
    description: 'Fetch a URL and extract readable content (SSRF-guarded). clean=false returns raw HTML.',
    inputSchema: dirSchema.extend({
      url: z.string().url(),
      clean: z.boolean().default(true),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      const config = await loadConfig(dir).catch(() => ({ min_clean_chars: 200 } as { min_clean_chars: number }));
      return fetchUrl(input.url as string, {
        clean: input.clean as boolean,
        minChars: config.min_clean_chars,
      });
    },
  },
  {
    name: 'build-prompt',
    description: 'Build a structured research prompt for the calling agent: entry schema, body-section guide, and security checklist embedded in `prompt`. Result size does not grow with the catalog — it does not contain a catalog table; call `search` first for dedup/overlaps/related.',
    inputSchema: dirSchema.extend({
      url: z.string().url().optional(),
      content: z.string(),
      source_metadata: z.record(z.string(), z.unknown()).optional(),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      return buildPrompt({
        dir,
        url: input.url as string | undefined,
        content: input.content as string,
        sourceMetadata: input.source_metadata as Record<string, unknown> | undefined,
      });
    },
  },
  {
    name: 'validate-entry',
    description: 'Validate a catalog entry against the schema',
    inputSchema: dirSchema.extend({
      entry: z.string(),
    }),
    handler: async (input) => {
      return validateEntry(input.entry as string);
    },
  },
  {
    name: 'write-entry',
    description: 'Write a validated catalog entry to disk',
    inputSchema: dirSchema.extend({
      entry: z.string(),
      name: z.string(),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      return writeEntry({
        dir,
        entry: input.entry as string,
        name: input.name as string,
      });
    },
  },
  {
    name: 'annotate-entry',
    description: 'Append a note under a ## section of an existing entry (deterministic; frontmatter + other sections byte-preserved). Use to add usage tips to a tool without rewriting it.',
    inputSchema: dirSchema.extend({
      name: z.string(),
      section: z.string(),
      body: z.string(),
    }),
    handler: async (input) => {
      const dir = resolveDir(input.dir as string | undefined);
      return annotateEntry({
        dir,
        name: input.name as string,
        section: input.section as string,
        body: input.body as string,
      });
    },
  },
];
