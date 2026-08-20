from datetime import datetime

from pydantic import BaseModel, EmailStr , Field


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


class ChangePasswordRequest(BaseModel):
    CurrentPassword: str
    NewPassword: str = Field(
        min_length=8,
        max_length=128,
    )

