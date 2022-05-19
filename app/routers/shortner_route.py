from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..controllers.shortner_controller import show_all, encode_link, get_long_link
from ..schemas import link_schema


router = APIRouter(tags=["link"], prefix="/links")


@router.get("/all", status_code=status.HTTP_200_OK)
def all(db : Session = Depends(get_db)):
    return show_all(db)


@router.post("/long", status_code=status.HTTP_200_OK)
def long_link( short_link: link_schema.ShortLink):
    return get_long_link(short_link)


@router.post("/encode", status_code=status.HTTP_201_CREATED)
def encode(link: link_schema.Link, db : Session = Depends(get_db)):
    return encode_link(link, db)