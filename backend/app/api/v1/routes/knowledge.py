from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.security import GetCurrentUser
from app.db.models.user import User
from app.db.session import GetDatabase
from app.schemas.knowledge_item import (
    KnowledgeItemCreate,
    KnowledgeItemResponse
)

from app.services.knowledge_services import CreateKnowledgeItem

Router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"],
)


@Router.post(
    "",
    response_model=KnowledgeItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def CreateKnowledge(
    Request: KnowledgeItemCreate,
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase),
):
    return CreateKnowledgeItem(
        Database=Database,
        UserId=CurrentUser.Id,
        Title=Request.Title,
        Content=Request.Content,
        Type=Request.Type,
        SourceUrl=Request.SourceUrl,
    )