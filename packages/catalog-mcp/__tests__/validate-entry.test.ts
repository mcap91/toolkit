// packages/catalog-mcp/__tests__/validate-entry.test.ts
import { describe, it, expect } from 'vitest';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateEntry } from '../src/core/validate-entry.js';

const FIXTURES_DIR = path.join(path.dirname(fileURLToPath(import.meta.url)), 'fixtures', 'wk-0070');

const validMarkdown = `---
name: test-tool
title: "Test Tool"
url: https://github.com/org/test-tool
source: text
source_url: https://example.com/post/1
category: skill
summary: "looks promising"
tags: [testing]
reviewed: 2026-06-03
acquired: 2026-06-03
---

## What it does

A test tool.

## Differentiators

It looks good.

## Mechanical details

Install with npm.

## Security

MIT license. No flags.
`;

describe('validateEntry', () => {
  it('accepts valid entry', () => {
    const result = validateEntry(validMarkdown);
    expect(result.valid).toBe(true);
    expect(result.errors).toEqual([]);
  });

  it('rejects entry with no frontmatter', () => {
    const result = validateEntry('Just some text');
    expect(result.valid).toBe(false);
    expect(result.errors.length).toBeGreaterThan(0);
  });

  it('rejects entry with a retired verdict key', () => {
    const bad = validMarkdown.replace('summary: "looks promising"', 'summary: "looks promising"\nverdict: maybe');
    const result = validateEntry(bad);
    expect(result.valid).toBe(false);
  });

  it('warns on missing acquired for existing entries', () => {
    const noAcquired = validMarkdown.replace('acquired: 2026-06-03\n', '');
    const result = validateEntry(noAcquired);
    expect(result.valid).toBe(true);
    expect(result.warnings.some((w) => w.includes('acquired'))).toBe(true);
  });

  it('warns on missing Security section', () => {
    const noSecurity = validMarkdown.replace('## Security\n\nMIT license. No flags.\n', '');
    const result = validateEntry(noSecurity);
    expect(result.valid).toBe(true);
    expect(result.warnings.some((w) => w.includes('Security'))).toBe(true);
  });

  // Golden fixture: a real pre-repair entry where the old parser kept the
  // block-scalar header (">") as the summary value instead of the folded text (WK-0070).
  it('rejects the unedited pre-repair golden fixture (bare block-scalar summary)', async () => {
    const raw = await readFile(path.join(FIXTURES_DIR, 'amazon-textract-textractor.md'), 'utf-8');
    const result = validateEntry(raw);
    expect(result.valid).toBe(false);
    expect(result.errors.some((e) => e.includes('summary'))).toBe(true);
  });
});
