/**
 * Human-readable labels for URL segments, shared by the breadcrumb schema and
 * the HTML site map. Unlisted segments fall back to title-cased slugs.
 */

const OVERRIDES: Record<string, string> = {
  "hvac-installation": "HVAC Installation",
  "when-to-hire-vs-diy": "When to Hire vs. DIY",
  "buy-vs-rent": "Buy vs. Rent",
  "is-it-right-for-you": "Is It Right for You?",
  "is-owner-building-right-recession": "Is Owner-Building Right in a Recession?",
  "state-guides": "State Guides",
  "start-here": "Start Here",
  "timing-and-scheduling": "Timing & Scheduling",
  "tools-and-equipment": "Tools & Equipment",
  "build-phases": "Build Phases",
  "move-in": "Move-In",
  "kitchen-and-bath": "Kitchen & Bath",
  "windows-and-doors": "Windows & Doors",
  "certificate-of-occupancy": "Certificate of Occupancy",
  faq: "FAQ",
};

const SMALL_WORDS = new Set(["a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the", "to", "vs", "with"]);

export function labelForSegment(segment: string): string {
  if (OVERRIDES[segment]) return OVERRIDES[segment];
  return segment
    .split("-")
    .map((word, index) =>
      index > 0 && SMALL_WORDS.has(word)
        ? word
        : word.charAt(0).toUpperCase() + word.slice(1)
    )
    .join(" ");
}
