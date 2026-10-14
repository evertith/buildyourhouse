/** Number formatting for the ledger: rounded mids, never fake precision. */

/** "$316,000": to the nearest hundred, which is how the ledger prints money. */
export function money100(n: number): string {
  return `$${(Math.round(n / 100) * 100).toLocaleString('en-US')}`;
}

/** "$158": whole dollars, for per-square-foot figures. */
export function money(n: number): string {
  return `$${Math.round(n).toLocaleString('en-US')}`;
}

/** "440": hours to the nearest ten (five under a hundred). */
export function hoursApprox(h: number): string {
  const step = h >= 100 ? 10 : 5;
  return (Math.round(h / step) * step).toLocaleString('en-US');
}

/** "12.34": a 0–1 share as a percentage string for widths. */
export function pct(share: number): string {
  return (Math.max(0, share) * 100).toFixed(2);
}

export function plural(n: number, one: string, many: string): string {
  return n === 1 ? one : many;
}
