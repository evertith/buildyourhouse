import type { MDXComponents } from 'mdx/types';
import CalloutBox from '@/components/CalloutBox';
import Checklist from '@/components/Checklist';
import StepGuide from '@/components/StepGuide';
import styles from '@/styles/article.module.css';

export function useMDXComponents(components: MDXComponents): MDXComponents {
  return {
    ...components,
    // Wrap all MDX content in article styles
    wrapper: ({ children }) => (
      <div className={styles.article}>{children}</div>
    ),
    // Make custom components available in MDX
    CalloutBox,
    Checklist,
    StepGuide,
  };
}
