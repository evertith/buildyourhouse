import React from 'react';
import styles from '@/styles/components/StepGuide.module.css';

interface Step {
  title: string;
  description: string | React.ReactNode;
}

interface StepGuideProps {
  steps: Step[];
  title?: string;
}

export default function StepGuide({ steps, title }: StepGuideProps) {
  return (
    <div className={styles.stepGuide}>
      {title && <h3 className={styles.title}>{title}</h3>}
      <div className={styles.steps}>
        {steps.map((step, index) => (
          <div key={index} className={styles.step}>
            <div className={styles.stepNumber}>{index + 1}</div>
            <div className={styles.stepContent}>
              <h4 className={styles.stepTitle}>{step.title}</h4>
              <div className={styles.stepDescription}>
                {typeof step.description === 'string' ? (
                  <p>{step.description}</p>
                ) : (
                  step.description
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
