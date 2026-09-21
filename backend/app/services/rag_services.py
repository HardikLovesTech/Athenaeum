from sqlalchemy.orm import Session

from app.services.search_services import SearchDocumentChunks


def BuildRAGContext(
    Database: Session,
    Query: str,
    UserId: int,
    KnowledgeItemId: int | None = None,
    Limit: int = 5,
) -> tuple[str, list]:
    Results = SearchDocumentChunks(
        Database=Database,
        Query=Query,
        UserId=UserId,
        KnowledgeItemId=KnowledgeItemId,
        Limit=Limit,
    )

    if not Results:
        return "", []

    ContextParts: list[str] = []
    Sources: list = []

    for DocumentChunk, Distance in Results:
        ContextParts.append(
            f"[Source Chunk {DocumentChunk.ChunkIndex}]\n"
            f"{DocumentChunk.Content}"
        )

        Sources.append(
            {
                "KnowledgeItemId": DocumentChunk.KnowledgeItemId,
                "ChunkIndex": DocumentChunk.ChunkIndex,
                "Content": DocumentChunk.Content,
                "Distance": Distance,
            }
        )

    Context = "\n\n".join(ContextParts)

    return Context, Sources