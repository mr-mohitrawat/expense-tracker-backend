from fastapi import FastAPI
from .core.db import Base, engine
from .models.user import User
from .models.expense import Expense

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return "This is root dir."