from fastapi import FastAPI, Request, Body, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app import database
from app.models import ShortenerCreate
from app.database import get_db
from app.shortener import create_shortened_url, redirect_shortened


templates = Jinja2Templates(directory="templates")

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("create.html", {"request": request })

@app.post("/")
def create(payload: ShortenerCreate = Body(...), db = Depends(get_db)):
    return create_shortened_url(payload=payload, db=db)

@app.get("/{shortener_id}")
def redirect(request: Request, shortener_id: str, db = Depends(get_db)):
    return redirect_shortened(db, request, shortener_id)
