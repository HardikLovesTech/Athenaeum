from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import GetCurrentUser
from app.db.session import GetDatabase
from app.db.models.user import User
from app.schemas.search import SearchRequest, SearchResult
from app.services.search_services import SearchDocumentChunks

Router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@Router.post("", response_model=list[SearchResult])
def Search(
        Request: SearchRequest,
        Database: Session = Depends(GetDatabase),
        CurrentUser: User = Depends(GetCurrentUser),
):
    Results = SearchDocumentChunks(
        Database=Database,
        Query=Request.Query,
        KnowledgeItemId=Request.KnowledgeItemId,
        Limit=Request.Limit,
    )

    return [
        SearchResult(
            Id=DocumentChunk.Id,
            KnowledgeItemId=DocumentChunk.KnowledgeItemId,
            ChunkIndex=DocumentChunk.ChunkIndex,
            Content=DocumentChunk.Content,
            Distance=Distance,
        )
        for DocumentChunk, Distance in Results
    ]