import { ReactNode } from 'react';
import { ArticleMetadata } from '@/lib/types';
import { formatDate } from '@/lib/utils';
import styles from '@/styles/ArticleLayout.module.css';

interface ArticleLayoutProps {
  metadata: ArticleMetadata;
  children: ReactNode;
}

export default function ArticleLayout({ metadata, children }: ArticleLayoutProps) {
  return (
    <article className={styles.article}>
      <header className={styles.header}>
        <div className={styles.breadcrumbs}>
          <a href="/">Home</a>
          <span className={styles.separator}>/</span>
          <a href={`/${metadata.category.toLowerCase()}`}>{metadata.category}</a>
        </div>

        <h1 className={styles.title}>{metadata.title}</h1>

        <div className={styles.meta}>
          <span className={styles.author}>By {metadata.author}</span>
          <span className={styles.separator}>•</span>
          <time className={styles.date}>{formatDate(metadata.date)}</time>
          {metadata.readTime && (
            <>
              <span className={styles.separator}>•</span>
              <span className={styles.readTime}>{metadata.readTime}</span>
            </>
          )}
          {metadata.difficulty && (
            <>
              <span className={styles.separator}>•</span>
              <span className={styles.difficulty}>
                Difficulty: <strong>{metadata.difficulty}</strong>
              </span>
            </>
          )}
        </div>

        {metadata.updated && metadata.updated !== metadata.date && (
          <div className={styles.updated}>
            Last updated: {formatDate(metadata.updated)}
          </div>
        )}

        {metadata.tags && metadata.tags.length > 0 && (
          <div className={styles.tags}>
            {metadata.tags.map(tag => (
              <span key={tag} className={styles.tag}>{tag}</span>
            ))}
          </div>
        )}
      </header>

      <div className={styles.content}>
        {children}
      </div>

      <footer className={styles.footer}>
        <div className={styles.disclaimer}>
          <strong>Important:</strong> Building codes and regulations vary by location.
          Always consult with licensed professionals and verify requirements with your
          local building department.
        </div>
      </footer>
    </article>
  );
}
