import contentDates from '@/lib/content-dates.json';
import { generateArticleSchema } from '@/lib/schema';

const SITE_URL = 'https://build-your-house.com';
const CONTENT_DATES = contentDates as Record<string, { published: string; modified: string }>;

interface ArticleSchemaProps {
  /** Route path, e.g. "/blog/first-30-days-as-owner-builder" */
  path: string;
  headline: string;
  description: string;
}

/**
 * Article JSON-LD for guide and blog pages. Dates come from git history via
 * src/lib/content-dates.json, so dateModified tracks real content updates.
 * Author is the site organization — the site is intentionally anonymous.
 */
export default function ArticleSchema({ path, headline, description }: ArticleSchemaProps) {
  const dates = CONTENT_DATES[path];
  const schema = generateArticleSchema({
    headline,
    description,
    image: `${SITE_URL}/og-image.jpg`,
    datePublished: dates?.published ?? '2025-11-17T00:00:00-05:00',
    dateModified: dates?.modified,
    author: {
      name: 'Build Your House',
      url: `${SITE_URL}/about`,
      type: 'Organization',
    },
    publisher: {
      name: 'Build Your House',
      logo: `${SITE_URL}/logo.png`,
    },
    url: `${SITE_URL}${path}`,
  });

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
}
