from pydantic import BaseModel

class RAGRequest(BaseModel):
    Query: str
    KnowledgeItemId: int | None = None

class RAGSource(BaseModel):
    KnowledgeItemId: int
    ChunkIndex: int
    Content: str
    Distance: float

class RAGResponse(BaseModel):
    Answer: str
    Sources: list[RAGSource]