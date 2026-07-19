import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Recover Your Download | Build Your House",
  robots: {
    index: false,
    follow: false,
  },
};

export default function RecoverLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
