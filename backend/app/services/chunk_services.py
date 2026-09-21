from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.document_chunk import DocumentChunk
from app.services.embedding_services import GenerateEmbedding


def ChunkText(
        Text: str,
        ChunkSize: int = 1000,
        ChunkOverlap: int = 200,
) -> list[str]:
    if not Text.strip():
        return []

    if ChunkSize <= 0:
        raise ValueError("Chunk Size has to be greater that zero")
    
    if ChunkOverlap >= ChunkSize:
        raise ValueError("Chunk Size has to be greater that Chunk overlap")


    Chunks :list[str] = []

    Start = 0
    TextLength = len(Text)
    Step = ChunkSize - ChunkOverlap

    while Start < TextLength:
        End = min(Start + ChunkSize , TextLength)

        Chunk = Text[Start:End].strip()

        if Chunk:
            Chunks.append(Chunk)

        Start += Step

    return Chunks



def CreateDocumentChunks(
        Database: Session,
        KnowledgeItemId: int,
        Content: str,
) -> list[DocumentChunk]:
    TextChunk = ChunkText(Content)

    DocumentChunks: list[DocumentChunk] = []

    for ChunkIndex, ChunkContent in enumerate(TextChunk):

        Embedding = GenerateEmbedding(ChunkContent)

        DocumentChunkRecord = DocumentChunk(
            KnowledgeItemId = KnowledgeItemId,
            ChunkIndex=ChunkIndex,
            Content=ChunkContent,
            Embedding=Embedding,
        )

        Database.add(DocumentChunkRecord)
        DocumentChunks.append(DocumentChunkRecord)

    Database.commit()

    for DatabaseChunkRecord in DocumentChunks:
        Database.refresh(DocumentChunkRecord)

    return DocumentChunks