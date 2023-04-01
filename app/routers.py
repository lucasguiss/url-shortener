from fastapi import APIRouter, Body, Depends, Request
from app.models import ShortenerCreate
from app.database import get_db
from app.shortener import create_shortened_url, redirect_shortened

shortener = APIRouter(
    prefix="/shortener",
    tags=["shortener"]
)

@shortener.post("")
def create(payload: ShortenerCreate = Body(...), db = Depends(get_db)):
    return create_shortened_url(payload=payload, db=db)

@shortener.get("/{shortener_id}")
def redirect(request: Request, shortener_id: str, db = Depends(get_db)):
    return redirect_shortened(db, request, shortener_id)
