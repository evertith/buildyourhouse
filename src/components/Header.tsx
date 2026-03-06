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
      <div className={styles.container}>
        <div className={styles.logo}>
          <Link href="/" onClick={closeMobileMenu}>
            Build Your House
          </Link>
        </div>

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
          <Link href="/resources" className={styles.navLink} onClick={closeMobileMenu}>
            Resources
          </Link>
          <Link href="/blog" className={styles.navLink} onClick={closeMobileMenu}>
            Blog
          </Link>
          <Link href="/about" className={styles.navLink} onClick={closeMobileMenu}>
            About
          </Link>
          <Link href="/shop" className={styles.navLink} onClick={closeMobileMenu}>
            Shop
          </Link>
          <Link href="/advisor" className={`${styles.navLink} ${styles.ctaLink}`} onClick={closeMobileMenu}>
            AI Advisor
          </Link>
        </nav>
      </div>
    </header>
  );
}
