import type { Metadata } from 'next';
import PricingTable from '@/components/PricingTable';
import ChatPreview from '@/components/ChatPreview';
import { generateFAQSchema, generateBreadcrumbSchema } from '@/lib/schema';

export const metadata: Metadata = {
  title: 'Pricing — Free Guides, Job Site Binder & Builder Pro with Reed AI',
  description:
    'Choose your owner-builder plan: free guides and calculators, the $97 Job Site Binder, or Builder Pro ($20/mo) with Reed AI general contractor. Cancel anytime.',
};

const faqs = [
  {
    question: 'What is Reed?',
    answer:
      'Reed is an AI general contractor built specifically for owner-builders. He draws on 15+ years of custom home building experience to answer your construction questions, help with code compliance, estimate materials, and prep you for inspections — available 24/7.',
  },
  {
    question: 'Can I cancel Builder Pro anytime?',
    answer:
      'Yes. Cancel anytime from your account. You keep access through the end of your billing period. No contracts, no cancellation fees.',
  },
  {
    question: 'Do I get the Job Site Binder with Builder Pro?',
    answer:
      'Yes! Builder Pro includes full access to the 229-page Job Site Binder system plus all future templates and checklists we release.',
  },
  {
    question: 'What if I already bought the Job Site Binder?',
    answer:
      "Email us and we'll credit your $97 binder purchase toward Builder Pro. We take care of existing customers.",
  },
  {
    question: 'Is the free content really free?',
    answer:
      'Absolutely. All guides, articles, state rules, and calculators are free forever. We believe every owner-builder deserves access to good information.',
  },
];

const breadcrumbs = [
  { name: 'Home', item: 'https://build-your-house.com' },
  { name: 'Pricing', item: 'https://build-your-house.com/pricing' },
];

export default function PricingPage() {
  const faqSchema = generateFAQSchema(faqs);
  const breadcrumbSchema = generateBreadcrumbSchema(breadcrumbs);

  return (
    <div className="content-container">
      {/* Structured Data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@graph': [faqSchema, breadcrumbSchema],
          }),
        }}
      />

      {/* Hero */}
      <section
        style={{
          textAlign: 'center',
          padding: 'var(--space-16, 4rem) 0 var(--space-8, 2rem)',
        }}
      >
        <h1
          style={{
            fontSize: 'var(--text-4xl, 2.5rem)',
            marginBottom: 'var(--space-4, 1rem)',
            lineHeight: 'var(--leading-tight, 1.2)',
          }}
        >
          Every Owner-Builder Needs a General Contractor in Their Pocket
        </h1>
        <p
          style={{
            fontSize: 'var(--text-xl, 1.25rem)',
            color: 'var(--text-secondary)',
            maxWidth: '700px',
            margin: '0 auto',
            lineHeight: 'var(--leading-relaxed, 1.7)',
          }}
        >
          Free guides to get started. The Job Site Binder to stay organized.
          Builder Pro with Reed AI to build with confidence.
        </p>
      </section>

      {/* Pricing Table */}
      <section style={{ padding: 'var(--space-8, 2rem) 0' }}>
        <PricingTable />
      </section>

      {/* Reed Demo Section */}
      <section
        style={{
          padding: 'var(--space-16, 4rem) 0',
          backgroundColor: 'var(--surface-warm, #f5f0eb)',
          margin: '0 calc(-1 * var(--space-8, 2rem))',
          paddingLeft: 'var(--space-8, 2rem)',
          paddingRight: 'var(--space-8, 2rem)',
        }}
      >
        <div style={{ textAlign: 'center', marginBottom: 'var(--space-8, 2rem)' }}>
          <h2 style={{ fontSize: 'var(--text-3xl, 2rem)', marginBottom: 'var(--space-4, 1rem)' }}>
            Meet Reed — Your AI General Contractor
          </h2>
          <p
            style={{
              fontSize: 'var(--text-lg, 1.125rem)',
              color: 'var(--text-secondary)',
              maxWidth: '600px',
              margin: '0 auto',
            }}
          >
            Ask Reed anything about your build. Here&apos;s a sample conversation:
          </p>
        </div>
        <ChatPreview />
      </section>

      {/* FAQ Section */}
      <section style={{ padding: 'var(--space-16, 4rem) 0', maxWidth: '800px', margin: '0 auto' }}>
        <h2
          style={{
            fontSize: 'var(--text-3xl, 2rem)',
            textAlign: 'center',
            marginBottom: 'var(--space-8, 2rem)',
          }}
        >
          Frequently Asked Questions
        </h2>
        <div className="faq-list">
          {faqs.map((faq, i) => (
            <div key={i} className="faq-item">
              <h3>{faq.question}</h3>
              <p>{faq.answer}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Final CTA */}
      <section
        style={{
          textAlign: 'center',
          padding: 'var(--space-12, 3rem)',
          backgroundColor: 'var(--surface-warm, #f5f0eb)',
          borderRadius: '12px',
          marginBottom: 'var(--space-16, 4rem)',
        }}
      >
        <h2 style={{ fontSize: 'var(--text-2xl, 1.75rem)' }}>Ready to Build With Confidence?</h2>
        <p
          style={{
            fontSize: 'var(--text-lg, 1.125rem)',
            color: 'var(--text-secondary)',
            marginBottom: 'var(--space-6, 1.5rem)',
          }}
        >
          Join hundreds of owner-builders who are saving $50K-$150K+ by acting as their own GC.
        </p>
        <a
          href="/start-here"
          className="button"
          style={{ marginRight: '12px' }}
        >
          Start for Free
        </a>
      </section>
    </div>
  );
}
