#!/usr/bin/env node
/**
 * Generates src/lib/content-dates.json: { "/route": { published, modified } }
 * from git history for every page file under src/app. Runs as `prebuild` so
 * sitemap lastmods, Article schema dates, and the RSS feed reflect real
 * per-page history instead of the build timestamp.
 *
 * One `git log` pass over the whole history: first time a page file appears
 * = published, last commit touching it = modified.
 */
import { execSync } from 'node:child_process';
import { existsSync, writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');

const PAGE_FILE = /^src\/app\/(.*?)\/?page\.(mdx|tsx)$/;

// CI deploys (Cloudflare Pages) may shallow-clone; truncated history would
// produce wrong published dates. Keep the committed JSON in that case.
try {
  const shallow = execSync('git rev-parse --is-shallow-repository', {
    cwd: repoRoot,
    encoding: 'utf8',
  }).trim();
  if (shallow === 'true') {
    console.log('content-dates: shallow clone detected, keeping committed content-dates.json');
    process.exit(0);
  }
} catch {
  console.log('content-dates: git unavailable, keeping committed content-dates.json');
  process.exit(0);
}

function routeFor(file) {
  const match = file.match(PAGE_FILE);
  if (!match) return null;
  return match[1] === '' ? '/' : `/${match[1]}`;
}

// --name-only with a sentinel-prefixed date line per commit, oldest first.
const log = execSync('git log --reverse --format=":::%aI" --name-only', {
  cwd: repoRoot,
  encoding: 'utf8',
  maxBuffer: 256 * 1024 * 1024,
});

const dates = {};
let currentDate = null;
for (const line of log.split('\n')) {
  if (line.startsWith(':::')) {
    currentDate = line.slice(3).trim();
    continue;
  }
  const file = line.trim();
  const route = routeFor(file);
  if (!route || !currentDate) continue;
  // Skip routes whose page file no longer exists (deleted sections live on in history).
  if (!dates[route] && !existsSync(resolve(repoRoot, file))) continue;
  if (!dates[route]) {
    dates[route] = { published: currentDate, modified: currentDate };
  } else {
    dates[route].modified = currentDate;
  }
}

const outPath = resolve(repoRoot, 'src/lib/content-dates.json');
const sorted = Object.fromEntries(
  Object.entries(dates).sort(([a], [b]) => a.localeCompare(b))
);
writeFileSync(outPath, `${JSON.stringify(sorted, null, 2)}\n`);
console.log(`content-dates: wrote ${Object.keys(sorted).length} routes to ${outPath}`);
