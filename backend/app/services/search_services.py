from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.document_chunk import DocumentChunk
from app.services.embedding_services import GenerateEmbedding


def SearchDocumentChunks(
        Database: Session,
        Query: str,
        KnowledgeItemId: int | None = None,
        Limit: int = 5,
) -> list[tuple[DocumentChunk, float]]:
    QueryEmbedding = GenerateEmbedding(Query)

    DistanceExpression = DocumentChunk.Embedding.cosine_distance(
        QueryEmbedding
    )

    Statement = (
        select (
            DocumentChunk,
            DistanceExpression.label("Distance"),
        )
        .where(DocumentChunk.Embedding.is_not(None))
        .order_by(DistanceExpression)
        .limit(Limit)
    )

    if KnowledgeItemId is not None:
        Statement = Statement.where(
            DocumentChunk.KnowledgeItemId == KnowledgeItemId
        )

    Results = Database.execute(Statement).all()


    return [
        (DocumentChunk , float(Distance))
        for DocumentChunk, Distance in Results
    ]