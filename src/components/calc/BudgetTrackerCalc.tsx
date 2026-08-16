'use client';

import { useEffect, useMemo, useState } from 'react';
import s from '@/styles/CalcSheet.module.css';
import CalcSheet, { BarRow } from './CalcSheet';
import { NumberField } from './fields';
import {
  BudgetCategoryInput,
  DEFAULT_BUDGET_CATEGORIES,
  DEFAULT_CONTINGENCY_PCT,
  calculateBudgetTracker,
} from '@/lib/calc/budgetTracker';
import { formatCurrency } from '@/lib/calc/format';

/**
 * W-04 is a ledger, not a two-input takeoff: the visitor types a planned and
 * an actual figure per phase and comes back to it every few weeks. So the
 * entries persist locally — losing a build's worth of typing on a page
 * refresh would make the tool useless — and the state is restored after
 * mount, never during render, so the server and client markup agree.
 */
const STORAGE_KEY = 'byh:budget-tracker:v1';

interface StoredState {
  categories: { id: string; planned: number; actual: number }[];
  contingencyPct: number;
}

export default function BudgetTrackerCalc() {
  const [categories, setCategories] = useState<BudgetCategoryInput[]>(DEFAULT_BUDGET_CATEGORIES);
  const [contingencyPct, setContingencyPct] = useState(DEFAULT_CONTINGENCY_PCT);
  const [hydrated, setHydrated] = useState(false);

  // Restore after mount — reading localStorage during render would produce
  // markup the server never sent. The one extra render this costs is the
  // price of a statically exported page that still remembers your entries.
  /* eslint-disable react-hooks/set-state-in-effect */
  useEffect(() => {
    try {
      const saved = window.localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved) as StoredState;
        if (Array.isArray(parsed?.categories)) {
          setCategories((prev) =>
            prev.map((c) => {
              const hit = parsed.categories.find((p) => p.id === c.id);
              return hit
                ? { ...c, planned: Number(hit.planned) || 0, actual: Number(hit.actual) || 0 }
                : c;
            })
          );
        }
        if (Number.isFinite(parsed?.contingencyPct)) setContingencyPct(parsed.contingencyPct);
      }
    } catch {
      // Storage blocked or corrupt — fall back to the default plan.
    }
    setHydrated(true);
  }, []);
  /* eslint-enable react-hooks/set-state-in-effect */

  useEffect(() => {
    if (!hydrated) return;
    try {
      const payload: StoredState = {
        categories: categories.map(({ id, planned, actual }) => ({ id, planned, actual })),
        contingencyPct,
      };
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
    } catch {
      // Private mode / quota — the sheet still works, it just won't remember.
    }
  }, [hydrated, categories, contingencyPct]);

  const setAmount = (id: string, field: 'planned' | 'actual', value: number) =>
    setCategories((prev) => prev.map((c) => (c.id === id ? { ...c, [field]: value } : c)));

  const reset = () => {
    setCategories(DEFAULT_BUDGET_CATEGORIES);
    setContingencyPct(DEFAULT_CONTINGENCY_PCT);
  };

  const result = useMemo(
    () => calculateBudgetTracker({ categories, contingencyPct }),
    [categories, contingencyPct]
  );

  // Before anything is spent the actual-cost bars would all be empty, so the
  // breakdown shows how the plan is allocated until the first dollar lands.
  const spending = result.totalActual > 0;
  const bars: BarRow[] = result.categories.map((c) => ({
    key: c.id,
    label: shortLabel(c.label),
    qty: spending ? c.actual : c.planned,
    valueLabel: formatCurrency(spending ? c.actual : c.planned),
  }));

  return (
    <CalcSheet
      slug="budget-tracker"
      sheetNo="W-04"
      sheetTitle="Budget worksheet"
      calculatorName="Budget Tracker"
      inputsLabel="Planned & spent"
      result={result}
      bars={bars}
      barsLabel={spending ? 'Where the money has gone' : 'Where the plan puts it'}
      finePrintBasis="your own planned and actual figures, with a phase counted on track inside ±5% of plan"
      inputsSummary={[
        { label: 'Contingency', value: `${contingencyPct}% of plan` },
        ...result.categories.map((c) => ({
          label: c.label,
          value: `${formatCurrency(c.planned)} planned / ${formatCurrency(c.actual)} spent`,
        })),
      ]}
    >
      <NumberField
        label="Contingency reserve"
        unit="%"
        value={contingencyPct}
        onChange={setContingencyPct}
        step={1}
        hint="Typically 10–20% of the planned total"
      />

      {categories.map((c) => (
        <div key={c.id} className={s.field}>
          <p className={s.colLabel}>{c.label}</p>
          {/* minmax(0,…): number inputs carry a ~230px intrinsic min-content
              that would otherwise blow this grid out past phone widths */}
          <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0,1fr) minmax(0,1fr)', gap: 'var(--space-3)' }}>
            <NumberField
              label="Planned"
              unit="$"
              value={c.planned}
              onChange={(v) => setAmount(c.id, 'planned', v)}
              step={1000}
            />
            <NumberField
              label="Spent"
              unit="$"
              value={c.actual}
              onChange={(v) => setAmount(c.id, 'actual', v)}
              step={1000}
            />
          </div>
        </div>
      ))}

      {result.flags.length > 0 && (
        <div className={s.field}>
          <span className={s.fieldLabel}>Flags</span>
          {result.flags.map((f) => (
            <span key={f} className={s.fieldHint}>
              {f}
            </span>
          ))}
        </div>
      )}

      <div className={`${s.field} no-print`}>
        {/* .toolBtn is hidden below 900px (copy/print are desktop tools); this
            one has to survive on a phone, so the display is forced back on. */}
        <button
          type="button"
          className={s.toolBtn}
          style={{ display: 'inline-block', minHeight: 44 }}
          onClick={reset}
        >
          Reset to the sample plan
        </button>
        <span className={s.fieldHint}>
          Your figures stay in this browser — they are never sent anywhere unless you email
          yourself the sheet below.
        </span>
      </div>
    </CalcSheet>
  );
}

function shortLabel(label: string): string {
  return label
    .replace('Site Prep & Foundation', 'Site/foundation')
    .replace('Framing & Exterior', 'Framing/ext.')
    .replace('Rough-Ins (MEP)', 'Rough-ins')
    .replace('Insulation & Drywall', 'Insul./drywall')
    .replace('Interior Finishes', 'Interior')
    .replace('Final & Landscaping', 'Final/site');
}
