from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "This is root dir."