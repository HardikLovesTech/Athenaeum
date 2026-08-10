from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.models.user import User
from app.db.session import GetDatabase

from app.schemas.auth import (
    LoginRequest,
    RefreshTokenRequest,
    RegisterRequest,
    TokenResponse,
)

from app.schemas.user import UserResponse

from app.services.auth_services import (
    AuthenticateUser,
    CreateRefreshToken,
    CreateUser,
    GenerateUserToken,
    GetUserByEmail,
    GetUserByUsername,
    GetValidRefreshToken,
    RevokeRefreshToken,
)


Router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@Router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def Register(
    Request: RegisterRequest,
    Database: Session = Depends(GetDatabase),
):
    ExistingEmail = GetUserByEmail(
        Database,
        Request.Email,
    )

    if ExistingEmail is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    ExistingUsername = GetUserByUsername(
        Database,
        Request.Username,
    )

    if ExistingUsername is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already registered",
        )

    return CreateUser(
        Database=Database,
        Email=Request.Email,
        Username=Request.Username,
        Password=Request.Password,
    )


@Router.post(
    "/login",
    response_model=TokenResponse,
)
def Login(
    Request: LoginRequest,
    Database: Session = Depends(GetDatabase),
):
    UserRecord = AuthenticateUser(
        Database,
        Request.Email,
        Request.Password,
    )

    if UserRecord is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    AccessToken = GenerateUserToken(
        UserRecord,
    )

    RefreshToken = CreateRefreshToken(
        Database,
        UserRecord.Id,
    )

    return TokenResponse(
        AccessToken=AccessToken,
        RefreshToken=RefreshToken,
        TokenType="bearer",
    )


@Router.post(
    "/token",
)
def Token(
    FormData: OAuth2PasswordRequestForm = Depends(),
    Database: Session = Depends(GetDatabase),
):
    UserRecord = AuthenticateUser(
        Database,
        FormData.username,
        FormData.password,
    )

    if UserRecord is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    AccessToken = GenerateUserToken(
        UserRecord,
    )

    return {
        "access_token": AccessToken,
        "token_type": "bearer",
    }


@Router.post(
    "/refresh",
    response_model=TokenResponse,
)
def Refresh(
    Request: RefreshTokenRequest,
    Database: Session = Depends(GetDatabase),
):
    TokenRecord = GetValidRefreshToken(
        Database,
        Request.RefreshToken,
    )

    if TokenRecord is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    UserRecord = Database.get(
        User,
        TokenRecord.UserId,
    )

    if UserRecord is None or not UserRecord.IsActive:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user",
        )

    RevokeRefreshToken(
        Database,
        TokenRecord,
    )

    AccessToken = GenerateUserToken(
        UserRecord,
    )

    NewRefreshToken = CreateRefreshToken(
        Database,
        UserRecord.Id,
    )

    return TokenResponse(
        AccessToken=AccessToken,
        RefreshToken=NewRefreshToken,
        TokenType="bearer",
    )