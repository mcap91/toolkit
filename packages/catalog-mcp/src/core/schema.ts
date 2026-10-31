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

export const DECISION_STATUSES = ['adopted', 'rejected'] as const;
export type DecisionStatus = (typeof DECISION_STATUSES)[number];

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

export const entrySchema = z
  .object({
    name: z.string().regex(/^[a-z0-9]+(-[a-z0-9]+)*$/, 'Must be kebab-case'),
    title: z.string().min(1),
    url: z.string().url().optional(),
    source_url: z.string().url().optional(),
    source: z.enum(ENTRY_SOURCES),
    category: z.enum(CATEGORIES),
    decision_status: z.enum(DECISION_STATUSES).optional(),
    summary: z.string().min(1),
    install: z.string().optional(),
    tags: z.array(z.string()).min(1),
    workflows: z.array(z.string()).optional(),
    reviewed: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    acquired: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).optional(),
    license: z.string().optional(),
    security_flags: z.array(z.string()).optional(),
    supersedes: z.array(z.string()).optional(),
    overlaps: z.array(z.string()).optional(),
  })
  .strict()
  .refine(
    (entry) => {
      if (!entry.source_url) return entry.source === 'text' || entry.source === 'unknown';
      return entry.source === deriveSource(entry.source_url);
    },
    {
      message:
        'source must equal the derivation from source_url (instagram/reddit/x/web); "unknown" is legacy-only and requires no source_url',
      path: ['source'],
    },
  );

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

