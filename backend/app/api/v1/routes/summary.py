from fastapi import APIRouter , Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import GetCurrentUser
from app.db.models.user import User
from app.db.session import GetDatabase
from app.services.summary_services import GenerateDocumentSummary
from app.schemas.summary import SummaryResponse

Router = APIRouter(
    prefix="/summary",
    tags=["Summary"],
)

@Router.post(
    "/{KnowledgeItemId}",
    response_model=SummaryResponse,
)
def GenerateSummary(
    KnowledgeItemId: int,
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase)
):
    try:
        Summary = GenerateDocumentSummary(
            Database=Database,
            KnowledgeItemId=KnowledgeItemId,
            UserId=CurrentUser.Id
        )
    except ValueError as E:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(E)
        )from E

    return SummaryResponse(
        Summary=Summary,
    )