from datetime import datetime , timedelta, timezone

import jwt
from fastapi import Depends, HTTPException , status
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.config  import AccessTokenExpireMinutes , SecretKey
from app.db.session import GetDatabase
from app.db.models.user import User

PasswordHasher = PasswordHash.recommended()

Algorithm = "HS256"

OAuth2Scheme = OAuth2PasswordBearer(
    tokenUrl = "/api/v1/auth/token"
)


def HashPassword(Password :str) -> str:
    return PasswordHasher.hash(Password)

def VerifyPassword(Password :str , PasswordHash :str) -> bool:
    return PasswordHasher.verify(Password , PasswordHash)


def CreateAccessToken(UserId :int) -> str:
    Expiration = datetime.now(timezone.utc) + timedelta(
        minutes=AccessTokenExpireMinutes
    )

    Payload = {
        "sub" : str(UserId),
        "exp":  Expiration
    }

    return jwt.encode(
        Payload,
        SecretKey,
        algorithm=Algorithm
    )

def GetCurrentUser(
        Token: str = Depends(OAuth2Scheme),
        Database: Session = Depends(GetDatabase),
) -> User:
    CredentialException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate" : "Bearer",
        },
    )

    try:
        Payload = jwt.decode(
            Token,
            SecretKey,
            algorithms = [Algorithm]
        )
        UserId = Payload.get("sub")

        if UserId is None:
            raise CredentialException

        UserId = int(UserId)

    except(
        jwt.InvalidTokenError,
        ValueError,
        TypeError,
    ):
        raise CredentialException

    CurrentUser = Database.get(
        User,
        UserId,
    )

    if CurrentUser is None:
        raise CredentialException

    if not CurrentUser.IsActive:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    return CurrentUser