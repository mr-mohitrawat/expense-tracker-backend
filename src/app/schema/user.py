from pydantic import BaseModel, Field
from datetime import datetime


class UserRequestDto(BaseModel):
    username: str = Field(..., description="User name", max_length=10, min_length=2)
    email: str = Field(..., description="Email")
    password: str = Field(...,  description="User Password", min_length=4, max_length=10)


class UserResponseDto(BaseModel):
    id: int = Field(..., description="The ID of expense")
    username: str = Field(..., description="User name", max_length=10, min_length=2)
    email: str = Field(..., description="Email")
    created_at: datetime = Field(..., description="The creation date of the expense")

    model_config={
        "from_attributes": True
    }