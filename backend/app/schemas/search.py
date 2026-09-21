from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    Query: str = Field(min_length = 1)
    KnowledgeItemId : int | None = None
    Limit: int = Field(default=5, ge = 1 , le=20)


class SearchResult(BaseModel):
    Id: int
    KnowledgeItemId: int
    ChunkIndex: int
    Content: str
    Distance: float