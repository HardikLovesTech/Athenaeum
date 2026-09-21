from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import GetCurrentUser
from app.db.models.user import User
from app.db.session import GetDatabase
from app.schemas.rag import RAGRequest , RAGResponse
from app.services.rag_services import BuildRAGContext

Router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@Router.post(
    "",
    response_model=RAGResponse,
)
def GenerateAnswer(
    Request: RAGRequest,
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase)
): 
    Context = BuildRAGContext(
        Database=Database,
        Query=Request.Query,
        UserId=CurrentUser.Id,
        KnowledgeItemId=Request.KnowledgeItemId,
    )

    return RAGResponse(
        Answer=Context,
    )

