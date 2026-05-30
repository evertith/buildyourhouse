import Section from '@/components/Section';
import CalloutBox from '@/components/CalloutBox';
import Icon, { type IconName } from '@/components/Icon';
import Link from 'next/link';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Free Owner-Builder Calculators — Cost, Materials, Timeline & Budget',
  description: 'Free calculators for owner-builders: estimate material quantities and costs, your potential savings, a realistic build timeline, and track your budget.',
};

const CALCULATORS: { href: string; icon: IconName; title: string; desc: string; cta: string }[] = [
  { href: '/feasibility/cost-savings-calculator', icon: 'calculator', title: 'Cost Savings Calculator', desc: 'See how much you could realistically save by acting as your own general contractor on your project.', cta: 'Calculate Savings →' },
  { href: '/calculators/material-estimator', icon: 'ruler', title: 'Material Estimator', desc: 'Estimate quantities and costs for the major materials — framing, concrete, roofing, drywall, and more.', cta: 'Use Calculator →' },
  { href: '/calculators/timeline-estimator', icon: 'schedule', title: 'Timeline Estimator', desc: 'Plan a realistic build schedule and time commitment based on your home size and how much you DIY.', cta: 'Estimate Timeline →' },
  { href: '/calculators/budget-tracker', icon: 'tools', title: 'Budget Tracker', desc: 'Track expenses against your budget phase by phase so overruns surface early instead of at the end.', cta: 'Track Budget →' },
];

export default function CalculatorsPage() {
  return (
    <div className="content-container">
      <h1>Owner-Builder Calculators</h1>

      <p>
        Free, no-signup calculators to help you plan and price your build. Estimate your potential
        savings, material quantities, a realistic timeline, and keep your budget on track — each one
        is based on 15+ years of general contracting experience.
      </p>

      <CalloutBox type="tip" title="Where to start">

        New to this? Run the <Link href="/feasibility/cost-savings-calculator">Cost Savings Calculator</Link> first
        to gut-check whether owner-building pencils out for your project, then use the others to plan the details.

      </CalloutBox>

      <Section title="The Calculators">
        <div className="resource-grid">
          {CALCULATORS.map((c) => (
            <Link key={c.href} href={c.href} className="resource-card">
              <div className="resource-icon"><Icon name={c.icon} size={32} /></div>
              <h3>{c.title}</h3>
              <p>{c.desc}</p>
              <div className="resource-link">{c.cta}</div>
            </Link>
          ))}
        </div>
      </Section>

      <Section title="More Free Tools">
        <p>
          Looking for checklists, contract templates, or a glossary of construction terms? Browse the
          full <Link href="/resources">resource library</Link>, or jump straight to the
          owner-builder <Link href="/start-here">roadmap</Link> to see how these tools fit into the whole build.
        </p>
      </Section>
    </div>
  );
}
