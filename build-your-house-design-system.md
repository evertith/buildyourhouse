# Build-Your-House.com - Complete Design System & Overhaul Specification

## Executive Summary

This is a comprehensive guide for couples planning to build their own homes - one of the biggest financial and emotional decisions of their lives. The design must inspire confidence, reduce overwhelm, and feel like a trusted expert is guiding them through the process.

**Design Philosophy:** Warm, trustworthy, and approachable - like having an experienced general contractor as your personal mentor.

---

## Color System

### Primary Colors

```css
/* Backgrounds */
--bg-primary: #faf8f5;        /* Warm off-white - main background */
--bg-secondary: #f0ede8;      /* Slightly darker warm gray - cards, sections */
--bg-tertiary: #e8e4df;       /* Subtle borders, dividers */

/* Text */
--text-primary: #2d2d2d;      /* Dark charcoal - body text */
--text-secondary: #5a5a5a;    /* Medium gray - secondary text, captions */
--text-heading: #1a1a1a;      /* Deep black - headings */

/* Accents */
--accent-primary: #d4763b;    /* Construction orange - CTAs, important callouts */
--accent-secondary: #5b8a72;  /* Sage green - tips, success states, checkboxes */
--accent-warning: #e67e22;    /* Warm orange - warnings, caution */
--accent-info: #3b7dbd;       /* Blueprint blue - informational callouts */

/* Interactive States */
--link-color: #c75f32;        /* Darker orange for links */
--link-hover: #a84d27;        /* Even darker on hover */
--button-primary: #d4763b;    /* Primary CTA buttons */
--button-primary-hover: #c75f32;
--button-secondary: #5b8a72;  /* Secondary buttons */
--button-secondary-hover: #4a7c59;
```

### Usage Guidelines

**Construction Orange (#d4763b):**
- Primary CTAs ("Start Here", "Download Guide")
- Important warnings about safety
- Highlighting critical steps
- Progress indicators
- Chapter/section numbers

**Sage Green (#5b8a72):**
- Success messages ("✓ Section Complete")
- Pro tips and expert advice boxes
- Completed checklist items
- Positive reinforcement elements
- "You can do this" encouragement

**Blueprint Blue (#3b7dbd):**
- Informational callouts
- Code references
- Technical specifications
- Permit information
- Building department details

**Warm Orange (#e67e22):**
- Warnings and cautions
- Safety-critical information
- Common mistakes to avoid
- Budget alerts

---

## Typography System

### Font Stack

```css
/* Headings */
--font-heading: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;

/* Body */
--font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;

/* Monospace (code, specifications) */
--font-mono: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, monospace;
```

### Type Scale

```css
/* Font Sizes */
--text-xs: 13px;      /* Fine print, captions */
--text-sm: 15px;      /* Secondary text */
--text-base: 18px;    /* Body text - IMPORTANT: Must be readable */
--text-lg: 20px;      /* Lead paragraphs */
--text-xl: 24px;      /* H4 */
--text-2xl: 28px;     /* H3 */
--text-3xl: 36px;     /* H2 */
--text-4xl: 48px;     /* H1 */
--text-5xl: 56px;     /* Hero headings */

/* Font Weights */
--weight-normal: 400;
--weight-medium: 500;
--weight-semibold: 600;
--weight-bold: 700;
--weight-extrabold: 800;

/* Line Heights */
--leading-tight: 1.2;    /* Headings */
--leading-snug: 1.4;     /* Subheadings */
--leading-normal: 1.6;   /* Body text default */
--leading-relaxed: 1.7;  /* Long-form content */
--leading-loose: 1.8;    /* Maximum readability */
```

### Typography Usage

**H1 (Page Titles):**
```css
font-size: 48px;
font-weight: 700;
line-height: 1.2;
color: #1a1a1a;
margin-bottom: 16px;
letter-spacing: -0.02em;
```

**H2 (Major Sections):**
```css
font-size: 36px;
font-weight: 700;
line-height: 1.3;
color: #1a1a1a;
margin-top: 60px;
margin-bottom: 24px;
```

**H3 (Subsections):**
```css
font-size: 28px;
font-weight: 600;
line-height: 1.4;
color: #2d2d2d;
margin-top: 40px;
margin-bottom: 16px;
```

**H4 (Minor Headings):**
```css
font-size: 24px;
font-weight: 600;
line-height: 1.4;
color: #2d2d2d;
margin-top: 32px;
margin-bottom: 12px;
```

**Body Text:**
```css
font-size: 18px;
font-weight: 400;
line-height: 1.7;
color: #2d2d2d;
margin-bottom: 20px;
```

**Lead Paragraph (intro text):**
```css
font-size: 20px;
font-weight: 400;
line-height: 1.6;
color: #2d2d2d;
margin-bottom: 32px;
```

---

## Spacing System

### Base Unit: 8px

```css
--space-1: 8px;
--space-2: 16px;
--space-3: 24px;
--space-4: 32px;
--space-5: 40px;
--space-6: 48px;
--space-7: 56px;
--space-8: 64px;
--space-10: 80px;
--space-12: 96px;
--space-16: 128px;
```

### Content Widths

```css
--width-narrow: 650px;    /* For very focused reading */
--width-content: 800px;   /* Primary content width */
--width-wide: 1000px;     /* Tables, images, wide content */
--width-full: 1200px;     /* Full site width */
```

### Container Padding

```css
--container-padding-mobile: 20px;
--container-padding-tablet: 40px;
--container-padding-desktop: 60px;
```

---

## Component Specifications

### 1. Page Layout

```css
.page-container {
  background-color: #faf8f5;
  min-height: 100vh;
}

.content-wrapper {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}

/* For wider elements */
.wide-content {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}
```

---

### 2. Header / Navigation

**Desktop Header:**
```
┌────────────────────────────────────────────────┐
│ Build Your House        Home  Guides  About    │
└────────────────────────────────────────────────┘
```

**Specifications:**
```css
header {
  background: #faf8f5;
  border-bottom: 1px solid #e8e4df;
  padding: 20px 40px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  color: #1a1a1a;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 32px;
}

.nav-link {
  font-size: 16px;
  font-weight: 500;
  color: #5a5a5a;
  text-decoration: none;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #d4763b;
}
```

---

### 3. Hero Section (Homepage)

```css
.hero {
  text-align: center;
  padding: 80px 20px 60px;
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 56px;
  font-weight: 800;
  line-height: 1.1;
  color: #1a1a1a;
  margin-bottom: 24px;
}

.hero .subtitle {
  font-size: 24px;
  font-weight: 400;
  line-height: 1.5;
  color: #5a5a5a;
  margin-bottom: 40px;
}

.hero .cta-buttons {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}
```

---

### 4. Button Components

**Primary Button (CTAs):**
```css
.button-primary {
  display: inline-block;
  padding: 16px 32px;
  background-color: #d4763b;
  color: #ffffff;
  font-size: 18px;
  font-weight: 600;
  text-decoration: none;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(212, 118, 59, 0.2);
}

.button-primary:hover {
  background-color: #c75f32;
  box-shadow: 0 4px 12px rgba(212, 118, 59, 0.3);
  transform: translateY(-2px);
}

.button-primary:active {
  transform: translateY(0);
}
```

**Secondary Button:**
```css
.button-secondary {
  display: inline-block;
  padding: 16px 32px;
  background-color: transparent;
  color: #d4763b;
  font-size: 18px;
  font-weight: 600;
  text-decoration: none;
  border-radius: 8px;
  border: 2px solid #d4763b;
  cursor: pointer;
  transition: all 0.2s ease;
}

.button-secondary:hover {
  background-color: #d4763b;
  color: #ffffff;
}
```

---

### 5. Callout Boxes / Info Boxes

**Pro Tip Box (Green):**
```css
.callout-tip {
  background-color: #f0f5f2;
  border-left: 4px solid #5b8a72;
  padding: 24px;
  margin: 32px 0;
  border-radius: 4px;
}

.callout-tip-title {
  font-size: 18px;
  font-weight: 700;
  color: #5b8a72;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.callout-tip-title::before {
  content: "💡";
  font-size: 20px;
}

.callout-tip-content {
  font-size: 16px;
  line-height: 1.6;
  color: #2d2d2d;
}
```

**Warning Box (Orange):**
```css
.callout-warning {
  background-color: #fef5f0;
  border-left: 4px solid #e67e22;
  padding: 24px;
  margin: 32px 0;
  border-radius: 4px;
}

.callout-warning-title {
  font-size: 18px;
  font-weight: 700;
  color: #e67e22;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.callout-warning-title::before {
  content: "⚠️";
  font-size: 20px;
}
```

**Info Box (Blue):**
```css
.callout-info {
  background-color: #f0f5fa;
  border-left: 4px solid #3b7dbd;
  padding: 24px;
  margin: 32px 0;
  border-radius: 4px;
}

.callout-info-title {
  font-size: 18px;
  font-weight: 700;
  color: #3b7dbd;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.callout-info-title::before {
  content: "ℹ️";
  font-size: 20px;
}
```

---

### 6. Checklist Component

```css
.checklist {
  background-color: #f0ede8;
  padding: 32px;
  margin: 40px 0;
  border-radius: 8px;
}

.checklist-title {
  font-size: 24px;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 24px;
}

.checklist-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid #e8e4df;
}

.checklist-item:last-child {
  border-bottom: none;
}

.checklist-checkbox {
  width: 24px;
  height: 24px;
  min-width: 24px;
  border: 2px solid #5b8a72;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.checklist-checkbox.checked {
  background-color: #5b8a72;
  position: relative;
}

.checklist-checkbox.checked::after {
  content: "✓";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 16px;
  font-weight: bold;
}

.checklist-label {
  font-size: 17px;
  line-height: 1.5;
  color: #2d2d2d;
  cursor: pointer;
}

.checklist-label.checked {
  text-decoration: line-through;
  color: #5a5a5a;
}
```

---

### 7. Step-by-Step Guide Component

```css
.step-guide {
  margin: 40px 0;
}

.step {
  display: flex;
  gap: 24px;
  margin-bottom: 48px;
  position: relative;
}

.step::before {
  content: "";
  position: absolute;
  left: 23px;
  top: 60px;
  bottom: -48px;
  width: 2px;
  background-color: #e8e4df;
}

.step:last-child::before {
  display: none;
}

.step-number {
  min-width: 48px;
  height: 48px;
  background-color: #d4763b;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: 700;
  z-index: 1;
}

.step-content {
  flex: 1;
}

.step-title {
  font-size: 24px;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 12px;
}

.step-description {
  font-size: 17px;
  line-height: 1.6;
  color: #2d2d2d;
}
```

---

### 8. Card Component (for resource grids)

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
  margin: 40px 0;
}

.card {
  background-color: #ffffff;
  border: 1px solid #e8e4df;
  border-radius: 8px;
  padding: 32px;
  transition: all 0.2s;
  cursor: pointer;
}

.card:hover {
  border-color: #d4763b;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transform: translateY(-4px);
}

.card-title {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 12px;
}

.card-description {
  font-size: 16px;
  line-height: 1.6;
  color: #5a5a5a;
  margin-bottom: 16px;
}

.card-link {
  font-size: 16px;
  font-weight: 600;
  color: #d4763b;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.card-link::after {
  content: "→";
}
```

---

### 9. Table of Contents (for long articles)

```css
.table-of-contents {
  background-color: #f0ede8;
  padding: 32px;
  margin: 40px 0;
  border-radius: 8px;
  border-left: 4px solid #d4763b;
}

.toc-title {
  font-size: 20px;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 16px;
}

.toc-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc-item {
  margin-bottom: 12px;
}

.toc-link {
  font-size: 16px;
  color: #5a5a5a;
  text-decoration: none;
  transition: color 0.2s;
  display: block;
  padding: 4px 0;
}

.toc-link:hover {
  color: #d4763b;
}

.toc-item-nested {
  margin-left: 20px;
  margin-top: 8px;
}
```

---

### 10. Progress Indicator

```css
.progress-indicator {
  margin: 40px 0;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background-color: #e8e4df;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #5b8a72 0%, #d4763b 100%);
  border-radius: 4px;
  transition: width 0.3s ease;
}

.progress-label {
  font-size: 14px;
  color: #5a5a5a;
  margin-top: 8px;
  text-align: right;
}
```

---

### 11. Quote / Testimonial

```css
.quote {
  background-color: #f0ede8;
  padding: 32px 40px;
  margin: 40px 0;
  border-left: 4px solid #5b8a72;
  border-radius: 4px;
  font-style: italic;
}

.quote-text {
  font-size: 20px;
  line-height: 1.6;
  color: #2d2d2d;
  margin-bottom: 16px;
}

.quote-author {
  font-size: 16px;
  font-weight: 600;
  color: #5a5a5a;
  font-style: normal;
}
```

---

### 12. Footer

```css
footer {
  background-color: #2d2d2d;
  color: #e8e4df;
  padding: 60px 40px 40px;
  margin-top: 120px;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
}

.footer-section h3 {
  font-size: 18px;
  font-weight: 700;
  color: #faf8f5;
  margin-bottom: 16px;
}

.footer-link {
  display: block;
  font-size: 15px;
  color: #e8e4df;
  text-decoration: none;
  margin-bottom: 8px;
  transition: color 0.2s;
}

.footer-link:hover {
  color: #d4763b;
}

.footer-bottom {
  max-width: 1200px;
  margin: 0 auto;
  padding-top: 32px;
  border-top: 1px solid #5a5a5a;
  text-align: center;
  font-size: 14px;
  color: #9ca3af;
}
```

---

## Responsive Breakpoints

```css
/* Mobile First Approach */

/* Small phones */
@media (max-width: 480px) {
  .hero h1 {
    font-size: 36px;
  }
  
  .content-wrapper {
    padding: 0 16px;
  }
}

/* Tablets */
@media (min-width: 768px) {
  .content-wrapper {
    padding: 0 32px;
  }
  
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .content-wrapper {
    padding: 0 40px;
  }
  
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

---

## Animation & Transitions

```css
/* Smooth transitions for interactive elements */
* {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

/* Fade in animation for page load */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in {
  animation: fadeIn 0.6s ease-out;
}

/* Hover states */
.hover-lift:hover {
  transform: translateY(-2px);
  transition: transform 0.2s ease;
}
```

---

## Accessibility Requirements

```css
/* Focus states must be visible */
*:focus {
  outline: 2px solid #d4763b;
  outline-offset: 2px;
}

/* Skip to content link */
.skip-to-content {
  position: absolute;
  top: -40px;
  left: 0;
  background: #d4763b;
  color: white;
  padding: 8px 16px;
  text-decoration: none;
  z-index: 100;
}

.skip-to-content:focus {
  top: 0;
}

/* Minimum contrast ratios */
/* All text must meet WCAG AA standards */
/* Body text: 4.5:1 minimum */
/* Large text (18px+): 3:1 minimum */
```

---

## Image Guidelines

**Photos to use:**
- Real construction photos (even if old)
- Your actual projects
- Tools and materials in use
- Progress photos showing phases

**Photos to AVOID:**
- Stock photos of models in hard hats
- Generic "happy homeowner" imagery
- Anything that looks staged

**Image specs:**
- Format: WebP with JPG fallback
- Max width: 1200px
- Compress for web (80-85% quality)
- Lazy load below the fold
- Always include alt text

---

## Content Guidelines

**Voice & Tone:**
- Professional but approachable
- "You" language (second person)
- Short paragraphs (2-4 sentences)
- Active voice over passive
- Avoid jargon (or explain it)
- Encourage and support

**Example Good:**
"You'll need to submit your plans to the building department. This usually takes 2-3 weeks, so plan accordingly."

**Example Bad:**
"Plans must be submitted to the appropriate municipal authority for review in accordance with local regulations."

---

## File Structure

```
app/
├── globals.css              (All CSS variables and base styles)
├── layout.tsx               (Root layout with header/footer)
├── page.tsx                 (Homepage)
├── about/
│   └── page.tsx
├── permitting/
│   ├── page.tsx            (Permitting overview)
│   ├── understanding-codes/
│   ├── permit-application/
│   └── ...
└── ...

components/
├── Header.tsx
├── Footer.tsx
├── CalloutBox.tsx          (InfoBox, Warning, Tip)
├── Checklist.tsx
├── StepGuide.tsx
├── Card.tsx
├── TableOfContents.tsx
├── ProgressBar.tsx
└── ...

styles/
├── components/
│   ├── Header.module.css
│   ├── Checklist.module.css
│   └── ...
```

---

## CRITICAL IMPLEMENTATION NOTES

1. **Mobile First:** Start with mobile design, scale up
2. **Readability is King:** 18px body text minimum, 1.7 line-height
3. **Generous Spacing:** Don't be afraid of white space
4. **Warm Colors:** This is about building a HOME, not a tech product
5. **Trust Signals:** Real photos, your experience, clear guidance
6. **Reduce Overwhelm:** Break content into digestible chunks
7. **Clear CTAs:** Always show next steps
8. **Fast Loading:** Optimize images, minimal JavaScript

---

## Testing Checklist

After implementation:
- [ ] Text is easily readable (18px+, good contrast)
- [ ] Colors feel warm and inviting (not cold/clinical)
- [ ] Spacing is generous (content has room to breathe)
- [ ] Navigation is simple and clear
- [ ] CTAs stand out but aren't aggressive
- [ ] Mobile experience is excellent
- [ ] Long articles have table of contents
- [ ] Checklists are interactive and satisfying
- [ ] Images load fast and look professional
- [ ] Overall vibe is "trustworthy expert" not "corporate website"

---

## Success Criteria

A visitor should think:
✅ "This person really knows what they're talking about"
✅ "I feel confident I can do this"
✅ "This is well-organized and easy to follow"
✅ "I trust this guidance"

NOT:
❌ "This looks like every other generic website"
❌ "This is overwhelming"
❌ "I can't read this (too small, poor contrast)"
❌ "This feels cold and impersonal"

---

The design should fade into the background and let your expertise and guidance shine through. Warm, trustworthy, actionable - like the best mentor you could ask for.
