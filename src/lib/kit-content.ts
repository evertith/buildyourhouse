/**
 * Content schema for a state permit kit product page.
 *
 * This is the authoring contract for the 50-state kit line: one KitContent
 * object per state, rendered by <KitProductPage>. Everything that is the same
 * in every state (layout, section headings, price framing, the binder
 * cross-sell, Product/FAQPage schema) lives in the component. Everything that
 * is state-specific lives here.
 *
 * Identity is NOT repeated here. State name, postal code, guide slug, and the
 * Stripe checkout URL are read from STATE_KITS at render time, so kits.ts stays
 * the single source of truth and a kit cannot drift from the registry that
 * ships it.
 *
 * Writing a new kit:
 *   1. Flip the state to 'shipped' in kits.ts with its checkoutUrl and hook.
 *   2. Create src/app/shop/<code>-permit-kit/page.tsx with `export const
 *      metadata` (hand-tuned per state for search) and one KitContent object.
 *   3. Render <KitProductPage content={CONTENT} />. No layout code.
 */

import type { IconName } from '@/components/Icon';
import type { FAQItem } from '@/lib/schema';

/** Every kit is $34. Also drives the plate, the hub, and the shop ladder. */
export const KIT_PRICE = 34;

/** One of the six documents in a kit. */
export interface KitDocument {
  /** Sheet number inside the kit, prefixed with the state code: 'NC.1'. */
  no: string;
  /** Extent, as printed in the index: '6 pages'. */
  pages: string;
  title: string;
  /** What the document does, in the buyer's terms. 2–3 sentences. */
  copy: string;
  /**
   * Page render for the index row. Optional — the four kits shipped so far
   * illustrate three of six documents and leave the directory and forms index
   * unillustrated, which keeps the index from turning into a gallery.
   * Path is authored, not derived: the first four kits use
   * /binder/<code>k-*.webp, later kits use /kits/<code>/*.webp.
   */
  thumb?: string;
  /** Caption under the render: 'NC.1 Exemption walkthrough'. */
  caption?: string;
  /** Alt text. Describe what is on the page, not that it is a page. */
  alt?: string;
}

/**
 * One entry in the statute-highlight strip — a thing this state's kit gets
 * right that general owner-builder advice gets wrong. Four is the house
 * standard. Each has to be checkable by the reader in about a minute; that is
 * the whole argument for the price.
 */
export interface KitHighlight {
  icon: IconName;
  /** The claim itself, set as a mono label. Keep it under ~60 characters. */
  label: string;
  /** The evidence: what the rule actually is and why the common version is wrong. */
  copy: string;
}

/** A page render used in the hero stack. */
export interface KitSheet {
  src: string;
  alt: string;
}

export interface KitContent {
  /** Must match a STATE_KITS slug, e.g. 'nc-permit-kit'. */
  slug: string;
  /** Italic line under the H1. One sentence, names this state's real problem. */
  heroSub: string;
  /** Total printed pages across the documents. Shown in the title block. */
  pageCount: number;
  /** Revision stamp for the order box: 'August 2026'. */
  revision: string;
  /** The six documents, in kit order. */
  documents: KitDocument[];
  /** The 'what you get' list in the order box. */
  includes: string[];
  /** Lead paragraph above the highlight strip. Names the state and the count. */
  highlightsLead: string;
  highlights: KitHighlight[];
  /** Sources line under the strip: which authorities were checked, and when. */
  sourceNote: string;
  faqs: FAQItem[];
  /** Two page renders for the hero: `front` sits square to the reader. */
  heroSheets: { front: KitSheet; back: KitSheet };
  /** Product schema description. Names the sources and the verification date. */
  productDescription: string;
  /** Social/schema image. Defaults to the shop's. */
  ogImage?: string;
  /**
   * "Verify locally" smallprint body. Every state names its permitting
   * authority differently — VA has independent cities ("your locality"),
   * TX splits city/unincorporated county — so override per state.
   * Default: "Statutes and code editions change. Confirm each rule with
   * your county — the kit prints its sources so you can."
   */
  verifyNote?: string;
  /** Binder cross-sell lead. Override when "gets your permit" needs
   *  state-specific wording (TX: permits, plural). */
  binderLead?: string;
}

/** Small-number words, so headings read 'Six documents' not '6 documents'. */
const WORDS = [
  'Zero', 'One', 'Two', 'Three', 'Four', 'Five',
  'Six', 'Seven', 'Eight', 'Nine', 'Ten',
];

export const countWord = (n: number): string => WORDS[n] ?? String(n);

/** Two-digit title-block figure: 6 -> '06'. */
export const dim = (n: number): string => String(n).padStart(2, '0');
