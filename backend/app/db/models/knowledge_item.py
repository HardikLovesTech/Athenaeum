import datetime

from sqlalchemy import DateTime, ForeignKey , String , Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class KnowledgeItem(Base):
    __tablename__ = "knowledge_items"

    Id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    UserId: Mapped[int] = mapped_column(
        ForeignKey("users.Id"),
        nullable=False,
        index=True,
    )

    Title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    Content: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    Type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="note"
    )

    SourceUrl: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
    )

    CreatedAt: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.datetime.now(datetime.UTC),
        nullable=False,
    )

    UpdatedAt: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.datetime.now(datetime.UTC),
        onupdate = lambda: datetime.datetime.now(datetime.UTC),
        nullable=False,
    )
    
    
    
    