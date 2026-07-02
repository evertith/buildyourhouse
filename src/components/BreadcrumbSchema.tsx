"use client";

import { usePathname } from "next/navigation";
import { generateBreadcrumbSchema } from "@/lib/schema";
import { labelForSegment } from "@/lib/route-labels";

const BASE_URL = "https://build-your-house.com";

// Sections with no index page — including them as linked crumbs would point at 404s.
const NON_LINKABLE_SEGMENTS = new Set(["planning", "move-in", "feasibility"]);

/**
 * Emits BreadcrumbList JSON-LD derived from the current path. Rendered from the
 * root layout so every page gets hierarchy markup; the static export includes
 * it in the prerendered HTML.
 */
export default function BreadcrumbSchema() {
  const pathname = usePathname();
  if (!pathname || pathname === "/") return null;

  const segments = pathname.split("/").filter(Boolean);
  const items = [{ name: "Home", item: `${BASE_URL}/` }];

  segments.forEach((segment, index) => {
    const isLast = index === segments.length - 1;
    if (!isLast && NON_LINKABLE_SEGMENTS.has(segment)) return;
    items.push({
      name: labelForSegment(segment),
      item: `${BASE_URL}/${segments.slice(0, index + 1).join("/")}`,
    });
  });

  if (items.length < 2) return null;

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{
        __html: JSON.stringify(generateBreadcrumbSchema(items)),
      }}
    />
  );
}
