import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { mkdtemp, rm, mkdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { persistEntry } from '../src/core/entry-io.js';

const valid = `---\nname: t\ntitle: "T"\nurl: https://x.com/t\nsource: text\nsource_url: https://example.com/post/1\ncategory: skill\nsummary: ok\ntags: [a]\nreviewed: 2026-06-08\n---\nbody\n`;

describe('persistEntry', () => {
  let dir: string;
  beforeEach(async () => {
    dir = await mkdtemp(path.join(os.tmpdir(), 'catalog-e-'));
    await mkdir(path.join(dir, 'catalog', 'entries'), { recursive: true });
  });
  afterEach(async () => { await rm(dir, { recursive: true, force: true }); });

  it('writes a valid entry with LF endings', async () => {
    const r = await persistEntry({ dir, name: 't', markdown: valid });
    const onDisk = await readFile(r.path, 'utf-8');
    expect(onDisk).not.toContain('\r\n');
    expect(onDisk).toContain('name: t');
  });

  it('refuses to overwrite without overwrite:true', async () => {
    await persistEntry({ dir, name: 't', markdown: valid });
    await expect(persistEntry({ dir, name: 't', markdown: valid })).rejects.toThrow(/already exists/);
  });

  it('rejects invalid markdown', async () => {
    await expect(persistEntry({ dir, name: 'bad', markdown: 'no frontmatter' })).rejects.toThrow(/Invalid entry/);
  });
});
