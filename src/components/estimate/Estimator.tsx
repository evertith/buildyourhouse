'use client';

/**
 * The whole-house estimator: state, URL sync, the engine call, and the
 * ledger-and-rail layout (Direction D). The profile lives in the query
 * string so an estimate is shareable and the state pages can pre-set it;
 * localStorage only remembers the last profile for convenience.
 *
 * Plans attached: `?read=<token>` names a plan read on the downloads
 * Worker. While it is unpaid, queued, or running, the ledger stays the free
 * estimate with a status strip under the title; when the read is ready the
 * geometry comes from the drawings and the chips become plan facts. The
 * `session_id` Stripe appends on return is verified once and dropped.
 *
 * The engine runs in well under a millisecond, so nothing is debounced
 * except the screen-reader announcement and the one-shot analytics event.
 */

import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import s from '@/styles/Estimate.module.css';
import { trackEvent } from '@/lib/analytics';
import { runEstimate } from '@/lib/estimate/estimate';
import { PROFILE_DEFAULTS } from '@/lib/estimate/geometry';
import type { Profile } from '@/lib/estimate/geometry';
import { DIY_DEFAULT } from '@/lib/estimate/labor';
import { measuredGeometry, planTitle } from '@/lib/estimate/measured';
import { parseProfile, serializeProfile } from '@/lib/estimate/profile';
import type { ProfileState } from '@/lib/estimate/profile';
import type { PhaseId } from '@/lib/estimate/types';
import AttachPanel from './AttachPanel';
import Ledger from './Ledger';
import MeasuredChips from './MeasuredChips';
import ProfileChips from './ProfileChips';
import Rail from './Rail';
import type { ExportKind } from './Rail';
import ReadingStatus from './ReadingStatus';
import StickyStrip from './StickyStrip';
import { CALCULATOR_SLUG, csvFilename, estimateCsv, estimateText } from './exports';
import { money100 } from './format';
import { usePlanRead } from './usePlanRead';

const STORAGE_KEY = 'byh-estimate-profile';
const ANNOUNCE_MS = 600;
const PROFILE_KEYS = ['sqft', 'stories', 'finish', 'found', 'state', 'roof', 'height', 'diy'];
const TOKEN_RE = /^[a-f0-9]{32}$/;

interface Props {
  /** next/font variable classes for Instrument Serif and Sans, scoped to this root. */
  fontClass: string;
}

interface ReadRef {
  token: string | null;
  sessionId: string | null;
  cancelled: boolean;
}

export default function Estimator({ fontClass }: Props) {
  const [state, setState] = useState<ProfileState>({ profile: PROFILE_DEFAULTS, diy: [...DIY_DEFAULT] });
  const [openId, setOpenId] = useState<PhaseId | null>('framing');
  const [copied, setCopied] = useState(false);
  const [announcement, setAnnouncement] = useState('');
  const [read, setRead] = useState<ReadRef>({ token: null, sessionId: null, cancelled: false });
  const [panelOpen, setPanelOpen] = useState(false);
  const hydrated = useRef(false);
  const useTracked = useRef(false);
  const urlHadProfile = useRef(false);
  const readProfileApplied = useRef(false);
  const rootRef = useRef<HTMLDivElement | null>(null);

  // The site header and promo banner are sticky; the phone strip and the
  // rail stick just below whatever of them is pinned.
  useEffect(() => {
    const root = rootRef.current;
    if (!root) return;
    const measure = () => {
      let bottom = 0;
      for (const el of document.querySelectorAll<HTMLElement>('body > header, body > div, body > aside')) {
        const pos = getComputedStyle(el).position;
        if (pos === 'sticky' || pos === 'fixed') {
          bottom = Math.max(bottom, el.getBoundingClientRect().bottom);
        }
      }
      root.style.setProperty('--est-top', `${Math.max(0, Math.round(bottom))}px`);
    };
    measure();
    window.addEventListener('resize', measure);
    return () => window.removeEventListener('resize', measure);
  }, []);

  const { profile, diy } = state;
  const planRead = usePlanRead(read.token, read.sessionId);
  const view = planRead.view;
  const measured = useMemo(
    () => (view?.status === 'ready' && view.geometry ? measuredGeometry(view.geometry, profile) : null),
    [view, profile]
  );
  const estimate = useMemo(
    () => runEstimate(measured ?? profile, profile.finish, profile.state, { diy }),
    [measured, profile, diy]
  );
  const planName = view?.plan.name ?? undefined;

  // Hydrate from the URL, else the last profile this browser used.
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const token = params.get('read');
    const sessionId = params.get('session_id');
    const cancelled = params.get('cancelled') === '1';
    if (token && TOKEN_RE.test(token)) {
      setRead({ token, sessionId, cancelled });
    }
    const fromUrl = PROFILE_KEYS.some((k) => params.has(k));
    urlHadProfile.current = fromUrl;
    if (fromUrl) {
      setState(parseProfile(params));
    } else {
      try {
        const saved = window.localStorage.getItem(STORAGE_KEY);
        if (saved) setState(parseProfile(new URLSearchParams(saved)));
      } catch {
        // Storage unavailable: defaults are fine.
      }
    }
    if (sessionId || cancelled) {
      // Verified once; a reload must not re-verify or re-announce the cancel.
      params.delete('session_id');
      params.delete('cancelled');
      const q = params.toString();
      window.history.replaceState(window.history.state, '', `${window.location.pathname}${q ? `?${q}` : ''}`);
    }
    // Let the state settle before URL sync starts.
    const id = window.setTimeout(() => {
      hydrated.current = true;
    }, 0);
    return () => window.clearTimeout(id);
  }, []);

  // A results link opened cold adopts the finish, state, and switches saved at attach time.
  useEffect(() => {
    if (!view || readProfileApplied.current) return;
    readProfileApplied.current = true;
    if (urlHadProfile.current || !view.profile) return;
    setState(parseProfile(new URLSearchParams(view.profile)));
  }, [view]);

  // Sync the URL and storage, announce the new total, fire estimate_use once.
  useEffect(() => {
    if (!hydrated.current) return;
    const profileQuery = serializeProfile(state);
    const q = new URLSearchParams(profileQuery);
    if (read.token) q.set('read', read.token);
    const qs = q.toString();
    const url = `${window.location.pathname}${qs ? `?${qs}` : ''}${window.location.hash}`;
    window.history.replaceState(window.history.state, '', url);
    try {
      window.localStorage.setItem(STORAGE_KEY, profileQuery.toString());
    } catch {
      // ignore
    }
    const t = window.setTimeout(() => {
      const tot = estimate.totals;
      setAnnouncement(
        `Estimate updated: cash to build ${money100(tot.cash.mid)}, ${tot.nDiy} ${tot.nDiy === 1 ? 'phase' : 'phases'} yourself.`
      );
      if (!useTracked.current) {
        useTracked.current = true;
        trackEvent('estimate_use', {
          calculator: CALCULATOR_SLUG,
          sqft: profile.heatedSf,
          stories: profile.stories,
          finish: profile.finish,
          foundation: profile.foundation,
          state: profile.state,
          measured: Boolean(measured),
        });
      }
    }, ANNOUNCE_MS);
    return () => window.clearTimeout(t);
    // The estimate is derived from state; profile fields are read for the event only.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [state, read.token, measured]);

  const onProfileChange = useCallback((patch: Partial<Profile>) => {
    setState((prev) => ({ ...prev, profile: { ...prev.profile, ...patch } }));
  }, []);

  const onChoice = useCallback((id: PhaseId, isDiy: boolean) => {
    setState((prev) => {
      const has = prev.diy.includes(id);
      if (has === isDiy) return prev;
      return { ...prev, diy: isDiy ? [...prev.diy, id] : prev.diy.filter((x) => x !== id) };
    });
    trackEvent('estimate_toggle', { calculator: CALCULATOR_SLUG, phase: id, choice: isDiy ? 'diy' : 'hire' });
  }, []);

  const onToggleOpen = useCallback((id: PhaseId) => {
    setOpenId((prev) => (prev === id ? null : id));
  }, []);

  const onExport = useCallback(
    async (kind: ExportKind) => {
      trackEvent('estimate_export', { calculator: CALCULATOR_SLUG, format: kind });
      if (kind === 'print') {
        window.print();
        return;
      }
      if (kind === 'copy') {
        try {
          await navigator.clipboard.writeText(estimateText(estimate, profile, window.location.href, planName));
          setCopied(true);
          window.setTimeout(() => setCopied(false), 1500);
        } catch {
          // Clipboard unavailable: quietly do nothing.
        }
        return;
      }
      if (kind === 'csv') {
        const blob = new Blob([estimateCsv(estimate, profile, planName)], { type: 'text/csv;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = csvFilename(profile, planName);
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.setTimeout(() => URL.revokeObjectURL(url), 1000);
      }
    },
    [estimate, profile, planName]
  );

  const openPanel = useCallback(() => {
    setPanelOpen(true);
    trackEvent('plan_read_open', { calculator: CALCULATOR_SLUG });
    window.setTimeout(() => {
      document.getElementById('attach-panel')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 0);
  }, []);

  const attachAnother = useCallback(() => {
    setRead({ token: null, sessionId: null, cancelled: false });
    openPanel();
  }, [openPanel]);

  const showStatus = Boolean(read.token) && !measured;
  const panelVisible = panelOpen && !measured;

  return (
    <div className={`${s.root} ${fontClass}`} ref={rootRef}>
      <StickyStrip estimate={estimate} />

      <div className={`${s.wrap} ${s.titleBlock}`}>
        <p className={s.eyebrow}>Cost to build a house calculator</p>
        <h1 className={s.h1}>{measured ? planTitle(planName) : 'Your house, costed.'}</h1>
        <p className={s.lede}>
          {measured
            ? 'Every phase the plans could settle is priced from your drawings, with the sheet beside each number; the rest is derived from the measured size and says so. Flip a phase to do it yourself and the number moves.'
            : 'Every phase from the permit to the mailbox, priced from your square footage with materials and labor shown apart. Flip a phase to do it yourself and the number moves. Change the state and the index moves it again. Attach your plans and the same ledger is measured from your drawings.'}
        </p>
        {measured ? (
          <MeasuredChips geometry={measured} profile={profile} onChange={onProfileChange} />
        ) : (
          <ProfileChips profile={profile} onChange={onProfileChange} />
        )}
        {showStatus && (
          <ReadingStatus
            view={view}
            missing={planRead.phase === 'missing'}
            cancelled={read.cancelled}
            error={planRead.error}
            onAttachAnother={attachAnother}
          />
        )}
        {panelVisible && (
          <div id="attach-panel">
            <AttachPanel profileQuery={serializeProfile(state).toString()} onClose={() => setPanelOpen(false)} />
          </div>
        )}
      </div>

      <div className={`${s.wrap} ${s.body}`}>
        <div className={s.grid}>
          <Ledger
            estimate={estimate}
            openId={openId}
            onToggleOpen={onToggleOpen}
            onChoice={onChoice}
            measuredMode={Boolean(measured)}
          />
          <aside className={s.rail} aria-label="Cash to build">
            <Rail
              estimate={estimate}
              profile={profile}
              copied={copied}
              onExport={onExport}
              view={view}
              measured={measured}
              planName={planName}
              onAttach={openPanel}
            />
          </aside>
        </div>
      </div>

      <div role="status" aria-live="polite" className="visually-hidden">
        {announcement}
      </div>
    </div>
  );
}
