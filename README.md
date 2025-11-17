# Build-Your-House.com

A comprehensive owner-builder resource website to help people build their own homes and save $50k-150k+.

## 🎉 What's Been Built

I've created a **production-ready foundation** for your owner-builder website with:

### ✅ Complete Technical Setup
- Next.js 14 with TypeScript
- MDX for rich content
- CSS Modules styling
- Static export for Cloudflare Pages
- Fully responsive design

### ✅ Core Pages (5 pages completed)
1. **Homepage** - Hero, value props, featured content
2. **Start Here** - 7-phase roadmap guide
3. **Cost Savings Calculator** - Interactive calculator
4. **Permitting Guide** - Comprehensive MDX guide (2,500+ words)
5. **Consulting Services** - 5 service tiers

### ✅ Reusable Components
- Header with full navigation
- Footer with multi-column links
- ArticleLayout for content pages
- CostSavingsCalculator component
- Calculator styling system

### ✅ Business Logic
- Cost savings calculations
- Material estimation functions
- Timeline estimation functions
- Utility functions

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Visit http://localhost:3000

# Build for production
npm run build

# Output is in /out directory
```

## 📊 What's Left to Build

You have a **solid foundation** but need ~50 more pages to complete the vision:

### Priority Content (Weeks 1-4)
- [ ] 3 more feasibility pages
- [ ] 4 more permitting pages
- [ ] 6 inspection pages
- [ ] 8 subcontractor pages
- [ ] 7 timing/scheduling pages

### Build Phases (Weeks 5-8)
- [ ] 17 build phase guides

### Tools & Resources (Weeks 9-10)
- [ ] 2 more calculators
- [ ] Resources section
- [ ] Tools & equipment section
- [ ] Blog setup
- [ ] About page

### State Guides (Ongoing)
- [ ] North Carolina (detailed)
- [ ] Top 10 states (Texas, Florida, California, etc.)

## 📝 How to Add Content

### Method 1: MDX Pages (for guides)

Create a new file:
```bash
# Example: create new inspection guide
touch src/app/inspections/framing-inspection/page.mdx
```

Add content:
```mdx
export const metadata = {
  title: 'Framing Inspection Guide | Build-Your-House.com',
  description: 'Complete guide to passing your framing inspection',
};

# Framing Inspection Guide

Your markdown content here...

## What Inspectors Check

- Structural members
- Joist spacing
- Beam sizing
```

### Method 2: React Pages (for dynamic pages)

```typescript
// src/app/new-page/page.tsx
import type { Metadata } from 'next';
import styles from './page.module.css';

export const metadata: Metadata = {
  title: 'Page Title',
  description: 'Description',
};

export default function NewPage() {
  return <div>Your content</div>;
}
```

## 🎨 Styling

All CSS uses CSS Modules and global variables:

```css
/* Available variables */
var(--color-primary)      /* Blue: #2c5282 */
var(--color-secondary)    /* Orange: #dd6b20 */
var(--color-text)         /* Dark gray */
var(--color-bg-light)     /* Light gray background */
var(--spacing-md)         /* 1rem */
var(--max-width)          /* 1200px */
```

## 🔧 Project Structure

```
src/
├── app/                    # Pages (Next.js App Router)
│   ├── page.tsx           # Homepage ✅
│   ├── start-here/        # Getting started ✅
│   ├── consulting/        # Services ✅
│   ├── feasibility/       # Assessment section (1/4 pages)
│   ├── permitting/        # Permits (1/5 pages)
│   └── [50+ more pages needed]
├── components/            # React components
│   ├── Header.tsx         ✅
│   ├── Footer.tsx         ✅
│   ├── ArticleLayout.tsx  ✅
│   └── CostSavingsCalculator.tsx ✅
├── lib/                   # Business logic
│   ├── calculators.ts     ✅
│   ├── utils.ts           ✅
│   └── types.ts           ✅
└── styles/                # CSS Modules
    ├── globals.css        ✅
    └── [component].module.css
```

## 💰 Monetization Ready

The site has integration points for:
- **Display Ads**: Add AdSense to layout
- **Affiliate Links**: Amazon, Home Depot (add to content)
- **Digital Products**: Link to Gumroad in resources
- **Consulting**: Email CTAs built-in ✅
- **Email Capture**: Ready for ConvertKit/Mailchimp

## 🚀 Deployment

### Cloudflare Pages Setup

1. Push to GitHub
2. Connect repo to Cloudflare Pages
3. Build settings:
   - Build command: `npm run build`
   - Output directory: `out`
   - Node version: 18+
4. Deploy!

## 📈 Content Strategy

Follow the patterns established:

1. **Homepage** → Drives to "Start Here"
2. **Start Here** → Links to all major sections
3. **Section Pages** → Deep guides with internal links
4. **Calculator Pages** → Interactive tools with CTAs
5. **Consulting** → Revenue generation

Every page should have:
- Clear title & meta description
- Internal links to related content
- CTAs to consulting or calculators
- Mobile-responsive design

## 🎯 Next Steps

### This Week
1. Run `npm run dev` and explore what's built
2. Add 3-4 feasibility pages using MDX
3. Complete permitting section
4. Test the calculator

### Next 2 Weeks
1. Build out inspection section (6 pages)
2. Create subcontractor section (8 pages)
3. Add state-specific guides (start with NC)

### Month 1 Goal
- 30+ pages of content
- All critical sections complete
- Ready to launch and drive traffic

## 📚 Resources

- Original plan: `/build-your-house-plan.md`
- Next.js docs: https://nextjs.org/docs
- MDX docs: https://mdxjs.com

## 💡 Tips

1. **Write from experience**: Use real GC stories and examples
2. **Be specific**: Include actual numbers, timelines, costs
3. **SEO matters**: Unique titles, good descriptions
4. **Internal linking**: Link related pages together
5. **Mobile first**: Test on phone regularly

## ⚠️ Important Notes

- **Build works**: `npm run build` creates static site in `/out`
- **Fast dev**: Hot reload on `npm run dev`
- **Type-safe**: TypeScript catches errors
- **No database**: Fully static, super fast
- **SEO ready**: Proper metadata on all pages

## 🆘 Common Tasks

### Add a new section
```bash
mkdir -p src/app/new-section
touch src/app/new-section/page.mdx
```

### Add a calculator
1. Add logic to `/src/lib/calculators.ts`
2. Create component in `/src/components/`
3. Create page in `/src/app/calculators/`

### Style a component
Create a `.module.css` file next to your component:
```css
.container {
  max-width: var(--max-width);
  margin: 0 auto;
}
```

---

**Built with Claude Code** | See `build-your-house-plan.md` for the complete vision
