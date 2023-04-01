from fastapi import FastAPI, Request
from app.routers import shortener
from app import database
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(shortener)

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("create.html", {"request": request })