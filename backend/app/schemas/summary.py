from pydantic import BaseModel

class SummaryResponse(BaseModel):
    Summary: str