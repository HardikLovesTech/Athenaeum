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

def GetKnowledgeItems(
    Database: Session,
    UserId: int,
) -> list[KnowledgeItem]:
    Statement = select(KnowledgeItem).where(
        KnowledgeItem.UserId == UserId
    )

    return list(Database.scalars(Statement).all())


def GetKnowledgeItem(
    Database: Session,
    UserId: int,
    KnowledgeItemId: int,
) -> KnowledgeItem | None:
    Statement = select(KnowledgeItem).where(
        KnowledgeItem.Id == KnowledgeItemId,
        KnowledgeItem.UserId == UserId,
    )

    return Database.scalar(Statement)