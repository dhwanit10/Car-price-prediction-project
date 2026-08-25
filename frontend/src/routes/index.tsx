import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/layout/Navbar";
import { Footer } from "@/components/layout/Footer";
import { Hero } from "@/components/sections/Hero";
import { Features } from "@/components/sections/Features";
import { Predictor } from "@/components/sections/Predictor";
import { DataScience } from "@/components/sections/DataScience";
import { FloatingWidgets } from "@/components/sections/Chatbot";

const TITLE = "CarCast — Know Your Car's True Worth in Seconds";
const DESCRIPTION =
  "AI-powered used car valuation trained on 15,000+ real listings. Get an instant fair price, market comparison and deal analysis.";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: TITLE },
      { name: "description", content: DESCRIPTION },
      { property: "og:title", content: TITLE },
      { property: "og:description", content: DESCRIPTION },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Index,
});

function Index() {
  return (
    <div className="min-h-screen">
      <Navbar />
      <main>
        <Hero />
        <Features />
        <Predictor />
        <DataScience />
      </main>
      <Footer />
      <FloatingWidgets />
    </div>
  );
}
