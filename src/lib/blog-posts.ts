/**
 * Registry of blog posts, kept in sync with the metadata exports of the
 * page.mdx files under src/app/blog. Used by the RSS feed. Add new posts
 * here when publishing.
 */

export interface BlogPost {
  slug: string;
  title: string;
  description: string;
}

export const BLOG_POSTS: BlogPost[] = [
  {
    slug: 'biggest-mistakes-owner-builders-make',
    title: '10 Biggest Owner-Builder Mistakes — And What They Cost',
    description:
      'The top 10 mistakes owner-builders make with real dollar amounts. Why they happen and exactly how to avoid each one.',
  },
  {
    slug: 'first-30-days-as-owner-builder',
    title: 'Your First 30 Days as an Owner-Builder — Critical Decisions to Make',
    description:
      'What to do in your first month as an owner-builder. The decisions that set up your entire project for success — or failure.',
  },
  {
    slug: 'how-to-choose-land-for-building',
    title: 'How to Choose Land for Building — Due Diligence Checklist',
    description:
      'What to check before buying land. Hidden costs, red flags, and the due diligence steps that prevent a $50,000 mistake.',
  },
  {
    slug: 'is-owner-building-right-recession',
    title: 'Building During a Recession — Smart Move or Bad Timing?',
    description:
      'Should you build during economic uncertainty? Interest rates, material costs, labor availability, and why life timing sometimes trumps market timing.',
  },
  {
    slug: 'managing-construction-loan-as-owner-builder',
    title: 'Managing Your Construction Loan — Draw Schedules & Documentation',
    description:
      'How construction loan draws work for owner-builders. Getting approved, managing the draw schedule, required documentation, and common pitfalls.',
  },
  {
    slug: 'tools-i-wish-i-bought-sooner',
    title: 'Tools I Wish I Bought Sooner — Owner-Builder ROI Stories',
    description:
      'The tools that paid for themselves on the job site. Real ROI calculations, what to buy vs. rent, and the purchases other owner-builders swear by.',
  },
];
