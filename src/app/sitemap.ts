import { MetadataRoute } from 'next';

export const dynamic = 'force-static';

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = 'https://build-your-house.com';

  // Main pages with high priority
  const mainPages = [
    {
      url: baseUrl,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'weekly' as const,
      priority: 1.0,
    },
    {
      url: `${baseUrl}/start-here`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/about`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    {
      url: `${baseUrl}/shop`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'weekly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/pricing`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'weekly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/contact`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
  ];

  // Blog section
  const blogPages = [
    {
      url: `${baseUrl}/blog`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'weekly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/blog/biggest-mistakes-owner-builders-make`,
      lastModified: new Date('2025-11-15'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/blog/first-30-days-as-owner-builder`,
      lastModified: new Date('2025-11-15'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/blog/how-to-choose-land-for-building`,
      lastModified: new Date('2025-11-15'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/blog/is-owner-building-right-recession`,
      lastModified: new Date('2025-11-15'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/blog/managing-construction-loan-as-owner-builder`,
      lastModified: new Date('2025-11-15'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/blog/tools-i-wish-i-bought-sooner`,
      lastModified: new Date('2025-11-15'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
  ];

  // Feasibility section
  const feasibilityPages = [
    {
      url: `${baseUrl}/feasibility/cost-savings-calculator`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/feasibility/is-it-right-for-you`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    {
      url: `${baseUrl}/feasibility/state-by-state-rules`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/feasibility/time-commitment`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
  ];

  // Calculators - high priority due to search opportunity
  const calculatorPages = [
    {
      url: `${baseUrl}/calculators/budget-tracker`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/calculators/material-estimator`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.9,
    },
    {
      url: `${baseUrl}/calculators/timeline-estimator`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.9,
    },
  ];

  // Permitting section
  const permittingPages = [
    {
      url: `${baseUrl}/permitting`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    {
      url: `${baseUrl}/permitting/common-permit-mistakes`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/permitting/permit-application-process`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/permitting/understanding-building-codes`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
    {
      url: `${baseUrl}/permitting/working-with-building-department`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    },
  ];

  // State guides - high priority traffic drivers
  const stateGuides = [
    'north-carolina', 'texas', 'florida', 'california', 'colorado',
    'washington', 'tennessee', 'georgia', 'arizona', 'virginia'
  ].map(state => ({
    url: `${baseUrl}/permitting/state-guides/${state}`,
    lastModified: new Date('2026-04-05'),
    changeFrequency: 'monthly' as const,
    priority: 0.8,
  }));

  // Planning section
  const planningPages = [
    'secure-land', 'house-plans', 'budget', 'financing', 'timeline'
  ].map(page => ({
    url: `${baseUrl}/planning/${page}`,
    lastModified: new Date('2026-04-05'),
    changeFrequency: 'monthly' as const,
    priority: 0.8,
  }));

  // Build phases
  const buildPhases = [
    'site-preparation', 'foundation', 'framing', 'roofing',
    'windows-and-doors', 'rough-in', 'electrical-rough-in', 'plumbing-rough-in',
    'hvac-installation', 'insulation', 'drywall', 'finish', 'interior-trim',
    'painting', 'flooring', 'kitchen-and-bath', 'final-finishes', 'landscaping'
  ].map(phase => ({
    url: `${baseUrl}/build-phases/${phase}`,
    lastModified: new Date('2026-04-05'),
    changeFrequency: 'monthly' as const,
    priority: 0.7,
  }));

  buildPhases.unshift({
    url: `${baseUrl}/build-phases`,
    lastModified: new Date('2026-04-05'),
    changeFrequency: 'monthly' as const,
    priority: 0.8,
  });

  // Move-in section
  const moveInPages = [
    'punch-list', 'certificate-of-occupancy', 'loan-conversion', 'moving-in'
  ].map(page => ({
    url: `${baseUrl}/move-in/${page}`,
    lastModified: new Date('2026-04-05'),
    changeFrequency: 'monthly' as const,
    priority: 0.7,
  }));

  // Inspections
  const inspectionPages = [
    {
      url: `${baseUrl}/inspections`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    ...['foundation-inspection', 'framing-inspection', 'rough-in-inspections',
      'insulation-inspection', 'final-inspection', 'common-inspection-failures'
    ].map(page => ({
      url: `${baseUrl}/inspections/${page}`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    })),
  ];

  // Subcontractors
  const subcontractorPages = [
    {
      url: `${baseUrl}/subcontractors`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    ...['finding-quality-subs', 'vetting-and-interviewing', 'getting-quotes',
      'contracts-and-agreements', 'managing-subs', 'payment-schedules',
      'dealing-with-problems', 'when-to-hire-vs-diy'
    ].map(page => ({
      url: `${baseUrl}/subcontractors/${page}`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    })),
  ];

  // Timing and Scheduling
  const timingPages = [
    {
      url: `${baseUrl}/timing-and-scheduling`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    ...['realistic-timeline', 'schedule-template', 'critical-path-method',
      'coordinating-trades', 'material-lead-times', 'weather-considerations',
      'common-delays'
    ].map(page => ({
      url: `${baseUrl}/timing-and-scheduling/${page}`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    })),
  ];

  // Tools and Equipment
  const toolsPages = [
    'essential-tools', 'safety-equipment', 'buy-vs-rent', 'tool-reviews'
  ].map(page => ({
    url: `${baseUrl}/tools-and-equipment/${page}`,
    lastModified: new Date('2026-04-05'),
    changeFrequency: 'monthly' as const,
    priority: 0.7,
  }));

  // Resources
  const resourcePages = [
    {
      url: `${baseUrl}/resources`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    ...['checklists', 'templates', 'glossary', 'recommended-tools'].map(page => ({
      url: `${baseUrl}/resources/${page}`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.6,
    })),
  ];

  // Newsletter
  const newsletterPages = [
    {
      url: `${baseUrl}/newsletter`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'monthly' as const,
      priority: 0.6,
    },
  ];

  // Legal pages
  const legalPages = [
    {
      url: `${baseUrl}/privacy`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'yearly' as const,
      priority: 0.3,
    },
    {
      url: `${baseUrl}/terms`,
      lastModified: new Date('2026-04-05'),
      changeFrequency: 'yearly' as const,
      priority: 0.3,
    },
  ];

  return [
    ...mainPages,
    ...blogPages,
    ...feasibilityPages,
    ...calculatorPages,
    ...planningPages,
    ...permittingPages,
    ...stateGuides,
    ...buildPhases,
    ...moveInPages,
    ...inspectionPages,
    ...subcontractorPages,
    ...timingPages,
    ...toolsPages,
    ...resourcePages,
    ...newsletterPages,
    ...legalPages,
  ];
}
