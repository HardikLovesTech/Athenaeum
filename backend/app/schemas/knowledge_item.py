from datetime import datetime

from pydantic import BaseModel , Field

class KnowledgeItemCreate(BaseModel):
    Title: str = Field(
        min_length=1,
        max_length=255,
    )

    Content : str | None = None

    Type : str = Field(
        default="note",
        max_length=50,
    )

    SourceUrl: str | None = Field(
        default=None,
        max_length=2048,
    )

class KnowledgeItemUpdate(BaseModel):
    Title: str = Field(
            min_length=1,
            max_length=255,
        )
    
    Content : str | None = None
    
    Type : str | None = Field(
        default="note",
        max_length=50,
    )
    
    SourceUrl: str | None = Field(
        default=None,
        max_length=2048,
    )


class KnowledgeItemResponse(BaseModel):
    Id: int
    UserId: int
    Title: str
    Content: str | None
    Type: str
    SourceUrl: str | None
    CreatedAt: datetime
    UpdatedAt: datetime

    model_config = {
        "from_attributes" : True,
    }