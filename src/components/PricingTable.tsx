'use client';

import styles from '@/styles/PricingTable.module.css';

const STRIPE_BINDER_URL = 'https://buy.stripe.com/5kQ28racn54z0ReeZ5fAc00';
const STRIPE_SUBSCRIPTION_URL = process.env.NEXT_PUBLIC_STRIPE_SUBSCRIPTION_URL || '#';

interface PricingTier {
  name: string;
  price: string;
  period: string;
  description: string;
  features: string[];
  cta: string;
  href: string;
  highlighted?: boolean;
}

const tiers: PricingTier[] = [
  {
    name: 'Free',
    price: '$0',
    period: 'forever',
    description: 'Everything you need to start planning your owner-builder project.',
    features: [
      'All guides and articles',
      'Basic calculators (cost, timeline, materials)',
      'State-by-state owner-builder rules',
      'Blog access',
      'Email newsletter with tips',
    ],
    cta: 'Start Reading',
    href: '/start-here',
  },
  {
    name: 'Job Site Binder',
    price: '$97',
    period: 'one-time',
    description: 'The complete printable toolkit for your job site.',
    features: [
      'Everything in Free',
      '229-page printable binder system',
      'Editable Word & Excel templates',
      'Contracts, checklists, and forms',
      'Budget tracking spreadsheets',
      'Inspection prep sheets',
      'Lifetime access + free updates',
    ],
    cta: 'Get the Binder',
    href: STRIPE_BINDER_URL,
  },
  {
    name: 'Builder Pro',
    price: '$20',
    period: '/month',
    description: 'Your AI general contractor in your pocket. Everything you need to build with confidence.',
    features: [
      'Everything in Free + Binder',
      'Reed AI General Contractor — 24/7 advice',
      'Ask unlimited questions about your build',
      'Code-specific answers for your jurisdiction',
      'Material estimates and cost guidance',
      'Inspection prep and scheduling advice',
      'Priority email support',
      'Cancel anytime',
    ],
    cta: 'Start Builder Pro',
    href: STRIPE_SUBSCRIPTION_URL,
    highlighted: true,
  },
];

export default function PricingTable() {
  return (
    <div className={styles.pricingGrid}>
      {tiers.map((tier) => (
        <div
          key={tier.name}
          className={`${styles.tier} ${tier.highlighted ? styles.tierHighlighted : ''}`}
        >
          {tier.highlighted && (
            <div className={styles.badge}>Most Popular</div>
          )}

          <div className={styles.tierHeader}>
            <h3 className={styles.tierName}>{tier.name}</h3>
            <div className={styles.tierPrice}>
              <span className={styles.priceAmount}>{tier.price}</span>
              <span className={styles.pricePeriod}>{tier.period}</span>
            </div>
            <p className={styles.tierDescription}>{tier.description}</p>
          </div>

          <ul className={styles.featureList}>
            {tier.features.map((feature, i) => (
              <li key={i} className={styles.feature}>
                <span className={styles.featureCheck}>&#10003;</span>
                {feature}
              </li>
            ))}
          </ul>

          <div className={styles.tierFooter}>
            <a
              href={tier.href}
              className={`${styles.ctaButton} ${tier.highlighted ? styles.ctaHighlighted : ''}`}
            >
              {tier.cta}
            </a>
          </div>
        </div>
      ))}
    </div>
  );
}
