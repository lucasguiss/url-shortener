from fastapi import FastAPI
from app.routers import shortener
from app import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(shortener)

@app.get("/")
def root():
    return { "message": "running" }