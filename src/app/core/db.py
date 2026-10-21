from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "sqlite:///./expense.db"

#  create engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={
        "check_same_thread": False
    }
)

LocalSession = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind = engine
)

# sessional
# This fucntion is used 
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()