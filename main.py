from fastapi import FastAPI
from app.routers import shortener

app = FastAPI()

app.include_router(shortener)

@app.get("/")
def root():
    return { "message": "running" }