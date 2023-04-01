from sqlalchemy.orm import Session
from fastapi import Request
from app.schemas import ShortenerSchema
from app.models import Shortener, ShortenerCreate
from app.utils import hash
from fastapi.responses import RedirectResponse
from datetime import datetime
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

def create_shortened_url(db: Session, payload: ShortenerCreate):
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    hash_id = hash(payload.redirect_url + now)
    db_shortener = ShortenerSchema(redirect_url=payload.redirect_url, id=hash_id)
    db.add(db_shortener)
    db.commit()
    db.flush(db_shortener)
    return Shortener.from_orm(db_shortener)

def redirect_shortened(db: Session, request: Request, id: str):
    found = db.query(ShortenerSchema).filter(ShortenerSchema.id == id).first()
    if not found:
        return templates.TemplateResponse("not-found.html", {"request": request })
    return RedirectResponse(found.redirect_url)