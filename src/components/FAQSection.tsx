import React from 'react';

type FAQ = {
  question: string;
  answer: string;
};

interface FAQSectionProps {
  title?: string;
  faqs: FAQ[];
}

export default function FAQSection({ title = 'Frequently Asked Questions', faqs }: FAQSectionProps) {
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map(({ question, answer }) => ({
      '@type': 'Question',
      name: question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: answer,
      },
    })),
  };

  return (
    <section className="faqSection">
      <h2>{title}</h2>
      {faqs.map(({ question, answer }, i) => (
        <div key={i}>
          <h3>{question}</h3>
          <p>{answer}</p>
        </div>
      ))}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
      />
    </section>
  );
}
