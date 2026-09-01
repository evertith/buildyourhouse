'use client';

/**
 * Site Plan Studio — the client root: reducer, layout, hydration, analytics.
 *
 * State is one `useReducer` over a small plan object with about a dozen
 * named actions. Adding a state library for one page would contradict a
 * codebase that has none, and the mutations here are all shaped like
 * "move this element" rather than like cross-cutting state.
 *
 * Violations are DERIVED on every render and never stored (§4.1). Two
 * sources of truth drift the first time a drag is interrupted, and a stale
 * conflict list on a permit drawing is worse than no conflict list.
 */

import { useEffect, useMemo, useReducer, useRef, useState } from 'react';
import s from '@/styles/SitePlanStudio.module.css';
import { trackEvent } from '@/lib/analytics';
import { check } from '@/lib/siteplan/check';
import { treatmentFor } from '@/lib/siteplan/adapt';
import { placeElement } from '@/lib/siteplan/defaults';
import { getStateRules } from '@/lib/siteplan/rules';
import { clearPlan, loadPlan, savePlan } from '@/lib/siteplan/storage';
import type {
  EdgeName,
  ElementKind,
  Plan,
  PlanElement,
  Setbacks,
  TitleFields,
} from '@/lib/siteplan/types';
import { EMPTY_PLAN } from '@/lib/siteplan/types';
import ConflictList from './ConflictList';
import ExportSheet from './ExportSheet';
import Inspector from './Inspector';
import LotForm from './LotForm';
import PlanCanvas from './PlanCanvas';
import SheetCapture from './SheetCapture';
import StateSelect, { VerificationChip } from './StateSelect';
import Toolbox from './Toolbox';

type Action =
  | { t: 'SET_LOT'; w: number; d: number; frontEdge?: EdgeName }
  | { t: 'ADD_ELEMENT'; kind: ElementKind }
  | { t: 'MOVE_ELEMENT'; id: string; x: number; y: number }
  | { t: 'NUDGE'; dx: number; dy: number }
  | { t: 'SET_EDGE_DISTANCE'; id: string; edge: EdgeName; feet: number }
  | { t: 'RESIZE_ELEMENT'; id: string; w: number; d: number }
  | { t: 'ROTATE_ELEMENT'; id: string; rot: number }
  | { t: 'SELECT'; id: string | null }
  | { t: 'DELETE_ELEMENT'; id: string }
  | { t: 'SET_STATE'; code: string }
  | { t: 'SET_SETBACK'; key: keyof Setbacks; value: number | null }
  | { t: 'SET_FRONT_EDGE'; edge: EdgeName }
  | { t: 'SET_NORTH'; deg: number }
  | { t: 'SET_TITLE_FIELD'; key: keyof TitleFields; value: string }
  | { t: 'HYDRATE'; plan: Plan }
  | { t: 'RESET' };

const mapEl = (
  plan: Plan,
  id: string,
  fn: (el: PlanElement) => PlanElement
): Plan => ({
  ...plan,
  elements: plan.elements.map((e) => (e.id === id ? fn(e) : e)),
});

function reducer(plan: Plan, a: Action): Plan {
  switch (a.t) {
    case 'SET_LOT':
      return {
        ...plan,
        lot: { w: a.w, d: a.d },
        frontEdge: a.frontEdge ?? plan.frontEdge,
      };
    case 'ADD_ELEMENT': {
      if (!plan.lot) return plan;
      const el = placeElement(a.kind, plan.lot, plan.elements, plan.frontEdge);
      return { ...plan, elements: [...plan.elements, el], selectedId: el.id };
    }
    case 'MOVE_ELEMENT':
      return mapEl(plan, a.id, (e) => ({ ...e, x: a.x, y: a.y }));
    case 'NUDGE':
      return plan.selectedId
        ? mapEl(plan, plan.selectedId, (e) => ({
            ...e,
            x: e.x + a.dx,
            y: e.y + a.dy,
          }))
        : plan;
    case 'SET_EDGE_DISTANCE': {
      // Translate so the element's NEAREST edge sits `feet` off that line —
      // the way a surveyor states a position, and it holds under rotation.
      if (!plan.lot) return plan;
      const el = plan.elements.find((e) => e.id === a.id);
      if (!el) return plan;
      const cur = currentEdgeDistance(el, plan.lot, a.edge);
      const delta = a.feet - cur;
      const sign = a.edge === 'west' || a.edge === 'north' ? 1 : -1;
      const horizontal = a.edge === 'west' || a.edge === 'east';
      return mapEl(plan, a.id, (e) => ({
        ...e,
        x: horizontal ? e.x + delta * sign : e.x,
        y: horizontal ? e.y : e.y + delta * sign,
      }));
    }
    case 'RESIZE_ELEMENT':
      return mapEl(plan, a.id, (e) => ({ ...e, w: a.w, d: a.d }));
    case 'ROTATE_ELEMENT':
      return mapEl(plan, a.id, (e) => ({ ...e, rot: a.rot }));
    case 'SELECT':
      return { ...plan, selectedId: a.id };
    case 'DELETE_ELEMENT':
      return {
        ...plan,
        elements: plan.elements.filter((e) => e.id !== a.id),
        selectedId: plan.selectedId === a.id ? null : plan.selectedId,
      };
    case 'SET_STATE':
      return { ...plan, stateCode: a.code };
    case 'SET_SETBACK':
      return { ...plan, setbacks: { ...plan.setbacks, [a.key]: a.value } };
    case 'SET_FRONT_EDGE':
      return { ...plan, frontEdge: a.edge };
    case 'SET_NORTH':
      return { ...plan, north: a.deg };
    case 'SET_TITLE_FIELD':
      return { ...plan, title: { ...plan.title, [a.key]: a.value } };
    case 'HYDRATE':
      return a.plan;
    case 'RESET':
      return EMPTY_PLAN;
    default:
      return plan;
  }
}

/** Distance from one lot edge to the element's nearest corner. */
function currentEdgeDistance(
  el: PlanElement,
  lot: { w: number; d: number },
  edge: EdgeName
): number {
  const hw = Math.abs(el.w / 2);
  const hd = Math.abs(el.d / 2);
  const a = (el.rot * Math.PI) / 180;
  const projX = Math.abs(hw * Math.cos(a)) + Math.abs(hd * Math.sin(a));
  const projY = Math.abs(hw * Math.sin(a)) + Math.abs(hd * Math.cos(a));
  if (edge === 'west') return el.x - projX;
  if (edge === 'east') return lot.w - (el.x + projX);
  if (edge === 'north') return el.y - projY;
  return lot.d - (el.y + projY);
}

/** Matches a media query, hydration-safe: false on the server, set in an effect. */
function useMedia(query: string): boolean {
  const [match, setMatch] = useState(false);
  useEffect(() => {
    if (typeof window.matchMedia !== 'function') return;
    const mq = window.matchMedia(query);
    const on = () => setMatch(mq.matches);
    on();
    mq.addEventListener('change', on);
    return () => mq.removeEventListener('change', on);
  }, [query]);
  return match;
}

export default function SitePlanStudio() {
  const [plan, dispatch] = useReducer(reducer, EMPTY_PLAN);
  const [activeRowId, setActiveRowId] = useState<string | null>(null);
  const [hoverElementId, setHoverElementId] = useState<string | null>(null);
  const [sheetOpen, setSheetOpen] = useState(false);
  const [restored, setRestored] = useState(false);
  const [editingLot, setEditingLot] = useState(false);

  const hydrated = useRef(false);
  const startFired = useRef(false);
  const shownViolations = useRef<Set<string>>(new Set());

  // Wide enough for the three-column grid; wide enough to drag precisely.
  const isDesktop = useMedia('(min-width: 1024px)');
  const canDrag = useMedia('(min-width: 768px)');

  const rules = plan.stateCode ? getStateRules(plan.stateCode) : null;
  const result = useMemo(() => check(plan, rules), [plan, rules]);
  const treatment = treatmentFor(rules, plan.stateCode);
  const selected = plan.elements.find((e) => e.id === plan.selectedId) ?? null;

  // ---- Hydration (§4.4): in an effect, never during render.
  useEffect(() => {
    if (hydrated.current) return;
    hydrated.current = true;
    const saved = loadPlan();
    if (saved) {
      dispatch({ t: 'HYDRATE', plan: saved });
      // Reading localStorage after mount is the only way to restore a plan
      // on a statically exported page: the first paint has to match the
      // server output, so this cannot move into render or an initialiser.
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setRestored(true);
      startFired.current = true;
      trackEvent('siteplan_restore', { elements: saved.elements.length });
    }
  }, []);

  // ---- Persistence, debounced 400 ms.
  useEffect(() => {
    if (!hydrated.current || !plan.lot) return;
    const t = setTimeout(() => savePlan(plan), 400);
    return () => clearTimeout(t);
  }, [plan]);

  // ---- siteplan_violation_shown, guarded by a ref set of fired rule ids.
  // Unguarded, a single drag emits hundreds of events and the GA4 property
  // is ruined for the month.
  useEffect(() => {
    for (const row of result.rows) {
      if (row.status !== 'violation' && row.status !== 'watch') continue;
      if (shownViolations.current.has(row.id)) continue;
      shownViolations.current.add(row.id);
      trackEvent('siteplan_violation_shown', {
        rule: row.id,
        state: plan.stateCode || 'none',
        verified: treatment === 'rules',
      });
    }
  }, [result.rows, plan.stateCode, treatment]);

  useEffect(() => {
    if (!sheetOpen) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setSheetOpen(false);
    };
    window.addEventListener('keydown', onKey);
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      window.removeEventListener('keydown', onKey);
      document.body.style.overflow = prevOverflow;
    };
  }, [sheetOpen]);

  const setState = (code: string) => {
    dispatch({ t: 'SET_STATE', code });
    if (code) {
      const r = getStateRules(code);
      trackEvent('siteplan_state_select', { state: code, verified: r.verified });
    }
  };

  const startPlan = (w: number, d: number, frontEdge: EdgeName) => {
    dispatch({ t: 'SET_LOT', w, d, frontEdge });
    setEditingLot(false);
    if (!startFired.current) {
      startFired.current = true;
      trackEvent('siteplan_start', {
        lot_w: w,
        lot_d: d,
        state: plan.stateCode || 'none',
      });
    }
  };

  const addElement = (kind: ElementKind) => {
    dispatch({ t: 'ADD_ELEMENT', kind });
    trackEvent('siteplan_element_add', { kind });
  };

  const reset = () => {
    clearPlan();
    shownViolations.current.clear();
    startFired.current = false;
    setRestored(false);
    setSheetOpen(false);
    setEditingLot(false);
    dispatch({ t: 'RESET' });
  };

  const onExport = (method: 'print' | 'svg') => {
    trackEvent('siteplan_export', {
      method,
      state: plan.stateCode || 'none',
      elements: plan.elements.length,
      conflicts: result.rows.filter((r) => r.status === 'violation').length,
    });
  };

  const shortCount = result.rows.filter(
    (r) => r.status === 'violation' || r.status === 'watch'
  ).length;
  const problemCount = shortCount + result.boundary.length + result.setbacks.length;

  // ---- Empty state: the lot form is the whole editor until a lot exists.
  if (!plan.lot || editingLot) {
    return (
      <div className={s.studio}>
        <Toolbar
          treatment={treatment}
          rules={rules}
          problemCount={0}
          onReset={reset}
          onPreview={() => setSheetOpen(true)}
          canPreview={false}
        />
        <div className={s.emptyWrap}>
          <LotForm
            stateCode={plan.stateCode}
            onStateChange={setState}
            onSubmit={startPlan}
          />
        </div>
      </div>
    );
  }

  return (
    <div className={s.studio}>
      <Toolbar
        treatment={treatment}
        rules={rules}
        problemCount={problemCount}
        onReset={reset}
        onPreview={() => setSheetOpen(true)}
        canPreview
      />

      {restored && (
        <p className={s.restored} role="status">
          Restored the plan you were drawing.{' '}
          <button type="button" className={s.linkBtn} onClick={reset}>
            Start over
          </button>
        </p>
      )}

      {!canDrag && (
        <p className={s.mobileNote}>
          Drawing is easier on a larger screen — your plan is saved on this
          device. Tap an element, then set its distances below.
        </p>
      )}

      <div className={s.grid}>
        {isDesktop && (
          <div className={s.colLeft}>
            <Toolbox
              plan={plan}
              onAdd={addElement}
              onEditLot={() => setEditingLot(true)}
              onSetback={(key, value) => dispatch({ t: 'SET_SETBACK', key, value })}
              onFrontEdge={(edge) => dispatch({ t: 'SET_FRONT_EDGE', edge })}
              onNorth={(deg) => dispatch({ t: 'SET_NORTH', deg })}
            />
          </div>
        )}

        <div className={s.colMain}>
          {/* compact: the state's owner-drawn paragraph runs to five lines
              for Alaska and would push the drawing below the fold. It prints
              in the rules panel instead; the counter note stays here. */}
          <StateSelect
            stateCode={plan.stateCode}
            rules={rules}
            treatment={treatment}
            onChange={setState}
            compact
          />
          <PlanCanvas
            key={`${plan.lot.w}x${plan.lot.d}`}
            plan={plan}
            result={result}
            activeRowId={activeRowId}
            hoverElementId={hoverElementId}
            onRowHover={setActiveRowId}
            onSelect={(id) => dispatch({ t: 'SELECT', id })}
            onMove={(id, x, y) => dispatch({ t: 'MOVE_ELEMENT', id, x, y })}
            onRotate={(id, rot) => dispatch({ t: 'ROTATE_ELEMENT', id, rot })}
            onNudge={(dx, dy) => dispatch({ t: 'NUDGE', dx, dy })}
            onDelete={() =>
              plan.selectedId &&
              dispatch({ t: 'DELETE_ELEMENT', id: plan.selectedId })
            }
            draggable={canDrag}
          />
        </div>

        <div className={s.colRight}>
          <Inspector
            plan={plan}
            selected={selected}
            onResize={(id, w, d) => dispatch({ t: 'RESIZE_ELEMENT', id, w, d })}
            onRotate={(id, rot) => dispatch({ t: 'ROTATE_ELEMENT', id, rot })}
            onSetEdgeDistance={(id, edge, feet) =>
              dispatch({ t: 'SET_EDGE_DISTANCE', id, edge, feet })
            }
            onDelete={(id) => dispatch({ t: 'DELETE_ELEMENT', id })}
            onHoverElement={setHoverElementId}
            draggable={canDrag}
          />
          <ConflictList
            result={result}
            rules={rules}
            activeRowId={activeRowId}
            onRowHover={setActiveRowId}
          />
        </div>

        {!isDesktop && (
          <div className={s.colLeft}>
            <Toolbox
              plan={plan}
              onAdd={addElement}
              onEditLot={() => setEditingLot(true)}
              onSetback={(key, value) => dispatch({ t: 'SET_SETBACK', key, value })}
              onFrontEdge={(edge) => dispatch({ t: 'SET_FRONT_EDGE', edge })}
              onNorth={(deg) => dispatch({ t: 'SET_NORTH', deg })}
            />
          </div>
        )}
      </div>

      {sheetOpen && (
        <SheetModal
          plan={plan}
          onClose={() => setSheetOpen(false)}
          onTitleChange={(key, value) => dispatch({ t: 'SET_TITLE_FIELD', key, value })}
          onExport={onExport}
          rules={rules}
          result={result}
        />
      )}
    </div>
  );
}

function Toolbar({
  treatment,
  rules,
  problemCount,
  onReset,
  onPreview,
  canPreview,
}: {
  treatment: ReturnType<typeof treatmentFor>;
  rules: ReturnType<typeof getStateRules> | null;
  problemCount: number;
  onReset: () => void;
  onPreview: () => void;
  canPreview: boolean;
}) {
  return (
    <div className={`${s.toolbar} no-print`}>
      <span className={s.toolbarNo}>SP-01 · Site plan</span>
      <VerificationChip treatment={treatment} rules={rules} />
      {problemCount > 0 && (
        <span className={s.toolbarFlag}>
          ⚠ {problemCount} to check
        </span>
      )}
      <span className={s.toolbarSpacer} />
      <button type="button" className={s.ghostBtn} onClick={onReset}>
        Reset
      </button>
      <button
        type="button"
        className={s.primaryBtnSm}
        onClick={onPreview}
        disabled={!canPreview}
      >
        Preview sheet ▸
      </button>
    </div>
  );
}

function SheetModal({
  plan,
  result,
  rules,
  onClose,
  onTitleChange,
  onExport,
}: {
  plan: Plan;
  result: ReturnType<typeof check>;
  rules: ReturnType<typeof getStateRules> | null;
  onClose: () => void;
  onTitleChange: (key: keyof TitleFields, value: string) => void;
  onExport: (method: 'print' | 'svg') => void;
}) {
  const closeOnSelf = (e: React.MouseEvent) => {
    if (e.target === e.currentTarget) onClose();
  };
  return (
    <div
      className={s.modal}
      role="dialog"
      aria-modal="true"
      aria-label="Sheet preview"
      onMouseDown={closeOnSelf}
    >
      <button
        type="button"
        className={`${s.modalClose} no-print`}
        onClick={onClose}
        aria-label="Close sheet preview"
      >
        ×
      </button>
      <div className={`${s.modalBar} no-print`}>
        <span className={s.toolbarNo}>SP-01 · Sheet preview</span>
        <span className={s.toolbarSpacer} />
      </div>
      <div className={s.modalBody} onMouseDown={closeOnSelf}>
        <ExportSheet
          plan={plan}
          result={result}
          rules={rules}
          onTitleChange={onTitleChange}
          onExport={onExport}
        />
        <SheetCapture plan={plan} result={result} rules={rules} />
      </div>
    </div>
  );
}
