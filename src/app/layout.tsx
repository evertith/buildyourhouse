import type { Metadata } from "next";
import Script from "next/script";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import "@/styles/globals.css";
import { generateOrganizationSchema, generateWebSiteSchema, schemaToScriptTag } from "@/lib/schema";

const siteUrl = "https://buildyourhouse.com";
const siteName = "Build Your House";
const siteDescription = "Step-by-step guidance from a retired general contractor to build your dream home yourself and save a fortune. Expert advice on permits, inspections, and managing subcontractors.";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "Build Your Own House - Save $50k-150k+ | Owner-Builder Guide",
    template: "%s | Build Your House",
  },
  description: siteDescription,
  keywords: [
    "owner builder",
    "build your own house",
    "general contractor",
    "building permits",
    "home construction",
    "construction management",
    "owner-builder",
    "save money building house",
    "building inspections",
    "subcontractor management",
  ],
  authors: [{ name: "Build Your House" }],
  creator: "Build Your House",
  publisher: "Build Your House",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  openGraph: {
    type: "website",
    locale: "en_US",
    url: siteUrl,
    siteName: siteName,
    title: "Build Your Own House - Save $50k-150k+ | Owner-Builder Guide",
    description: siteDescription,
    images: [
      {
        url: `${siteUrl}/og-image.jpg`,
        width: 1200,
        height: 630,
        alt: "Build Your House - Owner-Builder Guide",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Build Your Own House - Save $50k-150k+ | Owner-Builder Guide",
    description: siteDescription,
    images: [`${siteUrl}/og-image.jpg`],
    creator: "@buildyourhouse",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  verification: {
    // Add your verification codes here when you have them
    // google: "your-google-verification-code",
    // yandex: "your-yandex-verification-code",
    // bing: "your-bing-verification-code",
  },
  alternates: {
    canonical: siteUrl,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // Generate structured data for the organization and website
  const organizationSchema = generateOrganizationSchema({
    name: siteName,
    url: siteUrl,
    logo: `${siteUrl}/logo.png`,
    description: siteDescription,
    sameAs: [
      // Add your social media profiles here
      // "https://www.facebook.com/buildyourhouse",
      // "https://twitter.com/buildyourhouse",
      // "https://www.instagram.com/buildyourhouse",
      // "https://www.youtube.com/@buildyourhouse",
    ],
  });

  const websiteSchema = generateWebSiteSchema({
    name: siteName,
    url: siteUrl,
    description: siteDescription,
    // searchUrl: `${siteUrl}/search?q={search_term_string}`, // Uncomment when search is implemented
  });

  return (
    <html lang="en">
      <head>
        {/* Structured Data - Organization and Website Schema */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@graph": [organizationSchema, websiteSchema],
            }),
          }}
        />
      </head>
      <body>
        {/* Google Analytics */}
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-75MNQ8RDT7"
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-75MNQ8RDT7');
          `}
        </Script>

        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
