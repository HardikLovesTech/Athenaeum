from datetime import datetime , timedelta, timezone
import jwt

from pwdlib import PasswordHash

from app.core.config  import AccessTokenExpireMinutes , SecretKey

PasswordHasher = PasswordHash.recommended()

Algorithm = "HS256"

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