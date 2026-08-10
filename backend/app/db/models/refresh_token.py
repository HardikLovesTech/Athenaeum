import datetime
from sqlalchemy import DateTime , ForeignKey , String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class RefreshToken(Base):
    __tablename__ = "refresh_token"

    Id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    UserId: Mapped[int] = mapped_column(
        ForeignKey("users.Id" , ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    TokenHash: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
    )

    ExpiresAt : Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    RevokedAt: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    CreatedAt: Mapped[datetime.datetime] = mapped_column(
            DateTime(timezone=True),
            default= lambda: datetime.datetime.now(datetime.timezone.utc),
            nullable=False,
    )