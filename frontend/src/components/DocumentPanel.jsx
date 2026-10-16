
import {
  useCallback,
  useEffect,
  useRef,
  useState,
} from "react";

import {
  ArrowUpRight,
  Plus,
} from "lucide-react";

import DocumentCard from "./DocumentCard";

import {
  GetKnowledgeItems,
  UploadDocument,
} from "../services/api";

function DocumentsPanel() {
  const [Documents, SetDocuments] = useState([]);
  const [IsLoading, SetIsLoading] = useState(true);
  const [IsUploading, SetIsUploading] = useState(false);
  const [ErrorMessage, SetErrorMessage] = useState("");
  const [UploadMessage, SetUploadMessage] = useState("");
  const [ActiveFilter, SetActiveFilter] = useState("All");

  const FileInputRef = useRef(null);

  const LoadDocuments = useCallback(async () => {
    try {
      SetIsLoading(true);
      SetErrorMessage("");

      const Data = await GetKnowledgeItems();

      const Items = Array.isArray(Data)
        ? Data
        : Data?.Items ?? Data?.items ?? [];

      SetDocuments(Items);
    } catch (Error) {
      SetErrorMessage(
        Error.message || "Unable to load documents."
      );
    } finally {
      SetIsLoading(false);
    }
  }, []);

  useEffect(() => {
    LoadDocuments();
  }, [LoadDocuments]);


  async function HandleFileChange(Event) {
    const Input = Event.target;
    const SelectedFile = Input.files?.[0];

    if (!SelectedFile) return;

    SetUploadMessage("");
    SetErrorMessage("");

    const IsPdf =
      SelectedFile.type === "application/pdf" ||
      SelectedFile.name.toLowerCase().endsWith(".pdf");

    if (!IsPdf) {
      SetUploadMessage("Please select a PDF file.");
      Input.value = "";
      return;
    }

    try {
      SetIsUploading(true);

      const UploadedDocument = await UploadDocument(SelectedFile);

      console.log("Upload response:", UploadedDocument);

      SetUploadMessage(
        `Uploaded "${SelectedFile.name}". Refreshing documents...`
      );

      await LoadDocuments();
    } catch (Error) {
      console.error("PDF upload failed:", Error);

      SetUploadMessage(
        Error.message || "Unable to upload the PDF."
      );
    } finally {
      SetIsUploading(false);
      Input.value = "";
    }
  }


  function GetField(Item, PascalName, CamelName) {
    return Item?.[PascalName] ?? Item?.[CamelName];
  }

  function FormatDate(DateValue) {
    if (!DateValue) return "Date unavailable";

    const DateObject = new Date(DateValue);

    if (Number.isNaN(DateObject.getTime())) {
      return "Date unavailable";
    }

    return `Uploaded ${DateObject.toLocaleDateString()}`;
  }

  const FilteredDocuments = Documents.filter((Item) => {
    if (ActiveFilter === "All") return true;

    const Type = String(
      GetField(Item, "Type", "type") ?? ""
    ).toLowerCase();

    if (ActiveFilter === "PDF") {
      return Type === "pdf";
    }

    if (ActiveFilter === "Notes") {
      return Type === "note" || Type === "notes";
    }

    if (ActiveFilter === "Research") {
      return Type === "research";
    }

    return !["pdf", "note", "notes", "research"].includes(Type);
  });

  return (
    <section className="DocumentsPanel">
      <div className="PanelHeader">
        <h2>Your Documents</h2>

        <input
          ref={FileInputRef}
          type="file"
          accept=".pdf,application/pdf"
          hidden
          onChange={HandleFileChange}
        />

        <button
          className="SmallButton"
          disabled={IsUploading}
          onClick={() => FileInputRef.current?.click()}
        >
          <Plus size={15} />
          {IsUploading ? "Uploading..." : "Upload"}
        </button>
      </div>

      {UploadMessage && (
        <p role="status">{UploadMessage}</p>
      )}

      <div className="DocumentFilters">
        {["All", "PDF", "Notes", "Research", "Other"].map(
          (Filter) => (
            <button
              key={Filter}
              className={`Filter ${
                ActiveFilter === Filter ? "Active" : ""
              }`}
              onClick={() => SetActiveFilter(Filter)}
            >
              {Filter}
            </button>
          )
        )}
      </div>

      {IsLoading && (
        <p>Loading your documents...</p>
      )}

      {!IsLoading && ErrorMessage && (
        <div role="alert">
          <p>{ErrorMessage}</p>
          <button onClick={LoadDocuments}>
            Retry
          </button>
        </div>
      )}

      {!IsLoading &&
        !ErrorMessage &&
        FilteredDocuments.length === 0 && (
          <p>
            {Documents.length === 0
              ? "No documents yet. Upload your first document to get started."
              : "No documents match this filter."}
          </p>
        )}

      {!IsLoading &&
        !ErrorMessage &&
        FilteredDocuments.map((Item) => {
          const Id = GetField(Item, "Id", "id");

          const Title =
            GetField(Item, "Title", "title") ??
            "Untitled document";

          const Type = String(
            GetField(Item, "Type", "type") ?? "note"
          );

          const CreatedAt =
            GetField(Item, "CreatedAt", "createdAt") ??
            GetField(Item, "UpdatedAt", "updatedAt");

          const CategoryClass =
            Type.toLowerCase() === "pdf"
              ? "YellowTag"
              : Type.toLowerCase() === "research"
                ? "PurpleTag"
                : Type.toLowerCase() === "note"
                  ? "PeachTag"
                  : "CreamTag";

          return (
            <DocumentCard
              key={Id ?? Title}
              Title={Title}
              Size={Type.toUpperCase()}
              Time={FormatDate(CreatedAt)}
              Category={Type}
              CategoryClass={CategoryClass}
            />
          );
        })}

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

        <div className="Globe">◎</div>

        <button className="RoundArrow">
          <ArrowUpRight size={18} />
        </button>
      </div>
    </section>
  );
}

export default DocumentsPanel;
