import type { Metadata } from 'next';
import Link from 'next/link';
import Section from '@/components/Section';

export const metadata: Metadata = {
  title: 'AI Build Advisor — Your Personal Construction Expert',
  description: 'Get personalized construction advice from an AI trained on 15+ years of general contracting experience. State-specific answers, project memory, and guidance for every phase of your build.',
};

export default function AdvisorPage() {
  return (
    <div className="content-container">
      <Section spacing="large">
        <div style={{ textAlign: 'center', maxWidth: '700px', margin: '0 auto' }}>
          <h1 style={{ fontSize: 'var(--text-3xl)', lineHeight: 'var(--leading-tight)', marginBottom: 'var(--space-3)' }}>
            Your Personal AI Construction Advisor
          </h1>
          <p style={{ fontSize: 'var(--text-lg)', color: 'var(--text-secondary)', lineHeight: 'var(--leading-relaxed)', marginBottom: 'var(--space-6)' }}>
            Like having a retired general contractor on speed dial. Ask anything about your build and get specific, actionable advice tailored to your state, your phase, and your project.
          </p>
          <div style={{ display: 'flex', gap: 'var(--space-2)', justifyContent: 'center', flexWrap: 'wrap' }}>
            <Link
              href="/advisor/signup"
              className="button button-large"
              style={{ fontSize: 'var(--text-lg)', padding: 'var(--space-3) var(--space-8)' }}
            >
              Try Free — 5 Questions/Month
            </Link>
          </div>
        </div>
      </Section>

      <Section title="How It Works" spacing="large" background="warm">
        <div className="how-it-works-grid">
          <div className="step-card">
            <div className="step-number">1</div>
            <h3>Tell Us About Your Build</h3>
            <p>
              Your state, current phase, square footage, and approach.
              This becomes the context for every conversation.
            </p>
          </div>
          <div className="step-card">
            <div className="step-number">2</div>
            <h3>Ask Anything</h3>
            <p>
              Permits, inspections, subcontractors, costs, code questions,
              scheduling — just like asking a real GC.
            </p>
          </div>
          <div className="step-card">
            <div className="step-number">3</div>
            <h3>Get Specific Answers</h3>
            <p>
              Not generic advice — answers specific to your state, your county,
              your phase, and your project history.
            </p>
          </div>
          <div className="step-card">
            <div className="step-number">4</div>
            <h3>It Remembers Your Build</h3>
            <p>
              Come back next week and it knows your foundation passed inspection,
              your electrician is scheduled, and your permit expires in June.
            </p>
          </div>
        </div>
      </Section>

      <Section title="What You Can Ask" spacing="large">
        <div style={{ maxWidth: '700px', margin: '0 auto' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-2)' }}>
            {[
              '"Do I need a separate mechanical permit in Wake County, NC?"',
              '"My framing inspector failed me for anchor bolt spacing. What do I do?"',
              '"What should I budget for rough-in trades on a 2,000 sq ft ranch?"',
              '"How do I sequence my subs so nobody is waiting on someone else?"',
              '"Is spray foam worth the extra cost in my climate zone?"',
              '"What questions should I ask when interviewing electricians?"',
            ].map((q, i) => (
              <div key={i} style={{
                padding: 'var(--space-2)',
                background: 'var(--bg-secondary)',
                borderRadius: '10px',
                fontSize: 'var(--text-sm)',
                color: 'var(--text-secondary)',
                fontStyle: 'italic',
                lineHeight: '1.5',
              }}>
                {q}
              </div>
            ))}
          </div>
        </div>
      </Section>

      <Section title="Simple Pricing" spacing="large" background="warm">
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 'var(--space-3)', maxWidth: '800px', margin: '0 auto' }}>
          <div style={{ background: 'white', borderRadius: '12px', padding: 'var(--space-4)', textAlign: 'center', border: '1px solid var(--bg-tertiary)' }}>
            <h3 style={{ marginBottom: 'var(--space-1)' }}>Free</h3>
            <div style={{ fontSize: 'var(--text-2xl)', fontWeight: '800', color: 'var(--accent-primary)', margin: 'var(--space-1) 0' }}>$0</div>
            <p style={{ color: 'var(--text-secondary)', fontSize: 'var(--text-sm)', marginBottom: 'var(--space-3)' }}>5 questions/month</p>
            <Link href="/advisor/signup" style={{ color: 'var(--link-color)', fontWeight: '600', textDecoration: 'none' }}>Get Started</Link>
          </div>
          <div style={{ background: 'white', borderRadius: '12px', padding: 'var(--space-4)', textAlign: 'center', border: '2px solid var(--accent-primary)', position: 'relative' }}>
            <div style={{ position: 'absolute', top: '-12px', left: '50%', transform: 'translateX(-50%)', background: 'var(--accent-primary)', color: 'white', padding: '4px 16px', borderRadius: '20px', fontSize: '12px', fontWeight: '600' }}>MOST POPULAR</div>
            <h3 style={{ marginBottom: 'var(--space-1)' }}>Starter</h3>
            <div style={{ fontSize: 'var(--text-2xl)', fontWeight: '800', color: 'var(--accent-primary)', margin: 'var(--space-1) 0' }}>$19<span style={{ fontSize: 'var(--text-sm)', fontWeight: '400', color: 'var(--text-secondary)' }}>/mo</span></div>
            <p style={{ color: 'var(--text-secondary)', fontSize: 'var(--text-sm)', marginBottom: 'var(--space-3)' }}>50 questions/month</p>
            <Link href="/advisor/signup" className="button" style={{ display: 'inline-block' }}>Get Starter</Link>
          </div>
          <div style={{ background: 'white', borderRadius: '12px', padding: 'var(--space-4)', textAlign: 'center', border: '1px solid var(--bg-tertiary)' }}>
            <h3 style={{ marginBottom: 'var(--space-1)' }}>Pro</h3>
            <div style={{ fontSize: 'var(--text-2xl)', fontWeight: '800', color: 'var(--accent-primary)', margin: 'var(--space-1) 0' }}>$29<span style={{ fontSize: 'var(--text-sm)', fontWeight: '400', color: 'var(--text-secondary)' }}>/mo</span></div>
            <p style={{ color: 'var(--text-secondary)', fontSize: 'var(--text-sm)', marginBottom: 'var(--space-3)' }}>200 questions/month</p>
            <Link href="/advisor/signup" style={{ color: 'var(--link-color)', fontWeight: '600', textDecoration: 'none' }}>Get Pro</Link>
          </div>
        </div>
        <p style={{ textAlign: 'center', color: 'var(--text-secondary)', marginTop: 'var(--space-3)', fontSize: 'var(--text-sm)' }}>
          Cancel anytime. No contracts. Your data is always yours.
        </p>
      </Section>

      <Section spacing="large">
        <div style={{ textAlign: 'center', maxWidth: '600px', margin: '0 auto' }}>
          <h2 style={{ marginBottom: 'var(--space-2)' }}>Ready to Build With Confidence?</h2>
          <p style={{ color: 'var(--text-secondary)', marginBottom: 'var(--space-4)', lineHeight: '1.6' }}>
            Stop Googling construction questions at 10pm. Get answers from an AI advisor that knows
            your project, your state, and your phase — in seconds.
          </p>
          <Link
            href="/advisor/signup"
            className="button button-large"
            style={{ fontSize: 'var(--text-lg)', padding: 'var(--space-3) var(--space-8)' }}
          >
            Create Free Account
          </Link>
        </div>
      </Section>
    </div>
  );
}
