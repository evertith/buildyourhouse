import contentDates from '@/lib/content-dates.json';
import { BLOG_POSTS } from '@/lib/blog-posts';

export const dynamic = 'force-static';

const SITE_URL = 'https://build-your-house.com';
const CONTENT_DATES = contentDates as Record<string, { published: string; modified: string }>;

function escapeXml(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

export async function GET() {
  const items = BLOG_POSTS.map((post) => {
    const path = `/blog/${post.slug}`;
    const dates = CONTENT_DATES[path];
    const pubDate = dates ? new Date(dates.published).toUTCString() : new Date().toUTCString();
    return `    <item>
      <title>${escapeXml(post.title)}</title>
      <link>${SITE_URL}${path}</link>
      <guid isPermaLink="true">${SITE_URL}${path}</guid>
      <description>${escapeXml(post.description)}</description>
      <pubDate>${pubDate}</pubDate>
    </item>`;
  }).join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Build Your House — Owner-Builder Blog</title>
    <link>${SITE_URL}/blog</link>
    <atom:link href="${SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
    <description>Field-tested advice for owner-builders: permits, subcontractors, budgets, and lessons from real builds.</description>
    <language>en-us</language>
${items}
  </channel>
</rss>
`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
}
