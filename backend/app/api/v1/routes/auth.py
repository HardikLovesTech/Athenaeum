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

from app.core.security import HashPassword

from app.schemas.auth import (
    ForgotPasswordRequest,
    ForgotPasswordResponse,
    LoginRequest,
    RefreshTokenRequest,
    RegisterRequest,
    ResetPasswordRequest,
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
    CreatePasswordResetToken,
    DeletePasswordResetToken,
    GetUserIdFromPasswordResetToken,
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

@Router.post(
    "/forgot-password",
    response_model=ForgotPasswordResponse,
)
def ForgotPassword(
    Request: ForgotPasswordRequest,
    Database: Session = Depends(GetDatabase)
):
    UserRecord = GetUserByEmail(
        Database,
        Request.Email
    )

    if UserRecord is None:
        return ForgotPasswordResponse(
            Message="IF the account exists, a password reset token has been generated"
        )

    ResetToken = CreatePasswordResetToken(
        UserRecord
    )

    return ForgotPasswordResponse(
        Message="Password reset token generated",
        ResetToken=ResetToken
    )

@Router.post(
    "/reset-password",
)
def ResetPassword(
    Request: ResetPasswordRequest,
    Database: Session = Depends(GetDatabase)
):
    UserId = GetUserIdFromPasswordResetToken(
        Request.ResetToken,
    )

    if UserId is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired reset token"
        )

    UserRecord = Database.get(
        User,
        UserId
    )

    if UserRecord is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid reset token"
        )

    UserRecord.PasswordHash = HashPassword(
        Request.NewPassword
    )

    Database.commit()

    DeletePasswordResetToken(
        Request.ResetToken
    )

    return {
        "message": "Password reset successfully"
    }