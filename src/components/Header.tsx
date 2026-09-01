'use client';

import { useState } from 'react';
import Link from 'next/link';
import styles from '@/styles/Header.module.css';

/**
 * Categorized nav. Every category label is a real link to its hub page —
 * on touch devices (no hover) tapping a category navigates to the hub,
 * which lists everything the dropdown shows. Dropdowns open on hover and
 * :focus-within, so keyboard users tab through the category into its menu.
 */
type NavChild = { href: string; label: string };
type NavEntry = { href: string; label: string; items?: NavChild[] };

const NAV: NavEntry[] = [
  { href: '/start-here', label: 'Start Here' },
  {
    href: '/planning',
    label: 'Planning',
    items: [
      { href: '/feasibility', label: 'Feasibility' },
      { href: '/planning/budget', label: 'Budget' },
      { href: '/planning/house-plans', label: 'House Plans' },
      { href: '/planning/secure-land', label: 'Securing Land' },
      { href: '/planning/timeline', label: 'Timeline' },
    ],
  },
  {
    href: '/permitting',
    label: 'Permits',
    items: [
      { href: '/permitting', label: 'Permitting Guides' },
      { href: '/permitting/state-guides', label: 'All 50 State Guides' },
      { href: '/site-plan-studio', label: 'Site Plan Studio' },
      { href: '/inspections', label: 'Inspections' },
    ],
  },
  {
    href: '/build-phases',
    label: 'Build',
    items: [
      { href: '/build-phases', label: 'Build Phases' },
      { href: '/timing-and-scheduling', label: 'Scheduling & Lead Times' },
      { href: '/subcontractors', label: 'Subcontractors' },
      { href: '/move-in', label: 'Move-In' },
    ],
  },
  {
    href: '/calculators',
    label: 'Tools',
    items: [
      { href: '/calculators', label: 'Calculators' },
      { href: '/tools-and-equipment', label: 'Tools & Equipment' },
      { href: '/resources', label: 'Resources & Templates' },
    ],
  },
  { href: '/financing', label: 'Financing' },
  { href: '/blog', label: 'Blog' },
  { href: '/about', label: 'About' },
];

export default function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  const closeMobileMenu = () => {
    setMobileMenuOpen(false);
  };

  return (
    <header className={styles.header}>
      <div className={styles.draftMargin} />
      <div className={styles.container}>
        <Link href="/" className={styles.logo} onClick={closeMobileMenu}>
          <span className={styles.logoMark}>Build Your <em>House</em></span>
          <span className={styles.logoTag}>Owner-Builder<br />Field Guide</span>
        </Link>

        {/* Mobile Menu Button */}
        <button
          className={styles.mobileMenuButton}
          onClick={toggleMobileMenu}
          aria-label="Toggle mobile menu"
          aria-expanded={mobileMenuOpen}
        >
          <span className={`${styles.hamburger} ${mobileMenuOpen ? styles.hamburgerOpen : ''}`}>
            <span></span>
            <span></span>
            <span></span>
          </span>
        </button>

        {/* Navigation */}
        <nav className={`${styles.nav} ${mobileMenuOpen ? styles.navOpen : ''}`}>
          {NAV.map((entry) =>
            entry.items ? (
              <div key={entry.href} className={styles.navItem}>
                <Link href={entry.href} className={styles.navLink} onClick={closeMobileMenu}>
                  {entry.label}
                  <span className={styles.chev} aria-hidden="true">▾</span>
                </Link>
                <div className={styles.menu}>
                  {entry.items.map((item) => (
                    <Link
                      key={item.href + item.label}
                      href={item.href}
                      className={styles.menuLink}
                      onClick={closeMobileMenu}
                    >
                      {item.label}
                    </Link>
                  ))}
                </div>
              </div>
            ) : (
              <Link key={entry.href} href={entry.href} className={styles.navLink} onClick={closeMobileMenu}>
                {entry.label}
              </Link>
            )
          )}
          <Link href="/shop" className={`${styles.navLink} ${styles.ctaLink}`} onClick={closeMobileMenu}>
            Shop
          </Link>
        </nav>
      </div>
    </header>
  );
}
