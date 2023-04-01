from sqlalchemy.orm import Session
from app.schemas import ShortenerSchema
from app.models import Shortener, ShortenerCreate
from app.utils import hash
from fastapi.responses import RedirectResponse
from datetime import datetime


def create_shortened_url(db: Session, payload: ShortenerCreate):
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    hash_id = hash(payload.redirect_url + now)
    db_shortener = ShortenerSchema(redirect_url=payload.redirect_url, id=hash_id)
    db.add(db_shortener)
    db.commit()
    db.flush(db_shortener)
    return Shortener.from_orm(db_shortener)

def redirect_shortened(db: Session, id: str):
    found = db.query(ShortenerSchema).filter(ShortenerSchema.id == id).first()
    if not found:
        raise Exception()
    return RedirectResponse(found.redirect_url)