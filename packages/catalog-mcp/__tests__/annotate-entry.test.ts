import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { mkdtemp, rm, mkdir, writeFile, readFile } from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { annotateEntry } from '../src/core/annotate-entry.js';

const entry = `---
name: foo
title: "Foo"
url: https://github.com/o/foo
source: text
source_url: https://example.com/post/1
category: cli-tool
summary: "a tool"
tags: [x]
reviewed: 2026-06-17
---

## What it does

Does foo.

## Security

MIT.
`;

describe('annotateEntry', () => {
  let dir: string;
  beforeEach(async () => {
    dir = await mkdtemp(path.join(os.tmpdir(), 'catalog-an-'));
    await mkdir(path.join(dir, 'catalog', 'entries'), { recursive: true });
    await writeFile(path.join(dir, 'catalog', 'config.json'), '{"url_patterns":[]}', 'utf-8');
    await writeFile(path.join(dir, 'catalog', 'entries', 'foo.md'), entry, 'utf-8');
  });
  afterEach(async () => { await rm(dir, { recursive: true, force: true }); });
  const read = () => readFile(path.join(dir, 'catalog', 'entries', 'foo.md'), 'utf-8');

  it('creates a section when absent and preserves the rest', async () => {
    const r = await annotateEntry({ dir, name: 'foo', section: 'Usage notes', body: '- tip one' });
    expect(r.created).toBe(true);
    const out = await read();
    expect(out).toContain('## Usage notes\n\n- tip one');
    expect(out).toContain('## What it does\n\nDoes foo.');
    expect(out).toContain('## Security\n\nMIT.');
  });
  it('appends under an existing section in order', async () => {
    await annotateEntry({ dir, name: 'foo', section: 'Usage notes', body: '- tip one' });
    const r = await annotateEntry({ dir, name: 'foo', section: 'Usage notes', body: '- tip two' });
    expect(r.created).toBe(false);
    const out = await read();
    expect(out.indexOf('- tip one')).toBeLessThan(out.indexOf('- tip two'));
  });
  it('preserves frontmatter bytes exactly', async () => {
    const fmBefore = (await read()).split('---\n')[1];
    await annotateEntry({ dir, name: 'foo', section: 'Usage notes', body: '- tip' });
    expect((await read()).split('---\n')[1]).toBe(fmBefore);
  });
  it('throws on a missing entry', async () => {
    await expect(annotateEntry({ dir, name: 'nope', section: 'X', body: 'y' })).rejects.toThrow(/not found/);
  });

  it('parallel annotations of the same entry all land (sessions processed in parallel can hit one entry)', async () => {
    await Promise.all(Array.from({ length: 8 }, (_, i) =>
      annotateEntry({ dir, name: 'foo', section: 'Usage notes', body: `- tip ${i}` })));
    const out = await read();
    for (let i = 0; i < 8; i++) expect(out).toContain(`- tip ${i}`);
    expect(out.match(/^## Usage notes$/gm)).toHaveLength(1);
  });
});
