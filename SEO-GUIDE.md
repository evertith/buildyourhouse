# SEO Implementation Guide for Build Your House

This guide documents the SEO setup for buildyourhouse.com and provides instructions for maintaining and optimizing search engine visibility.

## Table of Contents

1. [Overview](#overview)
2. [What's Implemented](#whats-implemented)
3. [File Structure](#file-structure)
4. [How to Use Schema Markup](#how-to-use-schema-markup)
5. [Best Practices](#best-practices)
6. [Maintenance Tasks](#maintenance-tasks)
7. [Testing & Validation](#testing--validation)
8. [Performance Monitoring](#performance-monitoring)

---

## Overview

Build Your House uses a comprehensive SEO strategy built on Next.js 14 app router features. The implementation includes:

- Structured data (JSON-LD schema markup)
- Dynamic sitemap generation
- Optimized metadata for all pages
- Open Graph and Twitter Card tags
- Mobile-first responsive design
- Performance optimization

## What's Implemented

### 1. Root Layout SEO (`/src/app/layout.tsx`)

**Features:**
- Comprehensive metadata configuration
- Open Graph tags for social sharing
- Twitter Card tags
- Canonical URLs
- Robots directives
- Organization and WebSite schema markup
- Verification tag placeholders

**Key Elements:**
```typescript
- metadataBase: Sets the base URL for all relative URLs
- title.template: Automatic title suffixing for all pages
- openGraph: Social media preview configuration
- twitter: Twitter-specific preview configuration
- robots: Search engine crawling instructions
- verification: Search console verification codes
```

### 2. Dynamic Sitemap (`/src/app/sitemap.ts`)

**What it does:**
- Automatically generates XML sitemap at `/sitemap.xml`
- Includes all site routes with proper priority and change frequency
- Updates modification dates automatically
- Helps search engines discover and index all pages

**Priorities:**
- Homepage: 1.0 (highest)
- Main sections & calculators: 0.8-0.9
- Content pages: 0.7
- Legal pages: 0.3

**Change Frequencies:**
- Homepage & blog: Weekly
- Most content: Monthly
- Legal pages: Yearly

### 3. Robots.txt (`/public/robots.txt`)

**What it does:**
- Allows all search engines to crawl all content
- Points to sitemap location
- Can be customized to block specific bots or directories

### 4. Schema Markup Library (`/src/lib/schema.ts`)

**Available Schema Types:**

1. **Organization Schema**
   - Company/brand information
   - Contact details
   - Social media profiles

2. **Article Schema**
   - Blog posts
   - Author information
   - Publication dates

3. **Breadcrumb Schema**
   - Navigation hierarchy
   - Improves search result appearance

4. **FAQ Schema**
   - Question and answer pairs
   - Rich snippet potential

5. **HowTo Schema**
   - Step-by-step guides
   - Instruction content
   - Rich snippet potential

6. **WebSite Schema**
   - Site-wide information
   - Search functionality

7. **Course Schema**
   - Educational content
   - Training materials

---

## File Structure

```
build-your-house/
├── public/
│   └── robots.txt                    # Search engine crawler instructions
├── src/
│   ├── app/
│   │   ├── layout.tsx                # Root layout with SEO metadata
│   │   ├── sitemap.ts                # Dynamic sitemap generation
│   │   └── [pages]/page.tsx          # Individual pages (add metadata here)
│   ├── components/
│   │   └── EmailCapture.tsx          # Email capture component
│   ├── lib/
│   │   └── schema.ts                 # Schema markup helpers
│   └── styles/
│       └── EmailCapture.module.css   # Email capture styles
└── SEO-GUIDE.md                      # This file
```

---

## How to Use Schema Markup

### Adding Schema to a Blog Post

```tsx
// In your blog post page.tsx or page.mdx
import { generateArticleSchema } from '@/lib/schema';

export const metadata = {
  title: "Your Blog Post Title",
  description: "Your blog post description",
};

export default function BlogPost() {
  const articleSchema = generateArticleSchema({
    headline: "Your Blog Post Title",
    description: "Your blog post description",
    image: "https://buildyourhouse.com/images/blog-post.jpg",
    datePublished: "2025-01-15",
    dateModified: "2025-01-20",
    author: {
      name: "Build Your House",
      url: "https://buildyourhouse.com/about",
    },
    publisher: {
      name: "Build Your House",
      logo: "https://buildyourhouse.com/logo.png",
    },
    url: "https://buildyourhouse.com/blog/your-post-slug",
  });

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(articleSchema),
        }}
      />
      {/* Your content here */}
    </>
  );
}
```

### Adding Breadcrumbs

```tsx
import { generateBreadcrumbSchema } from '@/lib/schema';

const breadcrumbSchema = generateBreadcrumbSchema([
  { name: "Home", item: "https://buildyourhouse.com" },
  { name: "Blog", item: "https://buildyourhouse.com/blog" },
  { name: "Post Title", item: "https://buildyourhouse.com/blog/post-slug" },
]);

// Add to your component
<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }}
/>
```

### Adding FAQ Schema

```tsx
import { generateFAQSchema } from '@/lib/schema';

const faqSchema = generateFAQSchema([
  {
    question: "How much can I save as an owner-builder?",
    answer: "Owner-builders typically save between $50,000 to $150,000+ on their projects by eliminating general contractor fees and markups.",
  },
  {
    question: "Do I need a license to build my own house?",
    answer: "Requirements vary by state. Most states allow homeowners to build their primary residence without a contractor's license, but you'll still need permits and inspections.",
  },
]);
```

### Adding HowTo Schema

```tsx
import { generateHowToSchema } from '@/lib/schema';

const howToSchema = generateHowToSchema({
  name: "How to Obtain a Building Permit",
  description: "Step-by-step guide to getting your building permit approved",
  totalTime: "PT2H", // 2 hours in ISO 8601 format
  steps: [
    {
      name: "Prepare Your Documents",
      text: "Gather site plans, architectural drawings, and engineering reports.",
    },
    {
      name: "Submit Application",
      text: "Submit your complete application package to the building department.",
    },
    {
      name: "Review Process",
      text: "Wait for the building department to review your plans. This typically takes 2-4 weeks.",
    },
    {
      name: "Address Comments",
      text: "Respond to any plan review comments or requested changes.",
    },
    {
      name: "Receive Permit",
      text: "Once approved, pay the permit fees and receive your building permit.",
    },
  ],
});
```

---

## Best Practices

### Page Metadata

Every page should have unique, descriptive metadata:

```typescript
export const metadata: Metadata = {
  title: "Unique Page Title - Keep Under 60 Characters",
  description: "Unique description that accurately describes the page content. Keep between 150-160 characters for optimal search result display.",
  openGraph: {
    title: "Social Media Title",
    description: "Social media description",
    images: ["/path/to/image.jpg"],
  },
};
```

### Title Tag Guidelines

- **Length:** 50-60 characters (including site name)
- **Format:** Primary Keyword - Secondary Keyword | Brand Name
- **Unique:** Every page should have a unique title
- **Descriptive:** Clearly describe page content
- **Front-load keywords:** Put important keywords at the beginning

### Meta Description Guidelines

- **Length:** 150-160 characters
- **Unique:** Every page should have a unique description
- **Compelling:** Include a call-to-action
- **Keyword-rich:** Include target keywords naturally
- **Accurate:** Describe actual page content

### URL Structure

- Use descriptive, keyword-rich URLs
- Keep URLs short and readable
- Use hyphens (not underscores) to separate words
- Avoid special characters
- Use lowercase letters

**Good URL:** `/build-phases/foundation`
**Bad URL:** `/page?id=123&type=phase`

### Image Optimization

- Use descriptive file names: `foundation-inspection-checklist.jpg`
- Add alt text to all images
- Optimize file size (use WebP format when possible)
- Include image schema when relevant
- Use responsive images with `srcset`

### Internal Linking

- Link to related content within your site
- Use descriptive anchor text (avoid "click here")
- Create a logical site hierarchy
- Ensure important pages are no more than 3 clicks from homepage

---

## Maintenance Tasks

### Monthly Tasks

1. **Review Search Console Data**
   - Check for crawl errors
   - Review search performance
   - Identify new keyword opportunities

2. **Update Content**
   - Refresh outdated information
   - Add new content
   - Update publication dates when making significant changes

3. **Monitor Site Speed**
   - Check Core Web Vitals
   - Optimize images if needed
   - Review largest contentful paint (LCP)

### Quarterly Tasks

1. **Content Audit**
   - Review underperforming pages
   - Update or consolidate thin content
   - Identify content gaps

2. **Technical SEO Audit**
   - Check for broken links
   - Verify sitemap accuracy
   - Review mobile usability

3. **Competitor Analysis**
   - Review competitor rankings
   - Identify new keyword opportunities
   - Analyze content strategies

### Annual Tasks

1. **Comprehensive SEO Audit**
   - Full technical review
   - Content strategy assessment
   - Link profile analysis

2. **Schema Markup Review**
   - Update organization information
   - Review all structured data
   - Test for errors

---

## Testing & Validation

### Tools to Use

1. **Google Search Console**
   - Submit sitemap
   - Monitor crawl status
   - Track search performance
   - URL: https://search.google.com/search-console

2. **Rich Results Test**
   - Test schema markup
   - Preview how pages appear in search
   - URL: https://search.google.com/test/rich-results

3. **Schema Markup Validator**
   - Validate JSON-LD syntax
   - Check for errors
   - URL: https://validator.schema.org/

4. **PageSpeed Insights**
   - Test page speed
   - Check Core Web Vitals
   - URL: https://pagespeed.web.dev/

5. **Mobile-Friendly Test**
   - Verify mobile compatibility
   - URL: https://search.google.com/test/mobile-friendly

### Validation Checklist

- [ ] All pages have unique titles and descriptions
- [ ] Schema markup validates without errors
- [ ] Sitemap loads correctly at `/sitemap.xml`
- [ ] Robots.txt is accessible at `/robots.txt`
- [ ] Open Graph images display correctly on social media
- [ ] All internal links work
- [ ] Pages load in under 3 seconds
- [ ] Mobile responsive on all devices
- [ ] Images have alt text
- [ ] Core Web Vitals pass

---

## Performance Monitoring

### Key Metrics to Track

1. **Organic Traffic**
   - Total organic sessions
   - Organic conversion rate
   - Top landing pages

2. **Rankings**
   - Target keyword positions
   - Ranking distribution
   - Featured snippet opportunities

3. **Technical Health**
   - Crawl errors
   - Page speed scores
   - Core Web Vitals
   - Mobile usability

4. **Engagement Metrics**
   - Bounce rate
   - Average session duration
   - Pages per session

### Setting Up Tracking

1. **Google Analytics 4**
   - Install GA4 tracking code
   - Set up conversion goals
   - Create custom reports

2. **Google Search Console**
   - Verify domain ownership
   - Submit sitemap
   - Set up email alerts

3. **Bing Webmaster Tools**
   - Verify site
   - Submit sitemap
   - Monitor Bing-specific metrics

---

## Adding Verification Codes

When you have verification codes from search engines, add them to the root layout:

```typescript
// In /src/app/layout.tsx
export const metadata: Metadata = {
  // ... other metadata
  verification: {
    google: "your-google-verification-code",
    yandex: "your-yandex-verification-code",
    bing: "your-bing-verification-code",
  },
};
```

---

## Common Issues & Solutions

### Issue: Pages Not Appearing in Sitemap

**Solution:** Add the route manually to `/src/app/sitemap.ts` in the appropriate section.

### Issue: Schema Markup Errors

**Solution:** Use the Schema Markup Validator to identify errors. Common issues:
- Missing required fields
- Incorrect date formats (use ISO 8601)
- Invalid URLs (must be absolute, not relative)

### Issue: Slow Page Load Times

**Solution:**
- Optimize images (compress, use WebP)
- Minimize JavaScript
- Use Next.js Image component for automatic optimization
- Enable browser caching

### Issue: Duplicate Meta Descriptions

**Solution:** Ensure each page has a unique description in its metadata export.

---

## Email Capture Integration

The site includes an EmailCapture component for building your email list.

### Component Location
`/src/components/EmailCapture.tsx`

### Usage Example

```tsx
import EmailCapture from '@/components/EmailCapture';

<EmailCapture
  title="Join Our Newsletter"
  description="Get expert building tips delivered weekly."
  buttonText="Subscribe"
  placeholderText="your@email.com"
/>
```

### Email Service Integration

To connect to an email service (Mailchimp, ConvertKit, etc.):

1. Install the service's SDK/API client
2. Create an API route in `/src/app/api/subscribe/route.ts`
3. Pass a custom `onSubmit` function to the EmailCapture component

Example:

```typescript
// /src/app/api/subscribe/route.ts
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  const { email } = await request.json();

  // Add to your email service
  // Example: await mailchimp.lists.addListMember(listId, { email_address: email });

  return NextResponse.json({ success: true });
}
```

---

## Resources

- [Next.js Metadata Documentation](https://nextjs.org/docs/app/building-your-application/optimizing/metadata)
- [Google Search Central](https://developers.google.com/search)
- [Schema.org Documentation](https://schema.org/)
- [Open Graph Protocol](https://ogp.me/)
- [Twitter Card Documentation](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)

---

## Summary

This SEO implementation provides a solid foundation for search engine visibility. The key to success is:

1. **Consistent metadata** on all pages
2. **Regular content updates** with fresh, valuable information
3. **Performance monitoring** and optimization
4. **Technical maintenance** to fix issues promptly
5. **User-focused content** that answers real questions

Remember: SEO is an ongoing process, not a one-time task. Regular attention to these elements will improve your search rankings over time.

---

**Questions or Issues?**

If you encounter any SEO-related issues or need clarification on implementation, refer to this guide first. For technical implementation questions, consult the Next.js documentation linked above.

Last Updated: November 2025
