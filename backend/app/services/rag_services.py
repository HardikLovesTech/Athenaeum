from sqlalchemy.orm import Session

from app.services.search_services import SearchDocumentChunks

def BuildRAGContext(
        Database: Session,
        Query: str,
        UserId : int,
        KnowledgeItemId: int | None = None,
        limit: int = 5
) -> str:
    """
    Build a context for RAG (Retrieval-Augmented Generation) based on the provided query and optional knowledge item ID.

    Args:
        Database (Session): The SQLAlchemy database session.
        Query (str): The query string for which to build the context.
        UserId (int): The ID of the user making the request.
        KnowledgeItemId (int | None, optional): An optional knowledge item ID to filter the search. Defaults to None.
        limit (int, optional): The maximum number of document chunks to retrieve. Defaults to 5.

    Returns:
        str: A concatenated string of document chunks that serve as context for RAG.
    """
    # Retrieve relevant document chunks based on the query and optional knowledge item ID
    Results = SearchDocumentChunks(
        Database=Database,
        Query=Query,
        # UserId=UserId,
        KnowledgeItemId=KnowledgeItemId,
        Limit=limit
    )

    if not Results:
        return ""

    ContextParts: list[str] = []

    for DocumentChunk, Distance in Results:
        ContextParts.append(
            f"[Source Chunk {DocumentChunk.ChunkIndex}]\n"
            f"{DocumentChunk.Content}\n"
        )

    return "\n\n".join(ContextParts)