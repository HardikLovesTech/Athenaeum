from fastapi import APIRouter, Depends, status , HTTPException, UploadFile , File
from sqlalchemy.orm import Session

from app.services.document_services import ExtractPdfText
from app.core.security import GetCurrentUser
from app.db.models.user import User
from app.db.session import GetDatabase
from app.schemas.knowledge_item import (
    KnowledgeItemCreate,
    KnowledgeItemResponse,
    KnowledgeItemUpdate,
)

from app.services.knowledge_services import (
    CreateKnowledgeItem,
    GetKnowledgeItems,
    GetKnowledgeItem,
    UpdateKnowledgeItem,
    DeleteKnowledgeItem
)

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


@Router.get(
    "",
    response_model=list[KnowledgeItemResponse],
)
def GetKnowledge(
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase),
):
    return GetKnowledgeItems(
        Database=Database,
        UserId=CurrentUser.Id,
    )


@Router.get(
    "{KnowledgeItemId}",
    response_model=KnowledgeItemResponse,
)
def GetKnowledgebyId(
    KnowledgeItemId:int,
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase)
):
    KnowledgeItem = GetKnowledgeItem(
        Database=Database,
        UserId=CurrentUser.Id,
        KnowledgeItemId=KnowledgeItemId,
    )

    if KnowledgeItem is None:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Knowledge item not found"
        )

    return KnowledgeItem

@Router.patch(
    "/{KnowledgeItemId}",
    response_model=KnowledgeItemResponse,
)
def UpdateKnowledge(
    KnowledgeItemId: int,
    Request: KnowledgeItemUpdate,
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase),
):
    KnowledgeItem = UpdateKnowledgeItem(
        Database=Database,
        UserId=CurrentUser.Id,
        KnowledgeItemId=KnowledgeItemId,
        Title=Request.Title,
        Content=Request.Content,
        Type=Request.Type,
        SourceUrl=Request.SourceUrl,
    )

    if KnowledgeItem is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge item not found",
        )

    return KnowledgeItem

@Router.delete(
    "/{KnowledgeItemId}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def DeleteKnowledge(
    KnowledgeItemId: int,
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase),
):
    Deleted = DeleteKnowledgeItem(
        Database=Database,
        UserId=CurrentUser.Id,
        KnowledgeItemId=KnowledgeItemId,
    )

    if not Deleted:
        raise HTTPException(
            status_code=404,
            detail="Knowledge item not found",
        )



@Router.post(
    "/upload",
    response_model=KnowledgeItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def UploadKnowledgeDocument(
    File: UploadFile = File(...),
    CurrentUser: User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase),
):
    try:
        ExtractedText = ExtractPdfText(File)
    except ValueError as Error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(Error),
        ) from Error

    if not ExtractedText:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Could not extract text from PDF",
            )

    KnowledgeItem = CreateKnowledgeItem(
        Database=Database,
        UserId=CurrentUser.Id,
        Title=File.filename or "Uploaded Document",
        Content=ExtractedText,
        Type="pdf",
        SourceUrl=None,
    )

    return KnowledgeItem









    