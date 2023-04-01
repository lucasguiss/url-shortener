from fastapi import APIRouter

shortener = APIRouter(
    prefix="/shortener",
    tags=["shortener"]
)

@shortener.post("")
def create():
    return "test"

@shortener.get("/{shortener_id}")
def get_shortener_info(shortener_id: int):
    return ""