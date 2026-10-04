import {
  FileText,
  MoreVertical,
} from "lucide-react";

function DocumentCard({
  Title,
  Size,
  Time,
  Category,
  CategoryClass,
}) {
  return (
    <div className="DocumentCard">
      <div className="DocumentIcon">
        <FileText size={21} />
      </div>

      <div className="DocumentInfo">
        <div className="DocumentTitle">
          {Title}
        </div>

        <div className="DocumentMeta">
          <span>{Size}</span>
          <span>•</span>
          <span>{Time}</span>
        </div>
      </div>

      <div className={`DocumentTag ${CategoryClass}`}>
        {Category}
      </div>

      <button className="DocumentMenu">
        <MoreVertical size={17} />
      </button>
    </div>
  );
}

export default DocumentCard;