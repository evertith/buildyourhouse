import type { MDXComponents } from 'mdx/types';
import CalloutBox from '@/components/CalloutBox';
import Checklist from '@/components/Checklist';
import StepGuide from '@/components/StepGuide';
import DataTable from '@/components/DataTable';
import Section from '@/components/Section';
import FAQSection from '@/components/FAQSection';
import ProductPick from '@/components/ProductPick';
import AmazonLink from '@/components/AmazonLink';
import ArticleSchema from '@/components/ArticleSchema';
import BinderCTA from '@/components/BinderCTA';
import ProductCTA from '@/components/ProductCTA';
import CodeAlertCapture from '@/components/CodeAlertCapture';
import PlanningTools from '@/components/PlanningTools';
import LenderDirectory, { FeaturedLenderSlot } from '@/components/financing/LenderDirectory';
import LenderMatchForm from '@/components/financing/LenderMatchForm';
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
    ArticleSchema,
    BinderCTA,
    ProductCTA,
    CodeAlertCapture,
    PlanningTools,
    LenderDirectory,
    FeaturedLenderSlot,
    LenderMatchForm,
  };
}
