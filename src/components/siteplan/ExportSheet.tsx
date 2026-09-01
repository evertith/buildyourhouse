'use client';

/**
 * The letter sheet: preview and print target, one component (§3).
 *
 * Print-to-PDF is the hand-off format. Print CSS costs nothing, gives a true
 * vector PDF through the browser's own Save-as-PDF, and the codebase already
 * carries the `no-print` convention. jsPDF and svg2pdf are a dependency to
 * reproduce what Cmd+P already does perfectly, which is a bad trade on a
 * static-export site. The SVG download is thirty lines and is here for the
 * person who wants to edit the drawing, not for the permit counter.
 *
 * The drawing is rendered by the same PlanScene the editor uses, at a true
 * engineering scale: the viewBox is sized so one inch of paper is exactly
 * the feet printed in the title block, and a graphic bar scale is drawn
 * alongside so the sheet survives being photocopied at 94%.
 */

import { useMemo, useRef } from 'react';
import s from '@/styles/ExportSheet.module.css';
import { barScale, formatScale, pickScale } from '@/lib/siteplan/scale';
import { formatFeetShort } from '@/lib/siteplan/geometry';
import { geometryRows, sheetRows } from '@/lib/siteplan/check';
import type { StateSiteplanRules } from '@/lib/siteplan/rules';
import type { CheckResult, Plan, TitleFields } from '@/lib/siteplan/types';
import { ELEMENT_KINDS, KIND_LABEL } from '@/lib/siteplan/types';
import PlanScene from './PlanScene';
import TitleBlock, { NorthBox } from './TitleBlock';

/** Drawing window, inches. Portrait letter with a 0.5in margin is 7.5 x 10. */
const WIN_W = 5.05;
const WIN_H = 5.85;
/** Room outside the property line for the lot dimension lines and labels. */
const WIN_PAD = 0.5;
const PX_PER_IN = 96;
/** Height of the graphic bar scale band, inches. */
const BAR_H = 0.3;

interface Props {
  plan: Plan;
  result: CheckResult;
  rules: StateSiteplanRules | null;
  onTitleChange: (key: keyof TitleFields, value: string) => void;
  onExport: (method: 'print' | 'svg') => void;
}

const LEGEND = ELEMENT_KINDS.filter((k) => k !== 'structure');

export default function ExportSheet({
  plan,
  result,
  rules,
  onTitleChange,
  onExport,
}: Props) {
  const svgRef = useRef<SVGSVGElement | null>(null);
  const lot = plan.lot;

  const date = useMemo(() => {
    const d = new Date();
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(
      d.getDate()
    ).padStart(2, '0')}`;
  }, []);

  const feetPerInch = lot
    ? pickScale(lot.w, lot.d, WIN_W - WIN_PAD, WIN_H - WIN_PAD)
    : 20;
  const bar = barScale(feetPerInch);
  const rows = sheetRows(result);
  const geo = geometryRows(plan, result.rows);
  const conditional = result.notes.filter((n) => n.conditional);
  const negatives = result.notes.filter((n) => n.id.startsWith('null-'));
  const hedged = result.treatment === 'hedged';

  if (!lot) return null;

  // One inch of paper is exactly `feetPerInch` feet, so the viewBox spans
  // the window's width in inches times the scale.
  const vw = feetPerInch * WIN_W;
  const vh = feetPerInch * WIN_H;
  const viewBox = `${lot.w / 2 - vw / 2} ${lot.d / 2 - vh / 2} ${vw} ${vh}`;
  const u = vw / (WIN_W * PX_PER_IN);

  // The bar's viewBox has to carry the SAME aspect as the box it is drawn in,
  // or preserveAspectRatio fits it by height and the bar comes out a third of
  // its intended length with the tick labels crushed together.
  const barWIn = bar.totalFeet / feetPerInch;
  const barVbH = bar.totalFeet * (BAR_H / barWIn);

  const downloadSvg = () => {
    const node = svgRef.current;
    if (!node) return;
    const clone = node.cloneNode(true) as SVGSVGElement;
    clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    clone.setAttribute('width', `${WIN_W}in`);
    clone.setAttribute('height', `${WIN_H}in`);
    // The drawing leans on the site's custom properties; a standalone file
    // has no :root to inherit them from, so they are stamped on the SVG.
    const style = document.createElementNS('http://www.w3.org/2000/svg', 'style');
    style.textContent = `svg{--text-heading:#1a1710;--text-secondary:#56503f;--bg-primary:#f2ecdf;--hairline:rgba(35,32,25,0.16);--hairline-strong:rgba(35,32,25,0.32);--accent-primary:#c75a22;--accent-critical:#b23a2a;--accent-warning:#d98324;--accent-info:#2f5d7c;--font-mono:ui-monospace,'SF Mono',Menlo,monospace;}`;
    clone.insertBefore(style, clone.firstChild);
    const blob = new Blob([new XMLSerializer().serializeToString(clone)], {
      type: 'image/svg+xml;charset=utf-8',
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'site-plan-SP-01.svg';
    a.click();
    URL.revokeObjectURL(url);
    onExport('svg');
  };

  const print = () => {
    onExport('print');
    window.print();
  };

  return (
    <>
      {/* The sheet is 7.5in wide by definition. The frame scrolls and scales
          it so a phone never pushes the page sideways (§5). */}
      <div className={s.sheetFrame}>
        <div className={s.sheetScaler}>
          <div className={s.sheetRoot} id="sp-sheet">
        <div className={s.rule} />

        {/* A div, not a <header>: globals.css prints `header, footer, nav
            { display: none }`, which would silently drop the sheet's title
            and north arrow from every printed plan. */}
        <div className={s.sheetHead}>
          <div>
            <h3 className={s.sheetTitle}>Site plan</h3>
            <p className={s.sheetSub}>
              Owner-prepared plot plan
              {rules ? ` · ${rules.state}` : ''}
            </p>
          </div>
          <NorthBox deg={plan.north} />
        </div>

        <div className={s.sheetMain}>
          <div className={s.drawingCol}>
            <div className={s.window}>
              <svg
                ref={svgRef}
                className={s.drawing}
                viewBox={viewBox}
                width={`${WIN_W}in`}
                height={`${WIN_H}in`}
                preserveAspectRatio="xMidYMid meet"
                role="img"
                aria-label={`Site plan, ${lot.w} by ${lot.d} feet, drawn at ${formatScale(feetPerInch)}`}
              >
                <PlanScene plan={plan} result={result} u={u} mode="sheet" />
              </svg>
            </div>

            <div className={s.barScale}>
              <svg
                viewBox={`0 0 ${bar.totalFeet} ${barVbH}`}
                width={`${barWIn}in`}
                height={`${BAR_H}in`}
                preserveAspectRatio="xMinYMid meet"
                aria-hidden="true"
              >
                <line
                  x1="0"
                  y1={barVbH * 0.66}
                  x2={bar.totalFeet}
                  y2={barVbH * 0.66}
                  stroke="var(--text-heading)"
                  strokeWidth="1"
                  vectorEffect="non-scaling-stroke"
                />
                {/* Alternating filled cells: the convention that lets a bar
                    scale be read at a glance after a bad photocopy. */}
                {bar.ticks.slice(0, -1).map((tk, i) =>
                  i % 2 === 0 ? (
                    <rect
                      key={`f-${tk}`}
                      x={tk}
                      y={barVbH * 0.55}
                      width={bar.interval}
                      height={barVbH * 0.11}
                      fill="var(--text-heading)"
                    />
                  ) : null
                )}
                {bar.ticks.map((tk, i) => (
                  <g key={tk}>
                    <line
                      x1={tk}
                      y1={barVbH * 0.48}
                      x2={tk}
                      y2={barVbH * 0.84}
                      stroke="var(--text-heading)"
                      strokeWidth="1"
                      vectorEffect="non-scaling-stroke"
                    />
                    <text
                      x={tk}
                      y={barVbH * 0.3}
                      textAnchor={
                        i === 0 ? 'start' : i === bar.ticks.length - 1 ? 'end' : 'middle'
                      }
                      fontFamily="var(--font-mono)"
                      fontSize={barVbH * 0.36}
                      fill="var(--text-secondary)"
                    >
                      {tk}
                    </text>
                  </g>
                ))}
              </svg>
              <span className={s.barLabel}>
                feet · {formatScale(feetPerInch)}
              </span>
            </div>
          </div>

          <aside className={s.tableCol}>
            <p className={s.tableHead}>
              Separations
              <span className={s.tableState}>
                {rules ? rules.state : 'No state selected'}
              </span>
            </p>

            {result.treatment === 'none' && (
              <p className={s.tableEmpty}>
                No state was selected, so no separation requirement was checked.
                The dimensions on this drawing are still measured from what was
                drawn.
              </p>
            )}

            {result.treatment === 'local' && (
              <div className={s.tableNegative}>
                {negatives.slice(0, 2).map((n) => (
                  <p key={n.id} className={s.tableNegText}>
                    {n.text}
                  </p>
                ))}
              </div>
            )}

            {(result.treatment === 'rules' || hedged) && rows.length === 0 && (
              <p className={s.tableEmpty}>
                Nothing to check — no pair of elements on this drawing is
                governed by a distance in the schedule.
              </p>
            )}

            {(result.treatment === 'rules' || hedged) &&
              rows.map((r) => (
                <div
                  key={r.id}
                  className={`${s.tableRow} ${
                    r.status === 'violation'
                      ? s.tableRowBad
                      : r.status === 'watch'
                        ? s.tableRowWatch
                        : ''
                  }`}
                >
                  <p className={s.rowLabel}>{r.label}</p>
                  <p className={s.rowNums}>
                    <span>
                      {hedged ? '† ' : ''}
                      {r.hedged ? 'typ' : 'req'} {r.requiredFeet}&apos;
                    </span>
                    <span className={s.rowAct}>
                      act {formatFeetShort(r.measuredFeet ?? 0)}
                    </span>
                    <span className={s.rowMark}>
                      {r.status === 'violation' ? '✗' : r.status === 'watch' ? '!' : '✓'}
                    </span>
                  </p>
                  {r.citation && <p className={s.rowCite}>{r.citation}</p>}
                </div>
              ))}

            {geo.length > 0 && (
              <>
                <p className={s.tableMeasuredHead}>Measured from the drawing</p>
                {geo.map((g) => (
                  <div key={g.id} className={s.tableRow}>
                    <p className={s.rowLabel}>{g.label}</p>
                    <p className={s.rowNums}>
                      <span className={s.rowAct}>
                        {formatFeetShort(g.measuredFeet ?? 0)}
                      </span>
                    </p>
                  </div>
                ))}
              </>
            )}

            <p className={s.tableFoot}>
              {hedged ? (
                <>
                  † Typical values — {rules?.state}&apos;s requirements were not
                  verified. Confirm with your county health department.
                </>
              ) : result.treatment === 'none' ? (
                <>Distances measured from the drawing above.</>
              ) : (
                <>Sources verified {rules?.verifiedDate ?? 'August 2026'}</>
              )}
            </p>
          </aside>
        </div>

        <div className={s.legend}>
          <span className={s.legendKey}>Legend</span>
          {LEGEND.map((k) => (
            <span key={k} className={s.legendItem}>
              <LegendGlyph kind={k} />
              {KIND_LABEL[k].toLowerCase()}
            </span>
          ))}
          <span className={s.legendItem}>
            <svg viewBox="0 0 18 8" className={s.legendSvg} aria-hidden="true">
              <line x1="0" y1="4" x2="18" y2="4" stroke="var(--accent-info)" strokeWidth="1.2" strokeDasharray="6 3" />
            </svg>
            setback
          </span>
        </div>

        {(conditional.length > 0 || plan.title.irregular || negatives.length > 0) && (
          <div className={s.notes}>
            <span className={s.notesKey}>Notes</span>
            <div className={s.notesBody}>
              {plan.title.irregular && (
                <p className={s.note}>
                  <strong>Lot shape.</strong> {plan.title.irregular}
                </p>
              )}
              {result.treatment !== 'local' &&
                negatives.slice(0, 1).map((n) => (
                  <p key={n.id} className={s.note}>
                    <strong>{n.label}.</strong> {n.text}
                  </p>
                ))}
              {conditional.slice(0, 3).map((n) => (
                <p key={n.id} className={s.note}>
                  <strong>
                    {n.label}
                    {n.feet != null ? ` — ${n.feet} ft` : ''}.
                  </strong>{' '}
                  {n.text}
                  {n.citation ? ` (${n.citation})` : ''}
                </p>
              ))}
            </div>
          </div>
        )}

        <TitleBlock
          title={plan.title}
          onChange={onTitleChange}
          scaleLabel={formatScale(feetPerInch)}
          date={date}
          rules={rules}
          treatment={result.treatment}
        />
          </div>
        </div>
      </div>

      <div className={`${s.sheetTools} no-print`}>
        <p className={s.printHint}>
          In the print dialogue: set Margins to <strong>Default</strong>, turn{' '}
          <strong>Headers and footers</strong> off, and choose{' '}
          <strong>Save as PDF</strong>.
        </p>
        <div className={s.sheetBtns}>
          <button type="button" className={s.printBtn} onClick={print}>
            Print / Save as PDF
          </button>
          <button type="button" className={s.svgBtn} onClick={downloadSvg}>
            Download SVG
          </button>
        </div>
      </div>
    </>
  );
}

function LegendGlyph({ kind }: { kind: (typeof ELEMENT_KINDS)[number] }) {
  const ink = 'var(--text-heading)';
  return (
    <svg viewBox="0 0 18 10" className={s.legendSvg} aria-hidden="true">
      {kind === 'house' && <rect x="1" y="2" width="16" height="6" fill="none" stroke={ink} strokeWidth="1.6" />}
      {kind === 'well' && (
        <>
          <circle cx="9" cy="5" r="3" fill="none" stroke={ink} strokeWidth="1" />
          <line x1="4" y1="5" x2="14" y2="5" stroke={ink} strokeWidth="0.8" />
          <line x1="9" y1="0.5" x2="9" y2="9.5" stroke={ink} strokeWidth="0.8" />
        </>
      )}
      {kind === 'septicTank' && (
        <>
          <rect x="2" y="2" width="14" height="6" fill="none" stroke={ink} strokeWidth="1" />
          <rect x="3.6" y="3.4" width="10.8" height="3.2" fill="none" stroke={ink} strokeWidth="0.7" />
        </>
      )}
      {kind === 'drainfield' && (
        <>
          <rect x="1" y="2" width="16" height="6" fill="none" stroke={ink} strokeWidth="0.9" />
          <line x1="2" y1="4" x2="16" y2="4" stroke={ink} strokeWidth="0.7" strokeDasharray="2 1.5" />
          <line x1="2" y1="6" x2="16" y2="6" stroke={ink} strokeWidth="0.7" strokeDasharray="2 1.5" />
        </>
      )}
      {kind === 'driveway' && (
        <>
          <line x1="3" y1="1" x2="3" y2="9" stroke={ink} strokeWidth="1" />
          <line x1="15" y1="1" x2="15" y2="9" stroke={ink} strokeWidth="1" />
          <circle cx="9" cy="5" r="0.7" fill={ink} opacity="0.5" />
        </>
      )}
      {kind === 'waterEdge' && (
        <>
          <line x1="1" y1="5" x2="17" y2="5" stroke="#4a6b80" strokeWidth="1.5" />
          <path d="M3 5 q1.5 -2 3 0 M11 5 q1.5 -2 3 0" fill="none" stroke="#4a6b80" strokeWidth="0.8" />
        </>
      )}
    </svg>
  );
}
