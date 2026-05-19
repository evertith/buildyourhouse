# Quick Reference - New Features

## Email Capture Component

### Import and Use
```tsx
import EmailCapture from '@/components/EmailCapture';

<EmailCapture
  title="Join Our Newsletter"
  description="Get expert tips delivered weekly"
  buttonText="Subscribe"
  placeholderText="your@email.com"
/>
```

### Custom Integration
```tsx
<EmailCapture
  onSubmit={async (email) => {
    const response = await fetch('/api/subscribe', {
      method: 'POST',
      body: JSON.stringify({ email }),
    });
  }}
/>
```

### Props
- `title?` - Heading text (default: "Join Our Newsletter")
- `description?` - Subheading (default: "Get expert tips...")
- `buttonText?` - Button label (default: "Subscribe")
- `placeholderText?` - Input placeholder (default: "Enter your email")
- `onSubmit?` - Custom handler function

## Schema Markup

### Article Schema (Blog Posts)
```tsx
import { generateArticleSchema } from '@/lib/schema';

const schema = generateArticleSchema({
  headline: "Post Title",
  description: "Post description",
  datePublished: "2025-01-15",
  author: { name: "Author Name" },
  publisher: { name: "Build Your House" },
  url: "https://buildyourhouse.com/blog/post",
});

<script type="application/ld+json"
  dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />
```

### Breadcrumbs
```tsx
import { generateBreadcrumbSchema } from '@/lib/schema';

const breadcrumbs = generateBreadcrumbSchema([
  { name: "Home", item: "https://buildyourhouse.com" },
  { name: "Section", item: "https://buildyourhouse.com/section" },
  { name: "Page", item: "https://buildyourhouse.com/section/page" },
]);
```

### FAQ
```tsx
import { generateFAQSchema } from '@/lib/schema';

const faq = generateFAQSchema([
  { question: "How much can I save?", answer: "$50k-150k+" },
  { question: "Do I need a license?", answer: "Varies by state..." },
]);
```

### HowTo
```tsx
import { generateHowToSchema } from '@/lib/schema';

const howto = generateHowToSchema({
  name: "How to Get a Building Permit",
  description: "Step by step guide",
  steps: [
    { name: "Prepare Documents", text: "Gather required papers..." },
    { name: "Submit Application", text: "File with building dept..." },
  ],
});
```

## Page Metadata Template

```tsx
export const metadata = {
  title: "Page Title - 50-60 chars",
  description: "Page description 150-160 characters with keywords and call to action.",
  keywords: ["keyword1", "keyword2", "keyword3"],
  openGraph: {
    title: "Social Media Title",
    description: "Social description",
    images: ["/path/to/image.jpg"],
  },
  alternates: {
    canonical: "https://buildyourhouse.com/page-url",
  },
};
```

## SEO Checklist

### For Every New Page
- [ ] Unique title (50-60 chars)
- [ ] Unique description (150-160 chars)
- [ ] Canonical URL set
- [ ] Open Graph image (1200x630px)
- [ ] Relevant schema markup
- [ ] Breadcrumbs if nested
- [ ] Alt text on all images
- [ ] Internal links to related pages

### Monthly Tasks
- [ ] Check Google Search Console for errors
- [ ] Review performance reports
- [ ] Update content if needed
- [ ] Check Core Web Vitals

### When Publishing Blog Posts
1. Add Article schema
2. Add Breadcrumb schema
3. Set datePublished and dateModified
4. Include author information
5. Add Open Graph image
6. Internal link to related content
7. Include EmailCapture component

## URLs and Testing

- **Sitemap:** https://buildyourhouse.com/sitemap.xml
- **Robots.txt:** https://buildyourhouse.com/robots.txt
- **Newsletter:** https://buildyourhouse.com/newsletter
- **Schema Validator:** https://validator.schema.org/
- **Rich Results Test:** https://search.google.com/test/rich-results
- **PageSpeed Insights:** https://pagespeed.web.dev/

## File Locations

```
src/
├── app/
│   ├── layout.tsx              # Enhanced with SEO
│   ├── sitemap.ts              # Dynamic sitemap
│   └── newsletter/page.mdx     # Newsletter page
├── components/
│   └── EmailCapture.tsx        # Email component
├── lib/
│   └── schema.ts               # Schema helpers
└── styles/
    └── EmailCapture.module.css # Email styles

public/
└── robots.txt                  # Search engine rules

Root:
├── SEO-GUIDE.md               # Full SEO documentation
└── IMPLEMENTATION-SUMMARY.md  # Implementation details
```

## Common Commands

```bash
# Development
npm run dev

# Build
npm run build

# Check TypeScript
npx tsc --noEmit

# Lint
npm run lint
```

## Next Steps After Implementation

1. **Integrate Email Service**
   - Create `/src/app/api/subscribe/route.ts`
   - Add API key to `.env.local`
   - Test subscription flow

2. **Add Search Console**
   - Verify domain
   - Submit sitemap
   - Add verification code to layout.tsx

3. **Create Assets**
   - Open Graph image (1200x630px)
   - Logo (PNG)
   - Favicon

4. **Optimize Existing Pages**
   - Add schema to blog posts
   - Add breadcrumbs
   - Update meta descriptions
   - Add alt text to images

---

For detailed information, see **SEO-GUIDE.md**
