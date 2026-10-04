import {
  BookOpen,
  ChevronDown,
  Database,
  FileText,
  MessageSquare,
  Send,
  Sparkles,
} from "lucide-react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import StatCard from "./components/StatCard";
import DocumentsPanel from "./components/DocumentPanel";
import AskPanel from "./components/AskPanel";


import "./App.css";

function App() {
  return (
    <div className="App">
      <Navbar />

      <main>
        <Hero />

        <section className="Workspace">
          {/* Stats */}
          <aside className="StatsColumn">
            <StatCard
              Icon={FileText}
              Value="3"
              Label="Documents"
              ClassName="Yellow"
            />

            <StatCard
              Icon={MessageSquare}
              Value="12"
              Label="Questions Asked"
              ClassName="Peach"
            />

            <StatCard
              Icon={Sparkles}
              Value="5"
              Label="Summaries Generated"
              ClassName="Neutral"
            />

            <StatCard
              Icon={Database}
              Value="2.4 MB"
              Label="Total Storage"
              ClassName="Neutral"
            />

            <div className="QuoteCard">
              <p>
                "A second brain
                <br />
                for a smarter you."
              </p>

              <span>— Athenaeum</span>

              <div className="QuoteLine" />

              <div className="QuoteCircles">
                <span />
                <span />
              </div>
            </div>
          </aside>

          {/* Documents */}
          <DocumentsPanel />

          {/* Ask AI */}
          <AskPanel />
        </section>
      </main>
    </div>
  );
}


export default App;