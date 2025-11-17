import React from 'react';
import Link from 'next/link';
import styles from '@/styles/components/Card.module.css';

interface CardProps {
  href?: string;
  icon?: string;
  title: string;
  description: string;
  linkText?: string;
  onClick?: () => void;
}

export default function Card({
  href,
  icon,
  title,
  description,
  linkText = 'Learn More →',
  onClick
}: CardProps) {
  const content = (
    <>
      {icon && <div className={styles.icon}>{icon}</div>}
      <h3 className={styles.title}>{title}</h3>
      <p className={styles.description}>{description}</p>
      <span className={styles.link}>{linkText}</span>
    </>
  );

  if (href) {
    return (
      <Link href={href} className={styles.card}>
        {content}
      </Link>
    );
  }

  return (
    <div className={styles.card} onClick={onClick} role={onClick ? 'button' : undefined}>
      {content}
    </div>
  );
}
