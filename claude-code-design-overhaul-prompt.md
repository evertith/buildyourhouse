# PROMPT FOR CLAUDE CODE: Build-Your-House.com Design Overhaul

## Context

The build-your-house.com website has good content but needs a complete design overhaul. This is a guide for couples planning to build their own homes - one of the biggest decisions of their lives. The design must feel warm, trustworthy, and professional.

## Your Task

Completely redesign build-your-house.com following the attached design system specification. This is NOT a tech/calculator site - it's an expert guide that needs to inspire confidence and reduce overwhelm.

---

## Design Philosophy

**Think:** Professional contractor who's also a great teacher
**NOT:** Corporate website or tech startup

The design should:
- Feel WARM and INVITING (like coming home)
- Build TRUST and CONFIDENCE (expert guidance)
- Be CLEAR and APPROACHABLE (not overwhelming)
- Prioritize READABILITY (long-form content)

---

## Color Palette (CRITICAL - Use These Exact Colors)

```css
/* Copy this into your globals.css */
:root {
  /* Backgrounds */
  --bg-primary: #faf8f5;        /* Warm off-white */
  --bg-secondary: #f0ede8;      /* Card backgrounds */
  --bg-tertiary: #e8e4df;       /* Borders, dividers */
  
  /* Text */
  --text-primary: #2d2d2d;      /* Body text */
  --text-secondary: #5a5a5a;    /* Secondary text */
  --text-heading: #1a1a1a;      /* Headings */
  
  /* Accents */
  --accent-primary: #d4763b;    /* Construction orange - CTAs */
  --accent-secondary: #5b8a72;  /* Sage green - tips, success */
  --accent-warning: #e67e22;    /* Warnings */
  --accent-info: #3b7dbd;       /* Info boxes */
  
  /* Interactive */
  --link-color: #c75f32;
  --link-hover: #a84d27;
  --button-primary: #d4763b;
  --button-primary-hover: #c75f32;
}
```

---

## Typography (CRITICAL - Readability First)

```css
/* Base styles */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 18px;              /* NOT 16px - must be readable */
  line-height: 1.7;             /* Generous for long reading */
  color: var(--text-primary);
  background-color: var(--bg-primary);
}

h1 {
  font-size: 48px;
  font-weight: 700;
  line-height: 1.2;
  color: var(--text-heading);
  margin-bottom: 24px;
}

h2 {
  font-size: 36px;
  font-weight: 700;
  line-height: 1.3;
  color: var(--text-heading);
  margin-top: 60px;
  margin-bottom: 24px;
}

h3 {
  font-size: 28px;
  font-weight: 600;
  line-height: 1.4;
  color: var(--text-primary);
  margin-top: 40px;
  margin-bottom: 16px;
}

p {
  margin-bottom: 20px;
  max-width: 800px;  /* Comfortable reading width */
}
```

---

## Layout Structure

```css
/* Main content container */
.content-wrapper {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}

/* For wider content like tables */
.wide-content {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}
```

---

## Components to Create

### 1. Header Component

**Requirements:**
- Sticky at top
- Logo/site name on left: "Build Your House"
- Navigation links on right: Home, Guides, Resources, About
- Light background with subtle border
- Mobile: hamburger menu

**Styling:**
```css
header {
  background: var(--bg-primary);
  border-bottom: 1px solid var(--bg-tertiary);
  padding: 20px 40px;
  position: sticky;
  top: 0;
  z-index: 100;
}
```

---

### 2. Hero Section (Homepage)

**Content:**
```
Headline: "Build Your Own House and Save $50,000+"
Subtitle: "Complete guide from a licensed general contractor with 20+ years experience"
CTA Buttons: "Start Here" (primary) and "Browse Guides" (secondary)
```

**Styling:**
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
  color: var(--text-heading);
  margin-bottom: 24px;
}
```

---

### 3. CalloutBox Component (Multiple Types)

**Pro Tip Box (Green):**
```tsx
interface CalloutBoxProps {
  type: 'tip' | 'warning' | 'info';
  title: string;
  children: React.ReactNode;
}

// Styling for tip box
background: #f0f5f2;
border-left: 4px solid #5b8a72;
icon: 💡
```

**Warning Box (Orange):**
```
background: #fef5f0;
border-left: 4px solid #e67e22;
icon: ⚠️
```

**Info Box (Blue):**
```
background: #f0f5fa;
border-left: 4px solid #3b7dbd;
icon: ℹ️
```

---

### 4. Checklist Component

**Requirements:**
- Interactive checkboxes (save state to localStorage)
- Green checkmarks when checked
- Strikethrough text when checked
- Clean, satisfying interaction

**Example usage:**
```tsx
<Checklist title="Permitting Checklist">
  <ChecklistItem>Submit building plans to department</ChecklistItem>
  <ChecklistItem>Schedule plan review meeting</ChecklistItem>
  <ChecklistItem>Address any plan corrections</ChecklistItem>
</Checklist>
```

---

### 5. StepGuide Component

**Visual:**
```
[1] ──────  Step Title
            Step description and details
            
[2] ──────  Next Step Title
│           Details about this step
│           
[3] ──────  Final Step
            Conclusion
```

**Styling:**
- Orange numbered circles
- Connecting line between steps
- Clear hierarchy

---

### 6. Button Components

**Primary Button:**
```css
.button-primary {
  padding: 16px 32px;
  background-color: var(--accent-primary);
  color: white;
  font-size: 18px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(212, 118, 59, 0.2);
}

.button-primary:hover {
  background-color: var(--button-primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(212, 118, 59, 0.3);
}
```

**Secondary Button:**
```css
.button-secondary {
  padding: 16px 32px;
  background-color: transparent;
  color: var(--accent-primary);
  border: 2px solid var(--accent-primary);
  /* ... */
}
```

---

### 7. Card Component (for content grids)

**Use for:**
- Topic overview grids on homepage
- Resource listings
- Guide categories

**Styling:**
```css
.card {
  background: white;
  border: 1px solid var(--bg-tertiary);
  border-radius: 8px;
  padding: 32px;
  transition: all 0.2s;
}

.card:hover {
  border-color: var(--accent-primary);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transform: translateY(-4px);
}
```

---

### 8. TableOfContents Component

**For long articles:**
- Sticky sidebar OR top of article
- Auto-generated from h2/h3 tags
- Smooth scroll to sections
- Highlight current section

---

### 9. Footer Component

**Content:**
- Dark background (#2d2d2d)
- Light text
- 3-4 column layout
- Links to main sections
- Copyright info
- "Built with expertise by a licensed GC"

---

## Page Templates to Create

### Homepage Template

**Structure:**
1. Hero section (headline + CTA)
2. Brief intro (2-3 paragraphs)
3. Main topic cards (grid)
   - Permitting & Inspections
   - Finding Subcontractors
   - Timing & Scheduling
   - Build Phases
   - Tools & Equipment
   - Calculators
4. Why trust this guide section
5. CTA section

---

### Article/Guide Template

**Structure:**
1. Breadcrumb navigation
2. Article title (h1)
3. Last updated date
4. Table of contents (for long articles)
5. Content with proper heading hierarchy
6. Callout boxes where appropriate
7. Checklists where appropriate
8. Related articles section
9. CTA (consulting offer, email signup, etc.)

---

## Implementation Priority

### Phase 1: Foundation (Do First)
1. ✅ Set up color system in globals.css
2. ✅ Set up typography system
3. ✅ Create base layout (header, footer, container)
4. ✅ Redesign homepage with hero section

### Phase 2: Components (Do Second)
5. ✅ Create CalloutBox component (tip, warning, info)
6. ✅ Create Button components
7. ✅ Create Card component
8. ✅ Create Checklist component
9. ✅ Create StepGuide component

### Phase 3: Content Pages (Do Third)
10. ✅ Create article/guide template
11. ✅ Add TableOfContents to long articles
12. ✅ Apply new design to all content pages
13. ✅ Add breadcrumb navigation

### Phase 4: Polish (Do Last)
14. ✅ Add smooth transitions
15. ✅ Test mobile responsiveness
16. ✅ Optimize images
17. ✅ Add loading states if needed

---

## Mobile Responsiveness

**Breakpoints:**
```css
/* Mobile first */
@media (max-width: 640px) {
  h1 { font-size: 36px; }
  .hero h1 { font-size: 40px; }
  .content-wrapper { padding: 0 16px; }
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

---

## Content Migration

**For each existing page:**
1. Wrap in proper layout template
2. Apply typography styles
3. Add appropriate callout boxes where content needs emphasis
4. Convert any lists to proper checklists where applicable
5. Add table of contents if article is long (>1000 words)
6. Ensure proper heading hierarchy (h1 → h2 → h3)
7. Add breadcrumbs
8. Add "last updated" date

---

## What NOT to Do

❌ Don't use dark backgrounds (this isn't calculily)
❌ Don't use tiny text (18px minimum!)
❌ Don't use aggressive/bright colors
❌ Don't cram content together
❌ Don't use generic stock photos
❌ Don't make it look "corporate"
❌ Don't overwhelm with too many options
❌ Don't forget mobile users

---

## Success Criteria

After implementation, the site should:
✅ Feel warm and inviting (like a trusted mentor)
✅ Be easy to read (18px text, good spacing)
✅ Look professional but approachable
✅ Have clear visual hierarchy
✅ Guide users naturally to next steps
✅ Work perfectly on mobile
✅ Load fast
✅ Inspire confidence

**A visitor should think:**
"This person really knows what they're talking about, and I feel confident I can do this."

**NOT:**
"This looks like every other generic website" or "I can't read this."

---

## Testing Checklist

Before considering complete:
- [ ] Text is 18px or larger
- [ ] Colors match the warm palette (no dark theme)
- [ ] Spacing is generous (not cramped)
- [ ] All buttons have proper hover states
- [ ] Mobile navigation works (hamburger menu)
- [ ] All cards have hover effects
- [ ] Checklists are interactive
- [ ] Long articles have table of contents
- [ ] Footer has all required links
- [ ] Site loads in under 2 seconds
- [ ] No console errors
- [ ] Breadcrumbs work on all pages

---

## Reference Files

I've provided:
1. Complete design system specification (build-your-house-design-system.md)
2. This implementation prompt

Read the design system doc for detailed specifications on every component.

---

## Start Here

1. **First, show me the updated homepage** before proceeding
   - I want to see: hero section, color palette, typography, overall vibe
   - Get approval before updating all pages

2. **Then show me one article page** with the new template
   - Should have: proper layout, callout boxes, good typography
   - Get approval before migrating all content

3. **Then complete the full migration**
   - All pages using new design
   - All components implemented
   - Mobile tested

---

## Key Principle

**The design should get OUT OF THE WAY and let the expertise shine.**

This is NOT about flashy design. It's about:
- Making content easy to read
- Building trust through professionalism
- Reducing overwhelm through clarity
- Guiding people to success

Think: "The best textbook you've ever read" not "The flashiest website."

Warm. Trustworthy. Clear. Actionable.

Let's build something that actually helps people achieve their dreams of building their own home.

---

BEGIN IMPLEMENTATION. Show me homepage first.
