from fastapi import APIRouter, Depends, HTTPException, status
from ..schema.expense import ExpenseRequestDto, ExpenseResponseDto
from ..core.db import get_db
from sqlalchemy.orm import Session
from ..models.expense import Expense
from ..schema.api_response import ApiResponse
expense_router = APIRouter(
    prefix="/expenses"
)

@expense_router.post("/", response_model=ApiResponse, status_code=status.HTTP_201_CREATED)
def create_expense(expense_request_dto: ExpenseRequestDto, db: Session = Depends(get_db)):
    new_expense = Expense(
        title = expense_request_dto.title,
        description = expense_request_dto.description,
        amount = expense_request_dto.amount
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return ApiResponse(status="success", message="Expense created successfully", data={"expense": ExpenseResponseDto.model_validate(new_expense)})

@expense_router.get("/", response_model=ApiResponse)
def get_all_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return ApiResponse(
        status="success",
        message="Expenses retrieved successfully",
        data={"expenses": [ExpenseResponseDto.model_validate(expense) for expense in expenses]}
    )

@expense_router.get("/{expense_id}", response_model=ApiResponse)
def get_expense(expense_id: int , db: Session = Depends(get_db)):
   
  
    expense = db.get(Expense, expense_id)
    
    return ApiResponse(
        status="success",
        message="Expense Retrived successfully",
        data={"expense": ExpenseResponseDto.validate(expense)}
    )

@expense_router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.get(Expense, expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(expense)
    db.commit()
    return ApiResponse(
        status="success",
        message="Expense deleted successfully",
        data=None
    )