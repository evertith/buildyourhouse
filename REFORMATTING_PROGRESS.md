# Content Reformatting Progress

## Project Overview

Converting all Build-Your-House.com content pages from basic markdown to professional, scannable documentation with:
- HTML tables (with `className="dataTable"`)
- CalloutBox components (type: "tip", "warning", "info")
- Interactive Checklist components (with localStorage persistence)
- StepGuide components for processes
- Improved visual hierarchy and scannability
- Maximum 3-4 sentences per paragraph

## Completed Pages (13 Total)

### Permitting Section (6 pages)
1. ✅ `/src/app/feasibility/time-commitment/page.mdx`
2. ✅ `/src/app/permitting/page.mdx`
3. ✅ `/src/app/permitting/permit-application-process/page.mdx`
4. ✅ `/src/app/permitting/working-with-building-department/page.mdx`
5. ✅ `/src/app/permitting/common-permit-mistakes/page.mdx`
6. ✅ `/src/app/permitting/understanding-building-codes/page.mdx`

### Inspections Section (7 pages - COMPLETE!)
7. ✅ `/src/app/inspections/page.mdx`
8. ✅ `/src/app/inspections/foundation-inspection/page.mdx`
9. ✅ `/src/app/inspections/framing-inspection/page.mdx`
10. ✅ `/src/app/inspections/common-inspection-failures/page.mdx`
11. ✅ `/src/app/inspections/insulation-inspection/page.mdx`
12. ✅ `/src/app/inspections/rough-in-inspections/page.mdx` (950 lines)
13. ✅ `/src/app/inspections/final-inspection/page.mdx` (953 lines)

## Remaining Work

### Inspections Section
- ✅ COMPLETE! All 7 inspection pages reformatted

### Subcontractor Pages (9 pages)
Find with: `src/app/subcontractors/**/page.mdx`

### Timing & Scheduling Pages
Find with: `src/app/timing-scheduling/**/page.mdx`

### Feasibility Pages (remaining)
Find with: `src/app/feasibility/**/page.mdx`

### Build Phase Pages
Find with: `src/app/build-phases/**/page.mdx`

## Reformatting Patterns

### CalloutBox Usage
```mdx
<CalloutBox type="warning" title="Title Here">
Content with **markdown** support
</CalloutBox>

<CalloutBox type="tip" title="Pro Tip">
Helpful advice
</CalloutBox>

<CalloutBox type="info" title="Important">
Key information
</CalloutBox>
```

### Checklist Component
```mdx
<Checklist
  title="Descriptive Title"
  storageKey="unique-localStorage-key"
  items={[
    'Item 1 description',
    'Item 2 description',
    'Item 3 description'
  ]}
/>
```

### StepGuide Component
```mdx
<StepGuide
  steps={[
    {
      title: 'Step Title',
      description: <>Text with optional <strong>JSX</strong></>
    },
    {
      title: 'Another Step',
      description: <>More content</>
    }
  ]}
/>
```

### HTML Table Pattern
```mdx
<table className="dataTable">
  <thead>
    <tr>
      <th>Column 1</th>
      <th>Column 2</th>
      <th>Cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data</td>
      <td>More data</td>
      <td className="numeric">$1,000</td>
    </tr>
    <tr className="totalRow">
      <td><strong>TOTAL</strong></td>
      <td></td>
      <td className="numeric"><strong>$5,000</strong></td>
    </tr>
  </tbody>
</table>
```

## Key Principles

1. **Always read file first** before editing
2. **Convert ALL pipe-delimited tables** to HTML with dataTable className
3. **Add CalloutBoxes** for warnings, tips, and important info
4. **Convert checklists** to interactive Checklist components
5. **Add StepGuides** for multi-step processes
6. **Break up long paragraphs** into 2-4 sentence chunks
7. **Improve heading hierarchy** for scannability
8. **Use numeric className** for right-aligned number columns
9. **Use totalRow className** for sum/total rows

## Common Patterns to Look For

### In Original Files
- Pipe-delimited tables: `| Header | Header |`
- Markdown checklists: `- [ ] Item`
- Numbered processes: `1. Step one`
- Long paragraphs (more than 4-5 sentences)
- Important warnings buried in text
- Tips that should stand out

### What to Convert Them To
- Tables → HTML `<table className="dataTable">`
- Checklists → `<Checklist>` component
- Processes → `<StepGuide>` component
- Long paragraphs → Break into 2-3 sentence chunks
- Warnings → `<CalloutBox type="warning">`
- Tips → `<CalloutBox type="tip">`

## Finding Pages to Reformat

```bash
# Find all inspection pages
find src/app/inspections -name "page.mdx"

# Find all subcontractor pages
find src/app/subcontractors -name "page.mdx"

# Find all pages in a section
find src/app/[section-name] -name "page.mdx"

# Count lines in a file
wc -l path/to/file.mdx

# Find checklists and tables
grep -n "^-\s\[\s\]\|^|\s" path/to/file.mdx
```

## Components Available

All components are configured in `/src/mdx-components.tsx` and available globally in MDX files:
- `CalloutBox` - from `/src/components/CalloutBox.tsx`
- `Checklist` - from `/src/components/Checklist.tsx`
- `StepGuide` - from `/src/components/StepGuide.tsx`
- `Card` - from `/src/components/Card.tsx`

## CSS Styling

Table styling defined in `/src/styles/article.module.css`:
- `.dataTable` - Main table styling
- `.numeric` - Right-aligned numeric columns
- `.totalRow` - Highlighted total/sum rows

## Development Server

Dev server should be running on port 3000:
```bash
npm run dev
```

Check for errors after making changes. The build should complete without errors.

## Next Session Action Plan

1. **Complete remaining 2 inspection pages** (rough-in and final)
2. **Find and list all subcontractor pages**
3. **Reformat subcontractor pages** one by one with same quality
4. **Move to timing & scheduling section**
5. **Continue through remaining sections**

## Quality Checklist for Each Page

- [ ] Added CalloutBox for warnings/tips/info
- [ ] Converted ALL tables to HTML
- [ ] Converted checklists to Checklist component
- [ ] Added StepGuide for multi-step processes
- [ ] Broke up long paragraphs
- [ ] Improved heading hierarchy
- [ ] File compiles without errors
- [ ] Page is scannable (can understand from headings alone)

## User Approval Quote

User explicitly requested **"Option 1: high quality one-by-one"** approach.

Initial page (Time Commitment) was approved with: **"Yeah, that looks much better. Proceed"**

## Session Statistics

### Current Session (Session 2)
- **Pages completed this session**: 2 (rough-in-inspections, final-inspection)
- **Total pages completed**: 13
- **Token usage**: ~118k of 200k (59%)
- **Average quality**: High - comprehensive reformatting with tables, checklists, callouts
- **Build status**: Clean - no compilation errors
- **Estimated remaining**: 20-30 pages across multiple sections

### Cumulative Progress
- **Permitting Section**: 6/6 pages (100% complete)
- **Inspections Section**: 7/7 pages (100% complete) ✨
- **Overall completion**: ~35% of estimated total content

## Latest Updates (Current Session)

### Rough-In Inspections Page
**Reformatting completed**:
- ✅ 8 interactive Checklist components
- ✅ 5 HTML tables (electrical/plumbing/HVAC failures, cost of delay, regional variations)
- ✅ 8 CalloutBox components (warnings and tips)
- ✅ 1 StepGuide component
- ✅ 950 lines fully reformatted

**Key improvements**:
- Converted Top 10 Electrical Failures to scannable table
- Converted Top 10 Plumbing Failures to scannable table
- Converted Top 5 HVAC Failures to scannable table
- Created comprehensive pre-inspection checklists
- Added critical warnings for shower pan testing and AFCI/GFCI requirements

### Final Inspection Page
**Reformatting completed**:
- ✅ 4 interactive Checklist components (37 total items)
- ✅ 3 HTML tables (Top 15 failures, common fixes, cost breakdown)
- ✅ 6 CalloutBox components
- ✅ 2 StepGuide components
- ✅ 953 lines fully reformatted

**Key improvements**:
- Top 15 Final Inspection Failures in comprehensive table format
- Safety Items checklist (most critical for passing)
- Step-by-step prioritization guide for corrections
- Re-inspection process guide
- Pro tips for passing on first try
