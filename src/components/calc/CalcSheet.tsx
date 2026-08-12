'use client';

/**
 * The takeoff sheet — shared frame for every trade calculator
 * (design spec §3.2, §4.4–4.7, §5).
 *
 * The page-specific calculator component owns input state and the engine
 * call; this component renders the sheet chrome, the materials schedule,
 * cost dimension line, optional hatched breakdown bars, copy/print tools,
 * the mobile sticky bar, screen-reader announcements, and the tear-off
 * email capture.
 */

import { ReactNode, useEffect, useMemo, useRef, useState } from 'react';
import s from '@/styles/CalcSheet.module.css';
import { CalcResult } from '@/lib/calc/types';
import { formatCostRange, formatCurrency, formatQty } from '@/lib/calc/format';
import { trackEvent } from '@/lib/analytics';
import EstimateCapture from './EstimateCapture';

export interface BarRow {
  key: string;
  label: string;
  qty: number;
  valueLabel: string;
}

interface CalcSheetProps {
  slug: string;
  sheetNo: string; // "TO-02"
  sheetTitle: string; // "Drywall takeoff"
  calculatorName: string; // "Drywall Calculator"
  result: CalcResult;
  /** Current inputs, human-readable — feeds copy text and the estimate email. */
  inputsSummary: { label: string; value: string }[];
  /** Optional hatched breakdown (spec §4.6) — only when components are meaningful. */
  bars?: BarRow[];
  barsLabel?: string;
  /** One-line basis for the fine print: "quantities assume …" */
  finePrintBasis: string;
  children: ReactNode; // input fields
}

const ANNOUNCE_DEBOUNCE_MS = 600;

export default function CalcSheet({
  slug,
  sheetNo,
  sheetTitle,
  calculatorName,
  result,
  inputsSummary,
  bars,
  barsLabel,
  finePrintBasis,
  children,
}: CalcSheetProps) {
  const [copied, setCopied] = useState(false);
  const [announcement, setAnnouncement] = useState('');
  const [stickyHidden, setStickyHidden] = useState(true);
  const resultsRef = useRef<HTMLDivElement | null>(null);
  const firstRender = useRef(true);
  const useTracked = useRef(false);

  const resultKey = useMemo(() => JSON.stringify(result), [result]);

  // Debounced SR announcement + one-shot calculator_use (spec §5.3–5.4):
  // never on initial load, never per keystroke.
  useEffect(() => {
    if (firstRender.current) {
      firstRender.current = false;
      return;
    }
    const t = setTimeout(() => {
      const topLines = result.lines
        .slice(0, 3)
        .map((l) => `${formatQty(l.qty)} ${l.unit} ${l.label.toLowerCase()}`)
        .join(', ');
      setAnnouncement(
        `Takeoff updated: ${topLines}, cost ${formatCurrency(result.costLow)} to ${formatCurrency(result.costHigh)}.`
      );
      if (!useTracked.current) {
        useTracked.current = true;
        trackEvent('calculator_use', { calculator: slug });
      }
    }, ANNOUNCE_DEBOUNCE_MS);
    return () => clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [resultKey, slug]);

  // Mobile sticky bar: visible only while the schedule is off-screen.
  useEffect(() => {
    const node = resultsRef.current;
    if (!node || typeof IntersectionObserver === 'undefined') {
      setStickyHidden(false);
      return;
    }
    const obs = new IntersectionObserver(
      ([entry]) => setStickyHidden(entry.isIntersecting),
      { rootMargin: '0px 0px -40px 0px' }
    );
    obs.observe(node);
    return () => obs.disconnect();
  }, []);

  const copyTakeoff = async () => {
    const text = [
      `${calculatorName} — takeoff (${sheetNo})`,
      `build-your-house.com/calculators/${slug}`,
      '',
      'Inputs:',
      ...inputsSummary.map((i) => `  ${i.label}: ${i.value}`),
      '',
      'Materials:',
      ...result.lines.map((l) => `  ${l.label}: ${formatQty(l.qty)} ${l.unit}`),
      '',
      `Estimated material cost: ${formatCostRange(result.costLow, result.costHigh)}`,
      'Estimate only — verify against your plans and local prices.',
    ].join('\n');
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      trackEvent('calculator_copy', { calculator: slug });
      setTimeout(() => setCopied(false), 1500);
    } catch {
      // Clipboard unavailable — quietly do nothing rather than break the sheet.
    }
  };

  const maxBarQty = bars && bars.length ? Math.max(...bars.map((b) => b.qty)) : 0;
  const leadIndex =
    bars && bars.length ? bars.findIndex((b) => b.qty === maxBarQty) : -1;

  const estimatePayload = {
    calculator: slug,
    calculatorName,
    hero: `${formatQty(result.hero.qty)} ${result.hero.unit}`,
    inputs: inputsSummary,
    lines: result.lines.map((l) => ({
      label: l.label,
      value: `${formatQty(l.qty)} ${l.unit}${l.detail ? ` — ${l.detail}` : ''}`,
    })),
    cost: formatCostRange(result.costLow, result.costHigh),
  };

  return (
    <div className={s.sheet}>
      <div className={s.sheetHead}>
        <span className={s.sheetNo}>{sheetNo} · {sheetTitle}</span>
        <span className={`${s.sheetTools} no-print`}>
          <button type="button" className={s.toolBtn} onClick={copyTakeoff}>
            {copied ? 'Copied' : 'Copy takeoff'}
          </button>
          <button type="button" className={s.toolBtn} onClick={() => window.print()}>
            Print
          </button>
        </span>
      </div>

      <div className={s.sheetBody}>
        <div className={s.inputsCol}>
          <p className={s.colLabel}>Field measurements</p>
          {children}
        </div>

        <div className={s.resultsCol} id="takeoff" ref={resultsRef}>
          <div aria-hidden="true">
            <p className={s.colLabel}>Materials schedule</p>
            <div className={s.heroQty}>
              <span className={s.heroQtyVal}>{formatQty(result.hero.qty)}</span>
              <span className={s.heroQtyUnit}>
                {/* Skip the unit when the label already carries it ("Total studs"). */}
                {result.hero.label.toLowerCase().includes(result.hero.unit.toLowerCase())
                  ? result.hero.label
                  : `${result.hero.unit} · ${result.hero.label}`}
              </span>
            </div>
            {result.hero.detail && <p className={s.heroQtyDetail}>{result.hero.detail}</p>}

            <ul className={s.schedule}>
              {result.lines.map((line) => (
                <li key={line.id} className={s.schedLine}>
                  <span className={s.schedKey}>{line.label}</span>
                  <span className={s.schedLeader} />
                  <span className={s.schedVal}>{formatQty(line.qty)} {line.unit}</span>
                </li>
              ))}
            </ul>

            <div className={s.costDim}>
              <p className={s.costDimLabel}>
                Estimated material cost
                <span className={s.costDimNote}>national range</span>
              </p>
              <div
                className={s.costDimBar}
                role="img"
                aria-label={`Estimated material cost between ${formatCurrency(result.costLow)} and ${formatCurrency(result.costHigh)}`}
              >
                <span className={s.costLow}>{formatCurrency(result.costLow)}</span>
                <span className={s.costTrack}><span className={s.costSpan} /></span>
                <span className={s.costHigh}>{formatCurrency(result.costHigh)}</span>
              </div>
            </div>

            {bars && bars.length > 1 && (
              <div className={s.bars}>
                <p className={s.barsLabel}>{barsLabel ?? 'Where it goes'}</p>
                {bars.map((r, i) => (
                  <div key={r.key} className={s.barRow}>
                    <span className={s.barKey}>{r.label}</span>
                    <span className={s.barTrack}>
                      <span
                        className={`${s.barFill} ${i === leadIndex ? s.barFillLead : ''}`}
                        style={{ width: `${maxBarQty > 0 ? Math.max(2, (r.qty / maxBarQty) * 100) : 2}%` }}
                      />
                    </span>
                    <span className={s.barVal}>{r.valueLabel}</span>
                  </div>
                ))}
              </div>
            )}

            <p className={s.finePrint}>
              Estimate only. Quantities assume {finePrintBasis}; order after a
              takeoff from your actual plans. Prices are national ranges,
              August 2026 — get local quotes.
            </p>
          </div>

          {/* Screen-reader channel for the live results (spec §5.4). */}
          <div role="status" aria-live="polite" className="visually-hidden">
            {announcement}
          </div>
        </div>
      </div>

      <EstimateCapture payload={estimatePayload} />

      <p className={s.printMeta}>
        Printed from build-your-house.com/calculators/{slug} — estimate only.
      </p>

      <div
        className={`${s.stickyBar} ${stickyHidden ? s.stickyBarHidden : ''} no-print`}
        aria-hidden="true"
      >
        <span className={s.stickyBarQty}>
          {formatQty(result.hero.qty)} {result.hero.unit}
        </span>
        <a href="#takeoff" className={s.stickyBarLink}>View takeoff →</a>
      </div>
    </div>
  );
}
