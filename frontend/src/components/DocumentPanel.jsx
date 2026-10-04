import {
  ArrowUpRight,
  Plus,
} from "lucide-react";

import DocumentCard from "./DocumentCard";

function DocumentsPanel() {
  return (
    <section className="DocumentsPanel">
      <div className="PanelHeader">
        <h2>Your Documents</h2>

        <button className="SmallButton">
          <Plus size={15} />
          Upload
        </button>
      </div>

      <div className="DocumentFilters">
        <button className="Filter Active">All</button>
        <button className="Filter">PDF</button>
        <button className="Filter">Notes</button>
        <button className="Filter">Research</button>
        <button className="Filter">Other</button>
      </div>

      <DocumentCard
        Title="AWS Cloud Practitioner.pdf"
        Size="2.1 MB"
        Time="Uploaded 2 days ago"
        Category="Cloud"
        CategoryClass="YellowTag"
      />

      <DocumentCard
        Title="Python Notes.pdf"
        Size="1.3 MB"
        Time="Uploaded 1 week ago"
        Category="Programming"
        CategoryClass="PeachTag"
      />

      <DocumentCard
        Title="System Design Guide.pdf"
        Size="890 KB"
        Time="Uploaded 2 weeks ago"
        Category="System Design"
        CategoryClass="CreamTag"
      />

      <DocumentCard
        Title="Research Paper – LLMs.pdf"
        Size="1.8 MB"
        Time="Uploaded 3 weeks ago"
        Category="AI/ML"
        CategoryClass="PurpleTag"
      />

      <div className="KnowledgeCard">
        <div>
          <div className="KnowledgeEyebrow">
            <span />
            EXPLORE · LEARN · BUILD
          </div>

          <h3>
            Knowledge
            <br />
            without limits.
          </h3>

          <p>
            Upload your documents and unlock deeper
            <br />
            insights with AI.
          </p>
        </div>

        <div className="Globe">
          ◎
        </div>

        <button className="RoundArrow">
          <ArrowUpRight size={18} />
        </button>
      </div>
    </section>
  );
}

export default DocumentsPanel;