import React from 'react';

export type IconName =
  | 'permit'
  | 'subs'
  | 'schedule'
  | 'phases'
  | 'tools'
  | 'calculator'
  | 'check'
  | 'arrow'
  | 'compass'
  | 'ruler'
  | 'doc'
  | 'lock'
  | 'bolt';

const PATHS: Record<IconName, React.ReactNode> = {
  // Permitting & inspections — shield + check
  permit: (
    <>
      <path d="M12 2 3 6v6c0 5 3.8 8.4 9 10 5.2-1.6 9-5 9-10V6l-9-4Z" />
      <path d="m9 12 2 2 4-4" />
    </>
  ),
  // Subcontractors — hard hat
  subs: (
    <>
      <path d="M12 3a6 6 0 0 0-6 6v2h12V9a6 6 0 0 0-6-6Z" />
      <path d="M4 11h16" />
      <path d="M3 11v3a9 9 0 0 0 18 0v-3" />
      <path d="M12 3v3" />
    </>
  ),
  // Timing & scheduling — calendar + check
  schedule: (
    <>
      <rect x="3" y="4" width="18" height="17" rx="1.5" />
      <path d="M3 9h18M8 2v4M16 2v4" />
      <path d="m8 14 2.5 2.5L16 11" />
    </>
  ),
  // Build phases — crane / structure
  phases: (
    <>
      <path d="M4 21V4l13 3.5" />
      <path d="M4 8h13" />
      <path d="M17 7.5 21 9" />
      <path d="M9 21v-5h4v5" />
      <path d="M4 21h16" />
    </>
  ),
  // Tools & equipment — wrench
  tools: (
    <>
      <path d="m14 6 4 4L8 20l-5 1 1-5L14 6Z" />
      <path d="m12 8 4 4" />
      <path d="M17 3.5 20.5 7 18 9.5 14.5 6 17 3.5Z" />
    </>
  ),
  // Calculators
  calculator: (
    <>
      <rect x="4" y="2" width="16" height="20" rx="1.5" />
      <path d="M8 6h8" />
      <path d="M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15v3" />
    </>
  ),
  check: <path d="m5 12 4.5 4.5L19 7" />,
  arrow: (
    <>
      <path d="M5 12h14" />
      <path d="m13 6 6 6-6 6" />
    </>
  ),
  compass: (
    <>
      <circle cx="12" cy="12" r="9" />
      <path d="m15.5 8.5-2 5-5 2 2-5 5-2Z" />
    </>
  ),
  ruler: (
    <>
      <path d="M3 17 17 3l4 4L7 21l-4-4Z" />
      <path d="M7 11l2 2M11 7l2 2M15 11l2 2" />
    </>
  ),
  doc: (
    <>
      <path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9l-6-6Z" />
      <path d="M14 3v6h6M8 13h8M8 17h6" />
    </>
  ),
  // Secure checkout — padlock
  lock: (
    <>
      <rect x="4" y="10" width="16" height="11" rx="1.5" />
      <path d="M8 10V7a4 4 0 0 1 8 0v3" />
      <path d="M12 14v3" />
    </>
  ),
  // Instant access — lightning bolt
  bolt: <path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z" />,
};

interface IconProps {
  name: IconName;
  size?: number | string;
  className?: string;
  strokeWidth?: number;
}

export default function Icon({ name, size = 24, className, strokeWidth = 1.5 }: IconProps) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={strokeWidth}
      strokeLinecap="round"
      strokeLinejoin="round"
      className={className}
      aria-hidden="true"
      focusable="false"
    >
      {PATHS[name]}
    </svg>
  );
}
