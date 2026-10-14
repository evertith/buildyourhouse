/**
 * Client for the downloads Worker's plan-read routes: attach a plan set,
 * verify the checkout, poll the read, restart a cancelled checkout. The
 * token in the URL is the only credential, like a share link.
 */

import type { MeasuredPayload } from './estimate/measured';

export const WORKER_BASE_URL =
  process.env.NEXT_PUBLIC_DOWNLOADS_WORKER_BASE ??
  'https://buildyourhouse-downloads.azerothcorner.workers.dev';

export const PLAN_READ_PRICE = 20;
export const PLAN_PDF_MAX_BYTES = 100 * 1024 * 1024;
export const PLAN_PDF_MAX_SHEETS = 40;

export type PlanReadStatus = 'setup' | 'queued' | 'reading' | 'ready' | 'unsupported' | 'refunded';

export interface ProgressStep {
  key: string;
  label: string;
  status: 'pending' | 'running' | 'done' | 'failed' | 'skipped';
  detail?: string | null;
}

export interface PlanReadView {
  token: string;
  status: PlanReadStatus;
  plan: { name: string | null; pageCount: number | null };
  emailHint: string;
  progress: ProgressStep[];
  geometry: MeasuredPayload | null;
  reason: string | null;
  refunded: boolean;
  upgrade: { code: string; expiresAt: string | null } | null;
  /** The serialized profile (finish, state, diy) from the attach moment. */
  profile: string;
  createdAt: string;
  readyAt: string | null;
  justPaid?: boolean;
  amountCents?: number | null;
}

export type Foundation = 'from_plan' | 'slab' | 'raised_crawl' | 'basement';
export type FloorFraming = 'from_plan' | 'lumber' | 'i_joist' | 'floor_truss';
export type RoofFraming = 'from_plan' | 'stick' | 'truss';

export interface AttachMeta {
  email: string;
  foundation: Foundation;
  floorFraming: FloorFraming;
  roofFraming: RoofFraming;
  /** serializeProfile(...).toString(), so the results page restores finish and state. */
  profile: string;
}

export class PlanReadError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.status = status;
  }
}

async function readError(res: Response, fallback: string): Promise<PlanReadError> {
  let message = fallback;
  try {
    const data = await res.json();
    if (data && typeof data.error === 'string') message = data.error;
  } catch {
    // keep the fallback
  }
  return new PlanReadError(message, res.status);
}

export function formatMb(bytes: number): string {
  return `${(bytes / (1024 * 1024)).toFixed(bytes >= 10 * 1024 * 1024 ? 0 : 1)} MB`;
}

/** Stream the PDF to the Worker. Resolves to the token and the Stripe URL to go to. */
export async function createPlanRead(
  file: File,
  meta: AttachMeta
): Promise<{ token: string; checkout_url: string; page_count: number }> {
  const res = await fetch(`${WORKER_BASE_URL}/plan-read`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/pdf',
      'X-Plan-Email': encodeURIComponent(meta.email),
      'X-Plan-Name': encodeURIComponent(file.name),
      'X-Plan-Foundation': meta.foundation,
      'X-Plan-Floor': meta.floorFraming,
      'X-Plan-Roof': meta.roofFraming,
      'X-Plan-Profile': meta.profile,
    },
    body: file,
  });
  if (!res.ok) throw await readError(res, 'The upload did not go through. Try again in a minute.');
  return res.json();
}

export async function getPlanRead(token: string): Promise<PlanReadView> {
  const res = await fetch(`${WORKER_BASE_URL}/plan-read/${encodeURIComponent(token)}`, { cache: 'no-store' });
  if (!res.ok) throw await readError(res, 'That plan read could not be loaded.');
  return res.json();
}

export async function verifyPlanRead(token: string, sessionId: string): Promise<PlanReadView> {
  const res = await fetch(`${WORKER_BASE_URL}/plan-read/${encodeURIComponent(token)}/verify`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ session_id: sessionId }),
  });
  if (!res.ok) throw await readError(res, 'The payment could not be checked. The page will keep trying.');
  return res.json();
}

export async function checkoutPlanRead(token: string): Promise<{ checkout_url?: string } & Partial<PlanReadView>> {
  const res = await fetch(`${WORKER_BASE_URL}/plan-read/${encodeURIComponent(token)}/checkout`, {
    method: 'POST',
  });
  if (!res.ok) throw await readError(res, 'Checkout could not be started. Try again in a minute.');
  return res.json();
}
