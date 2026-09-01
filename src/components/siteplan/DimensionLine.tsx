/**
 * A dimension line in the Blueprint idiom, translated to SVG (§2.3):
 * hairline stroke, 45-degree end ticks — the drafting convention, not
 * arrowheads — and a mono label sitting on a paper-colored plate so it
 * stays readable over hatching.
 *
 * Tone carries the whole verified/hedged distinction: a violation is solid
 * and brick red and says "req.", a hedged shortfall is DASHED and amber and
 * says "typical". Hedging the banner alone gets ignored the moment someone
 * starts dragging; hedging the mark itself does not.
 */

import type { Pt } from '@/lib/siteplan/geometry';

export type DimTone = 'normal' | 'violation' | 'watch' | 'setback' | 'active';

const STROKE: Record<DimTone, string> = {
  normal: 'var(--hairline-strong)',
  violation: 'var(--accent-critical)',
  watch: 'var(--accent-warning)',
  setback: 'var(--accent-info)',
  active: 'var(--accent-primary)',
};

const TEXT: Record<DimTone, string> = {
  normal: 'var(--text-secondary)',
  violation: 'var(--accent-critical)',
  watch: 'var(--accent-warning)',
  setback: 'var(--accent-info)',
  active: 'var(--accent-primary)',
};

interface Props {
  a: Pt;
  b: Pt;
  label: string;
  tone?: DimTone;
  /** Dashed line — every hedged (typical-value) measurement. */
  dashed?: boolean;
  /** World units per CSS pixel, so ticks and text keep a constant size. */
  u: number;
  /** World units per text pixel. Smaller than `u` on a small canvas, where
      constant-size labels would otherwise swamp the drawing. */
  tu?: number;
  /** Shifts the label along the line to keep stacked dimensions apart. */
  shift?: number;
  /** Screen-only: hovering the matching inspector row highlights the line. */
  onEnter?: () => void;
  onLeave?: () => void;
}

export default function DimensionLine({
  a,
  b,
  label,
  tone = 'normal',
  dashed,
  u,
  tu,
  shift = 0,
  onEnter,
  onLeave,
}: Props) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const len = Math.hypot(dx, dy);
  if (!Number.isFinite(len)) return null;

  const ux = len < 1e-9 ? 1 : dx / len;
  const uy = len < 1e-9 ? 0 : dy / len;
  // The 45-degree tick: the line direction rotated a quarter turn, then bent
  // back 45 degrees. Drawn as one short stroke centered on the end point.
  const tick = 5 * u;
  const tx = (ux + -uy) * tick;
  const ty = (uy + ux) * tick;

  const t = tu ?? u;
  // Labels sit at the midpoint by default; `shift` walks them along the line
  // so two dimensions crossing the same area do not print on top of one
  // another. Clamped so a label never leaves its own dimension line.
  const at = Math.max(0.22, Math.min(0.78, 0.5 + shift));
  const mx = a.x + dx * at;
  const my = a.y + dy * at;
  const fs = 10.5 * t;
  const padX = 3.5 * t;
  const plateW = label.length * fs * 0.56 + padX * 2;
  const plateH = fs * 1.55;
  const weight = tone === 'normal' ? 1 : 1.6;

  return (
    <g
      className="sp-dim"
      onPointerEnter={onEnter}
      onPointerLeave={onLeave}
      style={onEnter ? { cursor: 'default' } : undefined}
    >
      <line
        x1={a.x}
        y1={a.y}
        x2={b.x}
        y2={b.y}
        stroke={STROKE[tone]}
        strokeWidth={weight}
        strokeDasharray={dashed ? '5 3' : undefined}
        vectorEffect="non-scaling-stroke"
      />
      <line
        x1={a.x - tx}
        y1={a.y - ty}
        x2={a.x + tx}
        y2={a.y + ty}
        stroke={STROKE[tone]}
        strokeWidth={weight}
        vectorEffect="non-scaling-stroke"
      />
      <line
        x1={b.x - tx}
        y1={b.y - ty}
        x2={b.x + tx}
        y2={b.y + ty}
        stroke={STROKE[tone]}
        strokeWidth={weight}
        vectorEffect="non-scaling-stroke"
      />
      <rect
        x={mx - plateW / 2}
        y={my - plateH / 2}
        width={plateW}
        height={plateH}
        fill="var(--bg-primary)"
        stroke={tone === 'normal' ? 'none' : STROKE[tone]}
        strokeWidth={0.75}
        vectorEffect="non-scaling-stroke"
      />
      <text
        x={mx}
        y={my}
        textAnchor="middle"
        dominantBaseline="central"
        fontFamily="var(--font-mono)"
        fontSize={fs}
        fontStyle={dashed ? 'italic' : undefined}
        fill={TEXT[tone]}
      >
        {label}
      </text>
    </g>
  );
}
