// packages/catalog-mcp/src/core/lint.ts
import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { entrySchema } from './schema.js';
import { parseFrontmatter, serializeFrontmatter } from './frontmatter.js';
import { catalogPaths } from './config.js';
import { loadTaxonomy, buildIndex, canonicalForTag, unclassifiedTags, type TaxonomyIndex } from './taxonomy.js';

interface LintResult {
  errors: string[];
  warnings: string[];
  missingCanonical: string[];
}

interface LintFileResult extends LintResult {
  file: string;
}

const RETIRED_FIELDS: Record<string, string> = {
  verdict: 'decision_status',
  verdict_reason: 'summary',
  status: '(removed)',
  decision_status: '(removed)',
  workflows: '(removed)',
  install: '(removed)',
  supersedes: '(removed)',
};

// catalog/template.md body sections, in order. `## How to use it` and `## Where to look next`
// are the only two allowed to be absent, and only when the entry has no `url` (WK-0099 OR, the
// overseer's `## Where to look next` decision).
const TEMPLATE_SECTIONS = [
  'What it is',
  'How it works',
  'How to use it',
  'Evaluation and limits',
  'Context from the source',
  'Where to look next',
  'Related',
  'Security',
] as const;
const OPTIONAL_WITHOUT_URL = new Set(['How to use it', 'Where to look next']);

// Headings from the pre-WK-0099 recipe that carried a verdict ("## Assessment", "## What to
// adopt") or restated the catalog's old mechanical-details framing ("## Differentiators",
// "## Mechanical details") — the catalog records facts, not opinions (WK-0099, WK-0051 precedent).
const REJECTED_HEADINGS = ['Assessment', 'What to adopt', 'Differentiators', 'Mechanical details'];

// Entries reviewed on or after this date were written (or rewritten) under the WK-0099 template;
// older entries predate it and fail these rules by design until the reprocess rewrites them —
// so the rules are warnings there, not errors, and `lint` stays usable on the live catalog.
const TEMPLATE_CUTOVER = '2026-10-31';

// Provenance (WK-0099): a source traceable to a specific post/page must carry the link it came
// in on. "web" (a bare link) and "unknown" (legacy, no recorded provenance) are exempt.
const SOURCE_REQUIRES_SOURCE_URL = new Set(['instagram', 'reddit', 'x', 'text']);

// WK-0097 OR-2: the operator's understanding goes into the entry itself, never a link to a
// private capture file — those paths are not even readable by anyone outside this repo.
const LOCAL_CAPTURE_PATTERNS = ['catalog/sources/', 'toolkit-workbench/'];

function headingLines(body: string): { text: string; index: number }[] {
  const lines = body.split('\n');
  const out: { text: string; index: number }[] = [];
  lines.forEach((line, index) => {
    const m = line.match(/^##\s+(.+?)\s*$/);
    if (m) out.push({ text: m[1], index });
  });
  return out;
}

function sectionContent(body: string, heading: string): string[] {
  const lines = body.split('\n');
  const headingRe = new RegExp(`^##\\s+${heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\s*$`);
  let start = -1;
  for (let i = 0; i < lines.length; i++) {
    if (headingRe.test(lines[i])) {
      start = i + 1;
      break;
    }
  }
  if (start === -1) return [];
  let end = lines.length;
  for (let i = start; i < lines.length; i++) {
    if (/^##\s+/.test(lines[i])) {
      end = i;
      break;
    }
  }
  return lines.slice(start, end).filter((l) => l.trim().length > 0);
}

// A line is "- <what you learn there> — <URL or repo path>" (WK-0099 overseer decision): accept
// an http(s) URL anywhere on the line, or a repo-relative path token (has a "/" and no spaces).
function hasUrlOrPath(line: string): boolean {
  if (/https?:\/\/\S+/.test(line)) return true;
  return /(?:^|\s)[\w.-]+(?:\/[\w.-]+)+(?:\s|$)/.test(line);
}

const EMPTY_TAX_INDEX: TaxonomyIndex = buildIndex({ canonical: {} });

const BARE_BLOCK_SCALAR_INDICATORS = new Set(['>', '>-', '>+', '|', '|-', '|+']);

// The old hand-rolled YAML parser silently kept the block-scalar header as the
// value instead of folding the continuation lines, so a corrupted field reads
// back as exactly one of these indicators (see WK-0070).
function findBareBlockScalars(value: unknown, path: string, out: string[]): void {
  if (typeof value === 'string') {
    if (BARE_BLOCK_SCALAR_INDICATORS.has(value)) out.push(path);
  } else if (Array.isArray(value)) {
    value.forEach((v, i) => findBareBlockScalars(v, `${path}[${i}]`, out));
  } else if (value && typeof value === 'object') {
    for (const [k, v] of Object.entries(value as Record<string, unknown>)) {
      findBareBlockScalars(v, path ? `${path}.${k}` : k, out);
    }
  }
}

export function lintEntry(
  filename: string,
  frontmatter: Record<string, unknown>,
  body: string,
  taxIndex: TaxonomyIndex = EMPTY_TAX_INDEX,
): LintResult {
  const errors: string[] = [];
  const warnings: string[] = [];
  const missingCanonical: string[] = [];

  // Retired-field detection — a friendly message ahead of the generic strict error.
  for (const [retired, target] of Object.entries(RETIRED_FIELDS)) {
    if (retired in frontmatter) {
      errors.push(`retired field "${retired}" — migrate to ${target}`);
    }
  }

  const bareBlockScalarPaths: string[] = [];
  findBareBlockScalars(frontmatter, '', bareBlockScalarPaths);
  for (const p of bareBlockScalarPaths) {
    errors.push(`${p}: bare block-scalar indicator — a YAML parser bug can leave this instead of the real text`);
  }

  const result = entrySchema.safeParse(frontmatter);
  if (!result.success) {
    for (const issue of result.error.issues) {
      errors.push(`${issue.path.join('.')}: ${issue.message}`);
    }
  }

  if (frontmatter.name && frontmatter.name !== filename) {
    errors.push(`name "${frontmatter.name}" does not match filename "${filename}"`);
  }

  if (!frontmatter.acquired) {
    warnings.push('missing acquired field (migration: backfill from git log)');
  }

  // Provenance (WK-0099): instagram/reddit/x/text sources name a specific post or page, so the
  // link it came in on must be recorded, not just implied by the derived source value.
  const source = frontmatter.source as string | undefined;
  if (source && SOURCE_REQUIRES_SOURCE_URL.has(source) && !frontmatter.source_url) {
    errors.push(`source "${source}" requires source_url (the link this entry's content came in on)`);
  }

  // WK-0097 OR-2: never a link to a private capture file — the understanding goes into the
  // entry itself.
  for (const pattern of LOCAL_CAPTURE_PATTERNS) {
    if (body.includes(pattern)) {
      errors.push(`body links to a local capture path ("${pattern}") — put the understanding in the entry, not a link to the capture`);
    }
  }

  // Body-section rules (template order, presence, rejected headings, Where-to-look-next line
  // shape): errors once an entry is reviewed under the template (TEMPLATE_CUTOVER), warnings
  // before, since the live catalog predates the template and the reprocess rewrites it.
  const reviewed = frontmatter.reviewed as string | undefined;
  const sectionIsError = Boolean(reviewed && reviewed >= TEMPLATE_CUTOVER);
  const sectionIssues: string[] = [];
  const hasUrl = Boolean(frontmatter.url);
  const headings = headingLines(body);
  const presentTemplateSections = headings
    .map((h) => h.text)
    .filter((t): t is (typeof TEMPLATE_SECTIONS)[number] =>
      (TEMPLATE_SECTIONS as readonly string[]).includes(t),
    );

  for (const section of TEMPLATE_SECTIONS) {
    if (OPTIONAL_WITHOUT_URL.has(section) && !hasUrl) continue;
    if (!presentTemplateSections.includes(section)) {
      sectionIssues.push(`missing required section "## ${section}"`);
    }
  }

  const presentIndices = presentTemplateSections.map((s) => TEMPLATE_SECTIONS.indexOf(s));
  for (let i = 1; i < presentIndices.length; i++) {
    if (presentIndices[i] < presentIndices[i - 1]) {
      sectionIssues.push('body sections are out of template order');
      break;
    }
  }

  for (const { text } of headings) {
    if (REJECTED_HEADINGS.includes(text)) {
      sectionIssues.push(`rejected heading "## ${text}" — the catalog records facts, not verdicts`);
    }
  }

  if (presentTemplateSections.includes('Where to look next')) {
    for (const line of sectionContent(body, 'Where to look next')) {
      if (!hasUrlOrPath(line)) {
        sectionIssues.push(`"## Where to look next" line carries no URL or repo path: "${line.trim()}"`);
      }
    }
  }

  for (const issue of sectionIssues) {
    (sectionIsError ? errors : warnings).push(issue);
  }

  // Taxonomy audit: an alias tag should also carry its canonical umbrella.
  const tags = (frontmatter.tags as string[]) ?? [];
  for (const tag of tags) {
    const c = canonicalForTag(tag, taxIndex);
    if (c && !tags.includes(c) && !missingCanonical.includes(c)) {
      warnings.push(`tag "${tag}" should also carry canonical "${c}"`);
      missingCanonical.push(c);
    }
  }

  return { errors, warnings, missingCanonical };
}

interface LintOptions {
  dir: string;
  files?: string[];
  fix?: boolean;
}

interface TaxonomySummary {
  aliasWithoutCanonical: number;
  unclassified: string[];
}

interface LintRunResult {
  results: LintFileResult[];
  taxonomy: TaxonomySummary;
}

export async function lint(options: LintOptions): Promise<LintRunResult> {
  const paths = catalogPaths(options.dir);
  const taxIndex = buildIndex(await loadTaxonomy(options.dir));
  let files = options.files;
  if (!files) {
    const allFiles = await readdir(paths.entries);
    files = allFiles.filter((f) => f.endsWith('.md'));
  }

  const results: LintFileResult[] = [];
  let aliasWithoutCanonical = 0;
  const unclassifiedSet = new Set<string>();

  for (const file of files) {
    const filePath = path.join(paths.entries, file);
    const content = await readFile(filePath, 'utf-8');
    const name = file.replace('.md', '');

    try {
      const parsed = parseFrontmatter(content);
      const result = lintEntry(name, parsed.frontmatter, parsed.body, taxIndex);

      if (options.fix && (result.errors.length > 0 || result.missingCanonical.length > 0)) {
        const fixed = applyFixes(parsed.frontmatter, result.missingCanonical);
        const newContent = serializeFrontmatter(fixed, parsed.body);
        await writeFile(filePath, newContent, 'utf-8');
      }

      if (result.missingCanonical.length > 0) aliasWithoutCanonical++;
      const tags = (parsed.frontmatter.tags as string[]) ?? [];
      for (const t of unclassifiedTags(tags, taxIndex)) unclassifiedSet.add(t);

      results.push({ file, ...result });
    } catch (err) {
      results.push({ file, errors: [`Parse error: ${err}`], warnings: [], missingCanonical: [] });
    }
  }

  return {
    results,
    taxonomy: { aliasWithoutCanonical, unclassified: [...unclassifiedSet].sort() },
  };
}

function applyFixes(
  fm: Record<string, unknown>,
  missingCanonical: string[] = [],
): Record<string, unknown> {
  const fixed = { ...fm };
  if (fixed.url === '') delete fixed.url;
  if (fixed.tags && !Array.isArray(fixed.tags)) fixed.tags = [];
  if (fixed.overlaps && !Array.isArray(fixed.overlaps)) fixed.overlaps = [];
  if (fixed.security_flags && !Array.isArray(fixed.security_flags)) fixed.security_flags = [];
  // Append missing canonical umbrella tags (dedup, preserve order).
  if (missingCanonical.length > 0) {
    const tags = Array.isArray(fixed.tags) ? [...(fixed.tags as string[])] : [];
    for (const c of missingCanonical) if (!tags.includes(c)) tags.push(c);
    fixed.tags = tags;
  }
  return fixed;
}
