'use client';

/**
 * The rules panel: what is wrong, what is close, and what the state
 * actually says.
 *
 * Order is severity order, and it is not negotiable. An element over the
 * property line outranks every separation conflict — a septic tank 8 ft from
 * the well is a design problem, a septic tank on the neighbor's land is a
 * different kind of problem. Then the owner's own setbacks, marked as the
 * owner's. Then the state's separations. Then the sourced findings.
 *
 * In a hedged state the heading is "Check these", the verb is "may need",
 * and the requirement column says "typical". Nothing is called a violation,
 * because nothing has been verified to violate.
 */

import s from '@/styles/SitePlanStudio.module.css';
import { formatFeetShort } from '@/lib/siteplan/geometry';
import type { CheckResult, MeasureRow } from '@/lib/siteplan/types';
import { EDGE_LABEL } from '@/lib/siteplan/types';
import type { StateSiteplanRules } from '@/lib/siteplan/rules';

interface Props {
  result: CheckResult;
  rules: StateSiteplanRules | null;
  activeRowId: string | null;
  onRowHover: (id: string | null) => void;
}

function Row({
  row,
  active,
  onHover,
}: {
  row: MeasureRow;
  active: boolean;
  onHover: (id: string | null) => void;
}) {
  const short = row.status === 'violation' || row.status === 'watch';
  const cls = [
    s.ruleRow,
    row.status === 'violation' ? s.ruleRowBad : '',
    row.status === 'watch' ? s.ruleRowWatch : '',
    row.status === 'unplaced' ? s.ruleRowIdle : '',
    active ? s.ruleRowActive : '',
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <li
      className={cls}
      onMouseEnter={() => onHover(row.id)}
      onMouseLeave={() => onHover(null)}
    >
      <div className={s.ruleHead}>
        <span className={s.ruleLabel}>{row.label}</span>
        <span className={s.ruleMark} aria-hidden="true">
          {row.status === 'violation' ? '✗' : row.status === 'watch' ? '!' : row.status === 'ok' ? '✓' : '·'}
        </span>
      </div>
      <p className={s.ruleNums}>
        {row.status === 'unplaced' ? (
          <span className={s.ruleIdleText}>
            Not measured — place both to check it.
          </span>
        ) : (
          <>
            <span className={s.ruleMeasured}>
              {formatFeetShort(row.measuredFeet ?? 0)}
            </span>
            <span className={s.ruleVerb}>
              {short ? (row.hedged ? ' may need ' : ' needs ') : ' against '}
            </span>
            <span className={row.hedged ? s.ruleReqHedged : s.ruleReq}>
              {row.hedged ? '† ' : ''}
              {row.requiredFeet} ft {row.hedged ? 'typical' : 'required'}
            </span>
            {row.edge ? (
              <span className={s.ruleEdge}> · {EDGE_LABEL[row.edge].toLowerCase()}</span>
            ) : null}
          </>
        )}
      </p>
      {row.citation && <p className={s.ruleCite}>{row.citation}</p>}
      {row.note && <p className={s.ruleNote}>{row.note}</p>}
    </li>
  );
}

export default function ConflictList({
  result,
  rules,
  activeRowId,
  onRowHover,
}: Props) {
  const { treatment, rows, boundary, setbacks, notes } = result;
  const hedged = treatment === 'hedged';
  const shortCount = rows.filter(
    (r) => r.status === 'violation' || r.status === 'watch'
  ).length;
  const measured = rows.filter((r) => r.status !== 'unplaced');
  const conditional = notes.filter((n) => n.conditional);
  const negatives = notes.filter((n) => !n.conditional && n.id.startsWith('null-'));
  const findings = notes.filter((n) => n.id.startsWith('finding-'));

  return (
    <div className={s.rulesPanel}>
      {boundary.length > 0 && (
        <section className={s.panelSection}>
          <p className={`${s.railLabel} ${s.railLabelBad}`}>
            Outside the property line · {boundary.length}
          </p>
          <ul className={s.ruleList}>
            {boundary.map((b) => (
              <li key={b.id} className={`${s.ruleRow} ${s.ruleRowBad}`}>
                <div className={s.ruleHead}>
                  <span className={s.ruleLabel}>{b.label}</span>
                  <span className={s.ruleMark} aria-hidden="true">✗</span>
                </div>
                <p className={s.ruleNums}>
                  Crosses the {EDGE_LABEL[b.edge].toLowerCase()} by{' '}
                  <span className={s.ruleMeasured}>{formatFeetShort(b.overFeet)}</span>.
                </p>
              </li>
            ))}
          </ul>
        </section>
      )}

      {setbacks.length > 0 && (
        <section className={s.panelSection}>
          <p className={`${s.railLabel} ${s.railLabelInfo}`}>
            Your setbacks · {setbacks.length}
          </p>
          <ul className={s.ruleList}>
            {setbacks.map((w) => (
              <li key={w.id} className={`${s.ruleRow} ${s.ruleRowSetback}`}>
                <div className={s.ruleHead}>
                  <span className={s.ruleLabel}>
                    {w.label} · {EDGE_LABEL[w.edge].toLowerCase()}
                  </span>
                  <span className={s.ruleMark} aria-hidden="true">!</span>
                </div>
                <p className={s.ruleNums}>
                  <span className={s.ruleMeasured}>{formatFeetShort(w.measuredFeet)}</span>
                  <span className={s.ruleVerb}> inside a </span>
                  <span className={s.ruleReq}>{w.requiredFeet} ft setback</span>
                </p>
                <p className={s.ruleNote}>
                  Setback as you entered it — confirm with your zoning ordinance.
                </p>
              </li>
            ))}
          </ul>
        </section>
      )}

      {treatment === 'none' && (
        <section className={s.panelSection}>
          <p className={s.railLabel}>Separations</p>
          <p className={s.panelEmpty}>
            No state selected, so nothing is checked. The drawing still
            measures — pick a state above and the tool will say what that
            state publishes, or that it publishes nothing.
          </p>
        </section>
      )}

      {(treatment === 'rules' || treatment === 'hedged') && (
        <section className={s.panelSection}>
          <p
            className={`${s.railLabel} ${shortCount > 0 ? (hedged ? s.railLabelWarn : s.railLabelBad) : ''}`}
          >
            {hedged ? 'Check these' : 'Separations'}
            {shortCount > 0 ? ` · ${shortCount}` : ''}
          </p>
          {measured.length === 0 && (
            <p className={s.panelEmpty}>
              Place a well and a septic tank or drainfield and the separations
              will measure themselves.
            </p>
          )}
          <ul className={s.ruleList}>
            {rows.map((row) => (
              <Row
                key={row.id}
                row={row}
                active={activeRowId === row.id}
                onHover={onRowHover}
              />
            ))}
          </ul>
          {hedged && (
            <p className={s.daggerNote}>
              † Typical values, not {rules?.state ?? 'this state'}&apos;s rule.
              Nothing here is a violation — it is a prompt to call your county
              health department.
            </p>
          )}
        </section>
      )}

      {negatives.length > 0 && (
        <section className={s.panelSection}>
          <p className={s.railLabel}>
            {treatment === 'local' ? 'What the research found' : 'No state distance for'}
          </p>
          <ul className={s.noteList}>
            {negatives.map((n) => (
              <li key={n.id} className={s.noteRow}>
                <p className={s.noteLabel}>{n.label}</p>
                <p className={s.noteText}>{n.text}</p>
              </li>
            ))}
          </ul>
        </section>
      )}

      {conditional.length > 0 && (
        <section className={s.panelSection}>
          <p className={s.railLabel}>Conditional and related distances</p>
          <p className={s.panelNote}>
            These are not blanket minimums, so the tool does not draw or check
            them. They are printed because each one changes a real site plan.
          </p>
          <ul className={s.noteList}>
            {conditional.map((n) => (
              <li key={n.id} className={s.noteRow}>
                <p className={s.noteLabel}>
                  {n.label}
                  {n.feet != null ? <span className={s.noteFeet}> {n.feet} ft</span> : null}
                </p>
                {n.text && <p className={s.noteText}>{n.text}</p>}
                {n.citation && <p className={s.ruleCite}>{n.citation}</p>}
              </li>
            ))}
          </ul>
        </section>
      )}

      {rules?.ownerDrawnAccepted && (
        <section className={s.panelSection}>
          <p className={s.railLabel}>Owner-drawn plans in {rules.state}</p>
          <p className={s.noteText}>{rules.ownerDrawnAccepted}</p>
        </section>
      )}

      {rules?.setbacksNote && (
        <section className={s.panelSection}>
          <p className={s.railLabel}>Setbacks in {rules.state}</p>
          <p className={s.noteText}>{rules.setbacksNote}</p>
        </section>
      )}

      {rules?.mustShow && rules.mustShow.length > 0 && (
        <section className={s.panelSection}>
          <p className={s.railLabel}>{rules.state} wants to see</p>
          <ul className={s.mustList}>
            {rules.mustShow.map((m) => (
              <li key={m}>{m}</li>
            ))}
          </ul>
        </section>
      )}

      {findings.length > 0 && (
        <section className={s.panelSection}>
          <p className={s.railLabel}>Worth knowing</p>
          <ul className={s.noteList}>
            {findings.map((n) => (
              <li key={n.id} className={s.noteRow}>
                <p className={s.noteText}>{n.text}</p>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
