'use client';

import React from 'react';
import styles from '@/styles/components/DataTable.module.css';

interface DataTableProps {
  headers: string[];
  rows: (string | number)[][];
  caption?: string;
}

export default function DataTable({ headers, rows, caption }: DataTableProps) {
  return (
    <div className={styles.tableWrapper}>
      <table className={styles.table}>
        {caption && <caption className={styles.caption}>{caption}</caption>}
        <thead>
          <tr>
            {headers.map((header, index) => (
              <th key={index} className={styles.header}>
                {header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, rowIndex) => (
            <tr key={rowIndex} className={rowIndex % 2 === 0 ? styles.evenRow : styles.oddRow}>
              {row.map((cell, cellIndex) => (
                <td key={cellIndex} className={styles.cell}>
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
