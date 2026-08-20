from sqlalchemy.orm import Session

from app.core.security import HashPassword, VerifyPassword
from app.db.models.user import User

def ChangeUserPassword(
        Database: Session,
        UserRecord: User,
        CurrentPassword: str,
        NewPassword: str,
) -> bool:
    if not VerifyPassword(
        CurrentPassword,
        UserRecord.PasswordHash,
    ):
        return False

    if VerifyPassword(
        NewPassword,
        UserRecord.PasswordHash,
    ):
        raise ValueError(
            "New password must be different from current password"
        )

    UserRecord.PasswordHash = HashPassword(NewPassword)

    Database.commit()
    Database.refresh(UserRecord)

    return True