from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.knowledge_item import KnowledgeItem

def CreateKnowledgeItem(
        Database: Session,
        UserId : int,
        Title: str,
        Content: str | None,
        Type: str,
        SourceUrl: str | None,
)-> KnowledgeItem:
    NewKnowledgeItem = KnowledgeItem(
        UserId = UserId,
        Title=Title,
        Content=Content,
        Type=Type,
        SourceUrl=SourceUrl
    )

    Database.add(NewKnowledgeItem)
    Database.commit()
    Database.refresh(NewKnowledgeItem)

    return NewKnowledgeItem