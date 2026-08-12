import Link from 'next/link';
import type { Metadata } from 'next';
import EmailCapture from '@/components/EmailCapture';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/permit-kits' },
  title: 'State Permit Kits for Owner-Builders — NC, GA, TX & VA',
  description:
    'State-specific owner-builder permit kits: the exemption walkthrough, permit application checklist, inspection sequence, and where-to-file directory — statute citations printed on the page. $34 per state.',
};

const KITS = [
  {
    href: '/shop/nc-permit-kit',
    state: 'North Carolina',
    hook: 'The owner exemption affidavit, the $40K lien-agent threshold, septic gating the permit, and the personally-present inspection rule.',
  },
  {
    href: '/shop/ga-permit-kit',
    state: 'Georgia',
    hook: 'The one-sale-per-24-months exemption trap, mandatory codes even in no-permit counties, and the two required performance tests.',
  },
  {
    href: '/shop/tx-permit-kit',
    state: 'Texas',
    hook: 'No state license or permit — and the traps that replace them: trade licensing, TCEQ septic, the energy code that applies anyway, coastal windstorm.',
  },
  {
    href: '/shop/va-permit-kit',
    state: 'Virginia',
    hook: 'The § 54.1-1101 exemption, the lien agent that protects you, VDH septic shot clocks, and the VDOT driveway permit almost nobody expects.',
  },
];

export default function PermitKitsPage() {
  return (
    <div className="content-container">
      <div style={{ padding: 'var(--space-8) 0 var(--space-10)' }}>
        <p className="bp-eyebrow">State permit kits · $34 each</p>
        <h1>Your State&apos;s Permitting Rules, as a Working Kit</h1>
        <p style={{ maxWidth: 'var(--width-content)' }}>
          Each kit is the same six documents, built for one state and verified against
          that state&apos;s statutes and agencies: the owner-builder exemption walkthrough,
          the permit application checklist, the inspection sequence, a where-to-file
          directory, and a forms index — with the citations printed on the page, so a
          permit clerk can check your work.
        </p>

        <div className="resource-grid">
          {KITS.map((k) => (
            <Link key={k.href} href={k.href} className="resource-card">
              <h3>{k.state}</h3>
              <p>{k.hook}</p>
              <div className="resource-link">See the {k.state} kit — $34 →</div>
            </Link>
          ))}
        </div>

        <div style={{ marginTop: 'var(--space-10)', maxWidth: 'var(--width-content)' }}>
          <EmailCapture
            title="Building in another state?"
            description="Tell us where — the states we build kits for next come straight from these requests. You'll get the owner-builder newsletter, and a note when your state's kit ships."
            buttonText="Request my state"
            placeholderText="you@example.com"
          />
        </div>
      </div>
    </div>
  );
}
