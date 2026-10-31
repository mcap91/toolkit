// packages/catalog-mcp/src/core/index-gen.ts
import { writeFile } from 'node:fs/promises';
import { readAllEntries } from './frontmatter.js';
import { catalogPaths } from './config.js';
import { cmpTitleLower, cmpRaw } from './sort.js';

interface IndexOptions {
  dir: string;
  format: 'full' | 'decision_status' | 'workflow' | 'category';
}

interface IndexResult {
  content: string;
  path: string;
  searchIndexPath: string;
  entryCount: number;
  decisionStatusCounts: Record<string, number>;
}

interface EntryData {
  name: string;
  title: string;
  category: string;
  decision_status: string;
  summary: string;
  tags: string[];
  workflows: string[];
}

interface SearchIndexEntry {
  name: string;
  title: string;
  url: string | undefined;
  category: string;
  decision_status: string;
  summary: string;
  body_summary: string;
  tags: string[];
  workflows: string[];
  license: string | undefined;
  security_flags: string[];
  reviewed: string | undefined;
  path: string;
}

function extractSummary(body: string): string {
  const match = body.match(/##\s*What it does\s*\n([\s\S]*?)(?=\n##\s|\n*$)/);
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
      decision_status: (fm.decision_status as string) ?? 'open',
      summary: fm.summary as string,
      tags: (fm.tags as string[]) || [],
      workflows: (fm.workflows as string[]) || [],
    });
  }

  const decisionStatusCounts: Record<string, number> = {};
  for (const e of entries) {
    decisionStatusCounts[e.decision_status] = (decisionStatusCounts[e.decision_status] || 0) + 1;
  }

  const sections: string[] = [];

  if (options.format === 'full' || options.format === 'decision_status') {
    sections.push(renderByDecisionStatus(entries));
  }
  if (options.format === 'full' || options.format === 'workflow') {
    sections.push(renderByWorkflow(entries));
  }
  if (options.format === 'full' || options.format === 'category') {
    sections.push(renderByCategory(entries));
  }

  const header = `# Catalog Index\n\nGenerated from ${entries.length} entries in \`catalog/entries/\`. Regenerate with the catalog \`index\` tool.\n`;
  const content = header + '\n' + sections.join('\n\n') + '\n';

  return { content, path: paths.index, searchIndexPath: paths.searchIndex, entryCount: entries.length, decisionStatusCounts };
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
      decision_status: (fm.decision_status as string) ?? 'open',
      summary: fm.summary as string,
      body_summary: extractSummary(parsed.body),
      tags: (fm.tags as string[]) || [],
      workflows: (fm.workflows as string[]) || [],
      license: fm.license as string | undefined,
      security_flags: (fm.security_flags as string[]) || [],
      reviewed: fm.reviewed as string | undefined,
      path: `catalog/entries/${name}.md`,
    });
  }

  const index = {
    description: 'Search index for the catalog. Each entry is an assessed external tool, skill, framework, or reference with a decision_status (adopted/rejected/open) and security review.',
    usage: 'Search by tags, category, decision_status, or keywords in summary/body_summary. Follow the path field for the full entry with security analysis and mechanical details.',
    generated: new Date().toISOString().slice(0, 10),
    count: entries.length,
    decision_statuses: { adopted: 'in use', rejected: 'evaluated and ruled out', open: 'stockpiled, undecided' },
    entries,
  };

  await writeFile(paths.searchIndex, JSON.stringify(index, null, 2) + '\n', 'utf-8');
  return { path: paths.searchIndex, count: entries.length };
}

function sortByTitle(entries: EntryData[]): EntryData[] {
  return [...entries].sort((a, b) => cmpTitleLower(a.title, b.title));
}

function renderByDecisionStatus(entries: EntryData[]): string {
  const sorted = ['adopted', 'rejected', 'open'].flatMap((v) =>
    sortByTitle(entries.filter((e) => e.decision_status === v)),
  );
  const rows = sorted.map(
    (e) =>
      `| [${e.title}](entries/${e.name}.md) | ${e.category} | ${e.decision_status} | ${e.summary} | ${e.tags.join(', ')} |`,
  );
  return [
    '## By Decision Status',
    '',
    '| Item | Category | Status | Reason | Tags |',
    '|---|---|---|---|---|',
    ...rows,
  ].join('\n');
}

function renderByWorkflow(entries: EntryData[]): string {
  const groups = new Map<string, EntryData[]>();
  for (const e of entries) {
    const workflows = e.workflows.length > 0 ? e.workflows : ['General'];
    for (const w of workflows) {
      if (!groups.has(w)) groups.set(w, []);
      groups.get(w)!.push(e);
    }
  }

  const sortedKeys = [...groups.keys()].sort((a, b) => {
    if (a === 'General') return 1;
    if (b === 'General') return -1;
    return cmpRaw(a, b);
  });

  const sections: string[] = ['## By Workflow'];
  for (const key of sortedKeys) {
    sections.push('');
    sections.push(`### ${key}`);
    sections.push('');
    for (const e of sortByTitle(groups.get(key)!)) {
      sections.push(
        `- [${e.title}](entries/${e.name}.md) — ${e.decision_status} — ${e.summary}`,
      );
    }
  }
  return sections.join('\n');
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
      sections.push(
        `- [${e.title}](entries/${e.name}.md) — ${e.decision_status} — ${e.summary}`,
      );
    }
  }
  return sections.join('\n');
}
