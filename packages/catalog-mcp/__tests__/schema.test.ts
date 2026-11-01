// packages/catalog-mcp/__tests__/schema.test.ts
import { describe, it, expect } from 'vitest';
import { entrySchema, CATEGORIES, ENTRY_SOURCES, deriveSource } from '../src/core/schema.js';

describe('entrySchema', () => {
  const validEntry = {
    name: 'test-tool',
    title: 'Test Tool',
    url: 'https://github.com/org/test-tool',
    source: 'unknown' as const, // no source_url set; "unknown" is the legacy no-provenance value
    category: 'skill' as const,
    summary: 'looks promising',
    tags: ['testing'],
    reviewed: '2026-06-03',
  };

  it('accepts a valid entry with all required fields', () => {
    const result = entrySchema.safeParse(validEntry);
    expect(result.success).toBe(true);
  });

  it('accepts entry without url (reference material)', () => {
    const { url, ...noUrl } = validEntry;
    const result = entrySchema.safeParse(noUrl);
    expect(result.success).toBe(true);
  });

  it('accepts entry with optional fields', () => {
    const full = {
      ...validEntry,
      topics: ['scRNA-seq'],
      related: ['other-tool'],
      acquired: '2026-06-01',
      license: 'MIT',
      security_flags: ['no-tests'],
      overlaps: ['similar-tool'],
    };
    const result = entrySchema.safeParse(full);
    expect(result.success).toBe(true);
  });

  it('defaults topics and related to an empty array when omitted', () => {
    const result = entrySchema.safeParse(validEntry);
    expect(result.success).toBe(true);
    if (result.success) {
      expect(result.data.topics).toEqual([]);
      expect(result.data.related).toEqual([]);
    }
  });

  it('rejects entry missing required name', () => {
    const { name, ...noName } = validEntry;
    const result = entrySchema.safeParse(noName);
    expect(result.success).toBe(false);
  });

  it('rejects invalid category', () => {
    const result = entrySchema.safeParse({ ...validEntry, category: 'banana' });
    expect(result.success).toBe(false);
  });

  it('does not include a status field (removed in v2.1.0)', () => {
    const result = entrySchema.safeParse(validEntry);
    expect(result.success).toBe(true);
    if (result.success) {
      expect('status' in result.data).toBe(false);
    }
    // .strict() also rejects a stray status key
    expect(entrySchema.safeParse({ ...validEntry, status: 'approved' }).success).toBe(false);
  });
});

// WK-0099 schema v2: the catalog records what a tool is, not an adoption decision — these four
// fields are retired and a strict schema must reject any entry still carrying one.
describe('entrySchema retired fields (WK-0099 schema v2)', () => {
  const base = {
    name: 'foo-bar',
    title: 'Foo Bar',
    source: 'unknown',
    category: 'skill',
    summary: 'one-line take',
    tags: ['x'],
    reviewed: '2026-06-16',
  };

  it('accepts an entry with none of the retired fields', () => {
    expect(entrySchema.safeParse(base).success).toBe(true);
  });
  it('rejects decision_status', () => {
    expect(entrySchema.safeParse({ ...base, decision_status: 'adopted' }).success).toBe(false);
  });
  it('rejects workflows', () => {
    expect(entrySchema.safeParse({ ...base, workflows: ['scRNA-seq'] }).success).toBe(false);
  });
  it('rejects install', () => {
    expect(entrySchema.safeParse({ ...base, install: 'npm install foo' }).success).toBe(false);
  });
  it('rejects supersedes', () => {
    expect(entrySchema.safeParse({ ...base, supersedes: ['old-tool'] }).success).toBe(false);
  });
  it('rejects the retired verdict field via .strict()', () => {
    expect(entrySchema.safeParse({ ...base, verdict: 'adopt' }).success).toBe(false);
  });
  it('rejects the retired verdict_reason field', () => {
    expect(entrySchema.safeParse({ ...base, verdict_reason: 'x' }).success).toBe(false);
  });
  it('requires summary', () => {
    const { summary, ...noSummary } = base;
    expect(entrySchema.safeParse(noSummary).success).toBe(false);
  });
});

// deriveSource is a deterministic host-mapping utility (OR-4, WK-0086); schema v2 no longer
// enforces source/source_url agreement at the schema level (lint.ts carries the provenance
// requirement instead), but the mapping itself is still pinned by test.
describe('deriveSource (OR-4 host mapping)', () => {
  it('maps instagram.com to instagram', () => {
    expect(deriveSource('https://instagram.com/reel/abc123/')).toBe('instagram');
  });
  it('maps an instagram subdomain (www.) to instagram', () => {
    expect(deriveSource('https://www.instagram.com/reel/abc123/')).toBe('instagram');
  });
  it('maps reddit.com to reddit', () => {
    expect(deriveSource('https://reddit.com/r/test/comments/abc/x/')).toBe('reddit');
  });
  it('maps a reddit subdomain (old.) to reddit', () => {
    expect(deriveSource('https://old.reddit.com/r/test/comments/abc/x/')).toBe('reddit');
  });
  it('maps redd.it to reddit', () => {
    expect(deriveSource('https://redd.it/abc123')).toBe('reddit');
  });
  it('maps x.com to x', () => {
    expect(deriveSource('https://x.com/user/status/123')).toBe('x');
  });
  it('maps twitter.com to x', () => {
    expect(deriveSource('https://twitter.com/user/status/123')).toBe('x');
  });
  it('maps a mobile subdomain (m.) of a mapped host to its source', () => {
    expect(deriveSource('https://m.twitter.com/user/status/123')).toBe('x');
  });
  it('maps any other real host to web', () => {
    expect(deriveSource('https://github.com/org/repo')).toBe('web');
  });
  it('maps a lookalike host that merely ends in the domain string (not a subdomain) to web, not the domain', () => {
    // "notinstagram.com" ends with "instagram.com" as a raw string but is not a subdomain of it —
    // the "." boundary in hostOrSubdomain must prevent a false match.
    expect(deriveSource('https://notinstagram.com/x')).toBe('web');
  });
  it('maps no source_url to text', () => {
    expect(deriveSource(undefined)).toBe('text');
  });
  it('never derives unknown — unknown is legacy-only, not a derivation output', () => {
    for (const url of [undefined, 'https://github.com/org/repo', 'https://instagram.com/reel/x/']) {
      expect(deriveSource(url)).not.toBe('unknown');
    }
  });
});

// Schema v2 (WK-0099): source_url is optional at the schema level for every source value — the
// "requires source_url when source is instagram/reddit/x/text" rule lives in lint.ts, not here,
// so an entry can be validated in isolation without re-deriving provenance from a URL.
describe('entrySchema source/source_url (WK-0099 schema v2)', () => {
  const base = {
    name: 'foo-bar',
    title: 'Foo Bar',
    category: 'skill' as const,
    summary: 'one-line take',
    tags: ['x'],
    reviewed: '2026-06-16',
  };

  it('accepts source_url with a matching source', () => {
    const result = entrySchema.safeParse({
      ...base,
      source_url: 'https://www.instagram.com/reel/abc123/',
      source: 'instagram',
    });
    expect(result.success).toBe(true);
  });

  it('accepts source: unknown even when source_url is present — schema no longer ties the two together', () => {
    const result = entrySchema.safeParse({
      ...base,
      source_url: 'https://github.com/org/repo',
      source: 'unknown',
    });
    expect(result.success).toBe(true);
  });

  it('accepts source: unknown when source_url is absent (legacy entries)', () => {
    const result = entrySchema.safeParse({ ...base, source: 'unknown' }).success;
    expect(result).toBe(true);
  });

  it('accepts source: text without source_url at the schema level (lint enforces the requirement, not the schema)', () => {
    const result = entrySchema.safeParse({ ...base, source: 'text' });
    expect(result.success).toBe(true);
  });

  it('accepts source: web without source_url at the schema level', () => {
    const result = entrySchema.safeParse({ ...base, source: 'web' });
    expect(result.success).toBe(true);
  });

  it('rejects an entry with no source field at all', () => {
    expect(entrySchema.safeParse(base).success).toBe(false);
  });

  it('ENTRY_SOURCES carries exactly the six OR-4 values', () => {
    expect([...ENTRY_SOURCES].sort()).toEqual(
      ['instagram', 'reddit', 'text', 'unknown', 'web', 'x'].sort(),
    );
  });
});
