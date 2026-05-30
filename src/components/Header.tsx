'use client';

import { useState } from 'react';
import Link from 'next/link';
import styles from '@/styles/Header.module.css';

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

        {/* Desktop Navigation */}
        <nav className={`${styles.nav} ${mobileMenuOpen ? styles.navOpen : ''}`}>
          <Link href="/" className={styles.navLink} onClick={closeMobileMenu}>
            Home
          </Link>
          <Link href="/start-here" className={styles.navLink} onClick={closeMobileMenu}>
            Start Here
          </Link>
          <Link href="/permitting" className={styles.navLink} onClick={closeMobileMenu}>
            Guides
          </Link>
          <Link href="/permitting/state-guides" className={styles.navLink} onClick={closeMobileMenu}>
            State Guides
          </Link>
          <Link href="/resources" className={styles.navLink} onClick={closeMobileMenu}>
            Resources
          </Link>
          <Link href="/blog" className={styles.navLink} onClick={closeMobileMenu}>
            Blog
          </Link>
          <Link href="/about" className={styles.navLink} onClick={closeMobileMenu}>
            About
          </Link>
          <Link href="/shop" className={`${styles.navLink} ${styles.ctaLink}`} onClick={closeMobileMenu}>
            Shop
          </Link>
        </nav>
      </div>
    </header>
  );
}
