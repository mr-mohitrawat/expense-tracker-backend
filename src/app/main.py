from fastapi import FastAPI
from .core.db import Base, engine
from .models.user import User
from .models.expense import Expense

from app.routers.expense import expense_router
from app.routers.user import user_routers
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return "This is root dir."

app.include_router(expense_router)
app.include_router(user_routers)