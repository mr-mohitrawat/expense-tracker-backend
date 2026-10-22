from ..core.db import get_db
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from ..models.user import User
from ..schema.user import UserResponseDto, UserRequestDto
from ..schema.api_response import ApiResponse
user_routers = APIRouter(
    prefix="/users"
)


@user_routers.get("/", response_model=ApiResponse)
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User)

    return ApiResponse(
        status="success",
        message="All Users",
        data={"users": [UserResponseDto.model_validate(user) for user in users]}
    )

@user_routers.post("/", response_model=ApiResponse)
def create_user(user: UserRequestDto, db: Session = Depends(get_db)):
    new_user = User(
        username = user.username,
        email = user.email,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return ApiResponse(
        status="success",
        message="User created",
        data={"user":  UserResponseDto.model_validate(new_user)}
    )

@user_routers.get("/{user_id}", response_model=ApiResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    return ApiResponse(
        status="success",
        message="User fetched",
        data={"user": UserResponseDto.model_validate(user)}
    )

@user_routers.delete("/{user_id}", response_model=ApiResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(user)
    db.commit()

    return ApiResponse(
        status="success",
        message="User Deleted successfully"
    )