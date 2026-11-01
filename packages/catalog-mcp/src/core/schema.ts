// packages/catalog-mcp/src/core/schema.ts
import { z } from 'zod';

export const CATEGORIES = [
  'skill',
  'hook',
  'plugin',
  'mcp-server',
  'agent-pattern',
  'cli-tool',
  'framework',
  'skill-generator',
  'meta-skill',
  'reference',
] as const;

export const SOURCES = ['manual', 'reddit', 'slack', 'email', 'other'] as const;

export type Category = (typeof CATEGORIES)[number];

// Entry provenance (OR-4, WK-0086). Distinct from SOURCES above, which describes how a queue
// item entered the intake pipeline — this describes where a catalog entry's content came from.
export const ENTRY_SOURCES = ['instagram', 'reddit', 'x', 'web', 'text', 'unknown'] as const;
export type EntrySource = (typeof ENTRY_SOURCES)[number];

type DerivableSource = Exclude<EntrySource, 'text' | 'unknown'>;

// Host -> entry source (OR-4). Matches the bare domain or any subdomain (www., old., m., ...).
const SOURCE_HOSTS: { domains: string[]; source: DerivableSource }[] = [
  { domains: ['instagram.com'], source: 'instagram' },
  { domains: ['reddit.com', 'redd.it'], source: 'reddit' },
  { domains: ['x.com', 'twitter.com'], source: 'x' },
];

function hostOrSubdomain(hostname: string, domain: string): boolean {
  return hostname === domain || hostname.endsWith(`.${domain}`);
}

/**
 * Deterministic entry-source derivation from a `source_url` (OR-4). No `source_url` -> 'text'.
 * Any other host (including an unparseable url) -> 'web'. Never derives 'unknown' — that value
 * is legacy-only and is never the output of this function.
 */
export function deriveSource(sourceUrl?: string): EntrySource {
  if (!sourceUrl) return 'text';
  let hostname: string;
  try {
    hostname = new URL(sourceUrl).hostname.toLowerCase();
  } catch {
    return 'web';
  }
  for (const { domains, source } of SOURCE_HOSTS) {
    if (domains.some((d) => hostOrSubdomain(hostname, d))) return source;
  }
  return 'web';
}

// Schema v2 (WK-0099): exactly 15 fields, the public entry contract in catalog/template.md.
// `decision_status`, `workflows`, `install` and `supersedes` are retired (lint.ts RETIRED_FIELDS);
// the catalog records what a tool is, not an adoption decision. `source_url` is optional here —
// lint enforces it is set when `source` is instagram/reddit/x/text (provenance, not schema shape).
export const entrySchema = z
  .object({
    name: z.string().regex(/^[a-z0-9]+(-[a-z0-9]+)*$/, 'Must be kebab-case'),
    title: z.string().min(1),
    url: z.string().url().optional(),
    source_url: z.string().url().optional(),
    source: z.enum(ENTRY_SOURCES),
    category: z.enum(CATEGORIES),
    summary: z.string().min(1),
    tags: z.array(z.string()).min(1),
    topics: z.array(z.string()).default([]),
    related: z.array(z.string()).default([]),
    overlaps: z.array(z.string()).optional(),
    acquired: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).optional(),
    reviewed: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    license: z.string().optional(),
    security_flags: z.array(z.string()).optional(),
  })
  .strict();

export type CatalogEntry = z.infer<typeof entrySchema>;

export const queueItemSchema = z
  .object({
    url: z.string().url().optional(),
    content: z.string().optional(),
    key: z.string(),
    source: z.enum(SOURCES).default('manual'),
    notes: z.string().optional(),
    context: z.record(z.string(), z.unknown()).optional(),
    added: z.string(),
  })
  .refine((i) => Boolean(i.url) || Boolean(i.content), {
    message: 'queue item requires a url or content',
  });

export type QueueItem = z.infer<typeof queueItemSchema>;

export const queueSchema = z.object({
  items: z.array(queueItemSchema),
});

const blockedDomainSchema = z.object({
  host: z.string(),
  allow_paths: z.array(z.string()).optional(),
});

export const configSchema = z.object({
  url_patterns: z.array(z.string()),
  blocked_domains: z.array(blockedDomainSchema).default([]),
  min_clean_chars: z.number().default(200),
  // WK-0098 (DEC-0004 amendment): semantic rescue off by default until proven; the lexical
  // sweep is unaffected either way.
  semantic_search: z.boolean().default(false),
});

export type BlockedDomain = z.infer<typeof blockedDomainSchema>;

export type CatalogConfig = z.infer<typeof configSchema>;

export const stateSchema = z.object({
  gmail_last_pull_iso: z.string().datetime().nullable().default(null),
});

export type CatalogState = z.infer<typeof stateSchema>;

export const dirSchema = z.object({
  dir: z.string().optional().describe('Target repo directory (auto-resolved if omitted)'),
});

