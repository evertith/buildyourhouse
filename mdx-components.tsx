import type { MDXComponents } from 'mdx/types';
import CalloutBox from '@/components/CalloutBox';
import Checklist from '@/components/Checklist';
import StepGuide from '@/components/StepGuide';
import DataTable from '@/components/DataTable';
import Section from '@/components/Section';
import FAQSection from '@/components/FAQSection';
import ProductPick from '@/components/ProductPick';
import AmazonLink from '@/components/AmazonLink';
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
    DataTable,
    Section,
    FAQSection,
    ProductPick,
    AmazonLink,
  };
}
