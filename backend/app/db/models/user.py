import datetime

from sqlalchemy import Boolean , DateTime , String
from sqlalchemy.orm import Mapped , mapped_column

from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    Id: Mapped[int] =mapped_column(
        primary_key=True,
        index=True,
    )

    Email: Mapped[str] =mapped_column(
            String(255),
            unique=True,
            nullable=False,
            index=True,
    )

    Username: Mapped[str] =mapped_column(
                String(50),
                unique=True,
                nullable=False,
                index=True,
    )

    PasswordHash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    IsActive: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    CreatedAt: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )


    UpdatedAt: Mapped[datetime.datetime] = mapped_column(
            DateTime,
            default=lambda: datetime.datetime.now(datetime.timezone.utc),
            onupdate=lambda: datetime.datetime.now(datetime.timezone.utc),
            nullable=False,
    )