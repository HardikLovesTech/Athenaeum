from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import GetDatabase
from app.db.models.user import User
from app.db.session import GetDatabase
from app.schemas.user import UserResponse
from app.core.security import GetCurrentUser

Router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@Router.get("/health")
def UserHealth(
    Database: Session = Depends(GetDatabase),
):
    return {
        "status" : "User service is running"
    }

@Router.get(
    "/me",
    response_model=UserResponse
)
def GetMe(
    CurrentUser: User = Depends(GetCurrentUser)

):
    return CurrentUser