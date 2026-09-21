from pydantic import BaseModel

class RAGRequest(BaseModel):
    Query: str
    KnowledgeItemId: int | None = None


class RAGResponse(BaseModel):
    Answer: str