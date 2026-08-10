import hashlib
import secrets

from datetime import datetime , timedelta , timezone
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import RefreshTokenExpireDays
from app.db.models.refresh_token import RefreshToken

from app.services.redis_services import (
    DeleteValue,
    GetValue,
    SetValue
)

from app.core.security import (
    CreateAccessToken,
    HashPassword,
    VerifyPassword,
)

from app.db.models.user import User

def GetUserByEmail(
        Database: Session,
        Email: str,
)-> User | None:
    Statement = select(User).where(
        User.Email == Email
    )
    return Database.scalar(Statement)

def GetUserByUsername(
        Database: Session,
        Username: str,
) -> User | None:
    Statement = select(User).where(
        User.Username == Username
    )

    return Database.scalar(Statement)


def CreateUser(
        Database: Session,
        Email: str,
        Username: str,
        Password:str,
) -> User:
    NewUser = User(
        Email=Email,
        Username = Username,
        PasswordHash=HashPassword(Password)
    )

    Database.add(NewUser)
    Database.commit()
    Database.refresh(NewUser)

    return NewUser


def AuthenticateUser(
            Database: Session,
            Email:str,
            Password: str,
) -> User | None:
    UserRecord = GetUserByEmail(
        Database,
        Email
    )

    if UserRecord is None:
        return None

    if not VerifyPassword(
        Password,
        UserRecord.PasswordHash,
    ):
        return None

    return UserRecord


def GenerateUserToken(UserRecord: User) -> str:
    return CreateAccessToken(UserRecord.Id)

def HashRefreshToken(Token: str) -> str:
    return hashlib.sha256(
        Token.encode("utf-8")
    ).hexdigest()

def CreateRefreshToken(
        Database : Session,
        UserId : int,
) -> str:

    Token = secrets.token_urlsafe(64)

    TokenHash = HashRefreshToken(Token)

    ExpiresAt = (
        datetime.now(timezone.utc) + timedelta(days=RefreshTokenExpireDays)
    )

    RefreshTokenRecord = RefreshToken(
        UserId = UserId,
        TokenHash=TokenHash,
        ExpiresAt=ExpiresAt,
    )

    Database.add(RefreshTokenRecord)
    Database.commit()

    return Token

def GetValidRefreshToken(
        Database : Session,
        Token: str,
) -> RefreshToken | None:
    TokenHash = HashRefreshToken(Token)
    Statement = select(RefreshToken).where(
        RefreshToken.TokenHash == TokenHash
    )

    TokenRecord = Database.scalar(Statement)

    if TokenRecord is None:
        return None

    if TokenRecord.RevokedAt is not None:
        return None

    if TokenRecord.ExpiresAt <= datetime.now(timezone.utc):
        return None

    return TokenRecord


def RevokeRefreshToken(
        Database: Session,
        TokenRecord: RefreshToken,
) -> None:

    TokenRecord.RevokedAt = datetime.now(timezone.utc)

    Database.commit()


def CreatePasswordResetToken(
        UserRecord: User,
) -> str:

    ResetToken = secrets.token_urlsafe(32)

    RedisKey = f"password-reset:{ResetToken}"

    SetValue(
        Key=RedisKey,
        Value=str(UserRecord.Id),
        ExpirationSeconds=900,
    )

    return ResetToken


def GetUserIdFromPasswordResetToken(
        ResetToken: str,
) -> int | None:

    RedisKey = f"password-reset:{ResetToken}"

    UserId = GetValue(
        Key=RedisKey
    )

    if UserId is None:
        return None

    try:
        return int(UserId)
    except ValueError:
        return None

def DeletePasswordResetToken(
        ResetToken: str,
) -> None:
    RedisKey = f"password-reset:{ResetToken}"

    DeleteValue(
        Key=RedisKey
    )

