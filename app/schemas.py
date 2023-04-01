from app.database import Base
from sqlalchemy import Column, String

class ShortenerSchema(Base):
    __tablename__ = "shortener"

    id = Column(type_=String, index=True, primary_key=True, unique=True)
    redirect_url = Column(type_=String, index=True, nullable=False)