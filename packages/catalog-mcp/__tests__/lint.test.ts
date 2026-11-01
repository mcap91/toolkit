// packages/catalog-mcp/__tests__/lint.test.ts
import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { mkdtemp, rm, mkdir, writeFile, readFile } from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { lintEntry, lint } from '../src/core/lint.js';
import { parseFrontmatter } from '../src/core/frontmatter.js';

const FIXTURES_DIR = path.join(path.dirname(fileURLToPath(import.meta.url)), 'fixtures', 'wk-0070');

describe('lintEntry', () => {
  const validFrontmatter = {
    name: 'test-tool',
    title: 'Test Tool',
    url: 'https://github.com/org/test-tool',
    source: 'unknown', // no source_url set; "unknown" is the legacy no-provenance value
    category: 'skill',
    summary: 'looks promising',
    tags: ['testing'],
    reviewed: '2026-06-03',
  };

  it('returns no errors for valid entry', () => {
    const result = lintEntry('test-tool', validFrontmatter, '## What it does\n## Why this verdict\n## Mechanical details\n## Security\n');
    expect(result.errors).toEqual([]);
  });

  it('errors on missing required field', () => {
    const { title, ...noTitle } = validFrontmatter;
    const result = lintEntry('test-tool', noTitle, '');
    expect(result.errors.length).toBeGreaterThan(0);
    expect(result.errors[0]).toContain('title');
  });

  it('errors on a retired verdict key', () => {
    const result = lintEntry('test-tool', { ...validFrontmatter, verdict: 'maybe' }, '');
    expect(result.errors.length).toBeGreaterThan(0);
  });

  // OR-4 (WK-0086): source is now required so every entry records its provenance; lint must
  // not let a new entry through silently without one.
  it('errors on a missing source field', () => {
    const { source, ...noSource } = validFrontmatter;
    const result = lintEntry('test-tool', noSource, '');
    expect(result.errors.some((e: string) => e.includes('source'))).toBe(true);
  });

  it('warns on missing acquired (migration)', () => {
    const result = lintEntry('test-tool', validFrontmatter, '## What it does\n');
    expect(result.warnings.some((w: string) => w.includes('acquired'))).toBe(true);
  });

  it('warns on a missing ## Security section before the template cutover (migration: the live catalog predates the template)', () => {
    const result = lintEntry('test-tool', validFrontmatter, '## What it does\n## Why this verdict\n');
    expect(result.warnings.some((w: string) => w.includes('Security'))).toBe(true);
  });

  it('errors on name mismatch with filename', () => {
    const result = lintEntry('wrong-name', validFrontmatter, '');
    expect(result.errors.some((e: string) => e.includes('name'))).toBe(true);
  });
});

describe('lintEntry — bare block-scalar guard (WK-0070)', () => {
  const validFrontmatter = {
    name: 'test-tool',
    title: 'Test Tool',
    url: 'https://github.com/org/test-tool',
    source: 'unknown', // no source_url set; "unknown" is the legacy no-provenance value
    category: 'skill',
    summary: 'looks promising',
    tags: ['testing'],
    reviewed: '2026-06-03',
  };

  // Golden fixture: a real pre-repair capture where the old parser kept the
  // block-scalar header (">") as the summary value instead of the folded text.
  it('errors naming "summary" on the unedited pre-repair golden fixture', async () => {
    const raw = await readFile(path.join(FIXTURES_DIR, 'amazon-textract-textractor.md'), 'utf-8');
    const { frontmatter, body } = parseFrontmatter(raw);
    const result = lintEntry('amazon-textract-textractor', frontmatter, body);
    expect(result.errors.some((e: string) => e.includes('summary'))).toBe(true);
  });

  it('reports no bare-indicator error once the fixture summary is replaced with real text', async () => {
    const raw = await readFile(path.join(FIXTURES_DIR, 'amazon-textract-textractor.md'), 'utf-8');
    const repaired = raw.replace('summary: ">"', 'summary: "A Python wrapper around Amazon Textract."');
    const { frontmatter, body } = parseFrontmatter(repaired);
    const result = lintEntry('amazon-textract-textractor', frontmatter, body);
    expect(result.errors.some((e: string) => e.includes('bare block-scalar'))).toBe(false);
  });

  const indicators = ['>', '>-', '>+', '|', '|-', '|+'];
  for (const indicator of indicators) {
    it(`errors when summary is exactly the bare indicator "${indicator}"`, () => {
      const result = lintEntry('test-tool', { ...validFrontmatter, summary: indicator }, '');
      expect(result.errors.some((e: string) => e.includes('bare block-scalar'))).toBe(true);
    });
  }

  it('does not error on a normal string that merely contains ">"', () => {
    const result = lintEntry('test-tool', { ...validFrontmatter, summary: 'a > b' }, '');
    expect(result.errors.some((e: string) => e.includes('bare block-scalar'))).toBe(false);
  });
});

describe('lint --fix no longer adds a status field (removed in v2.1.0)', () => {
  let dir: string;
  // Errored (no tags -> schema fails) AND no status -> previously triggered the status default.
  const erroredNoStatus = (name: string) =>
    `---\nname: ${name}\ntitle: "${name}"\nurl: https://x.com/${name}\ncategory: skill\nsummary: ok\nreviewed: 2026-06-08\n---\nbody\n`;

  beforeEach(async () => {
    dir = await mkdtemp(path.join(os.tmpdir(), 'catalog-lint-'));
    await mkdir(path.join(dir, 'catalog', 'entries'), { recursive: true });
    await writeFile(path.join(dir, 'catalog', 'entries', 'e1.md'), erroredNoStatus('e1'), 'utf-8');
  });
  afterEach(async () => { await rm(dir, { recursive: true, force: true }); });

  it('lint({fix:true}) does not write a status line', async () => {
    await lint({ dir, fix: true });
    const md = await readFile(path.join(dir, 'catalog', 'entries', 'e1.md'), 'utf-8');
    expect(md).not.toContain('status:');
  });
});

describe('lint taxonomy audit + retired keys', () => {
  let tmp: string;
  beforeEach(async () => {
    tmp = await mkdtemp(path.join(os.tmpdir(), 'catalog-lintx-'));
    await mkdir(path.join(tmp, 'catalog', 'entries'), { recursive: true });
    await writeFile(
      path.join(tmp, 'catalog', 'taxonomy.json'),
      JSON.stringify({ canonical: { 'meta-skill': ['skill-optimization'] } }),
      'utf-8',
    );
    // alias-without-canonical: has skill-optimization but NOT meta-skill (warning-only, no schema error)
    await writeFile(
      path.join(tmp, 'catalog', 'entries', 'skillopt.md'),
      `---\nname: skillopt\ntitle: "SkillOpt"\ncategory: skill\nsource: unknown\nsummary: "x"\ntags: [skill-optimization]\nreviewed: 2026-06-16\n---\nbody\n`,
      'utf-8',
    );
    // retired verdict key -> error
    await writeFile(
      path.join(tmp, 'catalog', 'entries', 'legacy.md'),
      `---\nname: legacy\ntitle: "Legacy"\ncategory: skill\nsource: unknown\nverdict: adopt\nsummary: "x"\ntags: [t]\nreviewed: 2026-06-16\n---\nbody\n`,
      'utf-8',
    );
  });
  afterEach(async () => { await rm(tmp, { recursive: true, force: true }); });

  it('warns when an alias tag lacks its canonical', async () => {
    const res = await lint({ dir: tmp });
    const e = res.results.find((r) => r.file === 'skillopt.md')!;
    expect(e.warnings.some((w) => /meta-skill/.test(w))).toBe(true);
  });
  it('--fix adds the missing canonical tag (warning-only entry)', async () => {
    await lint({ dir: tmp, fix: true });
    const after = await readFile(path.join(tmp, 'catalog', 'entries', 'skillopt.md'), 'utf-8');
    expect(after).toMatch(/meta-skill/);
  });
  it('flags a retired verdict key as an error', async () => {
    const res = await lint({ dir: tmp });
    const e = res.results.find((r) => r.file === 'legacy.md')!;
    expect(e.errors.some((x) => /verdict/.test(x))).toBe(true);
  });
  it('reports aliasWithoutCanonical in the taxonomy summary', async () => {
    const res = await lint({ dir: tmp });
    expect(res.taxonomy.aliasWithoutCanonical).toBeGreaterThanOrEqual(1);
  });
});

// WK-0099 schema v2: decision_status, workflows, install and supersedes are retired — the
// catalog records what a tool is, not an adoption decision (WK-0051 precedent). Each must
// surface the friendly retired-field message, not just the generic strict-schema error.
describe('lintEntry — WK-0099 retired fields', () => {
  const base = {
    name: 'test-tool',
    title: 'Test Tool',
    category: 'skill',
    source: 'unknown',
    summary: 'ok',
    tags: ['t'],
    reviewed: '2026-06-03',
  };

  it('errors on decision_status', () => {
    const result = lintEntry('test-tool', { ...base, decision_status: 'adopted' }, '');
    expect(result.errors.some((e) => e.includes('decision_status'))).toBe(true);
  });
  it('errors on workflows', () => {
    const result = lintEntry('test-tool', { ...base, workflows: ['x'] }, '');
    expect(result.errors.some((e) => e.includes('workflows'))).toBe(true);
  });
  it('errors on install', () => {
    const result = lintEntry('test-tool', { ...base, install: 'npm i x' }, '');
    expect(result.errors.some((e) => e.includes('install'))).toBe(true);
  });
  it('errors on supersedes', () => {
    const result = lintEntry('test-tool', { ...base, supersedes: ['old'] }, '');
    expect(result.errors.some((e) => e.includes('supersedes'))).toBe(true);
  });
});

// WK-0099 provenance: a source traceable to a specific post/page (instagram/reddit/x/text) must
// carry the link it came in on; "web" and "unknown" are exempt (a bare link, or no recorded
// provenance at all).
describe('lintEntry — source_url required for instagram/reddit/x/text (WK-0099)', () => {
  const base = {
    name: 'test-tool',
    title: 'Test Tool',
    category: 'skill' as const,
    summary: 'ok',
    tags: ['t'],
    reviewed: '2026-06-03',
  };

  for (const source of ['instagram', 'reddit', 'x', 'text']) {
    it(`errors when source is "${source}" and source_url is absent`, () => {
      const result = lintEntry('test-tool', { ...base, source }, '');
      expect(result.errors.some((e) => e.includes('source_url'))).toBe(true);
    });
    it(`accepts source "${source}" when source_url is present`, () => {
      const result = lintEntry(
        'test-tool',
        { ...base, source, source_url: 'https://example.com/post/1' },
        '## What it is\n\nx\n\n## How it works\n\nx\n\n## Evaluation and limits\n\nx\n\n## Context from the source\n\nx\n\n## Related\n\nx\n\n## Security\n\nx\n',
      );
      expect(result.errors.some((e) => e.includes('source_url'))).toBe(false);
    });
  }

  it('does not require source_url when source is "web"', () => {
    const result = lintEntry('test-tool', { ...base, source: 'web' }, '');
    expect(result.errors.some((e) => e.includes('source_url'))).toBe(false);
  });

  it('does not require source_url when source is "unknown" (legacy, no recorded provenance)', () => {
    const result = lintEntry('test-tool', { ...base, source: 'unknown' }, '');
    expect(result.errors.some((e) => e.includes('source_url'))).toBe(false);
  });
});

// WK-0097 OR-2: never a link to a private capture file — the understanding goes into the entry
// itself. Always an error (not date-gated): this is a privacy rule, not a depth-formatting one.
describe('lintEntry — local capture path rejection (WK-0097 OR-2)', () => {
  const base = {
    name: 'test-tool',
    title: 'Test Tool',
    category: 'skill' as const,
    source: 'unknown' as const,
    summary: 'ok',
    tags: ['t'],
    reviewed: '2026-01-01',
  };

  it('errors on a catalog/sources/ link in the body', () => {
    const result = lintEntry('test-tool', base, 'See [capture](catalog/sources/reddit/abc.md) for more.');
    expect(result.errors.some((e) => e.includes('local capture path'))).toBe(true);
  });
  it('errors on a toolkit-workbench/ link in the body', () => {
    const result = lintEntry('test-tool', base, 'See [run](toolkit-workbench/depth-pilot/root/) for more.');
    expect(result.errors.some((e) => e.includes('local capture path'))).toBe(true);
  });
  it('does not error on a normal github.com link', () => {
    const result = lintEntry('test-tool', base, 'See https://github.com/org/repo for more.');
    expect(result.errors.some((e) => e.includes('local capture path'))).toBe(false);
  });
  it('errors on a local capture link even on a recent, template-cutover entry', () => {
    const result = lintEntry('test-tool', { ...base, reviewed: '2026-10-31' }, 'catalog/sources/x.md');
    expect(result.errors.some((e) => e.includes('local capture path'))).toBe(true);
  });
});

// WK-0099: template.md's body sections must be present (modulo the url-gated two) and in order.
// Warnings before the template cutover (the live catalog predates the template and the
// reprocess rewrites it), errors from the cutover on (so `lint` still catches a bad new entry).
describe('lintEntry — required body sections (WK-0099 template)', () => {
  const withUrl = {
    name: 'test-tool',
    title: 'Test Tool',
    url: 'https://github.com/org/test-tool',
    category: 'skill' as const,
    source: 'unknown' as const,
    summary: 'ok',
    tags: ['t'],
  };
  const complete = '## What it is\n\nx\n\n## How it works\n\nx\n\n## How to use it\n\nx\n\n## Evaluation and limits\n\nx\n\n## Context from the source\n\nx\n\n## Where to look next\n\n- learn x — https://example.com\n\n## Related\n\nx\n\n## Security\n\nx\n';

  it('old entry (reviewed before the cutover) missing every section only warns, no errors', () => {
    const result = lintEntry('test-tool', { ...withUrl, reviewed: '2026-06-03' }, '## What it does\n');
    expect(result.errors).toEqual([]);
    expect(result.warnings.some((w) => w.includes('What it is'))).toBe(true);
  });

  it('entry reviewed on the cutover date, missing every section, errors', () => {
    const result = lintEntry('test-tool', { ...withUrl, reviewed: '2026-10-31' }, '## What it does\n');
    expect(result.errors.some((e) => e.includes('What it is'))).toBe(true);
  });

  it('a complete entry (reviewed on the cutover) with a url passes with no section errors', () => {
    const result = lintEntry('test-tool', { ...withUrl, reviewed: '2026-10-31' }, complete);
    expect(result.errors).toEqual([]);
  });

  it('a url-less entry may omit "How to use it" and "Where to look next" with no error', () => {
    const { url, ...noUrl } = withUrl;
    const body = '## What it is\n\nx\n\n## How it works\n\nx\n\n## Evaluation and limits\n\nx\n\n## Context from the source\n\nx\n\n## Related\n\nx\n\n## Security\n\nx\n';
    const result = lintEntry('test-tool', { ...noUrl, reviewed: '2026-10-31' }, body);
    expect(result.errors).toEqual([]);
  });

  it('a url entry omitting "Where to look next" errors on or after the cutover', () => {
    const body = '## What it is\n\nx\n\n## How it works\n\nx\n\n## How to use it\n\nx\n\n## Evaluation and limits\n\nx\n\n## Context from the source\n\nx\n\n## Related\n\nx\n\n## Security\n\nx\n';
    const result = lintEntry('test-tool', { ...withUrl, reviewed: '2026-10-31' }, body);
    expect(result.errors.some((e) => e.includes('Where to look next'))).toBe(true);
  });

  it('errors (on or after the cutover) when sections appear out of template order', () => {
    const outOfOrder = '## How it works\n\nx\n\n## What it is\n\nx\n\n## How to use it\n\nx\n\n## Evaluation and limits\n\nx\n\n## Context from the source\n\nx\n\n## Where to look next\n\n- x — https://example.com\n\n## Related\n\nx\n\n## Security\n\nx\n';
    const result = lintEntry('test-tool', { ...withUrl, reviewed: '2026-10-31' }, outOfOrder);
    expect(result.errors.some((e) => e.includes('out of template order'))).toBe(true);
  });

  it('every "## Where to look next" line must carry a URL or a repo path (errors on or after the cutover)', () => {
    const badLine = '## What it is\n\nx\n\n## How it works\n\nx\n\n## How to use it\n\nx\n\n## Evaluation and limits\n\nx\n\n## Context from the source\n\nx\n\n## Where to look next\n\n- just a vague note, nothing to fetch\n\n## Related\n\nx\n\n## Security\n\nx\n';
    const result = lintEntry('test-tool', { ...withUrl, reviewed: '2026-10-31' }, badLine);
    expect(result.errors.some((e) => e.includes('carries no URL or repo path'))).toBe(true);
  });

  it('a "## Where to look next" line with a repo-relative path (no URL) is accepted', () => {
    const pathLine = '## What it is\n\nx\n\n## How it works\n\nx\n\n## How to use it\n\nx\n\n## Evaluation and limits\n\nx\n\n## Context from the source\n\nx\n\n## Where to look next\n\n- the main loop — src/core/loop.ts\n\n## Related\n\nx\n\n## Security\n\nx\n';
    const result = lintEntry('test-tool', { ...withUrl, reviewed: '2026-10-31' }, pathLine);
    expect(result.errors).toEqual([]);
  });
});

// WK-0099: the pre-template recipe's verdict/old-framing headings are always rejected, not just
// date-gated by reviewed — but the message still reports as a warning before the cutover (same
// body-section date gate as the other template rules) and an error from the cutover on.
describe('lintEntry — rejected headings (WK-0099)', () => {
  const base = {
    name: 'test-tool',
    title: 'Test Tool',
    category: 'skill' as const,
    source: 'unknown' as const,
    summary: 'ok',
    tags: ['t'],
  };

  for (const heading of ['Assessment', 'What to adopt', 'Differentiators', 'Mechanical details']) {
    it(`errors on "## ${heading}" for an entry reviewed on or after the cutover`, () => {
      const result = lintEntry('test-tool', { ...base, reviewed: '2026-10-31' }, `## ${heading}\n\nx\n`);
      expect(result.errors.some((e) => e.includes(heading))).toBe(true);
    });
    it(`warns (does not error) on "## ${heading}" for an entry reviewed before the cutover`, () => {
      const result = lintEntry('test-tool', { ...base, reviewed: '2026-06-03' }, `## ${heading}\n\nx\n`);
      expect(result.errors.some((e) => e.includes(heading))).toBe(false);
      expect(result.warnings.some((w) => w.includes(heading))).toBe(true);
    });
  }
});
