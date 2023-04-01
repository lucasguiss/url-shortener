from fastapi import FastAPI
from app.routers import shortener
from app import database
from fastapi.staticfiles import StaticFiles

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(shortener)

@app.get("/")
def root():
    return { "message": "running" }