import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

from app.db.database import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    Id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    KnowledgeItemId: Mapped[int] = mapped_column(
        ForeignKey("knowledge_items.Id"),
        nullable=False,
        index=True,
    )

    ChunkIndex: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    Content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    Embedding: Mapped[list[float]  | None] = mapped_column(
        Vector(384),
        nullable=True
    )

    CreatedAt: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.datetime.now(datetime.UTC),
        nullable=False,
    )