/**
 * JSON-LD Schema Markup Helpers
 *
 * These functions generate structured data for better SEO and search engine understanding.
 * Use them in page metadata or components to add schema markup to your pages.
 */

export interface OrganizationSchemaProps {
  name: string;
  url: string;
  logo?: string;
  description?: string;
  address?: {
    streetAddress?: string;
    addressLocality?: string;
    addressRegion?: string;
    postalCode?: string;
    addressCountry?: string;
  };
  contactPoint?: {
    telephone?: string;
    contactType?: string;
    email?: string;
  };
  sameAs?: string[]; // Social media profiles
}

export interface ArticleSchemaProps {
  headline: string;
  description: string;
  image?: string;
  datePublished: string;
  dateModified?: string;
  author: {
    name: string;
    url?: string;
    type?: 'Person' | 'Organization';
  };
  publisher: {
    name: string;
    logo?: string;
  };
  url: string;
}

export interface BreadcrumbItem {
  name: string;
  item: string;
}

export interface FAQItem {
  question: string;
  answer: string;
}

export interface HowToStep {
  name: string;
  text: string;
  image?: string;
  url?: string;
}

export interface ProductSchemaProps {
  name: string;
  description: string;
  image: string; // Absolute URL
  url: string;   // Absolute URL of the product page
  price: number;
  priceCurrency: string;
  availability?: 'InStock' | 'OutOfStock' | 'PreOrder';
  brand?: string;
  sku?: string;
}

export interface HowToSchemaProps {
  name: string;
  description: string;
  image?: string;
  totalTime?: string; // ISO 8601 duration format (e.g., "PT2H30M")
  estimatedCost?: {
    currency: string;
    value: string;
  };
  supply?: string[];
  tool?: string[];
  steps: HowToStep[];
}

/**
 * Generate Organization schema markup
 */
export function generateOrganizationSchema(props: OrganizationSchemaProps) {
  const schema: Record<string, unknown> = {
    "@context": "https://schema.org",
    "@type": "Organization",
    name: props.name,
    url: props.url,
  };

  if (props.logo) {
    schema.logo = props.logo;
  }

  if (props.description) {
    schema.description = props.description;
  }

  if (props.address) {
    schema.address = {
      "@type": "PostalAddress",
      ...props.address,
    };
  }

  if (props.contactPoint) {
    schema.contactPoint = {
      "@type": "ContactPoint",
      ...props.contactPoint,
    };
  }

  if (props.sameAs && props.sameAs.length > 0) {
    schema.sameAs = props.sameAs;
  }

  return schema;
}

/**
 * Generate Article schema markup
 */
export function generateArticleSchema(props: ArticleSchemaProps) {
  const schema: Record<string, unknown> = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: props.headline,
    description: props.description,
    datePublished: props.datePublished,
    dateModified: props.dateModified || props.datePublished,
    author: {
      "@type": props.author.type ?? "Person",
      name: props.author.name,
      url: props.author.url,
    },
    publisher: {
      "@type": "Organization",
      name: props.publisher.name,
      logo: props.publisher.logo ? {
        "@type": "ImageObject",
        url: props.publisher.logo,
      } : undefined,
    },
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": props.url,
    },
  };

  if (props.image) {
    schema.image = props.image;
  }

  return schema;
}

/**
 * Generate BreadcrumbList schema markup
 */
export function generateBreadcrumbSchema(items: BreadcrumbItem[]) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      item: item.item,
    })),
  };
}

/**
 * Generate FAQPage schema markup
 */
export function generateFAQSchema(faqs: FAQItem[]) {
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs.map((faq) => ({
      "@type": "Question",
      name: faq.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: faq.answer,
      },
    })),
  };
}

/**
 * Generate Product schema markup.
 *
 * Deliberately omits aggregateRating and review: the binder has no verified
 * customer reviews yet, and inventing them would be both false and a Google
 * structured-data violation. Add them only when real reviews exist.
 */
export function generateProductSchema(props: ProductSchemaProps) {
  return {
    "@context": "https://schema.org",
    "@type": "Product",
    name: props.name,
    description: props.description,
    image: props.image,
    url: props.url,
    ...(props.brand ? { brand: { "@type": "Brand", name: props.brand } } : {}),
    ...(props.sku ? { sku: props.sku } : {}),
    offers: {
      "@type": "Offer",
      price: props.price,
      priceCurrency: props.priceCurrency,
      availability: `https://schema.org/${props.availability ?? "InStock"}`,
      url: props.url,
    },
  };
}

/**
 * Generate HowTo schema markup
 */
export function generateHowToSchema(props: HowToSchemaProps) {
  const schema: Record<string, unknown> = {
    "@context": "https://schema.org",
    "@type": "HowTo",
    name: props.name,
    description: props.description,
    step: props.steps.map((step, index) => ({
      "@type": "HowToStep",
      position: index + 1,
      name: step.name,
      text: step.text,
      image: step.image,
      url: step.url,
    })),
  };

  if (props.image) {
    schema.image = props.image;
  }

  if (props.totalTime) {
    schema.totalTime = props.totalTime;
  }

  if (props.estimatedCost) {
    schema.estimatedCost = {
      "@type": "MonetaryAmount",
      currency: props.estimatedCost.currency,
      value: props.estimatedCost.value,
    };
  }

  if (props.supply && props.supply.length > 0) {
    schema.supply = props.supply.map((supply) => ({
      "@type": "HowToSupply",
      name: supply,
    }));
  }

  if (props.tool && props.tool.length > 0) {
    schema.tool = props.tool.map((tool) => ({
      "@type": "HowToTool",
      name: tool,
    }));
  }

  return schema;
}

/**
 * Generate WebSite schema markup
 */
export function generateWebSiteSchema(props: {
  name: string;
  url: string;
  description?: string;
  searchUrl?: string; // URL template for search (e.g., "https://example.com/search?q={search_term_string}")
}) {
  const schema: Record<string, unknown> = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: props.name,
    url: props.url,
  };

  if (props.description) {
    schema.description = props.description;
  }

  if (props.searchUrl) {
    schema.potentialAction = {
      "@type": "SearchAction",
      target: {
        "@type": "EntryPoint",
        urlTemplate: props.searchUrl,
      },
      "query-input": "required name=search_term_string",
    };
  }

  return schema;
}

/**
 * Generate Course schema markup (useful for educational content)
 */
export function generateCourseSchema(props: {
  name: string;
  description: string;
  provider: {
    name: string;
    url?: string;
  };
  url?: string;
}) {
  return {
    "@context": "https://schema.org",
    "@type": "Course",
    name: props.name,
    description: props.description,
    provider: {
      "@type": "Organization",
      name: props.provider.name,
      url: props.provider.url,
    },
    url: props.url,
  };
}

/**
 * Utility function to convert schema object to JSON-LD script tag string
 * Use this in your component or page to output the schema
 */
export function schemaToScriptTag(schema: Record<string, unknown>): string {
  return JSON.stringify(schema);
}

/**
 * Helper to create multiple schemas in one script tag
 */
export function generateMultipleSchemas(schemas: Record<string, unknown>[]): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@graph": schemas,
  });
}
