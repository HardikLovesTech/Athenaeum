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



def UpdateKnowledgeItem(
    Database: Session,
    UserId: int,
    KnowledgeItemId: int,
    Title: str | None,
    Content: str | None,
    Type: str | None,
    SourceUrl: str | None,
) -> KnowledgeItem | None:
    KnowledgeItem = GetKnowledgeItem(
        Database=Database,
        UserId=UserId,
        KnowledgeItemId=KnowledgeItemId,
    )

    if KnowledgeItem is None:
        return None

    if Title is not None:
        KnowledgeItem.Title = Title

    if Content is not None:
        KnowledgeItem.Content = Content

    if Type is not None:
        KnowledgeItem.Type = Type

    if SourceUrl is not None:
        KnowledgeItem.SourceUrl = SourceUrl

    Database.commit()
    Database.refresh(KnowledgeItem)

    return KnowledgeItem

def DeleteKnowledgeItem(
    Database: Session,
    UserId: int,
    KnowledgeItemId: int,
) -> bool:
    KnowledgeItem = GetKnowledgeItem(
        Database=Database,
        UserId=UserId,
        KnowledgeItemId=KnowledgeItemId,
    )

    if KnowledgeItem is None:
        return False

    Database.delete(KnowledgeItem)
    Database.commit()

    return True