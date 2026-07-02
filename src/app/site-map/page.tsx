import type { Metadata } from 'next';
import Link from 'next/link';
import contentDates from '@/lib/content-dates.json';
import { labelForSegment } from '@/lib/route-labels';

export const metadata: Metadata = {
  title: 'Site Map — Every Guide, Calculator, and Resource',
  description:
    'A complete index of every owner-builder guide on Build Your House: all 50 state permit guides, 18 build phases, calculators, checklists, and more.',
  alternates: { canonical: '/site-map' },
};

const SECTION_ORDER = [
  'start-here',
  'feasibility',
  'planning',
  'permitting',
  'subcontractors',
  'timing-and-scheduling',
  'build-phases',
  'inspections',
  'move-in',
  'calculators',
  'tools-and-equipment',
  'resources',
  'blog',
  'shop',
  'newsletter',
  'about',
  'contact',
];

const HIDDEN_ROUTES = new Set(['/shop/success', '/privacy', '/terms', '/site-map']);

function titleForRoute(route: string): string {
  const segments = route.split('/').filter(Boolean);
  return segments.map(labelForSegment).join(' — ');
}

export default function SiteMapPage() {
  const routes = Object.keys(contentDates)
    .filter((route) => route !== '/' && !HIDDEN_ROUTES.has(route));

  const sections = new Map<string, string[]>();
  for (const route of routes) {
    const top = route.split('/')[1];
    if (!sections.has(top)) sections.set(top, []);
    sections.get(top)!.push(route);
  }

  const orderedSections = [
    ...SECTION_ORDER.filter((section) => sections.has(section)),
    ...[...sections.keys()].filter((section) => !SECTION_ORDER.includes(section)).sort(),
  ];

  return (
    <div className="content-container">
      <h1>Site Map</h1>
      <p>
        Every guide, calculator, and resource on the site. Not sure where to begin?{' '}
        <Link href="/start-here">Start here</Link>.
      </p>

      {orderedSections.map((section) => {
        const sectionRoutes = sections.get(section)!.sort();
        return (
          <section key={section}>
            <h2>{labelForSegment(section)}</h2>
            <ul>
              {sectionRoutes.map((route) => (
                <li key={route}>
                  <Link href={route}>
                    {titleForRoute(route.replace(`/${section}`, '')) || labelForSegment(section)}
                  </Link>
                </li>
              ))}
            </ul>
          </section>
        );
      })}
    </div>
  );
}
