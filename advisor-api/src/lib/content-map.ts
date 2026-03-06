// Maps build phases, topics, and states to relevant site content
// This is used to inject relevant guide content into the chat context

export interface ContentChunk {
  title: string;
  path: string;
  summary: string;
  category: 'phase' | 'inspection' | 'permitting' | 'planning' | 'subcontractor' | 'timing' | 'tools' | 'resources' | 'blog';
  phase?: string;
  state?: string;
}

export const PHASES = [
  'researching', 'planning', 'permitting', 'site-preparation', 'foundation',
  'framing', 'roofing', 'windows-and-doors', 'rough-in', 'insulation',
  'drywall', 'interior-trim', 'painting', 'flooring', 'kitchen-and-bath',
  'final-finishes', 'landscaping', 'move-in',
] as const;

export type Phase = typeof PHASES[number];

export const STATES = [
  'arizona', 'california', 'colorado', 'florida', 'georgia',
  'north-carolina', 'tennessee', 'texas', 'virginia', 'washington',
] as const;

export const STATE_DISPLAY_NAMES: Record<string, string> = {
  'arizona': 'Arizona',
  'california': 'California',
  'colorado': 'Colorado',
  'florida': 'Florida',
  'georgia': 'Georgia',
  'north-carolina': 'North Carolina',
  'tennessee': 'Tennessee',
  'texas': 'Texas',
  'virginia': 'Virginia',
  'washington': 'Washington',
};

// Content chunks organized by category
// In a future version, these summaries would be full extracted text from the MDX pages
// For now, they provide enough context for the AI to give relevant answers
const CONTENT: ContentChunk[] = [
  // Build phases
  { title: 'Site Preparation', path: '/build-phases/site-preparation', summary: 'Clearing, grading, excavation, utility trenching. Costs $1,500-$30,000+. First phase of construction. Includes tree removal, soil testing, erosion control.', category: 'phase', phase: 'site-preparation' },
  { title: 'Foundation Construction', path: '/build-phases/foundation', summary: 'Slab, crawl space, and basement foundations. Costs $4,000-$30,000+. Includes footings, rebar, concrete pouring, waterproofing, anchor bolts. Critical to get right.', category: 'phase', phase: 'foundation' },
  { title: 'House Framing', path: '/build-phases/framing', summary: 'Floor, wall, and roof framing. Lumber types, header sizing, load paths, sheathing. Costs $20,000-$50,000+ for materials and labor.', category: 'phase', phase: 'framing' },
  { title: 'Roofing', path: '/build-phases/roofing', summary: 'Shingle, metal, tile roofing. Underlayment, flashing, ridge vents, ice and water shield. Most owner-builders hire this out.', category: 'phase', phase: 'roofing' },
  { title: 'Windows and Doors', path: '/build-phases/windows-and-doors', summary: 'Window and door installation, flashing, weatherproofing. Energy ratings, sizing, ordering lead times.', category: 'phase', phase: 'windows-and-doors' },
  { title: 'Rough-In Overview', path: '/build-phases/rough-in', summary: 'Coordinating plumbing, electrical, HVAC rough-ins. Trade sequencing, inspection prep. All three must pass before insulation.', category: 'phase', phase: 'rough-in' },
  { title: 'Electrical Rough-In', path: '/build-phases/electrical-rough-in', summary: 'Panel sizing, circuit planning, wire types, NEC code. Box placement, GFCI/AFCI requirements, low voltage prewire.', category: 'phase', phase: 'rough-in' },
  { title: 'Plumbing Rough-In', path: '/build-phases/plumbing-rough-in', summary: 'Water supply lines, DWV system, venting, water heater rough-in. Pipe types, code requirements, pressure testing.', category: 'phase', phase: 'rough-in' },
  { title: 'HVAC Installation', path: '/build-phases/hvac-installation', summary: 'System sizing (Manual J), ductwork design, equipment selection. Central air, mini-splits, heat pumps compared.', category: 'phase', phase: 'rough-in' },
  { title: 'Insulation', path: '/build-phases/insulation', summary: 'Fiberglass batts, spray foam, blown-in. R-values by climate zone, air sealing, vapor barriers. Good DIY candidate.', category: 'phase', phase: 'insulation' },
  { title: 'Drywall', path: '/build-phases/drywall', summary: 'Hanging, taping, mudding, sanding. Finish levels 1-5. Costs per sheet, tools needed. Labor intensive.', category: 'phase', phase: 'drywall' },
  { title: 'Interior Trim', path: '/build-phases/interior-trim', summary: 'Baseboards, door casings, window trim, crown molding. Material types, tools, installation techniques.', category: 'phase', phase: 'interior-trim' },
  { title: 'Painting', path: '/build-phases/painting', summary: 'Interior and exterior painting. Surface prep, primer selection, costs per room. Good DIY task to save money.', category: 'phase', phase: 'painting' },
  { title: 'Flooring', path: '/build-phases/flooring', summary: 'Hardwood, tile, LVP, carpet compared. Costs per sq ft, durability, installation difficulty. Subfloor preparation.', category: 'phase', phase: 'flooring' },
  { title: 'Kitchen and Bath', path: '/build-phases/kitchen-and-bath', summary: 'Cabinets, countertops, tile work, plumbing fixtures. Most expensive finish phase. 6-12 week cabinet lead times.', category: 'phase', phase: 'kitchen-and-bath' },
  { title: 'Final Finishes', path: '/build-phases/final-finishes', summary: 'Hardware, light fixtures, appliance installation, touch-ups, punch list. Last steps before final inspection.', category: 'phase', phase: 'final-finishes' },
  { title: 'Landscaping', path: '/build-phases/landscaping', summary: 'Final grading, drainage, driveways, walkways, seeding/sodding. Required for CO in most jurisdictions.', category: 'phase', phase: 'landscaping' },

  // Inspections
  { title: 'Building Inspections Overview', path: '/inspections', summary: 'All inspections during residential construction: foundation, framing, rough-in (electrical, plumbing, HVAC), insulation, final. How to schedule and prepare.', category: 'inspection' },
  { title: 'Foundation Inspection', path: '/inspections/foundation-inspection', summary: 'What foundation inspectors check: footings, rebar, anchor bolts, waterproofing, setbacks. Common failures and how to prepare.', category: 'inspection', phase: 'foundation' },
  { title: 'Framing Inspection', path: '/inspections/framing-inspection', summary: 'Framing inspection checklist: structural connections, sheathing nailing, headers, load paths. IRC code references for common violations.', category: 'inspection', phase: 'framing' },
  { title: 'Rough-In Inspections', path: '/inspections/rough-in-inspections', summary: 'Electrical, plumbing, HVAC rough-in inspections. What each trade inspector checks. Must pass all three before insulation.', category: 'inspection', phase: 'rough-in' },
  { title: 'Insulation Inspection', path: '/inspections/insulation-inspection', summary: 'Energy code compliance: R-values by climate zone, air sealing, vapor barriers. Common failures.', category: 'inspection', phase: 'insulation' },
  { title: 'Final Inspection', path: '/inspections/final-inspection', summary: 'Final inspection for Certificate of Occupancy: life safety, egress, smoke detectors, handrails, GFCI, plumbing fixtures, mechanical.', category: 'inspection', phase: 'final-finishes' },
  { title: 'Common Inspection Failures', path: '/inspections/common-inspection-failures', summary: 'Top 20 inspection failures across all phases with fix costs and prevention strategies.', category: 'inspection' },

  // Permitting
  { title: 'Building Permits Guide', path: '/permitting', summary: 'Building permit process, costs ($500-$5,000+), required documents (site plan, construction drawings, engineering), review timeline.', category: 'permitting' },
  { title: 'Permit Application Process', path: '/permitting/permit-application-process', summary: 'Step-by-step permit application: pre-application meeting, documents needed, submittal, plan review, corrections, approval.', category: 'permitting' },
  { title: 'Common Permit Mistakes', path: '/permitting/common-permit-mistakes', summary: 'Wrong permit type, expired permits, unpermitted work, not pulling separate trades permits, not posting permit on site.', category: 'permitting' },
  { title: 'Building Codes', path: '/permitting/understanding-building-codes', summary: 'IRC vs IBC, how local amendments work, code editions, how to look up specific code sections.', category: 'permitting' },
  { title: 'Working With Building Department', path: '/permitting/working-with-building-department', summary: 'How to communicate with inspectors, schedule inspections, handle failed inspections, build good relationships.', category: 'permitting' },

  // Planning
  { title: 'Securing Land', path: '/planning/secure-land', summary: 'Finding and evaluating building lots. Zoning, utilities, soil testing, easements, due diligence checklist.', category: 'planning', phase: 'researching' },
  { title: 'House Plans', path: '/planning/house-plans', summary: 'Stock vs custom plans, plan modifications, what permits require, engineering requirements, plan review.', category: 'planning', phase: 'planning' },
  { title: 'Budget Planning', path: '/planning/budget', summary: 'Construction budget by phase, contingency (15-20%), cost per sq ft ranges, tracking methods.', category: 'planning', phase: 'planning' },
  { title: 'Construction Financing', path: '/planning/financing', summary: 'Construction loans for owner-builders: requirements, down payment (20-30%), draw schedules, lender requirements.', category: 'planning', phase: 'planning' },
  { title: 'Timeline Planning', path: '/planning/timeline', summary: 'Realistic construction timelines, phase durations, scheduling dependencies, buffer strategies.', category: 'planning', phase: 'planning' },

  // Subcontractors
  { title: 'Hiring Subcontractors', path: '/subcontractors', summary: 'Complete guide to finding, vetting, hiring, and managing subcontractors as an owner-builder.', category: 'subcontractor' },
  { title: 'Finding Quality Subs', path: '/subcontractors/finding-quality-subs', summary: 'Where to find subs: supply houses, trade associations, referrals, online platforms. Red flags.', category: 'subcontractor' },
  { title: 'Vetting Subcontractors', path: '/subcontractors/vetting-and-interviewing', summary: 'License verification, insurance requirements, reference checks, interview questions, red flags.', category: 'subcontractor' },
  { title: 'Getting Quotes', path: '/subcontractors/getting-quotes', summary: 'How to request bids, compare quotes, spot lowball estimates, negotiate fair prices.', category: 'subcontractor' },
  { title: 'Contracts', path: '/subcontractors/contracts-and-agreements', summary: 'Essential contract clauses: scope, payment terms, timeline, warranties, change orders, lien waivers.', category: 'subcontractor' },
  { title: 'Managing Subs', path: '/subcontractors/managing-subs', summary: 'Day-to-day management: scheduling, communication, quality control, site meetings, documentation.', category: 'subcontractor' },
  { title: 'Payment Schedules', path: '/subcontractors/payment-schedules', summary: 'Progress payments, retention, lien releases, never pay 100% upfront, payment timing.', category: 'subcontractor' },
  { title: 'Sub Problems', path: '/subcontractors/dealing-with-problems', summary: 'Handling delays, poor quality, disputes, no-shows, job abandonment. When to negotiate vs fire.', category: 'subcontractor' },
  { title: 'DIY vs Hire', path: '/subcontractors/when-to-hire-vs-diy', summary: 'Trade-by-trade analysis of DIY vs hiring. ROI calculations, risk levels, skill requirements.', category: 'subcontractor' },

  // Timing
  { title: 'Construction Scheduling', path: '/timing-and-scheduling', summary: 'Build schedule creation, critical path, trade coordination, delay prevention.', category: 'timing' },
  { title: 'Realistic Timeline', path: '/timing-and-scheduling/realistic-timeline', summary: 'Typical build durations by size: 1,500 sf = 10-14 months, 2,500 sf = 14-18 months. Factors that affect timeline.', category: 'timing' },
  { title: 'Material Lead Times', path: '/timing-and-scheduling/material-lead-times', summary: 'When to order: windows (8-12 weeks), cabinets (6-12 weeks), trusses (4-6 weeks), HVAC (2-4 weeks).', category: 'timing' },
  { title: 'Common Delays', path: '/timing-and-scheduling/common-delays', summary: 'Weather, permit delays, sub no-shows, material shortages, inspection failures. Prevention strategies.', category: 'timing' },

  // State guides
  { title: 'Arizona Owner-Builder Guide', path: '/permitting/state-guides/arizona', summary: 'AZ owner-builder permit requirements, desert construction considerations, Maricopa County specifics.', category: 'permitting', state: 'arizona' },
  { title: 'California Owner-Builder Guide', path: '/permitting/state-guides/california', summary: 'CA owner-builder exemption, seismic requirements, Title 24 energy code, high permit costs, county variations.', category: 'permitting', state: 'california' },
  { title: 'Colorado Owner-Builder Guide', path: '/permitting/state-guides/colorado', summary: 'CO owner-builder permits, mountain construction, altitude considerations, county-by-county requirements.', category: 'permitting', state: 'colorado' },
  { title: 'Florida Owner-Builder Guide', path: '/permitting/state-guides/florida', summary: 'FL owner-builder disclosure, hurricane codes (FBC), wind mitigation, flood zones, twice-per-year exemption.', category: 'permitting', state: 'florida' },
  { title: 'Georgia Owner-Builder Guide', path: '/permitting/state-guides/georgia', summary: 'GA owner-builder requirements, no state license needed for own home, county permit costs and processes.', category: 'permitting', state: 'georgia' },
  { title: 'North Carolina Owner-Builder Guide', path: '/permitting/state-guides/north-carolina', summary: 'NC owner-builder exemption from licensing, county-specific requirements, SEER requirements, wind zones.', category: 'permitting', state: 'north-carolina' },
  { title: 'Tennessee Owner-Builder Guide', path: '/permitting/state-guides/tennessee', summary: 'TN owner-builder friendly state, no state license required, county variation, low permit costs.', category: 'permitting', state: 'tennessee' },
  { title: 'Texas Owner-Builder Guide', path: '/permitting/state-guides/texas', summary: 'TX owner-builder act, 10-year residence requirement waiver, unincorporated areas may not require permits, wind zones.', category: 'permitting', state: 'texas' },
  { title: 'Virginia Owner-Builder Guide', path: '/permitting/state-guides/virginia', summary: 'VA owner-builder Class B exemption, RBC code adoption, specific county requirements.', category: 'permitting', state: 'virginia' },
  { title: 'Washington Owner-Builder Guide', path: '/permitting/state-guides/washington', summary: 'WA owner-builder permits, seismic requirements, energy code (WSEC), rain/moisture considerations.', category: 'permitting', state: 'washington' },

  // Move-in
  { title: 'Punch List', path: '/move-in/punch-list', summary: 'Creating thorough punch list, room-by-room method, getting subs back for fixes, quality standards.', category: 'phase', phase: 'final-finishes' },
  { title: 'Certificate of Occupancy', path: '/move-in/certificate-of-occupancy', summary: 'CO requirements, final inspection prep, common hold-ups, temporary CO options.', category: 'phase', phase: 'move-in' },
  { title: 'Loan Conversion', path: '/move-in/loan-conversion', summary: 'Converting construction loan to permanent mortgage. Appraisal, rate locks, timeline, costs.', category: 'phase', phase: 'move-in' },
  { title: 'Moving In', path: '/move-in/moving-in', summary: 'Final checklist: utilities, safety checks, warranty registration, appliance manuals, first-week tasks.', category: 'phase', phase: 'move-in' },
];

export function getRelevantContent(phase?: string, state?: string, query?: string): ContentChunk[] {
  const results: ContentChunk[] = [];
  const seen = new Set<string>();

  // Always include state-specific content if we know their state
  if (state) {
    const stateContent = CONTENT.filter(c => c.state === state);
    stateContent.forEach(c => { results.push(c); seen.add(c.path); });
  }

  // Include content for their current phase and adjacent phases
  if (phase) {
    const phaseIdx = PHASES.indexOf(phase as Phase);
    const relevantPhases = new Set<string>();
    relevantPhases.add(phase);
    // Include one phase before and after
    if (phaseIdx > 0) relevantPhases.add(PHASES[phaseIdx - 1]);
    if (phaseIdx < PHASES.length - 1) relevantPhases.add(PHASES[phaseIdx + 1]);

    const phaseContent = CONTENT.filter(c => c.phase && relevantPhases.has(c.phase) && !seen.has(c.path));
    phaseContent.forEach(c => { results.push(c); seen.add(c.path); });
  }

  // Simple keyword matching for the query
  if (query) {
    const queryLower = query.toLowerCase();
    const keywords = queryLower.split(/\s+/).filter(w => w.length > 3);

    const matched = CONTENT.filter(c => {
      if (seen.has(c.path)) return false;
      const text = `${c.title} ${c.summary} ${c.category}`.toLowerCase();
      return keywords.some(k => text.includes(k));
    });

    // Add top 5 keyword matches
    matched.slice(0, 5).forEach(c => { results.push(c); seen.add(c.path); });
  }

  // Always include the general permitting and inspection overviews if not already present
  const essentials = CONTENT.filter(c =>
    (c.path === '/permitting' || c.path === '/inspections' || c.path === '/subcontractors') &&
    !seen.has(c.path)
  );
  essentials.forEach(c => results.push(c));

  return results.slice(0, 15); // Cap at 15 chunks to keep context manageable
}

export function formatContentForPrompt(chunks: ContentChunk[]): string {
  if (chunks.length === 0) return '';

  return chunks.map(c =>
    `- ${c.title} (${c.path}): ${c.summary}`
  ).join('\n');
}
