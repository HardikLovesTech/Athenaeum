from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import GetCurrentUser
from app.db.models.user import User
from app.db.session import GetDatabase
from app.schemas.rag import RAGRequest , RAGResponse
from app.services.rag_services import BuildRAGContext
from app.services.llm_services import GenerateAnswer


Router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@Router.post(
    "",
    response_model=RAGResponse,
)
def GenerateRAGAnswer(
    Request: RAGRequest,
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase)
): 
    Context , Sources = BuildRAGContext(
        Database=Database,
        Query=Request.Query,
        UserId=CurrentUser.Id,
        KnowledgeItemId=Request.KnowledgeItemId,
    )

    Answer = GenerateAnswer(
        Query=Request.Query,
        Context=Context,
    )

    return RAGResponse(
        Answer=Answer,
        Sources=Sources,
    )

