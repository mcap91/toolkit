// packages/catalog-mcp/src/core/index-gen.ts
import { writeFile } from 'node:fs/promises';
import { readAllEntries } from './frontmatter.js';
import { catalogPaths } from './config.js';
import { cmpTitleLower, cmpRaw } from './sort.js';

interface IndexOptions {
  dir: string;
  format: 'full' | 'category';
}

interface IndexResult {
  content: string;
  path: string;
  searchIndexPath: string;
  entryCount: number;
}

interface EntryData {
  name: string;
  title: string;
  category: string;
  summary: string;
  tags: string[];
}

interface SearchIndexEntry {
  name: string;
  title: string;
  url: string | undefined;
  category: string;
  summary: string;
  body_summary: string;
  tags: string[];
  license: string | undefined;
  security_flags: string[];
  reviewed: string | undefined;
  path: string;
}

function extractSummary(body: string): string {
  const match = body.match(/##\s*What it (?:does|is)\s*\n([\s\S]*?)(?=\n##\s|\n*$)/);
  if (match) return match[1].trim();
  const trimmed = body.replace(/^#+\s.*\n*/gm, '').trim();
  if (trimmed.length <= 300) return trimmed;
  return trimmed.slice(0, 300).replace(/\s+\S*$/, '') + '…';
}

export async function generateIndex(options: IndexOptions): Promise<IndexResult> {
  const paths = catalogPaths(options.dir);
  const raw = await readAllEntries(paths.entries);
  const entries: EntryData[] = [];

  for (const [name, parsed] of raw) {
    const fm = parsed.frontmatter;

    entries.push({
      name,
      title: fm.title as string,
      category: fm.category as string,
      summary: fm.summary as string,
      tags: (fm.tags as string[]) || [],
    });
  }

  const sections: string[] = [];

  if (options.format === 'full') {
    sections.push(renderAllEntries(entries));
  }
  if (options.format === 'full' || options.format === 'category') {
    sections.push(renderByCategory(entries));
  }

  const header = `# Catalog Index\n\nGenerated from ${entries.length} entries in \`catalog/entries/\`. Regenerate with the catalog \`index\` tool.\n`;
  const content = header + '\n' + sections.join('\n\n') + '\n';

  return { content, path: paths.index, searchIndexPath: paths.searchIndex, entryCount: entries.length };
}

export async function generateAndWriteIndex(options: IndexOptions): Promise<IndexResult> {
  const result = await generateIndex(options);
  await writeFile(result.path, result.content, 'utf-8');
  return result;
}

export async function buildSearchIndex(dir: string): Promise<{ path: string; count: number }> {
  const paths = catalogPaths(dir);
  const raw = await readAllEntries(paths.entries);
  const entries: SearchIndexEntry[] = [];

  for (const [name, parsed] of raw) {
    const fm = parsed.frontmatter;
    entries.push({
      name,
      title: fm.title as string,
      url: fm.url as string | undefined,
      category: fm.category as string,
      summary: fm.summary as string,
      body_summary: extractSummary(parsed.body),
      tags: (fm.tags as string[]) || [],
      license: fm.license as string | undefined,
      security_flags: (fm.security_flags as string[]) || [],
      reviewed: fm.reviewed as string | undefined,
      path: `catalog/entries/${name}.md`,
    });
  }

  const index = {
    description: 'Search index for the catalog. Each entry describes an external tool, skill, framework, or reference captured from an outside source, with a security review.',
    usage: 'Search by tags, category, or keywords in summary/body_summary. Follow the path field for the full entry with security analysis and mechanical details.',
    generated: new Date().toISOString().slice(0, 10),
    count: entries.length,
    entries,
  };

  await writeFile(paths.searchIndex, JSON.stringify(index, null, 2) + '\n', 'utf-8');
  return { path: paths.searchIndex, count: entries.length };
}

function sortByTitle(entries: EntryData[]): EntryData[] {
  return [...entries].sort((a, b) => cmpTitleLower(a.title, b.title));
}

function renderAllEntries(entries: EntryData[]): string {
  const rows = sortByTitle(entries).map(
    (e) =>
      `| [${e.title}](entries/${e.name}.md) | ${e.category} | ${e.summary} | ${e.tags.join(', ')} |`,
  );
  return [
    '## All Entries',
    '',
    '| Item | Category | Summary | Tags |',
    '|---|---|---|---|',
    ...rows,
  ].join('\n');
}

function renderByCategory(entries: EntryData[]): string {
  const groups = new Map<string, EntryData[]>();
  for (const e of entries) {
    if (!groups.has(e.category)) groups.set(e.category, []);
    groups.get(e.category)!.push(e);
  }

  const sortedKeys = [...groups.keys()].sort(cmpRaw);

  const sections: string[] = ['## By Category'];
  for (const key of sortedKeys) {
    sections.push('');
    sections.push(`### ${key}`);
    sections.push('');
    for (const e of sortByTitle(groups.get(key)!)) {
      sections.push(`- [${e.title}](entries/${e.name}.md) — ${e.summary}`);
    }
  }
  return sections.join('\n');
}
