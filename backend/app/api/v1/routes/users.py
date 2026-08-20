from fastapi import APIRouter, Depends , HTTPException , status
from sqlalchemy.orm import Session

from app.db.session import GetDatabase
from app.db.models.user import User
from app.db.session import GetDatabase
from app.schemas.user import (
    ChangePasswordRequest,
    UserResponse,
    UpdateProfileRequest,
    )
from app.core.security import GetCurrentUser
from app.services.user_services import ChangeUserPassword

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


@Router.patch(
    "/me",
    response_model=UserResponse
)
def UpdateProfile(
        Request: UpdateProfileRequest,
        CurrentUser: User = Depends(GetCurrentUser),
        Database : Session = Depends(GetDatabase),
):
    ExisitingUser = Database.query(User).filter(
        User.Username == Request.Username,
        User.Id != CurrentUser.Id
    ).first()

    if ExisitingUser is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    CurrentUser.Username = Request.Username

    Database.commit()
    Database.refresh(CurrentUser)

    return CurrentUser


@Router.post(
    "/change-password"
)
def ChangePassword(
    Request: ChangePasswordRequest,
    CurrentUser : User = Depends(GetCurrentUser),
    Database: Session = Depends(GetDatabase),
):
    PasswordChange = ChangeUserPassword(
        Database  =Database,
        UserRecord=CurrentUser,
        CurrentPassword=Request.CurrentPassword,
        NewPassword=Request.NewPassword
    )

    if not PasswordChange:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect",
        )

    return {
        "message" : "Password changed succesfully"
    }