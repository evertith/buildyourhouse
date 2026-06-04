// Convert raw GFM task-list checkboxes (`- [ ]`) into the <Checklist> component.
// The MDX setup has no remark-gfm, so `- [ ]` renders as literal "[ ] text".
// For each consecutive run of checkbox lines, emit a <Checklist>; if the run is
// immediately preceded by a bold lead-in (`**Title:**`), use it as the title and drop it.
// Usage: node scripts/checkboxes-to-checklist.mjs <file.mdx> [--apply]
import { readFileSync, writeFileSync } from 'node:fs';

const file = process.argv[2];
const APPLY = process.argv.includes('--apply');
if (!file) { console.error('pass a file path'); process.exit(1); }

const fileSlug = file.split('/').slice(-2, -1)[0] || 'page';
const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40);
const escItem = s => s.replace(/\\/g, '\\\\').replace(/'/g, "\\'");

const lines = readFileSync(file, 'utf8').split('\n');
const out = [];
const usedKeys = new Set();
let i = 0, converted = 0;

const isCheckbox = l => /^\s*-\s*\[ \]\s+/.test(l);

while (i < lines.length) {
  if (isCheckbox(lines[i])) {
    const items = [];
    while (i < lines.length && isCheckbox(lines[i])) {
      items.push(lines[i].replace(/^\s*-\s*\[ \]\s+/, '').trim());
      i++;
    }
    // look back past blanks for a bold lead-in to use as the title
    let title = null, k = out.length - 1;
    while (k >= 0 && out[k].trim() === '') k--;
    const m = k >= 0 ? out[k].match(/^\*\*(.+?):?\*\*$/) : null;
    if (m) { title = m[1].trim(); out.length = k; }      // drop the lead-in + trailing blanks
    if (out.length && out[out.length - 1].trim() !== '') out.push('');

    let key = `${fileSlug}-${title ? slug(title) : 'checklist'}`;
    let n = 1; while (usedKeys.has(key)) { n++; key = `${fileSlug}-${title ? slug(title) : 'checklist'}-${n}`; }
    usedKeys.add(key);

    out.push('<Checklist');
    if (title) out.push(`  title="${title.replace(/"/g, '&quot;')}"`);
    out.push(`  storageKey="${key}"`);
    out.push('  items={[');
    for (const it of items) out.push(`    '${escItem(it)}',`);
    out.push('  ]}');
    out.push('/>');
    converted++;
  } else {
    out.push(lines[i]); i++;
  }
}

const result = out.join('\n');
if (APPLY) { writeFileSync(file, result); console.log(`APPLIED: ${converted} checklist blocks in ${file}`); }
else {
  console.log(`DRY RUN: ${converted} checklist blocks would convert in ${file}`);
  const idx = result.indexOf('<Checklist');
  console.log('\n--- first converted block preview ---\n' + result.slice(idx, idx + 320));
}
