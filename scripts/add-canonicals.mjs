// One-off: inject self-referencing `alternates.canonical` into every page's
// static `export const metadata` object, derived from the file's route.
// Usage: node scripts/add-canonicals.mjs [--apply]
import { readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';

const APPLY = process.argv.includes('--apply');
const files = execSync("find src/app \\( -name 'page.mdx' -o -name 'page.tsx' \\)")
  .toString().trim().split('\n').filter(Boolean);

const routeFor = (f) => {
  let r = f.replace(/^src\/app/, '').replace(/\/page\.(mdx|tsx)$/, '');
  return r === '' ? '/' : r;
};

// matches `export const metadata = {` or `export const metadata: Metadata = {`
const META_OPEN = /export const metadata(\s*:\s*Metadata)?\s*=\s*\{/;

let changed = 0, skipped = [];
for (const f of files) {
  const src = readFileSync(f, 'utf8');
  if (/canonical/.test(src)) { skipped.push([f, 'already has canonical']); continue; }
  if (!META_OPEN.test(src)) { skipped.push([f, 'no static metadata export']); continue; }
  const route = routeFor(f);
  const out = src.replace(META_OPEN, (m) => `${m}\n  alternates: { canonical: '${route}' },`);
  if (out === src) { skipped.push([f, 'no-op (regex)']); continue; }
  changed++;
  if (APPLY) writeFileSync(f, out);
  else if (changed <= 3) console.log(`--- ${f}  ->  canonical '${route}'\n` + out.split('\n').slice(0, 4).join('\n'));
}
console.log(`\n${APPLY ? 'APPLIED' : 'DRY RUN'}: ${changed} files would change, ${skipped.length} skipped`);
for (const [f, why] of skipped) console.log(`  skip: ${f}  (${why})`);
