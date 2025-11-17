# Content Creation Guide for Build-Your-House.com

This guide will help you efficiently create the remaining 50+ pages for the website.

## Content Templates

### Template 1: Guide Page (MDX)

Use this for educational content like guides, how-tos, and explanations.

```mdx
export const metadata = {
  title: '[Topic] Guide | Build-Your-House.com',
  description: 'Clear, specific description under 160 characters that includes target keyword',
};

# [Topic] - Clear, Benefit-Driven Title

Brief introduction (1-2 paragraphs) that explains:
- What this guide covers
- Why it matters to owner-builders
- What they'll learn

## Overview

High-level explanation of the topic.

## Why This Matters

Explain the consequences of getting it wrong and benefits of getting it right. Use real numbers:
- Cost implications: "$X saved" or "$Y wasted"
- Time impact: "2 weeks delay" or "Pass first try"
- Real examples from your experience

## Step-by-Step Process

### Step 1: [Action]
Clear, actionable instructions.

**What you need:**
- List of materials/info/resources

**Common mistakes:**
- ❌ Don't do this
- ✅ Do this instead

### Step 2: [Next Action]
Continue the pattern...

## Expert Tips

Share your real GC experience:
- "I've seen..." stories
- "On a recent build..." examples
- Specific numbers and timelines

## Common Questions

### Question 1?
Clear answer with specifics.

### Question 2?
Clear answer with specifics.

## What Can Go Wrong

List the top 5 mistakes and how to avoid them:

1. **Mistake**: Description
   - **Why it happens**: Reason
   - **How to avoid**: Solution
   - **Cost if you don't**: Specific impact

## Checklist

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

## Related Resources

- [Link to related guide](/path)
- [Link to calculator](/calculators/relevant)
- [Link to state guide](/state-guides/state)

## Need Help?

Brief CTA about consulting services.

[Schedule a Consultation](/consulting)
```

### Template 2: Inspection Guide

```mdx
export const metadata = {
  title: '[Phase] Inspection Guide - Pass on First Try',
  description: 'Complete guide to passing your [phase] inspection. Learn what inspectors check and common failure points.',
};

# [Phase] Inspection Guide

## When to Schedule

- Timing in build sequence
- How much advance notice needed
- What must be complete
- What must NOT be complete yet

## What the Inspector Checks

### Critical Items
1. **Item**: What they're looking for, code reference
2. **Item**: What they're looking for, code reference

### Common Check Points
- Bullet list of typical inspection points

## Before the Inspector Arrives

Prepare your site:
- [ ] Checklist item
- [ ] Checklist item
- [ ] Have permit posted
- [ ] Have plans on site

## During the Inspection

Best practices:
- Be present
- Be prepared to answer questions
- Have work lights ready
- Take notes

## Top 10 Failure Points

Based on actual GC experience:

1. **Failure**: [Specific issue]
   - **Code requirement**: [Reference]
   - **How to fix**: [Solution]
   - **Time to re-inspect**: [Timeline]

[Continue for all 10...]

## If You Fail

1. Don't panic - it happens to pros
2. Get specifics on what needs fixing
3. Fix it properly
4. Document with photos
5. Call for re-inspection

Re-inspection timeline: typically 1-3 days

## Photos: Pass vs. Fail

[Describe what good vs bad looks like for key items]

## Cost of Delay

If inspection fails:
- Re-inspection fee: $X-Y
- Delay to schedule: Z days
- Subcontractor delays: $X per day
- Total potential cost: $XX-XXX

## Related Inspections

- [Previous inspection](/inspections/previous)
- [Next inspection](/inspections/next)

## Need Pre-Inspection Review?

Consider our [on-site inspection prep service](/consulting).
```

### Template 3: Build Phase Guide

```mdx
export const metadata = {
  title: '[Phase Name] - Complete Owner-Builder Guide',
  description: '[Phase] guide for owner-builders. Timeline, costs, DIY difficulty, and step-by-step instructions.',
};

# [Phase Name]: Complete Guide

## Overview

- **Typical Duration**: X-Y weeks
- **DIY Difficulty**: ⭐⭐⭐☆☆ (3/5)
- **Typical Cost**: $X,000-Y,000
- **When to Hire**: Recommendation
- **Required Inspection**: Yes/No

## When This Phase Happens

Position in overall build sequence.

**Must be complete first:**
- Previous phase
- Related work

**Can happen in parallel:**
- Other work if any

## Should You DIY This Phase?

### DIY If:
- You have these skills
- You have these tools
- You have this much time

### Hire Out If:
- Conditions when hiring makes sense
- Specialized equipment needed
- Code/liability concerns

**My recommendation**: Specific advice based on experience

## Materials Needed

### Primary Materials
| Item | Quantity (per sq ft) | Typical Cost | Notes |
|------|---------------------|--------------|-------|
| Material | Amount | $X | Details |

### Tools Required
**Essential:**
- Tool 1
- Tool 2

**Nice to have:**
- Tool 3

**Specialized (rent):**
- Equipment

[Link to tool buying guide](/tools-and-equipment/[relevant])

## Step-by-Step Process

### Day 1-3: [Sub-phase]
Detailed instructions...

### Day 4-7: [Sub-phase]
Continue...

## Code Requirements

Key code items to follow:
- IRC Section X.X.X: [Requirement]
- IRC Section Y.Y.Y: [Requirement]

## Subcontractor Considerations

If hiring this out:

**What to look for:**
- Qualifications
- Experience indicators
- Red flags

**Typical pricing:**
- $X-Y per [unit]
- Total project: $X,000-Y,000

**Timeline:**
- Lead time to book: X weeks
- Duration once started: Y days

## Common Mistakes

1. **Mistake**: What people do wrong
   - **Why it's a problem**: Impact
   - **How to avoid**: Solution

[Continue for top 5-10 mistakes]

## Quality Checkpoints

Before moving to next phase, verify:
- [ ] Checkpoint 1
- [ ] Checkpoint 2
- [ ] Ready for inspection

## Budget Breakdown

Example for 2,000 sq ft home:

| Item | Cost | Notes |
|------|------|-------|
| Materials | $X,XXX | Description |
| Labor (if hiring) | $X,XXX | Description |
| Equipment rental | $XXX | Description |
| **Total** | **$X,XXX** | |

## Timeline Tips

- Best season: [Season]
- Weather considerations: [Issues]
- Scheduling with other trades: [Conflicts]

## Photos & Diagrams

[Descriptions of what to show]

## What Comes Next

After completing this phase:
1. [Next step]
2. [Inspection if needed]
3. [Next phase]

Link to: [Next Build Phase](/build-phases/next-phase)

## Calculator

Use our [Material Estimator](/calculators/material-estimator) for this phase.

## Questions?

[Link to consulting](/consulting) for personalized guidance.
```

## Writing Guidelines

### Voice & Tone
- **Authoritative but accessible**: "Here's what works based on building hundreds of homes"
- **Encouraging**: "Most people can do this with proper preparation"
- **Realistic**: "This will take longer than you think, and that's normal"
- **Practical**: Always include specific numbers, timelines, costs

### Use Real Numbers
❌ "It takes a while"
✅ "Plan for 4-6 weeks for a 2,000 sq ft home"

❌ "You'll save money"
✅ "Typical savings: $45,000-$60,000 on a $300,000 home (15-20% GC fee)"

❌ "Make sure it's strong enough"
✅ "Use 2x10 joists at 16" OC for a 14' span per IRC Table R502.3.1(1)"

### Include Warnings
Use callout format for critical information:

```markdown
⚠️ **WARNING**: Never cover work before inspection. This will fail and require expensive tear-out.

🚨 **CRITICAL**: Structural changes require permit amendments. Inspectors will red-tag unpermitted changes.

💡 **TIP**: Schedule your inspection for early morning. Inspectors are fresher and take more time.
```

### SEO Best Practices

Every page needs:

1. **Title**: 50-60 characters
   - Include target keyword
   - Make it benefit-driven
   - Format: "[Topic] - [Benefit] | Build-Your-House.com"

2. **Description**: 150-160 characters
   - Include target keyword
   - Explain what they'll learn
   - Include a benefit or number

3. **Headings**:
   - One H1 (page title)
   - Multiple H2s (major sections)
   - H3s and H4s as needed (subsections)

4. **Internal Links**:
   - Link to 3-5 related pages
   - Link to relevant calculators
   - Link to consulting when appropriate

5. **Keywords**:
   - Use naturally in content
   - Include in first paragraph
   - Use variations throughout

### Content Length Guidelines

- **Major guides**: 2,000-3,000 words
- **Build phase guides**: 1,500-2,500 words
- **Inspection guides**: 1,000-1,500 words
- **Calculators**: 500-1,000 words + tool
- **Checklists**: 500-800 words + list

## Quick Creation Workflow

1. **Choose template** based on content type
2. **Research** if needed (codes, costs, timelines)
3. **Write outline** - fill in all headings first
4. **Add content** - fill in each section
5. **Add specifics** - real numbers, examples, stories
6. **Add links** - internal links to related content
7. **Review SEO** - title, description, keywords
8. **Test locally** - `npm run dev`
9. **Commit** - descriptive commit message

## Content Priorities

Based on your plan, create content in this order:

### Week 1 (High Priority)
1. Feasibility pages (complete the section)
2. Permitting guides (critical pain point)
3. Inspection overview

### Week 2 (High Priority)
1. Subcontractor guides (critical pain point)
2. Common inspection failures
3. State guide: North Carolina (your state)

### Week 3-4 (Medium Priority)
1. Individual inspection guides
2. Timing/scheduling section
3. First 5 build phase guides

### Week 5-8 (Medium Priority)
1. Remaining build phase guides
2. Tool guides
3. Blog posts

### Week 9-10 (Lower Priority)
1. Additional state guides
2. Resources/templates
3. Glossary

## Efficiency Tips

### Batch Similar Content
- Write all inspection guides in one session
- Write all subcontractor guides together
- Build all calculators in one sprint

### Reuse Structures
- Copy template
- Change headings to match topic
- Fill in content
- This is faster than starting from scratch

### Use AI Assistance
You can use AI to:
- Generate initial outlines
- Research code requirements
- Draft sections
- **BUT**: Always add your real GC experience and specific numbers

### Track Progress
Mark completed pages in the README checklist:
```markdown
- [x] Page completed
- [ ] Page still needed
```

## Quality Checklist

Before considering a page complete:

- [ ] Has proper metadata (title, description)
- [ ] Title is benefit-driven and includes keyword
- [ ] First paragraph explains what/why/benefit
- [ ] Includes real numbers (costs, timelines)
- [ ] Has your GC experience/stories
- [ ] Includes specific examples
- [ ] Has internal links to 3-5 related pages
- [ ] Has clear headings (H2, H3 structure)
- [ ] Includes CTAs (consulting, calculators)
- [ ] Mobile-friendly (test on phone)
- [ ] No spelling/grammar errors
- [ ] Builds successfully (`npm run build`)

## Example: Fast Page Creation

Let's say you need to create "Finding Quality Subcontractors"

1. **Copy template** (15 seconds)
```bash
touch src/app/subcontractors/finding-quality-subs/page.mdx
```

2. **Add metadata** (1 minute)
```mdx
export const metadata = {
  title: 'Finding Quality Subcontractors - Owner Builder Guide',
  description: 'Learn how to find, evaluate, and select quality subcontractors for your owner-builder project. Insider tips from a licensed GC.',
};
```

3. **Write outline** (5 minutes)
- Where to look
- Red flags to avoid
- Green flags to seek
- Questions to ask
- Your experience finding subs

4. **Fill in content** (30 minutes)
Add your real GC knowledge and specific examples

5. **Add links** (3 minutes)
Link to vetting guide, contract guide, calculator

6. **Test** (2 minutes)
```bash
npm run dev
```

Total time: **~40 minutes per page**

At this pace:
- 1 page/day = 50 days
- 2 pages/day = 25 days (5 work weeks)
- 3 pages/day = 17 days (3.5 work weeks)

## Next Steps

1. Review the templates above
2. Start with highest-priority content
3. Use batch creation for efficiency
4. Track your progress in README
5. Test locally as you go
6. Deploy when you have 20-30 pages

The foundation is built. Now it's about creating content consistently using these patterns.
