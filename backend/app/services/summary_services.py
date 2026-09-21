from sqlalchemy.orm import Session

from app.db.models.knowledge_item import KnowledgeItem
from app.services.llm_services import GenerateAnswer

def GenerateDocumentSummary(
        Database: Session,
        KnowledgeItemId: int,
        UserId: int
) -> str:
    KnowledgeItemRecord = (
        Database.query(KnowledgeItem)
        .filter(
            KnowledgeItem.Id == KnowledgeItemId,
            KnowledgeItem.UserId == UserId
        )
    .first()
    )

    if KnowledgeItemRecord is None:
        raise ValueError("Knowledge item not found")


    if not KnowledgeItemRecord.Content:
        raise ValueError("Knowledge item has no content")


    Prompt = """
Summarize the provided document clearly and concisely.

Focus on:
- The main topic
- The key concepts
- The most important points
- Important conclusions or takeaways

Do not add information that is not present in the document.
""".strip()

    Context = f"""
{Prompt}
Document:
{KnowledgeItemRecord.Content}
""".strip()

    return GenerateAnswer(
        Query="Summarize this document",
        Context=Context,
    )