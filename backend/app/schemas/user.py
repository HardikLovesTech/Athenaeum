from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    Id: int
    Email: EmailStr
    Username: str
    IsActive: bool
    Role: str
    CreatedAt: datetime

    model_config = {
        "from_attributes": True,
    }

class UpdateProfileRequest(BaseModel):
    Username: str