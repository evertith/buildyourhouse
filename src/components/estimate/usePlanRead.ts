'use client';

/**
 * Follows one plan read: verifies the checkout once when the page lands with
 * a session id, then polls while StudTally is reading. Fires the GA4
 * events that belong to the read (purchase, verified, ready), each deduped
 * per session or token so reloads do not double-count.
 */

import { useCallback, useEffect, useRef, useState } from 'react';
import { trackEvent } from '@/lib/analytics';
import { getPlanRead, PLAN_READ_PRICE, PlanReadError, verifyPlanRead } from '@/lib/planRead';
import type { PlanReadView } from '@/lib/planRead';

const POLL_MS = 5000;
const ACTIVE = new Set(['queued', 'reading']);

export interface PlanReadState {
  phase: 'idle' | 'loading' | 'view' | 'missing' | 'error';
  view: PlanReadView | null;
  error: string | null;
}

function remember(key: string): boolean {
  try {
    if (sessionStorage.getItem(key)) return false;
    sessionStorage.setItem(key, '1');
  } catch {
    // Storage unavailable: track anyway; a rare double count beats a missed sale.
  }
  return true;
}

export function usePlanRead(token: string | null, sessionId: string | null) {
  const [state, setState] = useState<PlanReadState>({ phase: token ? 'loading' : 'idle', view: null, error: null });
  const timer = useRef<number | null>(null);
  const readyTracked = useRef(false);

  const apply = useCallback(
    (view: PlanReadView) => {
      setState({ phase: 'view', view, error: null });
      if (view.status === 'ready' && !readyTracked.current) {
        readyTracked.current = true;
        if (remember(`plan_read_ready_${view.token}`)) {
          trackEvent('plan_read_ready', { calculator: 'material-estimator', token: view.token.slice(0, 8) });
        }
      }
    },
    []
  );

  const refresh = useCallback(async () => {
    if (!token) return;
    try {
      apply(await getPlanRead(token));
    } catch (err) {
      if (err instanceof PlanReadError && err.status === 404) {
        setState({ phase: 'missing', view: null, error: null });
      } else {
        setState((prev) => ({ ...prev, phase: prev.view ? 'view' : 'error', error: (err as Error).message }));
      }
    }
  }, [token, apply]);

  // First load: verify when a session id came back from Stripe, else fetch.
  useEffect(() => {
    if (!token) {
      setState({ phase: 'idle', view: null, error: null });
      return;
    }
    let cancelled = false;
    (async () => {
      if (sessionId) {
        try {
          const view = await verifyPlanRead(token, sessionId);
          if (cancelled) return;
          if (view.status !== 'setup') {
            if (remember(`purchase_tracked_${sessionId}`)) {
              const value = view.amountCents != null ? view.amountCents / 100 : PLAN_READ_PRICE;
              trackEvent('plan_read_verified', { calculator: 'material-estimator' });
              trackEvent('purchase', {
                transaction_id: sessionId,
                currency: 'USD',
                value,
                items: [{ item_id: 'plan-read', item_name: 'Measured Whole-House Estimate', price: value, quantity: 1 }],
              });
            }
          }
          apply(view);
          return;
        } catch {
          // Fall through to a plain fetch; the webhook may already have started the read.
        }
      }
      if (!cancelled) await refresh();
    })();
    return () => {
      cancelled = true;
    };
  }, [token, sessionId, apply, refresh]);

  // Poll while the read is active.
  useEffect(() => {
    const status = state.view?.status;
    if (!token || !status || !ACTIVE.has(status)) return;
    timer.current = window.setTimeout(refresh, POLL_MS);
    return () => {
      if (timer.current) window.clearTimeout(timer.current);
    };
  }, [token, state.view, refresh]);

  return { ...state, refresh };
}
